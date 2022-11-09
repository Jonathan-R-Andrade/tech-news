from tech_news.analyzer.search_engine import convert_news
from tech_news.database import find_top_5_news


# Requisito 10
def top_5_news():
    news = find_top_5_news()
    return convert_news(news)


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
