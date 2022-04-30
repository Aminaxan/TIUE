import tkinter as tk
from tkinter import *


class SampleApp(tk.Tk):

    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, Hotel, ROOMS, Conferences, Restaurants, photos, Help, ):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='nsew')

            self.show_frame('StartPage')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="pink")

        self.controller = controller
        self.controller.title('Hotel')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Hotel', font=('Candara', 50, 'bold'), fg='black', bg='pink')
        big_lable.pack(pady=30)

        login_lable = tk.Label(self, text='Entry login', font=('Candara', 15, 'bold'), bg='pink', fg='black')
        login_lable.pack(pady=30)

        my_login = tk.StringVar()
        login_entry = tk.Entry(self, textvariable=my_login, font=('Candara', 15, 'bold'), bg='pink', fg='black')
        login_entry.pack(pady=30)

        password_lable = tk.Label(self, text='Entry password', font=('Candara', 15, 'bold'), bg='pink', fg='black')
        password_lable.pack(pady=30)

        my_password = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=my_password, font=('Candara', 15, 'bold'), bg='pink', fg='black')
        password_entry.pack(pady=30)

        def check_password():
            if my_password.get() == '1' and my_login.get() == 'a':
                controller.show_frame('MenuPage')


            else:
                right_lable['text'] = 'Invalid password or login'

        password_button = tk.Button(self, text='Sign in', command=check_password,
                                    font=('Candara', 15, 'bold'), bg='pink', fg='black')
        password_button.pack()
        right_lable = tk.Label(self, font=('Candara', 15, 'bold'), bg='pink', fg='black')
        right_lable.pack(pady=30)


class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        self.controller = controller
        big_lable = tk.Label(self, text='Welcome in Hotel', font=('Candara', 50, 'bold'), fg='black',
                             bg='white')
        big_lable.pack(pady=30)
        big_lable.place(x=200, y=40)

        def get_Hotel():
            controller.show_frame('Hotel')

        contact_button = tk.Button(self, text="Hotel", command=(get_Hotel), font=('Candara', 20, 'bold'),
                                   fg='black', bg='white')
        contact_button.pack(pady=30)
        contact_button.place(x=10, y=500)

        def get_ROOMS():
            controller.show_frame('ROOMS')

        contact_button = tk.Button(self, text="Номера", command=(get_ROOMS), font=('Candara', 20, 'bold'),
                                   fg='black', bg='white')
        contact_button.pack(pady=30)
        contact_button.place(x=10, y=400)

        def get_Conferences():
            controller.show_frame('Conferences')

        contact_button = tk.Button(self, text="Конференции", command=(get_Conferences), font=('Candara', 20, 'bold'),
                                   fg='black', bg='white')
        contact_button.pack(pady=30)
        contact_button.place(x=10, y=300)

        def get_Restaurants():
            controller.show_frame('Restaurants')

        contact_button = tk.Button(self, text="Рестораны и бары", command=(get_Restaurants), font=('Candara', 20, 'bold'),
                                   fg='black', bg='white')
        contact_button.pack(pady=30)
        contact_button.place(x=10, y=200)

        def get_photos():
            controller.show_frame('photos')

        contact_button = tk.Button(self, text="Фотографии и отзывы", command=(get_photos), font=('Candara', 20, 'bold'),
                                   fg='black', bg='white')
        contact_button.pack(pady=30)
        contact_button.place(x=300, y=200)

        def get_Help():
            controller.show_frame('Help')

        contact_button = tk.Button(self, text="HELP", command=(get_Help), font=('Candara', 20, 'bold'), fg='black',
                                   bg='white')
        contact_button.pack(pady=30)
        contact_button.place(x=300, y=300)


