# tkinter chomp exempel
# Vahid Mosavat
# Redigerad av David Kaméus
# 2022-01-01

# använd din lösning till labb 4! byt ut chomp_functions mot filen dina funktioner ligger i (och se till att alla filer ligger i samma mapp som du kör programmet ifrån)
from labb4del2 import chomp, check_winner, create_chocolate_bar

from tkinter import * # importera alla bas-tkinter grejer
from tkinter.font import Font # importera Font klassen om du vill ändra typsnitt och textstorlekar
from tkinter.messagebox import showerror # messagebox är bra för att informera användaren om fel

# i den här filen förklaras inte tkinter koncepten helt, så jag rekommenderar starkt att läsa mer om det själv.

# bra referens för tkinter: https://tkdocs.com/shipman/
# lite gammal och refererar till python2 istället för 3, men förklarar tkinter delarna väl.

# mer uppdaterad tutorial: http://tkdocs.com/tutorial/index.html
# python-dokumentation för tkinter: https://docs.python.org/3/library/tkinter.html

# några länkar om koncept i den här filen:
# LabelFrame: https://tkdocs.com/shipman/labelframe.html
# Button: https://tkdocs.com/shipman/button.html
# Frame: https://tkdocs.com/shipman/frame.html
# Label: https://tkdocs.com/shipman/albel.html
# Entry: https://tkdocs.com/shipman/entry.html
# IntVar: https://tkdocs.com/shipman/control-variables.html
# Validation (onödigt avancerat): https://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter/4140988#4140988 

def play_the_turn(row, col, buttons, matrix, window):
    """
    Hantera spellogik för en runda.
    indata:
        row, col: det index i matrisen som spelaren klickat på
        buttons: matrisen med Button objekt, som faktiskt visas på skärmen
        matrix: den matris med strängar som chomp-spelet körs i
        window: den LabelFrame som knapparna visas inom, och vars text är vems tur det är 
    """
    if row == 0 and col == 0: # det går inte att äta den förgiftade biten, så om någon klickat här avbryter vi bara
        return 
    chomp(matrix, row, col) # ät den valda delen av chokladkakan i bakgrunden
    chomp_view(buttons,matrix) # ta bort de ätna delarna ur den grafiska representationen av chokladkakan
    
    # uppdatera vems tur det är och kolla om någon vunnit
    if check_winner(matrix): 
        player = current_player(window['text'])      
        window['text'] = f"Player {player} wins!!!"
    else:
        player = next_player(window['text'])
        window['text'] = f"Player {player}'s turn!"

def current_player(text):
    """
    Tar in en text på formen 'Player x's turn' där x är 1 eller 2 och returnerar x
    """
    return "1" if "1" in text else "2"

def next_player(text):
    """
    Tar in en text på formen 'Player x's turn' där x är 1 eller 2och returnerar den spelare som inte är x
    """
    return "2" if "1" in text else "1"

def create_graphic_chocolate_bar(window, matrix):
    """
    Genererar och placerar en matris med Button objekt utifrån en chomp-matris
    indata:
        window: en LabelFrame som knapparna ska visas i
        matrix: en färdig chomp-matris med siffersträngar för rad och kolumn eller ett P för den förgiftade biten
    """
    rows = len(matrix) # antalet radet i matrisen
    cols = len(matrix[0]) # alla rader kommer vara lika långa i början, så det räcker att bara kolla en av dem
    if rows < 0 or cols < 0: # något har gått fel om detta händer
        return 

    # använder listomfattningar (eng. List comprehensions) för att skapa spelbrädet
    # ekvivalent med:
    # buttons = []
    # for i in range(...):
    #     temp = []
    #     for j in range(...):
    #         temp.append(Button(...))
    #     buttons.append(temp)
    buttons = [
        [
            Button(
                window, # ange knappens master-objekt, så det går att hålla koll på widget-hierarkin
                font=Font(size=18), # jag använder bara fonten för att ange storlek, men det går att göra flera inställningar här 
                # i det här fallet bestämmer fonten även storleken på rutorna automatiskt, som även kan anges manuellt
                text=matrix[j-1][i-1].replace("P", "☠"), # ta strängen från chomp-matrisen som text och gör den förgiftade biten lite finare
                # använd lambda-uttryck för att säga vad som händer när man klickar på knappen.
                # bind variabler i lambdauttrycket om det är deras nuvarande värde som är viktigt (ex. loop-räknarna, i och j)
                command=lambda a = j, b = i: play_the_turn(a-1, b-1, buttons, matrix, window),
                disabledforeground="red", # ange en färg för de knappar som är avstängda. I det här exemplet är det bara en knapp som blir avstängd.
            ) 
            for i in range(1,cols+1)
        ] 
        for j in range(1,rows+1)
    ]
    # Många tkinter objekt kan indexeras som dictionaries. Annars finns configure metoden för det.
    buttons[0][0]['state'] = DISABLED # stäng av knappen för den förgiftade biten. DISABLED är en konstant som finns i tkinter modulen och den motsvarar strängen "disabled"

    # gör knapparna synliga och placera dem på rätt plats 
    for i, row in enumerate(buttons):
        for j, button in enumerate(row):
            button.grid(row=i,column=j)
  

