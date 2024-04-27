import tkinter as tk
from tkinter import ttk

class ScrollTable:
    def __init__(self, master):
        self.index = 1
        self.master = master
        print("updated")

        self.table_frame = tk.Frame(self.master, width=300, height=40)
        self.table_frame.place(x=0, y=355)

        # scrollbar
        self.table_scroll = tk.Scrollbar(self.table_frame)
        self.table_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.table_scroll = tk.Scrollbar(self.table_frame, orient='horizontal')
        self.table_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.Table = ttk.Treeview(self.table_frame, yscrollcommand=self.table_scroll.set, xscrollcommand=self.table_scroll.set)

        self.Table.pack()
        self.table_scroll.config(command=self.Table.yview)
        self.table_scroll.config(command=self.Table.xview)
        

        # define our column
        self.Table['columns'] = ('Order', 'malware', 'file', 'path')

        # format our column
        self.Table.column("#0", width=0, stretch=tk.NO)
        self.Table.column("Order", anchor=tk.CENTER)#, width=80)
        self.Table.column("malware", anchor=tk.CENTER)#, width=80)
        self.Table.column("file", anchor=tk.CENTER)#, width=80)
        self.Table.column("path", anchor=tk.CENTER)#, width=80)

        # Create Headings
        self.Table.heading("#0", text="", anchor=tk.CENTER)
        self.Table.heading("Order", text="Id", anchor=tk.CENTER)
        self.Table.heading("malware", text="malware", anchor=tk.CENTER)
        self.Table.heading("file", text="file", anchor=tk.CENTER)
        self.Table.heading("file", text="file", anchor=tk.CENTER)
        self.Table.heading("path", text="path", anchor=tk.CENTER)


    def insert_data(self, data):
        try:
            for i, item in enumerate(data):
                print(item)
                self.Table.insert(parent='', index='end', iid=2, text='', values=item)
        except Exception as e:
            print("errror: ", str(e))

    def clear_data(self):
        self.Table.delete(*self.Table.get_children())
