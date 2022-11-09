from tech_news.analyzer.search_engine import convert_news
from tech_news.database import find_top_5_news, find_top_5_categories


# Requisito 10
def top_5_news():
    news = find_top_5_news()
    return convert_news(news)


# Requisito 11
def top_5_categories():
    top_5_categories = find_top_5_categories()
    return [category["_id"] for category in top_5_categories]
