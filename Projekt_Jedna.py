"""první projekt do Engeto Online Python Akademie
autor:Tomáš Dušátko
emial:mumlan02@seznam.cz
discord:3chester#0023"""

texts = [
    """Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley.""",
    """At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present."""
]
users={'bob':'123',
       'ann':'pass123',
       'mike':'password123',
       'liz':'pass123',
       }

username= input("Jaké je vaše jméno?\n")
if username in users:
    password= input("jaké je vaše heslo?\n")

if username not in users:
    print("uživatelské jéno nebylo nalezeno program se ukončuje")
else:
    if users[username] == password:
        print(f"Ahoj {username}!")
        print("Vyberte text napsáním čísla 1 až 3:")
        choice = input()
        
        if not choice.isdigit() or not (1<= int(choice) <=len(texts)):
            print("program se ukončuje z duvodu zadání nesprávného čísla")
        else:
            text = texts[int(choice) - 1]
            print(f"Vybraný text:\n{text}")
            
            words = text.split()
            pocet_slov = len(words)
            pocet_slov_zacinajici_velkym_p = sum(1 for word in words if word[0].isupper() and word[0].isalpha())
            pocet_slov_velkymi_p = sum(1 for word in words if word.isupper() and word.isalpha())
            pocet_slov_malymi_p = sum(1 for word in words if word.islower())
            pocet_cisel = sum(1 for word in words if word.isdigit())
            soucet_vsech_cisel= sum(int(word) for word in words if word.isdigit())

            print(f"Počet slov: {pocet_slov}")
            print(f"Počet slov začínající velkým písmenem: {pocet_slov_zacinajici_velkym_p}")
            print(f"Počet slov velkými písmeny: {pocet_slov_velkymi_p}")
            print(f"počet slov mylými písmeny: {pocet_slov_malymi_p}")
            print(f"Počet čísel: {pocet_cisel}")
            print(f"součet všech čísel je: {soucet_vsech_cisel}")
            
            word_lengths = {}
            for word in words:
                clean_word = ''.join(char for char in word if char.isalnum())
                length=len(clean_word)
                if length in word_lengths:
                    word_lengths[length] += 1
                else:
                    word_lengths[length] = 1
            
            print("Četnost délek slov:")
            for length in sorted(word_lengths):
                print(f"{length}|{'*' * word_lengths[length]}|{word_lengths[length]}")
            
    else:
        print("zadané heslo je špatně program se ukoncí.")