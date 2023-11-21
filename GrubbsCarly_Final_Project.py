# Created by Carly Grubbs, 11/21/2023
# Bible Study Application
# This application will assist you in reviewing the different grouping of books of the Bible
# It will allow the user to search the ASV for a specific verse
# Help keep track of their own bible study
# Linking to a website to allow for a topical search of the bible 

# Importing libraries
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import datetime as dt
import openpyxl

path = "Books_Of_The_Bible.jpg" # Setting up the path to the background image
exists = True

# Function to open a website to topic search the boble
def openTopical():
    webbrowser.open("https://www.openbible.info/topics/")
    
# Function to open a PDF of the bible titles
def openBibleDescriptions():
    webbrowser.open_new(r"Bible_Chapter_Titles.pdf")
    
# Function to open a PDF of the help
def helpDocument():
    webbrowser.open_new(r"READ_ME.pdf")

#  Function to open a reading plan for the bible  
def Daily_Reading_Plan():
    webbrowser.open_new(r"daily_reading_plan.xlsx")

# Function to open descriptions about the breakdown of the books of the bible    
def Law():
    webbrowser.open_new(r"Law_Books.pdf")

def History():
    webbrowser.open_new(r"Hist_Books.pdf")
    
def Wisdom():
    webbrowser.open_new(r"Wisdom_Books.pdf")
    
def Prophets():
    webbrowser.open_new(r"Prophets_Books.pdf")
    
def Gospels():
    webbrowser.open_new(r"Gospels_Books.pdf")
    
def Church_Hist():
    webbrowser.open_new(r"Church_History_Books.pdf")
    
def Pauls_Letters():
    webbrowser.open_new(r"Pauls_Letters_Books.pdf")
    
def General_Letters():
    webbrowser.open_new(r"General_Letters_Books.pdf")
    
def Prophecy():
    webbrowser.open_new(r"Prophecy_Books.pdf")
    
# Function to search a CSV file to display desired bible verse   
def search():
    bible_verse = search_book.get().upper() + " " + search_chapter.get() + ":" + search_verse.get()
    bible_search = Toplevel(win)
    bible_search.title("Bible Verse Search")
    bible_search.geometry("600x200")
    Label(bible_search, text ="Bible Verse Serch").pack()
    label1 = Label(bible_search, text = search_book.get() + " " + search_chapter.get() + ":" + search_verse.get(), font= ("Helvetica 14")).pack()
    
    wb = openpyxl.load_workbook("asv.xlsx")
    ws = wb.active

    for row in ws.rows:
        if row[0].value == bible_verse:
            for cell in row:
                verse = (cell.value)
            verse_label = Label(bible_search, text = verse, font = ("Helvetica 14"), wraplength = 300).pack()
             
# Function to close the application
def close():
    exit()
    
date = dt.datetime.now() # Setting a variable date equal to now

# Format the date
format_date=f"{date:%B %d %Y}"

# Class to create window frame to hold the menu options at the top
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        
        menu = Menu(self.master)
        self.master.config(menu = menu)
        
        fileMenu = Menu(menu)
        fileMenu.add_command(label = "Bible Study Chapter Titles", command = openBibleDescriptions)
        fileMenu.add_command(label = "Topical Bible Search", command = openTopical)
        fileMenu.add_command(label = "Daily Reading Plan", command = Daily_Reading_Plan)
        fileMenu.add_command(label = "Help", command = helpDocument)
        fileMenu.add_command(label = "Exit", command = close)
        menu.add_cascade(label = "File", menu = fileMenu)
        
# Setting up main window of the application               
win = Tk()
app = Window(win)

win.geometry("771x1200") # Setting the size of the application window

img = ImageTk.PhotoImage(Image.open(path)) # Opening the picture for the background of the application

label = Label(win, text=format_date, font=("Calibri", 25)).pack() # Displaying today's date

