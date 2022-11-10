from typing import Union, List, Tuple
from tabulate import tabulate
import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)

OPTIONS_LIST = (
    "Selecione uma das opções a seguir:\n"
    " 0 - Popular o banco com notícias;\n"
    " 1 - Buscar notícias por título;\n"
    " 2 - Buscar notícias por data;\n"
    " 3 - Buscar notícias por tag;\n"
    " 4 - Buscar notícias por categoria;\n"
    " 5 - Listar top 5 notícias;\n"
    " 6 - Listar top 5 categorias;\n"
    " 7 - Sair.\n"
)
NEWS_HEADERS = ["Título", "Link"]
CATEGORY_HEADER = ["Categoria"]


def get_table(data: List[Union[List, Tuple]], headers: List[str]):
    width = 100 if len(data) > 0 else None
    table = tabulate(
        data,
        headers=headers,
        tablefmt="fancy_grid",
        maxheadercolwidths=width,
        maxcolwidths=width,
    )
    return table


def populate_database():
    amount_of_news = input("Digite quantas notícias serão buscadas: ")
    print("\nPopulando o banco de dados...")
    get_tech_news(int(amount_of_news))
    print("Banco de dados populado")


def search_news_by_title():
    title = input("Digite o título: ")
    news = search_by_title(title)
    table = get_table(news, headers=NEWS_HEADERS)
    print("\n", table, sep="")


def search_news_by_date():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    news = search_by_date(date)
    table = get_table(news, headers=NEWS_HEADERS)
    print("\n", table, sep="")


def search_news_by_tag():
    tag = input("Digite a tag: ")
    news = search_by_tag(tag)
    table = get_table(news, headers=NEWS_HEADERS)
    print("\n", table, sep="")


def search_news_by_category():
    category = input("Digite a categoria: ")
    news = search_by_category(category)
    table = get_table(news, headers=NEWS_HEADERS)
    print("\n", table, sep="")


def show_top_5_news():
    news = top_5_news()
    table = get_table(news, headers=NEWS_HEADERS)
    print("\n", table, sep="")


def show_top_5_categories():
    categories = top_5_categories()
    categories = [[category] for category in categories]
    table = get_table(categories, headers=CATEGORY_HEADER)
    print("\n", table, sep="")


functions = {
    "0": populate_database,
    "1": search_news_by_title,
    "2": search_news_by_date,
    "3": search_news_by_tag,
    "4": search_news_by_category,
    "5": show_top_5_news,
    "6": show_top_5_categories,
}


# Requisito 12
def analyzer_menu():
    print(OPTIONS_LIST)

    option = input("Digite o número da opção: ")

    if option == "7":
        print("Encerrando script")
        return 0

    try:
        functions[option]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
        return 1
    except Exception as error:
        print(error, file=sys.stderr)
        return 2
