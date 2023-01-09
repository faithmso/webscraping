from Quote_Scrapper.locators.quote_locators import QuoteLocators


class QuoteParser:

    """
    Given one specific quote divs, find out the data about the quote (quote content, author, tags).
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author} >'

    @property
    def content(self):
        locator = QuoteLocators.Content
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.Author
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.Tags
        return [e.srring for e in self.parent(locator)]


