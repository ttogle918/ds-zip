"""
Bare Minimum Requirements
OOP에서 중요한 것은 기능별로 정확한 설계입니다.

요구사항:
    아래 작성된 내용은 전체 설명이 아니기 때문에 소스코드를 보시면서 설계를 하시길 바랍니다.

    Person(사람)
        사서 또는 이용자에 대한 기본정보를 보여준다.

    Librarian(사서)
    사서는 Person으로부터 상속을 받야야한다.
    사서에 대한 정보(변수): 이름, 나이, 관리하는 책 리스트(private)

        주요 기능
            사서는 관리하는 책 리스트에 책을 추가하는 함수를 가지고 있다.
            사서는 서적을 대출해주는 함수를 가지고 있다.
            사서가 관리하는 책의 리스트는 외부에서 접근할 수 없다.
            사서는 관리하는 책의 리스트를 반환하는 함수를 가지고 있다.

    User(이용자)
        이용자는 Person으로부터 상속을 받야야한다.
        이용자에 대한 정보(변수): 이름, 나이, 빌린 책 리스트(private)

        주요 기능
            이용자는 책을 빌리는 함수를 가지고 있다.
            이용자는 빌린 책을 반환하는 함수를 가지고 있다.
            이용자가 빌린 책의 리스트는 외부에서 접근할 수 없다.
            이용자는 빌린 책의 리스트를 반환하는 함수를 가지고 있다.

"""


class Person:
    def introduce(self):
        print('안녕하세요! 제 이름은 {}, {}살 입니다!'.format(self.name, self.age))
        
        
class Book:
    def __init__(self, name, librarian):
        self.name = name
        self.librarian = librarian


class Librarian:
    def __init__():
        ##### 소스코드를 작성해주세요 #####
        pass # 문제를 푸실 때 pass를 지워주세요

    def add_book():   #새책을 받거나, 반납받는 함수
        ##### 소스코드를 작성해주세요 #####
        pass # 문제를 푸실 때 pass를 지워주세요

    def remove_book():    #책을 빌려주는 함수
        ##### 소스코드를 작성해주세요 #####
        pass # 문제를 푸실 때 pass를 지워주세요

    def get_book_list(self):    #관리중인 책 목록을 반환하는 함수
        ##### 소스코드를 작성해주세요 #####
        pass # 문제를 푸실 때 pass를 지워주세요


class User:
    def __init__():
        ##### 소스코드를 작성해주세요 #####
        pass # 문제를 푸실 때 pass를 지워주세요

    def borrow_book(): #책을 대출하는 함수
        ##### 소스코드를 작성해주세요 #####
        pass # 문제를 푸실 때 pass를 지워주세요

    def return_book(): #책을 반납하는 함수
        ##### 소스코드를 작성해주세요 #####
        pass # 문제를 푸실 때 pass를 지워주세요

    def get_borrowed_list():    #빌린 책 목록을 반환하는 함수
        ##### 소스코드를 작성해주세요 #####
        pass # 문제를 푸실 때 pass를 지워주세요
