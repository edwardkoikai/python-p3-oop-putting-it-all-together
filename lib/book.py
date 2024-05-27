class Book:
    def __init__(self, title="And Then There Were None", page_count=272):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """The page_count must be an integer"""
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        self._page_count = page_count
        
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

book = Book("The World According to Garp", 69)
book.turn_page()