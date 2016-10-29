def create_bookstore(name):
    a={}
    a['name']=name
    a['authors']=[]
    a['id']=[]
    a['books']=[]
    a['isbn']=[]
    return a

def add_author(bookstore, name, nationality):
    bookstore['authors'].append(name)
    bookstore['id'].append(name+nationality)
    auth={}
    auth['name']=name
    auth['nationality']=nationality
    auth['id']=name+nationality
    bookstore[name]=auth
    return auth

def get_author_by_name(bookstore, name):
    return bookstore[name]

    
def get_author_by_id(bookstore, author_id):
    return bookstore[bookstore['authors'][idtoauth(bookstore, author_id)]]
    #return store['authors'][idtoauth(bookstore, author_id)]

def idtoauth(bookstore, author_id):
    for i,a in enumerate(bookstore['id']):
        if a==author_id:#bookstore['authors'][0]
            return i    

def add_book(bookstore, title, isbn, author_id):
    bookstore['books'].append(title)
    bookstore['isbn'].append(isbn)
    book={}
    book['title']=title
    book['isbn']=isbn
    book['id']=isbn
    book['author_id']=author_id
    bookstore[title]=book
    return book

def get_book_by_title(bookstore, title):
    return bookstore[title]

def get_book_by_id(bookstore, book_id):
    return bookstore[bookstore['books'][isbntobook(bookstore, book_id)]]

def isbntobook(bookstore, book_id):
    for i,a in enumerate(bookstore['isbn']):
        if a==book_id:
            return i
    
def get_books_by_author(bookstore, author_id):
    b=[]
    for i in bookstore['books']:
        if bookstore[i]['author_id']==author_id:
            print(bookstore[i]['title'])
            b.append(bookstore[i])
    return b