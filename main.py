import tkinter as tk
from tkinter import filedialog
import pandas as pd
from mail_api import send_email

class DataStorage:
    def __init__(self):
        self.name_value = tk.StringVar()
        self.email_value = tk.StringVar()
        self.count_fine_value = tk.StringVar()
        self.deadline_fine_value = tk.StringVar()

def get_entries(data_storage, name_entry, email_entry, count_fine_entry, deadline_fine_entry):
    data_storage.name_value = name_entry.get()
    data_storage.email_value = email_entry.get()
    data_storage.count_fine_value = count_fine_entry.get()
    data_storage.deadline_fine_value = deadline_fine_entry.get()

    print(data_storage.name_value, data_storage.email_value, data_storage.count_fine_value, data_storage.deadline_fine_value)

    send_email_now(data_storage)

def send_email_now(data_storage):
    name = data_storage.name_value
    email = data_storage.email_value
    count_of_debt = data_storage.count_fine_value
    deadline = data_storage.deadline_fine_value
    subject = "Долги перед УрФУ"
    print(email)

    body = f"Уважаемый {name}, \n "\
            f"Ваша задолженность перед Уральским Федеральным Университетом составляет {count_of_debt} рублей \n "\
            f"Требуем погасить долг до {deadline} \n" \
            f"\n С уважением, деканат ИРИТ-РТФ'"
    print(body)
    
    our_email = 'urfu-123@urfu-123.iam.gserviceaccount.com'
    send_email(our_email, email, subject, body)

def make_label(root, text):
    label = tk.Label(root, text=text)
    label.pack(anchor='w', pady=5)
    entry = tk.Entry(root, width=70)
    entry.pack(pady=10)
    return entry

def open_csv(data_storage):
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    our_email = 'urfu-123@urfu-123.iam.gserviceaccount.com'
    subject = "Долги перед УрФУ"
    if filename:
        file_csv = pd.read_csv(filename, delimiter=',')
        file_csv = file_csv.astype(str)
        try:
            for columns, rows in file_csv.iterrows():
                row_list = rows.values.tolist()
                print(*row_list)
                body = f"Уважаемый {row_list[0]}, \n "\
                    f"Ваша задолженность перед Уральским Федеральным Университетом составляет {row_list[2]} рублей \n "\
                    f"Требуем погасить долг до {row_list[3]} \n" \
                    f"\n С уважением, деканат ИРИТ-РТФ'"
                print(body)
                send_email(our_email, row_list[1], subject, body)
        except pd.errors.EmptyDataError:
            print('CSV файл пуст')

if __name__ == "__main__":
    root = tk.Tk()

    data_storage = DataStorage()
    name_entry = make_label(root, "Введите ФИО студента:")
    email_entry = make_label(root, "Введите электронную почту студента:")
    count_fine_entry = make_label(root, "Введите сумму задолженности:")
    deadline_fine_entry = make_label(root, "Введите дедлайн задолженности:")
    button = tk.Button(root, text="Подтвердить", command=lambda: get_entries(data_storage, name_entry, email_entry, count_fine_entry, deadline_fine_entry))
    button.pack()

    open_button = tk.Button(root, text="Открыть CSV", command=lambda: open_csv(data_storage))
    open_button.pack()
    root.mainloop()
