import tkinter as tk

class DataStorage:
    def __init__(self):
        self.name_value = tk.StringVar()
        self.email_value = tk.StringVar()
        self.count_fine_value = tk.StringVar()
        self.deadline_fine_value = tk.StringVar()

def get_entries(data_storage):
    data_storage.name_value = name_entry.get()
    data_storage.email_value = email_entry.get()
    data_storage.count_fine_value = count_fine_entry.get()
    data_storage.deadline_fine_value = deadline_fine_entry.get()

    print(data_storage.name_value, data_storage.email_value, data_storage.count_fine_value, data_storage.deadline_fine_value)

def make_label(root, text):
    label = tk.Label(root, text=text)
    label.pack(anchor='w', pady=5)
    entry = tk.Entry(root, width=70)
    entry.pack(pady=10)
    return entry

if __name__ == "__main__":
    root = tk.Tk()

    data_storage = DataStorage()
    name_label = make_label(root, "Введите ФИО студента:")
    email_label = make_label(root, "Введите электронную почту студента:")
    count_fine_label = make_label(root, "Введите сумму задолженности:")
    deadline_fine_label = make_label(root, "Введите дедлайн задолженности:")
    button = tk.Button(root, text="Подтвердить", command=lambda: get_entries(data_storage))
    button.pack()

    root.mainloop()

    print(data_storage.name_value.get(), data_storage.email_value.get(), data_storage.count_fine_value.get(), data_storage.deadline_fine_value.get())

