from tkinter import *
from functools import partial
import random


class MojeMenu(Frame):
    # funkcja inicjujaca caly program
    def __init__(self, menu):
        listaxow = []
        suma = 6000
        Frame.__init__(self, menu)
        self.configure(background='slate blue')
        self.grid()
        # wszystko widoczne z menu
        tekst = Label(self, text="MENU", height=6, width=50, fg="red", font='Verdana 18 bold', bg='slate blue')
        tekst.pack()
        Button(self, text="Nowa Gra", height=3, width=65, font='Verdana 15', fg='red', bg='medium slate blue',
               command=partial(self.gra, suma, listaxow)).pack()
        Button(self, text="Instrukcja", height=3, width=65, font='Verdana 15', fg='red', bg='medium slate blue',
               command=self.instrukcja).pack()
        Button(self, text="Tworcy", height=3, width=65, font='Verdana 15', fg='red', bg='medium slate blue',
               command=self.tworcy).pack()
        Button(self, text="Wyjdz", height=3, width=65, font='Verdana 15', fg='red', bg='medium slate blue',
               command=menu.destroy).pack()

    def wymiana(self, suma, listaxow):
        for widget in menu.winfo_children():
            widget.destroy()
        suma -= 2000
        print("%d", listaxow)
        listaxow.pop()
        print("%d", listaxow)
        wymiana = Label(menu, text="Pytanie zostanie zmienione", height=4, width=80, fg="red",
                             font='Verdana 18 bold', bg='slate blue')
        wymiana.pack()
        Button(menu, text="Okej", height=4, width=80, font='Verdana 18', fg='red', bg='medium slate blue',
               command=partial(self.gra, suma, listaxow)).pack()



    # funckja sprawdzajaca poprawnosc odpowiedzi
    def poprawna(self, pytanie, odpowiedz, x, suma, listaxow):
        for widget in menu.winfo_children():
            widget.destroy()
        if odpowiedz == pytanie[4 + x][0]:
            suma += 2000
            sprawdzenie = Label(menu, text="Odpowiedz poprawna", height=4, width=80, fg="red",
                             font='Verdana 18 bold', bg='slate blue')
            sprawdzenie.pack()
            sumatekst = Label(menu, text="Stan konta: " + str(suma), height=4, width=80, fg="red",
                              font='Verdana 18 bold', bg='slate blue')
            sumatekst.pack()
            Button(menu, text="Okej", height=4, width=80, font='Verdana 18', fg='red', bg='medium slate blue',
                   command=partial(self.gra, suma, listaxow)).pack()
        else:
            suma -= 3000
            sprawdzenie = Label(menu, text="Odpowiedz niepoprawna", height=4, width=80, fg="red",
                             font='Verdana 18 bold', bg='slate blue')
            sprawdzenie.pack()
            sumatekst = Label(menu, text="Stan konta: " + str(suma), height=4, width=80, fg="red",
                              font='Verdana 18 bold', bg='slate blue')
            sumatekst.pack()
            Button(menu, text="Okej", height=4, width=80, font='Verdana 18', fg='red', bg='medium slate blue',
                   command=partial(self.gra, suma, listaxow)).pack()

    # funckja wyswietlajaca pytania i odpowiedzi, oraz konczaca gre
    def gra(self, suma, listaxow):
        for widget in menu.winfo_children():
            widget.destroy()
        menu.configure(background='slate blue')

        x = (random.randrange(0, 495, 5))
        # przez to zmniejszam szanse na powtorzenie pytania
        for s in listaxow:
            if s == x:
                x = (random.randrange(0, 495, 5))

        listaxow.append(x)

        with open('pytania.txt', 'r') as notatnik:
            pytanie = notatnik.readlines()
            nrpytania = Label(menu, text="Pytanie nr " + str(len(listaxow)), height=4, width=80, fg="red", font='Verdana 20 bold',
                           bg='slate blue')
            nrpytania.pack()
            tekst1 = Label(menu, text=pytanie[x], height=4, width=100, fg="red", font='Verdana 20 bold',
                           bg='slate blue')
            tekst1.pack()
            Button(menu, text=pytanie[x + 1], height=4, width=100, fg="red", font='Verdana 18',
                    bg='medium slate blue', command=partial(self.poprawna, pytanie, "a", x, suma, listaxow)).pack()
            Button(menu, text=pytanie[x + 2], height=4, width=100, fg="red", font='Verdana 18',
                   bg='medium slate blue', command=partial(self.poprawna, pytanie, "b", x, suma, listaxow)).pack()
            Button(menu, text=pytanie[x + 3], height=4, width=100, fg="red", font='Verdana 18',
                   bg='medium slate blue', command=partial(self.poprawna, pytanie, "c", x, suma, listaxow)).pack()
            if(suma > 2000):
                Button(menu, text="Wymiana pytania", height=4, width=100, fg="red", font='Verdana 18',
                    bg='medium slate blue', command=partial(self.wymiana, suma, listaxow)).pack()

        if (len(listaxow)>10 or suma<=0):
            for widget in menu.winfo_children():
                widget.destroy()
            if (suma < 0):
                suma = 0
            koniecgry = Label(menu, text="Koniec gry", height=4, width=80, fg="red", font='Verdana 20 bold',
                           bg='slate blue')
            if (suma > 0):
                stankonta = Label(menu, text="Gratulacje, udalo Ci sie wygrac " + str(suma), height=4, width=80, fg="red",
                                  font='Verdana 20 bold', bg='slate blue')
                stankonta.pack()
            if (suma == 0):
                stankonta = Label(menu, text="Niestety, Twoj koncowy stan konta to " + str(suma), height=4, width=80,
                                  fg="red", font='Verdana 20 bold', bg='slate blue')
                stankonta.pack()

            koniecgry.pack()
            Button(menu, text="Wyjdz", height=4, width=80, font='Verdana 20', fg='red', bg='medium slate blue',
                   command=menu.destroy).pack()

    # funkcja wyswietlajaca tworcow
    def tworcy(self):
        tworcy = Toplevel(menu)
        tworcy.title("Tworcy")
        tekst = Label(tworcy, text="Michal Bubel, Dawid Ciochon", height=6, width=50, fg="red", font='Verdana 18 bold',
                      bg='slate blue')
        tekst.pack()
        Button(tworcy, text="Wyjdz", height=3, width=65, font='Verdana 15', fg='red',
                           bg='medium slate blue', command=tworcy.withdraw).pack()

    # funkcja wyswietlajaca instrukcje
    def instrukcja(self):
        instrukcja = Toplevel(menu)
        instrukcja.title("Instrukcja")
        tekst = Label(instrukcja, text="""Instrukcja gry: 
        Tematem projektu jest gra w stylu milionerzy,
    ktorej zasady sa nastepujace: gracz otrzymuje na wejsciu 6000,
    kazda poprawna odpowiedz to 2000, natomiast niepoprawna to strata 3000, a
    wymiana pytania to strata 2000. Pytania losowane sa z puli, a gra toczy 
    sie do momentu, gdy gracz odpowie poprawnie na 10 pytan lub nie bedzie 
    mial na koncie punktow.""", height=10, width=95, fg="red",
                      font='Verdana 18 bold', bg='slate blue')
        tekst.pack()
        Button(instrukcja, text="Wyjdz", height=3, width=124, font='Verdana 15', fg='red',
               bg='medium slate blue', command=instrukcja.withdraw).pack()


menu = Tk()
menu.title("Milionerzy")
app = MojeMenu(menu)
menu.mainloop()
