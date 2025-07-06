import datetime
import re
from fastapi import HTTPException, APIRouter, Depends
from pydantic import BaseModel
from sqlmodel import Session, select
from constants import API_URL
from utils import execute_request, get_vinted_headers
from config.models import User, get_session
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/accounting",
)


class CleanConversations(BaseModel):
    monthsToKeep: int


class ExportSalesData(BaseModel):
    period: str


@router.post("/export-sales-data")
def export_sales_data(
    export_sales_data: ExportSalesData,
    session: Session = Depends(get_session),
):
    # todo: implement api call to get real data

    articles_bought_prices_data = [
        [12.50, 8.90, 15.00, 22.30, 5.50],
        [18.75, 11.20, 25.80, 9.90, 14.60, 33.40],
        [7.30, 19.95, 16.75, 12.10, 28.50],
        [21.40, 13.85, 9.60, 17.20, 11.95, 24.90, 8.75],
        [15.60, 20.30, 12.40, 18.90, 26.75, 14.50],
        [19.80, 8.40, 23.70, 16.30, 10.95, 29.60],
        [13.20, 17.95, 11.80, 22.40, 15.90, 25.30, 120.33],
    ]

    articles_sold_prices_data = [
        [18.90, 14.50, 23.00, 31.50, 12.90],
        [27.40, 19.80, 38.50, 16.75, 22.90, 45.60],
        [13.70, 29.50, 24.90, 19.40, 42.80],
        [32.10, 21.75, 16.20, 26.90, 19.95, 37.50, 15.40],
        [24.80, 31.90, 19.60, 28.50, 39.75, 23.30],
        [29.70, 15.90, 36.40, 25.80, 18.95, 44.20],
        [21.60, 27.50, 19.30, 34.80, 24.90, 38.90, 17.80],
    ]
    total_articles_bought = sum(
        len(articles_bought) for articles_bought in articles_bought_prices_data
    )
    total_articles_sold = sum(
        len(articles_sold) for articles_sold in articles_sold_prices_data
    )

    turnover_data = [sum(articles_sold) for articles_sold in articles_sold_prices_data]
    gross_profit_data = [
        sum(articles_sold) - sum(articles_bought)
        for articles_bought, articles_sold in zip(
            articles_bought_prices_data, articles_sold_prices_data
        )
    ]
    labels = [
        "Jan 24",
        "Fév 24",
        "Mar 24",
        "Avr 24",
        "Mai 24",
        "Jun 24",
        "Jul 24",
    ]

    data = {
        "labels": labels,
        "turnover_data": turnover_data,
        "gross_profit_data": gross_profit_data,
        "total_turnover": sum(turnover_data),
        "maximum_turnover": max(turnover_data),
        "minimum_turnover": min(turnover_data),
        "average_turnover": sum(turnover_data) / len(turnover_data),
        "total_gross_profit": sum(gross_profit_data),
        "maximum_gross_profit": max(gross_profit_data),
        "minimum_gross_profit": min(gross_profit_data),
        "average_gross_profit": sum(gross_profit_data) / len(gross_profit_data),
        "articles_bought_prices_data": articles_bought_prices_data,
        "total_articles_bought": total_articles_bought,
        "average_article_bought_price": sum(
            sum(articles_bought) for articles_bought in articles_bought_prices_data
        )
        / total_articles_bought,
        "average_nb_articles_bought": total_articles_bought
        / len(articles_bought_prices_data),
        "most_expensive_article_bought": max(
            max(articles_bought) for articles_bought in articles_bought_prices_data
        ),
        "least_expensive_article_bought": min(
            min(articles_bought) for articles_bought in articles_bought_prices_data
        ),
        "articles_sold_prices_data": articles_sold_prices_data,
        "total_articles_sold": sum(
            sum(articles_sold) for articles_sold in articles_sold_prices_data
        ),
        "average_article_sold_price": sum(
            sum(articles_sold) for articles_sold in articles_sold_prices_data
        )
        / total_articles_sold,
        "average_nb_article_sold": total_articles_sold / len(articles_sold_prices_data),
        "most_expensive_article_sold": max(
            max(articles_sold) for articles_sold in articles_sold_prices_data
        ),
        "least_expensive_article_sold": min(
            min(articles_sold) for articles_sold in articles_sold_prices_data
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
