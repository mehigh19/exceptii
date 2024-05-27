# Scrieti o functie care citeste un string de la tastatura si afiseaza lungimea lui. Tratati cazul in care textul nu este string
# Fiind dat un dictionar {"a":1,"b":2,"c":3} scrieti o functie care primeste ca parametru cheia si returneaza valoarea
# 5

def fc_string():
    try:
        n = input('Input a string: ')
        if n.isdigit():
            return 'Please introduce a valid string, not a number.'
        return len(n)
    except Exception as e:
        return f'An error occurred: {e}'


print(fc_string())