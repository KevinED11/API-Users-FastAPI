print("\n".join(["fizzbuzz" if number % 15 == 0
                 else "fizz" if number % 3 == 0
                 else "buzz" if number % 5 == 0
                 else str(number)
                 for number in range(1,101)
                 ]))
