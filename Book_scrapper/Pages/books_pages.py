from bs4 import BeautifulSoup

from Book_scrapper.Locators.books_pages_locators import BooksPageLocators
from Book_scrapper.Parsers.books import BookParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BooksPageLocators.BOOKS
        quote_tags = self.soup.select(locator)
        return [BookParser(e) for e in quote_tags]
