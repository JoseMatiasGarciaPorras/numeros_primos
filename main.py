from math import factorial


def is_primo(number):
    # if number == 1:
    #     return False
    # else:
    #     contador = 0
    # for i in range(1, number + 1):
    #     if i == 1 or i == number:
    #         continue
    #     elif number % i == 0:
    #         contador += 1
    #
    # if contador == 0:
    #     return True
    # else:
    #     return False
    factorial_number = factorial(number - 1) + 1
    if factorial_number % number == 0:
        return True
    else:
        return False


def run():
    number = int(input('Introduce un número: '))
    if is_primo(number):
        print('{} es primo'.format(number))
    else:
        print('{} no es primo'.format(number))



if __name__ == '__main__':
    run()
