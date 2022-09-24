# Laboration 5 - Minimodul med class och metoder

class TV:
    '''en klass med attribut, och metoder som användes i filen TV_simulator'''

    #skapar attributen för alla objekten som skapas av klass TV
    def __init__(self, tv_name, max_channel, current_channel, max_volume, current_volume):
        self.tv_name = tv_name
        self.max_channel = max_channel
        self.current_channel = current_channel
        self.max_volume = max_volume
        self.current_volume = current_volume

    #metod som byter kanal om till anviven kanal om den kanalen finns på den tvn
    def change_channel(self, new_channel):
        if 0 < new_channel <= self.max_channel:
            self.current_channel = new_channel
            return True 
        else:
            return False

    #metod som ökar ljudvolymen till vald tv om volymen är mindre än maxvolymen
    def increase_volume(self):
        if self.current_volume < self.max_volume:
            self.current_volume += 1
            return True
        else:
            return False

    #metod som sänker ljudvolymen till vald tv om volymen är större än 0
    def decrease_volume(self):
        if self.current_volume > 0:
            self.current_volume -= 1 
            return True
        else:
            return False

    #metod som skapar en string som skriver ut tvns namn
    def __str__(self):
        return self.tv_name

    #metod som skapar en string som skriver ut tvns nuvarande kanal och ljudvolym
    def str_for_tv(self):
        return self.tv_name + "\nKanal: " + str(self.current_channel) + "\nVolym: " + str(self.current_volume) 

    #metod som skapar en string som skriver ut all information som finns om vald tv
    def str_for_file(self):
        return self.tv_name + "," + str(self.max_channel) + "," + str(self.current_channel) + ","+str(self.max_volume) + "," + str(self.current_volume)
