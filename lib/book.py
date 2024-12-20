#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def get_title(self):
        return self._title

    def set_title(self, title):
        if isinstance(title, str):
            self._title = title.strip().title() 
        else:
            print("Title must be a string.")

    title = property(get_title, set_title)

    def get_page_count(self):
        print("Retrieving page_count.")
        return self._page_count

    def set_page_count(self, page_count):
        if isinstance(page_count, int):  
            print(f"Setting page_count to {page_count}.")
            self._page_count = page_count
        else:
            print("page_count must be an integer")  

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")  


Anne = Book("Pirates of Caribbean", 400)
print(Anne.title)
print(Anne.page_count)
Anne.turn_page()    
        
    
        