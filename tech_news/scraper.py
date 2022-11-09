import requests
from requests.exceptions import ReadTimeout
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    sleep(1)
    headers = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=headers, timeout=3)
    except ReadTimeout:
        return None

    if response.status_code == 200:
        return response.text
    return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links = selector.css("a.cs-overlay-link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page_link


def remove_invalid_characters(text: str):
    text = text.replace("\xa0", "")
    text = text[:-1] if text.endswith(" ") else text
    return text


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    page_data = dict()

    title = selector.css("h1.entry-title::text").get()
    timestamp1 = selector.css("p.post-modified-info::text").re_first(
        r"\d{2}/\d{2}/\d{4}"
    )
    timestamp2 = selector.css("li.meta-date::text").re_first(
        r"\d{2}/\d{2}/\d{4}"
    )
    comments_count = selector.css("h5.title-block::text").re_first(r"\d+")
    summary = selector.css("div.entry-content p")[0].css("*::text").getall()

    page_data["url"] = selector.css('link[rel="canonical"]::attr(href)').get()
    page_data["title"] = remove_invalid_characters(title)
    page_data["timestamp"] = timestamp1 or timestamp2
    page_data["writer"] = selector.css("a.url.fn.n::text").get()
    page_data["comments_count"] = int(comments_count) if comments_count else 0
    page_data["summary"] = remove_invalid_characters("".join(summary))
    page_data["tags"] = selector.css(".post-tags ul li a::text").getall()
    page_data["category"] = selector.css(".category-style .label::text").get()

    return page_data


# Requisito 5
def get_tech_news(amount):
    news = []
    news_page_url = "https://blog.betrybe.com/"

    while news_page_url and len(news) < amount:
        html_content = fetch(news_page_url)
        news_links = scrape_novidades(html_content)

        for link in news_links:
            news_page = fetch(link)
            news_data = scrape_noticia(news_page)
            news.append(news_data)
            if len(news) == amount:
                break

        news_page_url = scrape_next_page_link(html_content)

    create_news(news)
    return news
