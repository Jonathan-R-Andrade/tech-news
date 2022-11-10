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


def populate_database():
    amount_of_news = input("Digite quantas notícias serão buscadas: ")
    print("\nPopulando o banco de dados...")
    get_tech_news(int(amount_of_news))
    print("Banco de dados populado")


def search_news_by_title():
    title = input("Digite o título: ")
    news = search_by_title(title)
    print("\n", news, sep="")


def search_news_by_date():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    news = search_by_date(date)
    print("\n", news, sep="")


def search_news_by_tag():
    tag = input("Digite a tag: ")
    news = search_by_tag(tag)
    print("\n", news, sep="")


def search_news_by_category():
    category = input("Digite a categoria: ")
    news = search_by_category(category)
    print("\n", news, sep="")


def show_top_5_news():
    news = top_5_news()
    print("\n", news, sep="")


def show_top_5_categories():
    categories = top_5_categories()
    print("\n", categories, sep="")


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
