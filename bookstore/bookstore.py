import pprint

def create_bookstore(name):
    return {'name': name, 'books': [], 'authors': []}

def search_dic(dic,val,obj, cList=False):
    print('GBBA')
    results = []
    for i in dic:
        if i[val] == obj:
            if not cList:
                return i
            else:
                results.append(i)
    return results                

def add_author(bookstore, name, nationality):
    author = {'name': name, 'nationality': nationality, 'id': len(bookstore['authors'])}
    bookstore['authors'].append(author)
    return author

def get_author_by_name(bookstore, name):
    return search_dic(bookstore['authors'],'name',name)

def get_author_by_id(bookstore, author_id):
    return search_dic(bookstore['authors'],'id',author_id)        

def add_book(bookstore, title, isbn, author_id):
    book = {'title': title, 'isbn': isbn, 'author_id': author_id, 'id': len(bookstore['books'])}
    bookstore['books'].append(book)
    return book

def get_book_by_title(bookstore, title):
    return search_dic(bookstore['books'],'title',title)           

def get_book_by_id(bookstore, book_id):
    return search_dic(bookstore['books'],'id',book_id)         

def get_books_by_author(bookstore, author_id):
    return search_dic(bookstore['books'],'author_id',author_id, cList=True)