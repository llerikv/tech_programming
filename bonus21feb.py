library_books = {
    "B001": {"title": "Основы Python", "borrower": "Алиса", "due_date": -5, "fine_rate": 0.50},
    "B002": {"title": "Наука о данных", "borrower": "Боб", "due_date": 3, "fine_rate": 0.75},
    "B003": {"title": "Введение в ИИ", "borrower": None, "due_date": 0, "fine_rate": 0.25},
    "B004": {"title": "Алгоритмы", "borrower": "Алиса", "due_date": 2, "fine_rate": 1.00}
}
def data_books(books):
    fines = {}
    for book_id, book in books.items():
        title = book["title"]
        borrower = book["borrower"]
        due_date = book["due_date"]
        fine_rate = book["fine_rate"]

        if borrower is None:
            status = "Доступна"
            fine = 0
        elif due_date < 0:
            status = "В срок"
            fine = 0
        else:
            status = "Просрочена"
            fine = due_date * fine_rate

        if borrower:
            fines[borrower] = fines.get(borrower, 0) + fine

        if status == "Просрочена":
            print(f"Книга {book_id}: {title}, Заемщик: {borrower}, Статус: {status}, Дней просрочки: {due_date}, Штраф: ${fine:.2f}")
        else:
            print(f"Книга {book_id}: {title}, Заемщик: {borrower if borrower else 'Нет'}, Статус: {status}, Штраф: ${fine:.2f}")

        if fines:
            top_borrower = max(fines, key=fines.get)
            print(f"Заемщик с наибольшими штрафами: {top_borrower}, Общий штраф: ${fines[top_borrower]:.2f}")

data_books(library_books)