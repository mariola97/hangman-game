import random

rijeci = [['The Godfather', 'The Dark Knight', 'Scarface', 'Gladiator', 'The Matrix', 'Goodfellas', 'Fight Club', 'Titanic', 'Joker', 'The Batman'],
          ['Minecraft', "Assassin's Creed", 'The Witcher 3', 'God Of War', 'Grand Theft Auto', 'Call of Duty', 'Elden Ring', 'Terraria', 'Red Dead Redemption', 'League of Legends'],
          ['Albert Einstein', 'Leonardo da Vinci', 'Elon Musk', 'Kanye West', 'Donald Trump', 'Cristiano Ronaldo', 'Jon Jones', 'Michael Jackson', 'The Rock', 'Rihanna'],
          ['Jack Daniels', 'Belvedere', 'Jagermeister', 'Bombay Sapphire', 'Bacardi', 'Hennessy', 'Clase Azul', 'Moet & Chandon', 'Johnnie Walker', 'Chivas']]
          

         # ['Minecraft", "Assassin's Creed", 'The Witcher 3', 'God Of War', 'Grand Theft Auto', 'Call of Duty', 'Elden Ring', 'Terraria', 'Red Dead Redemption', 'League of Legends']]
     #   [],
     #   []]
         
     #   [],
      #  []]
kategorije = {
"1": "Filmovi",
"2": "Igrice",
"3": "Poznate Osobe",
"4": "Alkoholna Pica"
print("Kategorije")
print("-
print("\n".join("{}. {}".format(k, v) for k, v in kategorije.items()))
odabirkategorije = int(input('Unesi broj odgovarajuce kategorije koji zelis pogadjati: '))
=
prikazkategorije str(odabirkategorije)
odabirKategorije -= 1
skrivenaRijec random.choice(rijeci [odabirkategorije])
skrRjLower = skrivenaRijec.lower()
print(skrivenaRijec)
otkrivanjeRijeci = ['_' if slovo.isalpha() else slovo for slovo in skrivenaRijec] #Postavlja se underscore za sva slova (ako su slova, a ako ne ostavlja se sta je prije bilo tjst. space
def updateOtkrivanje(slovo, skrRjLower, otkrivanjeRijeci): #Funkcija za updateanje slova u skrivenoj rijeci
update = False
for i, char in enumerate (skrRjLower): #Napravljen loop koji ide kroz svako slovo u skrivenoj rijeci if char == slovo:
otkrivanjeRijeci[i] = skrivenaRijec[i] update = True
return update
def provjera (otkrivanjeRijeci, skrivenaRijec): #Provjera je li korisnik pobjedio
return "".join(otkrivanjeRijeci)
==
skrivenaRijec