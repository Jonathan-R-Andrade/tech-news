from tech_news.analyzer.search_engine import convert_news
from tech_news.database import get_collection
from pymongo import ASCENDING, DESCENDING


# Requisito 10
def top_5_news():
    news_collection = get_collection()
    news = list(
        news_collection.find({})
        .sort([("comments_count", DESCENDING), ("title", ASCENDING)])
        .limit(5)
    )
    return convert_news(news)


# Requisito 11
def top_5_categories():
    news_collection = get_collection()
    pipeline = [
        {"$group": {"_id": "$category", "total": {"$sum": 1}}},
        {"$sort": {"total": -1, "_id": 1}},
        {"$limit": 5},
    ]
    top_5_categories = list(news_collection.aggregate(pipeline))
    return [category["_id"] for category in top_5_categories]
