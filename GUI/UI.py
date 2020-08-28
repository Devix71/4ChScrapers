import tkinter as tk
from tkinter import Spinbox
from tkinter import scrolledtext
from tkinter import ttk

import API_reader
import scraper
from tooltips import ToolTip

class GUI():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("4chan thread downloader")
        self.create_widgets()

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def _get_link(self):
        brd = self.board.get()
        idd = self.ID.get()
        value = self.spin.get()
        link = value + "/" + brd + "/thread/" + idd
        name = self.FName.get()
        path = self.FPath.get()
        API_reader.picture_download_single(path, brd, idd)
        scraper.scraperr(link, path, name)
        self.scrol.insert(tk.INSERT, "The scraped thread is " + value + "/" + brd + "/thread/" + idd + '\n')
        self.scrol.insert(tk.INSERT, "The file is named " + name + ".json and it is saved at " + path + '\n')

    def _downloadP(self):
        brod = self.board_api.get()
        path = self.path_api.get()
        self.scrol.insert(tk.INSERT, "The scraped threads are located at " + path + '\n')
        API_reader.picture_download(path, brod)

    def _downloadT(self):
        brod = self.board_api.get()
        path = self.path_api.get()
        self.scrol.insert(tk.INSERT, "The scraped threads are located at " + path + '\n')
        API_reader.text_download(path, brod)

    def _downloadA(self):
        brod = self.board_api.get()
        path = self.path_api.get()
        self.scrol.insert(tk.INSERT, "The scraped threads are located at " + path + '\n')
        API_reader.all_download(path, brod)

    # find out why it doesn't work
    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)  # Create Tab Control

        tab1 = ttk.Frame(tabControl)  # Create a tab
        tabControl.add(tab1, text='Download a thread')  # Add the tab
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text="Download a board")

        tabControl.pack(expand=1, fill="both")

        confy1 = ttk.LabelFrame(tab1, text='What to scrap')
        confy1.grid(column=0, row=0, padx=8, pady=10)

        a_label = ttk.Label(confy1, text="Board :")
        a_label.grid(column=0, row=0, sticky='W', padx=10)
        b_label = ttk.Label(confy1, text="Thread ID :")
        b_label.grid(column=1, row=0, sticky='W', padx=10)
        c_label = ttk.Label(confy1, text="NSFW board or not :")
        c_label.grid(column=3, row=0, sticky='W', padx=10)
        d_label = ttk.Label(confy1, text="Output :")
        d_label.grid(column=0, row=3, padx=10, pady=5, sticky='W')
        e_label = ttk.Label(confy1, text="File name :")
        e_label.grid(column=0, row=2, padx=10, pady=5, sticky='W')
        f_label = ttk.Label(confy1, text="File Path :")
        f_label.grid(column=2, row=2, padx=10, pady=5, sticky='E')

        self.board = tk.StringVar()
        board_entered = ttk.Entry(confy1, width=12, textvariable=self.board)
        board_entered.grid(column=0, row=1, sticky='W', padx=10, pady=3)

        self.ID = tk.StringVar()
        id_entered = ttk.Entry(confy1, width=12, textvariable=self.ID)
        id_entered.grid(column=1, row=1, sticky='W', padx=10, pady=3)
        values = ("https://boards.4channel.org", "https://boards.4chan.org")
        self.spin = Spinbox(confy1, values=values, width=25)
        self.spin.grid(column=3, row=1, sticky='W', padx=10, pady=3)
        self.win.iconbitmap('iconitza.ico')
        self.linker = ttk.Button(confy1, text="Scrap Thread", command=self._get_link)
        self.linker.grid(column=4, sticky="W", padx=10, pady=5, row=2)
        self.FName = tk.StringVar()
        self.FName_entered = ttk.Entry(confy1, width=12, textvariable=self.FName)
        self.FName_entered.grid(column=1, row=2, padx=10, pady=5, sticky='W')
        self.FPath = tk.StringVar()
        self.FPath_entered = ttk.Entry(confy1, width=20, textvariable=self.FPath)
        self.FPath_entered.grid(column=3, row=2, padx=10, pady=5, sticky='W')
        scrol_w = 60
        scrol_h = 1
        self.scrol = scrolledtext.ScrolledText(confy1, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrol.grid(column=0, row=4, sticky='WE', columnspan=6, padx=5, pady=10)

        ToolTip(self.FPath_entered, 'The path must be formatted like this: drive:\\folder\\')
        ToolTip(self.FName_entered, "The extension is .json, no need to specify it")

        confy2 = ttk.LabelFrame(tab2, text='Settings')
        confy2.grid(column=0, row=0, padx=8, pady=8)
        confy3 = ttk.LabelFrame(tab2, text="Image Download Only")
        confy3.grid(column=2, row=0, padx=8, pady=8, sticky='N')
        confy4 = ttk.LabelFrame(tab2, text="Text Download Only")
        confy4.grid(column=2, row=1, padx=0, pady=4, sticky='N')
        confy5 = ttk.LabelFrame(tab2, text="Output")
        confy5.grid(column=0, row=1, padx=0, pady=4, sticky='N')

        g_label = ttk.Label(confy2, text="Board :")
        g_label.grid(column=0, row=0, sticky='W', padx=10)

        self.board_api = tk.StringVar()
        board_api_entered = ttk.Entry(confy2, width=12, textvariable=self.board_api)
        board_api_entered.grid(column=0, row=1, sticky='W', padx=10, pady=3)

        h_label = ttk.Label(confy2, text="Path :")
        h_label.grid(column=1, row=0, sticky='W', padx=10)

        self.path_api = tk.StringVar()
        self.path_api_entered = ttk.Entry(confy2, width=12, textvariable=self.path_api)
        self.path_api_entered.grid(column=1, row=1, sticky='W', padx=10, pady=3)
        ToolTip(self.path_api_entered, 'The path must be formatted like this: drive:\\folder\\')

        self.downloader = ttk.Button(confy3, text="Download", command=self._downloadP)
        self.downloader.grid(column=0, sticky="E", padx=40, pady=5, row=1)

        self.downloaderT = ttk.Button(confy4, text="Download", command=self._downloadT)
        self.downloaderT.grid(column=0, sticky="W", padx=35, pady=5, row=1)

        self.downloaderALL = ttk.Button(confy2, text="Download All", command=self._downloadA)
        self.downloaderALL.grid(column=2, sticky="W", padx=15, pady=5, row=1)

        self.scroll = scrolledtext.ScrolledText(confy5, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scroll.grid(column=0, row=2, sticky='WE', columnspan=6, padx=5, pady=3)


gui = GUI()
gui.win.mainloop()
