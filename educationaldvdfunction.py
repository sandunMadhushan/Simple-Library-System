from model import Educationaldvd


def print_info(dvd):
    print(
        f"DVD NO: {dvd.dvd_no}, Title: {dvd.title}, Subject: {dvd.subject}, Rental Price: {dvd.rental_price}, Available Copies:{dvd.copies}"
    )


class EducationaldvdFunction:
    def __init__(self):
        self.list_of_dvd = []
        self.__initial_data()

    def __initial_data(self):
        a_dvd1 = Educationaldvd(
            dvd_no="10",
            title="Birth of the Solar System",
            subject="Astronomy",
            rental_price=2.50,
            copies=10,
        )
        a_dvd2 = Educationaldvd(
            dvd_no="11",
            title="Pythagoras Theorem",
            subject="Math",
            rental_price=1.00,
            copies=50,
        )
        a_dvd3 = Educationaldvd(
            dvd_no="12",
            title="The Newton Law",
            subject="Science",
            rental_price=3.50,
            copies=20,
        )
        self.list_of_dvd.append(a_dvd1)
        self.list_of_dvd.append(a_dvd2)
        self.list_of_dvd.append(a_dvd3)

    def add(self):
        __dvd_no = input("Enter DVD Number:").strip().upper()
        __title = input("title:").strip().upper()
        __subject = input("Subject:")
        __rental_price = float(input("rental price:"))
        __copies = int(input("copies:"))

        a_dvd = Educationaldvd(
            dvd_no=__dvd_no,
            title=__title,
            subject=__subject,
            rental_price=__rental_price,
            copies=__copies,
        )
        self.list_of_dvd.append(a_dvd)
        print(f"DVD added {a_dvd.dvd_no}-{a_dvd.title}")

    def remove(self):
        __dvd_no = input("Enter DVD number:")
        matched_data = list(x for x in self.list_of_dvd if x.isbn_no == __dvd_no)
        for x in matched_data:
            self.list_of_dvd.remove(x)
            print("Item Removed.")

    def lend(self):
        __dvd_no = input("Enter DVD number:")
        __copies = int(input("Enter lend copies:"))
        matched_data = list(x for x in self.list_of_dvd if x.dvd_no == __dvd_no)
        for x in matched_data:
            x.copies -= __copies
            print("DVD Lent")

    def receive(self):
        __dvd_no = input("Enter DVD number:")
        __copies = int(input("Enter receive copies:"))
        matched_data = list(x for x in self.list_of_dvd if x.dvd_no == __dvd_no)
        for x in matched_data:
            x.copies += __copies
            print(f"DVD(s) Received with {__copies} Copies")

    def display_all(self):
        for x in self.list_of_dvd:
            print_info(dvd=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_dvd if x.copies > 0)
        for x in matched_data:
            print_info(dvd=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_dvd if x.copies == 0)
        for x in matched_data:
            print_info(dvd=x)
