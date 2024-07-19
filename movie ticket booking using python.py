#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('                                WELCOME TO BOOK MY SHOW                              ')
print(''' Choose you language to book a ticket for the movie:
      1.Tamil
      2.English''')
a=int(input('Enter your language: '))
if a==1:
    print('''List of tamil movies availabe now :
          1.Alaipayuthe
          2.Ponniyin Selvan
          3.Ghilli
          4.Vinnai thandi Varuvaya''')
    b=int(input('Enter your movie for booking: '))
    if b==1:
        print('''The locations available for alaipayuthe movie are:
              1.Chennai
              2.Madurai
              3.Trichy
              4.kanyakumari''')
    elif b==2:
         print('''The locations available for Ponniyin selvan movie are:
              1.Chennai
              2.Madurai
              3.Salem''')
    elif b==3:
        print('''The locations available for ghilli movie are:
              1.Chennai
              2.Tanjore''')
    elif b==4:
        print('''The locations available for alaipayuthe movie are:
              1.Chennai
              2.Madurai
              ''')
    else:
        print('Enter a valid location............!!!!!!')
    
    c=int(input('Choose your location for booking:'))
    if c==1 or c==3:
        print('''List of theatres in chennai to watch alaipayuthe movie:
                  1.Kamala theatre
                  2.PVR
                  3.Inox
                  4.Rajkamal cinemas''')
    elif c==2 or c==4:
        print('''List of theatres in chennai to watch alaipayuthe movie:
                  1.Vetri theatre
                  2.PVR
                  3.Kumaran cinemas ''')
    else:
        print('Enter the valid theatre...!!!!!!!')
        
    d=int(input('choose your theatre:'))
    if d==1 or d==3:
        print('''Show timings available are:
                      1. 10.a.m
                      2. 3.a.m
                      3. 9.p.m''')
    elif d==2 or d==4 or d==5:
        print('''Show timings available are:
                      1. 9.30.a.m
                      2. 2.30.a.m
                      3. 7.p.m''')
    else:
        print(' enter a valid timing...!!!!')
    
    
    e=int(input('choose your timing:'))
    if e==1 or e==3:
        print('''The ticket price available are:
                      1.60 rs
                      2.120 rs
                      3.190 rs''')
    elif e==2:
        print('''The ticket price available are:
                      1.110 rs
                      2.190 rs''')
    else:
        print('Enter valid price:')
    

    f=int(input('Choose your ticket price: '))


    print(f'''
                          
        If you want to confirm the booking , 
        click '1' for continue
        click '0' for exit''')
    g=int(input('Enter your choice to confirm: '))
    if g==1:
        import random
        otp=random.randrange(1500,9999)
        print('The OTP for your ticket booking is:',otp)
        print('Your ticket was successfully booked. Thank you for using bookmyshow. Enjoy your movie..!!!!')
    elif g==0:
        print('OOPS! You exit from the bookmyshow movie booking')
    
                    
            
if a==2:
    print('''List of tamil movies availabe now : 
    1.Conjuring
    2.Titanic''')
    b=int(input('Enter your movie for booking: '))
    if b==1:
        print('''The locations available for alaipayuthe movie are:
              1.Chennai
              2.Madurai''')
    elif b==2:
        print('''The locations available for alaipayuthe movie are:
              1.Chennai
              2.Trichy''')
    c=int(input('Choose your location for booking:')) 
    if c==1 or c==2:
        print('''List of theatres in chennai to watch alaipayuthe movie:
                  1.Kamala theatre
                  2.PVR''')
    else:
        print('Enter the valid theatre...!!!!!!!')
    
    d=int(input('choose your theatre:'))
    if d==1 or d==2:
        print('''Show timings available are:
                      1. 10.a.m
                      2. 3.a.m
                      3. 9.p.m''')
    else:
        print(' enter a valid timing...!!!!')
    
    e=int(input('choose your timing:'))
    if e==1 or e==2 or e==3:
        print('''The ticket price available are:
                      1.60 rs
                      2.120 rs
                      3.190 rs''')
    else:
        print('Enter valid price:')
    

    f=int(input('Choose your ticket price:'))


    print(f'''If you want to confirm the booking , 
           click '1' for continue
           click '0' for exit''')
    g=int(input('Enter your choice to confirm: '))
    if g==1:
        import random
        otp=random.randrange(1500,9999)
        print(f'''The OTP for your ticket booking is:'{otp}
               Your ticket was successfully booked. Thank you for using bookmyshow. Enjoy your movie..!!!!''')
    elif g==0:
        print('OOPS! You exit from the bookmyshow movie booking')

            


# In[ ]:





# In[ ]:




