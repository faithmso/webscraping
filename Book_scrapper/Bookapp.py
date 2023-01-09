import requests

from Book_scrapper.Pages.books_pages import BooksPage

page_content = requests.get('https://books.toscrape.com/').content
page = BooksPage(page_content)


books = page.books

for book in books:
    print(book)



