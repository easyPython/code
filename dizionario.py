python = dict()
python['soluzionediproblemi'] = 'SOLUZIONE DI PROBLEMI: Il procedimento di formulare un problema, trovare una soluzione ed esprimerla.'
python['linguaggiodialtolivello'] = 'LINGUAGGIO DI ALTO LIVELLO: Un linguaggio di programmazione come Python, progettato per essere facilmente leggibile e utilizzabile dagli uomini.'
python['linguaggiodibassolivello'] = 'LINGUAGGIO DI BASSO LIVELLO: Un linguaggio di programmazione che è progettato per essere facilmente eseguibile da un computer; è chiamato anche "linguaggio macchina" o "linguaggio assembly".'
python['portabilità'] = 'PORTABILITA: Caratteristica di un programma di poter essere eseguito su computer di tipo diverso.'
python['interprete'] = 'INTERPRETE: Un programma che legge un altro programma e lo esegue.'
python['prompt'] = 'PROMPT: Serie di caratteri mostrati dall’interprete per indicare che è pronto a ricevere input dall’utente.'
python['programma'] = 'PROGRAMMA: Serie di istruzioni che specificano come effettuare un’elaborazione.'
python['istruzionedistampa'] = 'ISTRUZIONE DI STAMPA: Istruzione che ordina all’interprete Python di visualizzare un valore sullo schermo.'
python['operatore'] = 'OPERATORE: Simbolo speciale che rappresenta un calcolo semplice come l’addizione, la moltiplicazione o il concatenamento di stringhe.'
python['valore'] = 'VALORE: Una unità fondamentale di dati, come un numero o una stringa, che un programma elabora.'
python['tipo'] = 'TIPO: Una categoria di valori.'
python['intero'] = 'INTERO: Tipo che rappresenta i numeri interi.'

ciclo = 0

while ciclo >= 0:
    
    keyinput = input('\n' 'Chiave? ')   #input dell'utente
    keyinput2 = ''.join(keyinput.split())   #rimuove gli spazi nell'input dell'utente
    keyinput3 = keyinput2.casefold()   #normalizza l'input per la ricerca case insensitive
    keyinput4 = keyinput.upper()   #trasforma l'input in lettere maiuscole per la stampa del risultato

    if keyinput == '':
        break
    else:
        if keyinput3 in python:
            print('\n{value}'.format(value=python[keyinput3]))
        else:
            print('\nLemma non presente')


"""for keys, values in python.items():
    print(keys.upper(), ': ', values, '\n', sep='')"""
