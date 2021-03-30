books = input(). split('&')
data = input().split(' | ')

while not data[0] == 'Done':
    command, book = data[0], data[1]
    if command == 'Add Book':
        if book not in books:
            books.insert(0, book)
    elif command == 'Take Book':
        if book in books:
            books.remove(book)
    elif command == 'Swap Books':
        book_2 = data[2]
        if book in books and book_2 in books:
            book_idx = books.index(book)
            book_2_idx = books.index(book_2)
            books[book_idx], books[book_2_idx] = books[book_2_idx], books[book_idx]
    elif command == 'Insert Book':
        books.append(book)
    elif command == 'Check Book':
        index = int(data[1])
        if not index > len(books):
            print(books[index])

    data = input().split(' | ')

print(', '.join(books))