# Setting up the enter information for the bible verse search
label1 = Label(win, text = "Please enter the book, chapter, and verse you are needing to review.", font = ("Helvetica", 12)).pack()
search_book = Entry(win, text = "Book", font = ("Helvetica", 12))
search_book.insert(END, "Book of the Bible")
search_book.pack(side = "top")
search_chapter = Entry(win, text = "Chapter", font = ("Helvetica", 12))
search_chapter.insert(END, "Chapter")
search_chapter.pack(side = "top")
search_verse = Entry(win, text = "Verse", font = ("Helvetica", 12))
search_verse.insert(END, "Verse")
search_verse.pack(side = "top")

# Creating search button
search_button = Button(win, text = "Search", font = ("Helvetica", 12), command = search).pack()

# Adding title to application window
win.wm_title("Bible Study Application")
label = tkinter.Label(win, image = img).pack(fill = "both", expand = "yes")

# Adding the various buttons to describe the groups of books
law_btn = PhotoImage(file = "C:/FinalProjectFiles/law_btn_pic.png")
img_label = Label(image = law_btn)
law = Button(win, image = law_btn, command = Law, activebackground = "gold")
law.config(height = 133, width = 318)
law.place(x = 38, y = 400)

hist_btn = PhotoImage(file = "C:/FinalProjectFiles/hist_btn_pic.png")
img_label = Label(image = hist_btn)
hist = Button(win, image = hist_btn, command = History, activebackground = "orange")
hist.config(height = 190, width = 318)
hist.place(x = 38, y = 545)

wisdom_btn = PhotoImage(file = "C:/FinalProjectFiles/wisdom_btn_pic.png")
img_label = Label(image = wisdom_btn)
wisdom = Button(win, image = wisdom_btn, command = Wisdom, activebackground = "yellow")
wisdom.config(height = 130, width = 318)
wisdom.place(x = 38, y = 750 )

prophets_btn = PhotoImage(file = "C:/FinalProjectFiles/prophets_btn_pic.png")
img_label = Label(image = prophets_btn)
prophets = Button(win, image = prophets_btn, command = Prophets, activebackground = "green")
prophets.config(height = 250, width = 318)
prophets.place(x = 38, y = 890)

gospels_btn = PhotoImage(file = "C:/FinalProjectFiles/gospels_btn_pic.png")
gospels_label = Label(image = gospels_btn)
gospels = Button(win, image = gospels_btn, command = Gospels, activebackground = "blue")
gospels.config(height = 113, width = 318)
gospels.place(x = 409, y = 400)

church_hist_btn = PhotoImage(file = "C:/FinalProjectFiles/church_hist_btn_pic.png")
church_hist_label = Label(image = church_hist_btn)
church_hist = Button(win, image = church_hist_btn, command = Church_Hist, activebackground = "green")
church_hist.config(height = 90, width = 318)
church_hist.place(x = 409, y = 525)

pauls_letters_btn = PhotoImage(file = "C:/FinalProjectFiles/pauls_letters_btn_pic.png")
pauls_letters_label = Label(image = pauls_letters_btn)
pauls_letters = Button(win, image = pauls_letters_btn, command = Pauls_Letters, activebackground = "red")
pauls_letters.config(height = 210, width = 318)
pauls_letters.place(x = 409, y = 625)

general_letters_btn = PhotoImage(file = "C:/FinalProjectFiles/gen_letters_btn_pic.png")
general_letters_label = Label(image = general_letters_btn)
general_letters = Button(win, image = general_letters_btn, command = General_Letters, activebackground = "orange")
general_letters.config(height = 150, width = 318)
general_letters.place(x = 409, y = 845)

prophecy_btn = PhotoImage(file = "C:/FinalProjectFiles/prophecy_btn_pic.png")
prophecy_label = Label(image = prophecy_btn)
prophecy = Button(win, image = prophecy_btn, command = Prophecy, activebackground = "yellow")
prophecy.config(height = 95, width = 318)
prophecy.place(x = 409, y = 1010)

# Running the application
win.mainloop()
