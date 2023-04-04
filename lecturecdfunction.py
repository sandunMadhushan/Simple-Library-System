from model import Lecturecd


def print_info(cd):
    print(
        f"CD NO: {cd.cd_no}, Title: {cd.title}, Subject: {cd.subject}, Rental Price: {cd.rental_price}, Available Copies:{cd.copies}"
    )


class LectureCDFunction:
    def __init__(self):
        self.list_of_cd = []
        self.__initial_data()

    def __initial_data(self):
        a_cd1 = Lecturecd(
            cd_no="21",
            title="Basics of Western Music",
            subject="Music,",
            rental_price=1.50,
            copies=50,
        )
        a_cd2 = Lecturecd(
            cd_no="22",
            title="Japanese Language",
            subject="Foreign Languages",
            rental_price=2.00,
            copies=3,
        )
        a_cd3 = Lecturecd(
            cd_no="23",
            title="Bringing Tony Home",
            subject="English Literature",
            rental_price=3.00,
            copies=15,
        )
        self.list_of_cd.append(a_cd1)
        self.list_of_cd.append(a_cd2)
        self.list_of_cd.append(a_cd3)

    def add(self):
        __cd_no = input("Enter CD Number:").strip().upper()
        __title = input("title:").strip().upper()
        __subject = input("Subject:")
        __rental_price = float(input("rental price:"))
        __copies = int(input("copies:"))

        a_cd = Lecturecd(
            cd_no=__cd_no,
            title=__title,
            subject=__subject,
            rental_price=__rental_price,
            copies=__copies,
        )
        self.list_of_cd.append(a_cd)
        print(f"CD added {a_cd.cd_no}-{a_cd.title}")

    def remove(self):
        __cd_no = input("Enter CD number:")
        matched_data = list(x for x in self.list_of_cd if x.isbn_no == __cd_no)
        for x in matched_data:
            self.list_of_cd.remove(x)
            print("Item Removed.")

    def lend(self):
        __cd_no = input("Enter CD number:")
        __copies = int(input("Enter lend copies:"))
        matched_data = list(x for x in self.list_of_cd if x.cd_no == __cd_no)
        for x in matched_data:
            x.copies -= __copies
            print("CD Lent")

    def receive(self):
        __cd_no = input("Enter CD number:")
        __copies = int(input("Enter receive copies:"))
        matched_data = list(x for x in self.list_of_cd if x.cd_no == __cd_no)
        for x in matched_data:
            x.copies += __copies
            print(f"CD(s) Received with {__copies} Copies")

    def display_all(self):
        for x in self.list_of_cd:
            print_info(cd=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_cd if x.copies > 0)
        for x in matched_data:
            print_info(cd=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_cd if x.copies == 0)
        for x in matched_data:
            print_info(cd=x)
