import tkinter as tk
from tkinter import simpledialog

def load_answers():
    try:
        with open("responses.txt", "r") as file:
            for response in file:
                listbox.insert(tk.END, response.strip())
    except FileNotFoundError:
        pass  # Файл не найден, игнорируем ошибку

def save_answers():
    with open("responses.txt", "w") as file:
        responses = listbox.get(0, tk.END)
        for response in responses:
            file.write(response + "\n")

def add_answer():
    answer = simpledialog.askstring("Ввод", "Введите ваш ответ для сохранения:")
    if answer:
        listbox.insert(tk.END, answer)
        save_answers()

def copy_answer():
    if listbox.curselection():
        selected = listbox.get(listbox.curselection())
        window.clipboard_clear()
        window.clipboard_append(selected)

def delete_answer():
    if listbox.curselection():
        listbox.delete(listbox.curselection())
        save_answers()

# Создание основного окна
window = tk.Tk()
window.title("Быстрые ответы")
window.configure(bg='lightblue')
window.geometry("500x550")

# Создание и расположение виджетов
listbox = tk.Listbox(window, height=20, width=70)
listbox.pack(pady=(10, 20))

add_button = tk.Button(window, text="Добавить ответ", command=add_answer, bg='green', fg='white',height=2,width=60)
add_button.pack(pady=(10, 5))

copy_button = tk.Button(window, text="Копировать ответ", command=copy_answer, bg='blue', fg='white',height=2,width=60)
copy_button.pack(pady=(10, 5))

delete_button = tk.Button(window, text="Удалить ответ", command=delete_answer, bg='red', fg='white',height=2,width=60)
delete_button.pack(pady=(10, 5))

load_answers()  # Загружаем сохраненные ответы при запуске

# Запуск основного цикла обработки событий
window.mainloop()
