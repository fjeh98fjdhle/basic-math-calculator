from Funktion_berechnen import cleaning_fx
from Funktion_berechnen import restoring_func
from Funktion_berechnen import exchange_x
from engine import calculate



def collect_func():
    #list processing
    list = cleaning_fx()
    list = restoring_func(list)
    list = exchange_x(list)
    return list 

def start():
    list = collect_func()
    list = calculate(list)

    return list

a = start()
print(a)
