from tech_news.database import search_news
import datetime


def convert_news(news_list: list[dict]):
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 6
def search_by_title(title: str):
    news_found = search_news({"title": {"$regex": title, "$options": "i"}})
    return convert_news(news_found)


# Requisito 7
def search_by_date(date: str):
    try:
        date = datetime.date.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")
    news_found = search_news({"timestamp": date.strftime("%d/%m/%Y")})
    return convert_news(news_found)


# Requisito 8
def search_by_tag(tag: str):
    news_found = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return convert_news(news_found)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
