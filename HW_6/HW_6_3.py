# realization school library
import datetime as Date


class Book():
    def __init__(self, name, author, *args):
        self._name = name
        self._author = author
        try:
            self._publication = args[0]
            self._year = args[1]
            self._pages = args[2]
            self._count = args[3]
        except:
            pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publication(self):
        return self._publication

    @publication.setter
    def publication(self, value):
        self._publication = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value

    @property
    def type(self):
        return self._type

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value



class FictionBook(Book):
    _genres = ('Detective', 'Historical', 'Classic', 'Romance', 'Mystery',
        'Adventure', 'Poetry', 'Tale', 'Thriller', 'Horror',
        'Fantasy_and_Fantasy', 'Humor', 'Science')
    _type = 'Fiction'

    @property
    def genres(self):
        return self._genres


class AppliedBook(Book):
    _subTypes = ('Cooking', 'Tips', 'Health', 'Needlework', 'Psychology',
        'Science', 'Hobbies', 'Spiritual', 'History', 'Secrets')
    _type = 'Applied'

    @property
    def subTypes(self):
        return self._subTypes


class SpecializedBook(Book):
    _subTypes = ('Cooking', 'Atlas', 'Directory', 'Catalog', 'Dictionary')
    _type = 'Specialized'

    @property
    def subTypes(self):
        return self._subTypes


class Reader():
    def __init__(self, name, surname, grade):
        self._name = name
        self._surname = surname
        self._grade = grade


class Accounting():
    def issueBook(self, Book, Reader):
        self._date = Date.datetime.now()

    def acceptBook(self, Book, Reader):
        self._date = Date.datetime.now()
