import datetime
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlmodel import Session
from constants import API_URL
from utils import execute_request, get_vinted_headers
from config.models import get_session

router = APIRouter(
    prefix="/accounting",
)


class CleanConversations(BaseModel):
    monthsToKeep: int


class ExportSalesData(BaseModel):
    period: str


def get_transactions_data(year, month, headers):
    page = 1
    url = f"{API_URL}wallet/invoices/{year}/{month}?page={page}"
    response = execute_request("GET", url, headers)

    data = response.json()
    total_records = data["invoice_lines_pagination"]["total_records"]
    total_pages = data["invoice_lines_pagination"]["total_pages"]

    if total_records == 0:
        return {
            "bought_data": [],
            "sold_data": [],
        }

    bought_data = []
    sold_data = []

    while page <= total_pages:
        url = f"{API_URL}wallet/invoices/{year}/{month}?page={page}"
        response = execute_request("GET", url, headers)
        data = response.json()

        for line in data["invoice_lines"]:
            amount = float(line["amount"]["amount"])
            if line.get("entity_type") == "payout":
                continue
            if line["type"] == "debit":
                sold_data.append(amount)
            else:
                bought_data.append(amount)

        page += 1

    return {
        "bought_data": bought_data,
        "sold_data": sold_data,
    }


def get_labels(start_year, start_month, headers):
    url = f"{API_URL}wallet/invoices/current"
    response = execute_request("GET", url, headers)
    data = response.json()
    history = data["history"]

    labels = [
        f"{item['title']} {str(item['year'])[-2:]}"
        for item in history
        if (item["year"] > start_year)
        or (item["year"] == start_year and item["month"] >= start_month)
    ]

    labels.reverse()
    return labels


def get_join_date(headers):
    url = f"{API_URL}wallet/invoices/current"
    response = execute_request("GET", url, headers)
    data = response.json()
    history = data["history"]
    return {
        "year": history[-1]["year"],
        "month": history[-1]["month"],
        "title": history[-1]["title"],
    }


def get_months_to_fetch(period, headers):
    """Generate list of (year, month) tuples based on period"""
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month

    months_to_fetch = []

    if period == "sinceBegin":
        join_date = get_join_date(headers)
        start_year = join_date["year"]
        start_month = join_date["month"]
    elif period == "ytd":
        start_year = current_year
        start_month = 1
    elif period == "last1M":
        if current_month == 1:
            start_year = current_year - 1
            start_month = 12
        else:
            start_year = current_year
            start_month = current_month - 1
    elif period == "last3M":
        for i in range(3, 0, -1):
            if current_month - i <= 0:
                year = current_year - 1
                month = 12 + (current_month - i)
            else:
                year = current_year
                month = current_month - i
            months_to_fetch.append((year, month))
        return months_to_fetch
    elif period == "last6M":
        for i in range(6, 0, -1):
            if current_month - i <= 0:
                year = current_year - 1
                month = 12 + (current_month - i)
            else:
                year = current_year
                month = current_month - i
            months_to_fetch.append((year, month))
        return months_to_fetch
    elif period == "last1Y":
        for i in range(12, 0, -1):
            if current_month - i <= 0:
                year = current_year - 1
                month = 12 + (current_month - i)
            else:
                year = current_year
                month = current_month - i
            months_to_fetch.append((year, month))
        return months_to_fetch
    else:
        return [(current_year, current_month)]

    # Generate months from start to current
    year = start_year
    month = start_month

    while (year < current_year) or (year == current_year and month <= current_month):
        months_to_fetch.append((year, month))
        month += 1
        if month > 12:
            month = 1
            year += 1

    return months_to_fetch