class Hotel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="red")
        self.controller = controller
        self.controller.title('Hotel')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='ABOUT Hotel ', font=('Candara', 50, 'bold'), fg='white', bg='red')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='Отель Премиум Класса для Бизнеса и Отдыха \n',
                        font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=30)

        text = tk.Label(self,
                        text='Наши меры по обеспечению безопасности \n',
                        font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=30)

        text = tk.Label(self,
                        text='Удобства \n',
                        font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=30)

        big_lable = tk.Label(self, font=('Candara', 50, 'bold'), fg='white', bg='red')
        big_lable.pack(pady=30)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage, font=('Candara', 10, 'bold'), fg='white',
                                  bg='black')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)



class ROOMS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="red")
        self.controller = controller
        self.controller.title('Hotel')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Наши номера ', font=('Candara', 50, 'bold'), fg='white', bg='red')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='Одноместный номер \n', font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=30)

        text = tk.Label(self, text='Двухместный номер  \n', font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=50)

        text = tk.Label(self, text='Номера повышенной комфортности  \n', font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=50)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage, font=('Candara', 10, 'bold'), fg='black',
                                  bg='white')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)


class Conferences(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="red")
        self.controller = controller
        self.controller.title('Hotel')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Залы', font=('Candara', 50, 'bold'), fg='white', bg='red')
        big_lable.pack(pady=30)

        text = tk.Label(self, text='Tashkent \n', font=('Candara', 15, 'bold'), fg='white',
                        bg='red')
        text.pack(pady=10)

        text = tk.Label(self, text='Samarkand \n', font=('Candara', 15, 'bold'), fg='white', bg='red')
        text.pack(pady=10)

        text = tk.Label(self, text='Boardroom \n', font=('Candara', 15, 'bold'),
                        fg='white',
                        bg='red')
        text.pack(pady=10)

        text = tk.Label(self, text='Ballroom \n', font=('Candara', 15, 'bold'),
                        fg='white',
                        bg='red')
        text.pack(pady=10)

        text = tk.Label(self, text='Fergana \n', font=('Candara', 15, 'bold'),
                        fg='white',
                        bg='red')
        text.pack(pady=10)

        text = tk.Label(self, text='Bukhara \n', font=('Candara', 15, 'bold'),
                        fg='white',
                        bg='red')
        text.pack(pady=10)

        text = tk.Label(self, text='Bukhara2  \n', font=('Candara', 15, 'bold'),
                        fg='white',
                        bg='red')
        text.pack(pady=10)


        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage, font=('Candara', 10, 'bold'), fg='white',
                                  bg='black')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)


class Restaurants(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="red")
        self.controller = controller
        self.controller.title('Hotel')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Рестораны и бары', font=('Candara', 50, 'bold'), fg='white', bg='red')
        big_lable.pack(pady=30)

        text = tk.Label(self, text='Khiva Restaurant  \n',
                        font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=50)

        text = tk.Label(self, text='Sette Restaurant & Bar  \n',
                        font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=50)

        text = tk.Label(self, text='Chai Lounge   \n',
                        font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=50)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage, font=('Candara', 10, 'bold'), fg='white',
                                  bg='black')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)


class photos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="red")
        self.controller = controller
        self.controller.title('Hotel')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Фотографии и отзывы', font=('Candara', 50, 'bold'), fg='white', bg='red')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='Отель \n', font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=30)

        text = tk.Label(self, text='Номера  \n', font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=50)

        text = tk.Label(self, text='Питание  \n', font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=50)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage, font=('Candara', 10, 'bold'), fg='black',
                                  bg='white')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)


class Help(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="red")
        self.controller = controller
        self.controller.title('Hotel')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='HELP', font=('Candara', 50, 'bold'), fg='white', bg='red')
        big_lable.pack(pady=30)

        text = tk.Label(self, text='IF you have some problems call me    (998-94-651-80-92)  \n', font=('Candara', 20, 'bold'), fg='white', bg='red')
        text.pack(pady=50)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage, font=('Candara', 10, 'bold'), fg='white',
                                  bg='black')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)


if __name__ == '__main__':
    app = SampleApp()
    app.mainloop()

