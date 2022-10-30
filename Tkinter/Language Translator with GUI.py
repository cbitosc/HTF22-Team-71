# importing modules
import tkinter.font as font
from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator
from tkinter import messagebox
from functools import partial

translator = Translator()

# initializing window
Screen = Tk()
Screen.title("Language Translator")
Screen.geometry("1520x780+0+0")
Screen.config(background='#a8dadc')

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

# tuple for choosing languages
inputlang = {'Hindi', 'English', 'French', 'German', 'Spanish', 'Chinese', 'Arabic', 'Portuguese', 'Indonesian', 'Japanese', 'Russian', 'Korean'}
LanguageChoices = {'Hindi', 'English', 'French', 'German', 'Spanish', "Chinese", 'Arabic', 'Portuguese', 'Indonesian', 'Japanese', 'Russian', 'Korean'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')


def Translate():
    user_input_translated = translator.translate(TextVar.get(), dest=TranslateLanguageChoice.get(),
                                                 src=InputLanguageChoice.get())
    OutputVar.set(user_input_translated.text)


def registration():
    def register_user(username,password):
        user_name = username.get()
        pass_word = password.get()
        file = open('login credentials.csv', 'a')
        file.write(user_name+',')
        file.write(pass_word+'\n')
        file.close()
        messagebox.showinfo('Registration','Registration successfull')
    reg = Toplevel(Screen)
    reg.geometry('400x400+1050+100')
    reg.title('Registration')
    Label(reg, text="Registration", font=("Times New roman", 16)).place(x=180, y=50)
    Label(reg, text="User Name : ", font=("Times New roman", 16)).place(x=50, y=100)
    username = StringVar()
    Entry(reg, textvariable=username).place(x=250, y=100)

    # password label and password entry box
    Label(reg, text="Password :", font=("Times New roman", 16)).place(x=50, y=150)
    password = StringVar()
    Entry(reg, textvariable=password, show='*').place(x=250, y=150)
    regButton = Button(reg, text="Register", command=lambda: register_user(username, password),
                         highlightcolor='Red',
                         relief=RAISED, font=("Times New roman", 16))
    regButton.place(x=180, y=200)
    login_prompt = Button(reg, text="Already have an account, Login.", foreground='blue', command=lambda:reg.destroy(),
                      borderwidth=0, font=("Times New roman", 12, 'underline'))

    login_prompt.place(x=100, y=250)
    reg.mainloop()


def login():
    def validateLogin(username, password):
        user_name = username.get()
        pass_word = password.get()
        file = open('login credentials.csv', 'r')
        headers = file.readline()
        credentials = file.readline()
        log = 0
        while credentials != '':
            s = credentials.split(',')
            print(s)
            if s[0] == user_name:
                if s[1][:-1] == pass_word:
                    messagebox.showinfo("Login info", "Login successful")
                    log = 1
                    break
            credentials = file.readline()
        if log==0:
            messagebox.showinfo("Login info", "Login Unsuccessful")
        file.close()

    # window
    tkWindow = Toplevel(Screen)
    tkWindow.geometry('400x400+1050+100')
    tkWindow.title('Login')

    # username label and text entry box
    Label(tkWindow, text="Login", font=("Times New roman", 16)).place(x=180, y=50)
    Label(tkWindow, text="User Name : ", font=("Times New roman", 16)).place(x=50, y=100)
    username = StringVar()
    Entry(tkWindow, textvariable=username).place(x=250, y=100)

    # password label and password entry box
    Label(tkWindow, text="Password :", font=("Times New roman", 16)).place(x=50, y=150)
    password = StringVar()
    Entry(tkWindow, textvariable=password, show='*').place(x=250, y=150)

    # login button
    loginButton = Button(tkWindow, text="Login", command=lambda: validateLogin(username,password), highlightcolor='Red',
                         relief=RAISED, font=("Times New roman", 16))
    loginButton.place(x=180, y=200)
    register = Button(tkWindow, text="Don't have an account, Register Now.",foreground='blue', command=registration, borderwidth=0, font=("Times New roman",12,'underline'))

    register.place(x=100,y=250)
    tkWindow.mainloop()


# Title and menu
Titlefont = font.Font(size=20)
Buttonfont = font.Font(size=15)
image = Image.open("Translate.jpg")
image_resize = image.resize((50, 50))
logo = ImageTk.PhotoImage(image_resize)
Label(Screen, image=logo).place(x=20, y=20)

image1 = Image.open("login.jpg")
image1_resize = image1.resize((152, 40))
loginbutton = ImageTk.PhotoImage(image1_resize)
Button(Screen, image=loginbutton, command=login, font=Buttonfont, borderwidth=0).place(x=1300, y=20)
Label(Screen, text="Language Translator",fg='#e63946' ,font=Titlefont, borderwidth=10).place(x=100, y=20)
InputLanguageChoiceMenu = OptionMenu(Screen, InputLanguageChoice, *inputlang)
InputLanguageChoiceMenu.config(font=Buttonfont)
Label(Screen, text="Choose a Language",fg='#457b9d', font=Buttonfont).place(x=20, y=90)
InputLanguageChoiceMenu.place(x=250, y=90)
image2 = Image.open("translate_symbol.jpg")
image2_resize = image2.resize((40, 40))
trans_sym = ImageTk.PhotoImage(image2_resize)
Label(Screen, image=trans_sym).place(x=700, y=85)

# choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen, TranslateLanguageChoice, *LanguageChoices)
Label(Screen, text="Translated Language",fg='#1d3557',font=Buttonfont).place(x=750, y=90)
NewLanguageChoiceMenu.config(font=Buttonfont)
NewLanguageChoiceMenu.place(x=1000, y=90)

TextVar = StringVar()
Entry(Screen, textvariable=TextVar, font=Buttonfont).place(x=20, y=130, width=720, height=400)
OutputVar = StringVar()
Entry(Screen, textvariable=OutputVar, font=Buttonfont).place(x=750, y=130, width=720, height=400)

# Button for calling function
Button(Screen, text="Translate", command=Translate, relief=GROOVE, font=Buttonfont, background='black',
       foreground='white').place(x=20, y=560)
menu = Screen.nametowidget(NewLanguageChoiceMenu.menuname)
menu.config(font=Buttonfont)
menu1 = Screen.nametowidget(InputLanguageChoiceMenu.menuname)
menu1.config(font=Buttonfont)
mainloop()
