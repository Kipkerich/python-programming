


# Book class

class Book:
    def __init__(self, chapters):
        self.chapters = chapters  # instance variable
        self.choice = None        # Initialize choice to None

    def choose_chapter(self, choice):
        # List of chapters available
        available_chapters = ["1", "2", "3", "4"]
        if choice in available_chapters:
            self.choice = choice
            print(f"You have chosen Chapter {choice}")
        else:
            print("Not available")

class PageBook(Book):
    def __init__(self, chapters, pages):
        super().__init__(chapters) # Initialize the parent class
        self.pages = pages

    def check_pages(self, chapter):
        #check if the chapter exists in the page dictionary
        if chapter in self.pages:
            print(f"Chapter {chapter} has {self.pages[chapter]} pages")
        else:
            print(f"{chapter} not found in the book.")

# Example usage
chapters = input("Enter the chapter list (comma-separated): ").split(", ")
pages = {
    "1": 10,
    "2": 15,
    "3": 8,
    "4": 20
}

new_book = PageBook(chapters, pages)
print(f"Chapters in the book: {new_book.chapters}")

chapter_to_choose = input("Choose a chapter: ")
new_book.choose_chapter(chapter_to_choose)

if chapter_to_choose in pages:
    new_book.check_pages(chapter_to_choose)
