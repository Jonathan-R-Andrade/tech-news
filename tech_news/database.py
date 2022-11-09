# Este é o arquivo de funções de acesso ao banco de dados. Basta importar e
# chamar as funçoes
# Atenção: este arquivo não deve ser alterado. Mudanças aqui não serão
# refletidas no avaliador automático.

from pymongo import MongoClient, ASCENDING, DESCENDING
from decouple import config
import copy

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


def create_news(data):
    db.news.insert_many(copy.deepcopy(data))


def insert_or_update(notice):
    return (
        db.news.update_one(
            {"url": notice["url"]}, {"$set": notice}, upsert=True
        ).upserted_id
        is not None
    )


def find_news():
    return list(db.news.find({}, {"_id": False}))


def find_top_5_news():
    return list(
        db.news.find({})
        .sort([("comments_count", DESCENDING), ("title", ASCENDING)])
        .limit(5)
    )


def find_top_5_categories():
    pipeline = [
        {"$group": {"_id": "$category", "total": {"$sum": 1}}},
        {"$sort": {"total": -1, "_id": 1}},
        {"$limit": 5},
    ]
    return list(db.news.aggregate(pipeline))


def search_news(query):
    return list(db.news.find(query))


def get_collection():
    return db.news
