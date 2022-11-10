import sys

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
    input("Digite quantas notícias serão buscadas: ")
    print("populate_database")


def search_news_by_title():
    input("Digite o título: ")
    print("search_news_by_title")


def search_news_by_date():
    input("Digite a data no formato aaaa-mm-dd: ")
    print("search_news_by_date")


def search_news_by_tag():
    input("Digite a tag: ")
    print("search_news_by_tag")


def search_news_by_category():
    input("Digite a categoria: ")
    print("search_news_by_category")


def show_top_5_news():
    print("show_top_5_news")


def show_top_5_categories():
    print("show_top_5_categories")


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
