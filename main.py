import math


def func():
    formula = str(input('Обери формулу(P, A, C)? '))
    try:
        if formula == 'P':
            n = int(input('n = '))
            if n > 0:
                print('Відповідь:', math.factorial(n))
            else:
                print("'n' повинно бути більшим за нуль!")
                
        elif formula == 'A':
            n = int(input('n = '))
            k = int(input('k = '))
            if n > 0 and k > 0 and n > k:
                n_fak = math.factorial(n)
                n_min_k_fak = math.factorial(n-k)
                print('Відповідь:', n_fak/n_min_k_fak)
            else:
                print("'n' та 'k'повинні бути числами більшими за нуль, при чому n > k!")

        elif formula == 'C':
            n = int(input('n = '))
            k = int(input('k = '))
            if n > 0 and k > 0 and n > k:
                n_fak = math.factorial(n)
                k_fak = math.factorial(k)
                n_min_k_fak = math.factorial(n-k)
                znamennyk = n_min_k_fak * k_fak
                print('Відповідь:', n_fak/znamennyk)
            else:
                print("'n' та 'k'повинні бути числами більшими за нуль, при чому n > k!")


        else:
            print('Обери одну з трьох формул (P, A, C)')

    except ValueError:
        print("'n' та 'k'повинні бути числами більшими за нуль, при чому n > k!")
func()


while True:
    again_yes_or_no = input('Заново? [y/n]: ')

    if again_yes_or_no == 'y':
        func()
    else:
        break