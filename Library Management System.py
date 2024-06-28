class LibraryItem:
    def __init__(self, title, author, category, item_id):
        self.title = title
        self.author = author
        self.category = category
        self.item_id = item_id
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}, Category: {self.category}, ID: {self.item_id}, Checked Out: {self.is_checked_out}"

class Book(LibraryItem):
    def __init__(self, title, author, category, item_id):
        super().__init__(title, author, category, item_id)

class Magazine(LibraryItem):
    def __init__(self, title, author, category, item_id):
        super().__init__(title, author, category, item_id)

class DVD(LibraryItem):
    def __init__(self, title, author, category, item_id):
        super().__init__(title, author, category, item_id)
class Library:
    def __init__(self):
        self.items = []
        self.checked_out_items = {}

    def add_item(self, item):
        self.items.append(item)
        print(f"Item {item.title} added to the library.")

    def check_out_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                if not item.is_checked_out:
                    item.is_checked_out = True
                    self.checked_out_items[item_id] = item
                    print(f"Item {item.title} checked out.")
                    return
                else:
                    print(f"Item {item.title} is already checked out.")
                    return
        print(f"No item found with ID {item_id}.")

    def return_item(self, item_id):
        if item_id in self.checked_out_items:
            item = self.checked_out_items.pop(item_id)
            item.is_checked_out = False
            print(f"Item {item.title} returned.")
        else:
            print(f"No item found with ID {item_id} checked out.")

    def search_items(self, keyword):
        results = [item for item in self.items if keyword.lower() in item.title.lower() or keyword.lower() in item.author.lower() or keyword.lower() in item.category.lower()]
        for item in results:
            print(item)

    def manage_fines(self):
        # Placeholder for fine management logic
        pass
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add item")
        print("2. Check out item")
        print("3. Return item")
        print("4. Search items")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")
            item_id = input("Enter item ID: ")
            item_type = input("Enter item type (Book/Magazine/DVD): ")

            if item_type.lower() == "book":
                item = Book(title, author, category, item_id)
            elif item_type.lower() == "magazine":
                item = Magazine(title, author, category, item_id)
            elif item_type.lower() == "dvd":
                item = DVD(title, author, category, item_id)
            else:
                print("Invalid item type.")
                continue

            library.add_item(item)

        elif choice == "2":
            item_id = input("Enter item ID to check out: ")
            library.check_out_item(item_id)

        elif choice == "3":
            item_id = input("Enter item ID to return: ")
            library.return_item(item_id)

        elif choice == "4":
            keyword = input("Enter keyword to search: ")
            library.search_items(keyword)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
