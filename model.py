class Book:
    def __init__(self, isbn_no, title, book_format, subject, rental_price, copies):
        self.isbn_no = isbn_no
        self.title = title
        self.book_format = book_format
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies


class Magazine:
    def __init__(self, magazine_no, title, color_format, subject, rental_price, copies):
        self.magazine_no = magazine_no
        self.title = title
        self.color_format = color_format
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies


class Educationaldvd:
    def __init__(self, dvd_no, title, subject, rental_price, copies):
        self.dvd_no = dvd_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies


class Lecturecd:
    def __init__(self, cd_no, title, subject, rental_price, copies):
        self.cd_no = cd_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies
