import re

from Book_scrapper.Locators.books_locators import BooksLocators


class BookParser:
    """
    A class to take in an HTML page(or part of it), and find properties of an item on it.
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £{self.price}, {self.rating} stars >'

    @property
    def name(self):
        locator = BooksLocators.Name
        item_name = self.parent.select_one(locator).attrs['title']
        return item_name

    @property
    def link(self):
        locator = BooksLocators.Link
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def rating(self):
        locator = BooksLocators.Rating
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        return rating_number

    @property
    def price(self):
        locator = BooksLocators.Price
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))


