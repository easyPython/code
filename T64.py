print("Una variabile è un nome che si riferisce a un valore.\n\n\
L'istruzione di assegnazione crea una nuova variabile e le assegna un valore.\n\n\
Esempio:\n\n\
x = 'Come va?'\n")

n = 0

while n >= 0:

    keyinput = input("Prova ad assegnare una stringa a una variabile 'x'\n\n")

    keyinput = keyinput.casefold() 

    if keyinput.startswith("x='") and keyinput.endswith("'") and isinstance(keyinput, str):
        print('ok')
    elif keyinput.startswith("x = '") and keyinput.endswith("'") and isinstance(keyinput, str):
        print('ok')
    elif keyinput.startswith('x="') and keyinput.endswith('"') and isinstance(keyinput, str):
        print('ok')
    elif keyinput.startswith('x = "') and keyinput.endswith('"') and isinstance(keyinput, str):
        print('ok')
            
    else:
        print('no')
