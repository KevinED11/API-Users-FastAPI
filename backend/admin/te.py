import sys

reto = ("fizzbuzz" if number % 15 == 0
        else "fizz" if number % 3 == 0
        else "buzz" if number % 5 == 0
        else str(number)
        for number in range(1, 10000000))

print("expresión generadora")
print(sys.getsizeof(reto))
print(sys.getsizeof("\n".join(reto)))

print("expresion generadora en una linea junto con join")
print(sys.getsizeof("\n".join(("fizzbuzz" if number % 15 == 0
        else "fizz" if number % 3 == 0
        else "buzz" if number % 5 == 0
        else str(number)
        for number in range(1, 10000000)))))

lista = ["fizzbuzz" if number % 15 == 0
         else "fizz" if number % 3 == 0
         else "buzz" if number % 5 == 0
         else str(number)
         for number in range(1, 10000000)]

print("compression de listas")
print(sys.getsizeof(lista))
print(sys.getsizeof("\n".join(lista)))

print("comprenssion de listas junto con join en una línea")
print(sys.getsizeof("\n".join(["fizzbuzz" if number % 15 == 0
         else "fizz" if number % 3 == 0
         else "buzz" if number % 5 == 0
         else str(number)
         for number in range(1, 10000000)])))
