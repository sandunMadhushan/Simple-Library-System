from model import Magazine


def print_info(magazine):
    print(
        f"Magazine No: {magazine.magazine_no}, Title: {magazine.title}, Format: {magazine.color_format}, Subject: {magazine.subject}, Rental Price: {magazine.rental_price}, Available Copies:{magazine.copies}"
    )


class MagazineFunction:
    def __init__(self):
        self.list_of_magazine = []
        self.__initial_data()

    def __initial_data(self):
        a_magazine1 = Magazine(
            magazine_no="01",
            title="History of Cricket",
            color_format="color",
            subject="Sports",
            rental_price=5.00,
            copies=7,
        )  # type: ignore
        a_magazine2 = Magazine(
            magazine_no="ISBN9876",
            title="Types of Animal Species",
            color_format="Paperback",
            subject="Science",
            rental_price=10.50,
            copies=8,
        )  # type: ignore
        a_magazine3 = Magazine(
            magazine_no="ISBN0003",
            title="Title3",
            color_format="Format3",
            subject="Science",
            rental_price=32.50,
            copies=3,
        )
        self.list_of_magazine.append(a_magazine1)
        self.list_of_magazine.append(a_magazine2)
        self.list_of_magazine.append(a_magazine3)

    def add(self):
        __magazine_no = input("Enter Magazine Number:").strip().upper()
        __title = input("title:").strip().upper()
        __color_format = input("color format:")
        __subject = input("Subject:")
        __rental_price = float(input("rental price:"))
        __copies = int(input("copies:"))

        a_magazine = Magazine(
            magazine_no=__magazine_no,
            title=__title,
            color_format=__color_format,
            subject=__subject,
            rental_price=__rental_price,
            copies=__copies,
        )
        self.list_of_magazine.append(a_magazine)
        print(f"Magazine added {a_magazine.magazine_no}-{a_magazine.title}")

    def remove(self):
        __magazine_no = input("Enter Magazine number:")
        matched_data = list(
            x for x in self.list_of_magazine if x.magazine_no == __magazine_no
        )
        for x in matched_data:
            self.list_of_magazine.remove(x)
            print("Item Removed.")

    def lend(self):
        __magazine_no = input("Enter Magazine number:")
        __copies = int(input("Enter lend copies:"))
        matched_data = list(
            x for x in self.list_of_magazine if x.magazine_no == __magazine_no
        )
        for x in matched_data:
            x.copies -= __copies
            print("Magazine Lent")

    def receive(self):
        __magazine_no = input("Enter Magazine number:")
        __copies = int(input("Enter receive copies:"))
        matched_data = list(
            x for x in self.list_of_magazine if x.magazine_no == __magazine_no
        )
        for x in matched_data:
            x.copies += __copies
            print(f"Magazine Received with {__copies} Copies")

    def display_all(self):
        for x in self.list_of_magazine:
            print_info(magazine=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_magazine if x.copies > 0)
        for x in matched_data:
            print_info(magazine=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_magazine if x.copies == 0)
        for x in matched_data:
            print_info(magazine=x)