def chomp_view(buttons, matrix):
    """
    Ta bort de knappar vars motsvarande sträng i chomp-matrisen blivit raderade
    indata:
        buttons: en matris av Button objekt
        matrix: den motsvarande chomp-matrisen
    """
    i=0
    while i < len(buttons):
        j=0
        while j < len(buttons[i]):
            if i >= len(matrix) or j>=len(matrix[i]):
                 buttons[i][j].grid_forget() # grid_forget säger åt grid systemet att ta bort widgeten
            j+=1
        i+=1

def intcheck(p):
    """
    Kollar att en sträng är ett tal eller tom
    """
    return p.isdigit() or p == ""

class GameGUI:
    """
    En klass som håller koll på knapparna, men mest reset-funktionerna.
    Det är inte nödvändigt att använda en klass här, men det kan vara lättare än att skicka med allt till alla funktioner
    om man också vill undvika globala variabler
    """
    def __init__(self, window, rows, cols):
        self.window = window
        self.rst_frame = Frame(window) # ett utrymme att ha reset-grejerna i
        # IntVar är en variabel som bara kan innehålla heltal
        self.rst_width_var = IntVar() 
        self.rst_height_var = IntVar()
        # skapa några rutor med texter som vi kan ha input-fälten i 
        self.rst_width_box = LabelFrame(self.rst_frame, text="Width")
        self.rst_height_box = LabelFrame(self.rst_frame, text="Height")
        # skapa input-fälten. Använd IntVar:arna för att spara det man skriver in i.
        # validate funktionaliteten är komplicerad, men gör så att det inte går att skriva in annat än heltal i input-fälten.
        # om du är intresserad kan du läsa mer om det här: https://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter/4140988#4140988
        self.rst_width_entry = Entry(self.rst_width_box, textvariable=self.rst_width_var, validate='key', validatecommand=(window.register(intcheck), "%P"))
        self.rst_height_entry = Entry(self.rst_height_box, textvariable=self.rst_height_var, validate='key', validatecommand=(window.register(intcheck), "%P"))
        # skapa en knapp som startar ett nytt spel när man klickar på den
        self.rst_btn = Button(self.rst_frame, text="New game", command=lambda: self.new_game())
    
        # skapa den LabelFrame som ska hålla koll på knapparna och vems tur det är
        self.chocolate_frame = LabelFrame(window, text="Player 1's turn!")
        # skapa en chomp-matris att utgå ifrån
        matrix = create_chocolate_bar(rows, cols)
        # skapa en grafisk representation av chomp-matrisen
        create_graphic_chocolate_bar(self.chocolate_frame, matrix)

        # placera och synliggör alla widgets
        self.chocolate_frame.grid(row=0, column=0) # denna hamnar direkt i window
        self.rst_frame.grid(row=1, column=0) # denna hamnar också direkt i window

        # dessa ligger i rst_frame, så de är oberoende av grid-systemet i window
        self.rst_btn.grid(row=0, column=0) 
        self.rst_width_box.grid(row=0, column=1)
        self.rst_height_box.grid(row=0, column=2)
        # dessa ligger i varsin LabelFrame, så de är oberoende av andra grid-system 
        self.rst_width_entry.grid(row=0, column=0) 
        self.rst_height_entry.grid(row=0, column=0)
    
    def new_game(self):
        """
        Starta ett nytt spel med den storlek man angivit
        """
        # hämta talen från IntVar:arna
        rows = self.rst_height_var.get()
        cols = self.rst_width_var.get()
        if rows < 2 or rows > 9 or cols < 2 or cols > 9: # kolla att spelplanen är i rimlig storlek
            showerror("Invalid game size", "Make sure game size is an integer in [2..10)") # meddela användaren att det är fel annars och avbryt metoden
            return
        self.chocolate_frame.destroy() # Ta bort den gamla rutan som höll koll på knappar och vems tur det är
        self.chocolate_frame = LabelFrame(self.window, text="Player 1's turn!") # skapa en ny sådan
        create_graphic_chocolate_bar(self.chocolate_frame, create_chocolate_bar(rows, cols)) # Gör en ny grafisk representation
        self.chocolate_frame.grid(row=0, column=0) # gör den synlig


def main():
    rows, cols = (6, 7)
    window = Tk() # skapa ett Tk objekt att utgå ifrån, öppna ett fönster
    window.title("Chomp Game") # sätt titeln på fönstret

    # skapa ett GUI-objekt som håller koll på alla widgets.
    # det är inte nödvändigt att ha en klass till GUI:n men det kan hjälpa när man ska hålla koll på flera saker och inte vill skicka dem mellan funktioner
    GameGUI(window, rows, cols) 
    
    window.mainloop() # fortsätt tills fönstret ska stängas

if __name__ == "__main__":
    main()


