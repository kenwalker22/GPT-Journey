import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import openpyxl
import pandas as pd


class AddressBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Address Book")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open Excel File", command=self.load_data)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)
        self.help_menu.add_command(label="Info", command=self.show_info)

        self.address_frame = ttk.Frame(self)
        self.address_frame.pack(fill=tk.BOTH, expand=True)

        self.address_tree = ttk.Treeview(self.address_frame)
        self.address_tree["columns"] = ("address", "phone")
        self.address_tree.column("#0", width=120, minwidth=25)
        self.address_tree.column("address", width=300, minwidth=150)
        self.address_tree.column("phone", width=120, minwidth=120)

        self.address_tree.heading("#0", text="Name", anchor=tk.W)
        self.address_tree.heading("address", text="Address", anchor=tk.W)
        self.address_tree.heading("phone", text="Phone", anchor=tk.W)

        self.address_tree.pack(fill=tk.BOTH, expand=True)

    def load_data(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All Files", "*.*")],
        )
        if file_path:
            self.df = pd.read_excel(file_path)

            self.address_tree.delete(*self.address_tree.get_children())
            for index, row in self.df.iterrows():
                self.address_tree.insert(
                    "", "end", text=row["Name"], values=(row["Address"], row["Phone"])
                )

    def show_about(self):
        tk.messagebox.showinfo("About", "Address Book App\nVersion 1.0")

    def show_info(self):
        tk.messagebox.showinfo("Info", "Created using Python and Tkinter.")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = AddressBook()
    app.run()