@router.post("/export-sales-data")
def export_sales_data(
    export_sales_data: ExportSalesData,
    headers: dict = Depends(get_vinted_headers),
):
    # Get months to fetch based on period
    months_to_fetch = get_months_to_fetch(export_sales_data.period, headers)

    articles_bought_prices_data = []
    articles_sold_prices_data = []

    for year, month in months_to_fetch:
        data = get_transactions_data(year, month, headers)
        articles_bought_prices_data.append(data["bought_data"])
        articles_sold_prices_data.append(data["sold_data"])

    total_articles_bought = sum(
        len(articles_bought) for articles_bought in articles_bought_prices_data
    )
    total_articles_sold = sum(
        len(articles_sold) for articles_sold in articles_sold_prices_data
    )

    # Handle empty data cases
    if not articles_bought_prices_data or not articles_sold_prices_data:
        return {
            "labels": [],
            "turnover_data": [],
            "gross_profit_data": [],
            "total_turnover": 0,
            "maximum_turnover": 0,
            "minimum_turnover": 0,
            "average_turnover": 0,
            "total_gross_profit": 0,
            "maximum_gross_profit": 0,
            "minimum_gross_profit": 0,
            "average_gross_profit": 0,
            "articles_bought_prices_data": articles_bought_prices_data,
            "total_articles_bought": total_articles_bought,
            "average_article_bought_price": 0,
            "average_nb_articles_bought": 0,
            "most_expensive_article_bought": 0,
            "least_expensive_article_bought": 0,
            "articles_sold_prices_data": articles_sold_prices_data,
            "total_articles_sold": total_articles_sold,
            "average_article_sold_price": 0,
            "average_nb_article_sold": 0,
            "most_expensive_article_sold": 0,
            "least_expensive_article_sold": 0,
        }

    turnover_data = [sum(articles_sold) for articles_sold in articles_sold_prices_data]
    gross_profit_data = [
        sum(articles_sold) - sum(articles_bought)
        for articles_bought, articles_sold in zip(
            articles_bought_prices_data, articles_sold_prices_data
        )
    ]

    data = {
        "labels": get_labels(months_to_fetch[0][0], months_to_fetch[0][1], headers),
        "turnover_data": turnover_data,
        "gross_profit_data": gross_profit_data,
        "total_turnover": sum(turnover_data),
        "maximum_turnover": max(turnover_data) if turnover_data else 0,
        "minimum_turnover": min(turnover_data) if turnover_data else 0,
        "average_turnover": (
            sum(turnover_data) / len(turnover_data) if turnover_data else 0
        ),
        "total_gross_profit": sum(gross_profit_data),
        "maximum_gross_profit": max(gross_profit_data) if gross_profit_data else 0,
        "minimum_gross_profit": min(gross_profit_data) if gross_profit_data else 0,
        "average_gross_profit": (
            sum(gross_profit_data) / len(gross_profit_data) if gross_profit_data else 0
        ),
        "articles_bought_prices_data": articles_bought_prices_data,
        "total_articles_bought": total_articles_bought,
        "average_article_bought_price": abs(
            sum(sum(articles_bought) for articles_bought in articles_bought_prices_data)
            / total_articles_bought
        ),
        "average_nb_articles_bought": total_articles_bought
        / len(articles_bought_prices_data),
        "most_expensive_article_bought": (
            abs(
                max(
                    max(articles_bought)
                    for articles_bought in articles_bought_prices_data
                    if articles_bought
                )
            )
            if articles_bought_prices_data
            else 0
        ),
        "least_expensive_article_bought": (
            abs(
                min(
                    min(articles_bought)
                    for articles_bought in articles_bought_prices_data
                    if articles_bought
                )
            )
            if articles_bought_prices_data
            else 0
        ),
        "articles_sold_prices_data": articles_sold_prices_data,
        "total_articles_sold": sum(
            sum(articles_sold) for articles_sold in articles_sold_prices_data
        ),
        "average_article_sold_price": sum(
            sum(articles_sold) for articles_sold in articles_sold_prices_data
        )
        / total_articles_sold,
        "average_nb_article_sold": (
            total_articles_sold / len(articles_sold_prices_data)
            if articles_sold_prices_data
            else 0
        ),
        "most_expensive_article_sold": (
            max(
                max(articles_sold)
                for articles_sold in articles_sold_prices_data
                if articles_sold
            )
            if articles_sold_prices_data
            else 0
        ),
        "least_expensive_article_sold": (
            min(
                min(articles_sold)
                for articles_sold in articles_sold_prices_data
                if articles_sold
            )
            if articles_sold_prices_data
            else 0
        ),
    }

    return data


@router.post("/clean-conversations")
async def clean_conversations(
    clean_conversations: CleanConversations,
    session: Session = Depends(get_session),
    headers: dict = Depends(get_vinted_headers),
):
    page = 1
    nb_conversations_deleted = 0

    response = execute_request(
        "GET", f"{API_URL}inbox?page={page}?per_page=20", headers, session=session
    )

    total_pages = response.json()["pagination"]["total_pages"]

    while page < total_pages:
        response = execute_request(
            "GET", f"{API_URL}inbox?page={page}?per_page=20", headers, session=session
        )

        for conversation in response.json()["conversations"]:
            if (
                datetime.datetime.now()
                - datetime.datetime.strptime(
                    conversation["updated_at"].split("+")[0], "%Y-%m-%dT%H:%M:%S"
                )
            ).days > clean_conversations.monthsToKeep * 30:
                nb_conversations_deleted += 1
                if not conversation["is_deletion_restricted"]:
                    execute_request(
                        "DELETE",
                        f"{API_URL}conversations/{conversation['id']}",
                        headers,
                        session=session,
                    )

        page += 1

    return {
        "message": "Conversations cleaned",
        "nnConversationsDeleted": nb_conversations_deleted,
    }
