import random

rijeci = [['The Godfather', 'The Dark Knight', 'Scarface', 'Gladiator', 'The Matrix', 'Goodfellas', 'Fight Club', 'Titanic', 'Joker', 'The Batman'],
          ['Minecraft', "Assassin's Creed", 'The Witcher 3', 'God Of War', 'Grand Theft Auto', 'Call of Duty', 'Elden Ring', 'Terraria', 'Red Dead Redemption', 'League of Legends'],
          ['Albert Einstein', 'Leonardo da Vinci', 'Elon Musk', 'Kanye West', 'Donald Trump', 'Cristiano Ronaldo', 'Jon Jones', 'Michael Jackson', 'The Rock', 'Rihanna'],
          ['Jack Daniels', 'Belvedere', 'Jagermeister', 'Bombay Sapphire', 'Bacardi', 'Hennessy', 'Clase Azul', 'Moet & Chandon', 'Johnnie Walker', 'Chivas']]   

kategorije = {
  "1": "Filmovi",
  "2": "Igrice",
  "3": "Poznate Osobe",
  "4": "Alkoholna Pica"
}

print("Kategorije")
print("--------------")
print("\n".join("{}. {}".format(k, v) for k, v in kategorije.items()))
odabirKategorije = int(input('Unesi broj odgovarajuce kategorije koji zelis pogadjati: '))
prikazKategorije = str(odabirKategorije)
skrivenaRijec = random.choice(rijeci[odabirKategorije-1])
skrRjLower = skrivenaRijec.lower()
print(skrivenaRijec)
otkrivanjeRijeci = ['_' if slovo.isalpha() else slovo for slovo in skrivenaRijec] #Postavlja se underscore za sva slova (ako su slova, a ako ne ostavlja se sta je prije bilo tjst. space

def updateOtkrivanje(slovo, skrRjLower, otkrivanjeRijeci): #Funkcija za updateanje slova u skrivenoj rijeci
  update = False
  for i, char in enumerate (skrRjLower): #Napravljen loop koji ide kroz svako slovo u skrivenoj rijeci if char == slovo:
    if char == slovo:
      otkrivanjeRijeci[i] = skrivenaRijec[i]
      update = True
  return update

def provjera (otkrivanjeRijeci, skrivenaRijec): #Provjera je li korisnik pobjedio
  return "".join(otkrivanjeRijeci) == skrivenaRijec

def prikazStanja(otkrivanjeRijeci):
  return " ".join(otkrivanjeRijeci)

pokusaji = 0
netocnaSlova = []
while True:
  print(f"Kategorija {kategorije[prikazStanja]}")
  print(f"\n{prikazStanja(otkrivanjeRijeci)}")
  unosSlova = input("\nUnesi slovo: ").lower()
  if unosSlova in netocnaSlova or unosSlova in "".join(otkrivanjeRijeci):
    print("Vec si iskoristio to slovo.")
    continue
  
  updated = updateOtkrivanje(unosSlova, skrRjLower, otkrivanjeRijeci)
  
  if not updated:
    netocnaSlova.append(unosSlova)
    print(f"\n'{unosSlova}' nije u rijeci. \n")
    pokusaji += 1
  
  if pokusaji == 6:
    print("Iskoristio si sve pokusaje. Igra je gotova.")
    break
  
  if provjera(otkrivanjeRijeci, skrivenaRijec):
    print(prikazStanja(otkrivanjeRijeci))
    print("Cestitam! Pogodio si rijec.")
    break
  else:
    print(f"\nBroj netocnih pokusaja {pokusaji}")
    print(f"Netocan slova koja su vec probana: {', '.join(netocnaSlova)}\n")