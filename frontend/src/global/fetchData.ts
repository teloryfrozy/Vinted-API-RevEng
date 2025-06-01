import { API_BASE_URL } from "./constants";

type FetchDataResult = {
    success: boolean;
    data?: any;
    error?: string;
};

async function processResponseData(response: Response): Promise<FetchDataResult> {
    try {
        const data = await response.json();

        if (response.ok) {
            return {
                success: true,
                data: data,
            };
        } else {
            return {
                success: false,
                error: data.detail ? data.detail : "Unknown error",
            };
        }
    } catch (error) {
        return {
            success: false,
            error: "Invalid JSON response",
        };
    }
}

export async function fetchData(
    method: "POST" | "GET" | "DELETE" | "PUT",
    path: string,
    body?: Record<string, any>,
): Promise<FetchDataResult> {
    try {
        const response = await fetch(`${API_BASE_URL}${path}`, {
            method: method,
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
            },
            body: body ? JSON.stringify(body) : undefined,
        });
        if (!response) {
            return {
                success: false,
                error: "No server response",
            };
        }

        return processResponseData(response);
    } catch (error) {
        return {
            success: false,
            error: "Network error",
        };
    }
}
