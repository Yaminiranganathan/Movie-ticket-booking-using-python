import random

print('                                WELCOME TO BOOK MY SHOW                              ')

while True:
    print('''Choose your language to book a ticket for the movie:
      1. Tamil
      2. English''')
    
    while True:
        a = int(input('Enter your language: '))
        if a in [1, 2]:
            break  # valid input, exit the loop
        else:
            print('Invalid input. Please enter 1 for Tamil or 2 for English.')

    if a == 1:
        print('''List of Tamil movies available now:
          1. Alaipayuthe
          2. Ponniyin Selvan
          3. Ghilli
          4. Vinnai Thandi Varuvaya''')
        
        while True:
            b = int(input('Enter your movie for booking: '))
            if b in [1, 2, 3, 4]:
                break
            else:
                print('Invalid movie option. Please choose a valid movie.')

        if b == 1:
            print('''The locations available for Alaipayuthe movie are:
              1. Chennai
              2. Madurai
              3. Trichy
              4. Kanyakumari''')
        elif b == 2:
            print('''The locations available for Ponniyin Selvan movie are:
              1. Chennai
              2. Madurai
              3. Salem''')
        elif b == 3:
            print('''The locations available for Ghilli movie are:
              1. Chennai
              2. Tanjore''')
        elif b == 4:
            print('''The locations available for Vinnai Thandi Varuvaya movie are:
              1. Chennai
              2. Madurai''')

        while True:
            c = int(input('Choose your location for booking: '))
            if c in [1, 2, 3, 4]:
                break
            else:
                print('Invalid location. Please enter a valid option.')

        if c == 1:
            print('''List of theatres in Chennai:
                  1. Kamala Theatre
                  2. PVR
                  3. Inox
                  4. Rajkamal Cinemas''')
        elif c == 2:
            print('''List of theatres in Madurai:
                  1. Vetri Theatre
                  2. PVR
                  3. Kumaran Cinemas''')
        elif c == 3:
            print('''List of theatres in Trichy:
                  1. Sangeetha
                  2. PVR''')
        elif c == 4:
            print('''List of theatres in Kanyakumari:
                  1. Meenakshi Cinemas
                  2. Sathyam Cinemas''')

        while True:
            d = int(input('Choose your theatre: '))
            if d in [1, 2, 3, 4]:
                break
            else:
                print('Invalid theatre option. Please choose a valid theatre.')

        if d in [1, 3]:
            print('''Show timings available:
                      1. 10:00 AM
                      2. 3:00 PM
                      3. 9:00 PM''')
        elif d in [2, 4]:
            print('''Show timings available:
                      1. 9:30 AM
                      2. 2:30 PM
                      3. 7:00 PM''')

        while True:
            e = int(input('Choose your timing: '))
            if e in [1, 2, 3]:
                break
            else:
                print('Invalid timing. Please choose a valid timing.')

        print('''The ticket price available are:
                      1. 60 Rs
                      2. 120 Rs
                      3. 190 Rs''')

        while True:
            f = int(input('Choose your ticket price: '))
            if f in [1, 2, 3]:
                break
            else:
                print('Invalid price. Please choose a valid price.')

        print(f'''If you want to confirm the booking, 
               click '1' to continue
               click '0' to exit''')

        while True:
            g = int(input('Enter your choice to confirm: '))
            if g in [1, 0]:
                break
            else:
                print('Invalid input. Please enter 1 to confirm or 0 to exit.')

        if g == 1:
            otp = random.randrange(1500, 9999)
            print(f'The OTP for your ticket booking is: {otp}')
            print('Your ticket was successfully booked. Thank you for using Book My Show. Enjoy your movie!')
        elif g == 0:
            print('OOPS! You exited from the Book My Show movie booking.')
        break  # exit the loop after booking is done

    elif a == 2:
        print('''List of English movies available now: 
          1. Conjuring
          2. Titanic''')

        while True:
            b = int(input('Enter your movie for booking: '))
            if b in [1, 2]:
                break
            else:
                print('Invalid movie option. Please choose a valid movie.')

        if b == 1:
            print('''The locations available for Conjuring movie are:
              1. Chennai
              2. Madurai''')
        elif b == 2:
            print('''The locations available for Titanic movie are:
              1. Chennai
              2. Trichy''')

        while True:
            c = int(input('Choose your location for booking: '))
            if c in [1, 2]:
                break
            else:
                print('Invalid location. Please enter a valid option.')

        print('''List of theatres:
                  1. Kamala Theatre
                  2. PVR''')

        while True:
            d = int(input('Choose your theatre: '))
            if d in [1, 2]:
                break
            else:
                print('Invalid theatre option. Please choose a valid theatre.')

        print('''Show timings available:
                      1. 10:00 AM
                      2. 3:00 PM
                      3. 9:00 PM''')

        while True:
            e = int(input('Choose your timing: '))
            if e in [1, 2, 3]:
                break
            else:
                print('Invalid timing. Please choose a valid timing.')

        print('''The ticket price available are:
                      1. 60 Rs
                      2. 120 Rs
                      3. 190 Rs''')

        while True:
            f = int(input('Choose your ticket price: '))
            if f in [1, 2, 3]:
                break
            else:
                print('Invalid price. Please choose a valid price.')

        print(f'''If you want to confirm the booking, 
               click '1' to continue
               click '0' to exit''')

        while True:
            g = int(input('Enter your choice to confirm: '))
            if g in [1, 0]:
                break
            else:
                print('Invalid input. Please enter 1 to confirm or 0 to exit.')

        if g == 1:
            otp = random.randrange(1500, 9999)
            print(f'The OTP for your ticket booking is: {otp}')
            print('Your ticket was successfully booked. Thank you for using Book My Show. Enjoy your movie!')
        elif g == 0:
            print('OOPS! You exited from the Book My Show movie booking.')
        break  # exit the loop after booking is done
