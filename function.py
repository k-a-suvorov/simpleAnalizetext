try:
    import pyperclip
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    from time import sleep
    import sys
    import os
except ImportError:
    print("Ошибка загрузки модулей, исправьте код программы!")

try:    
    def help():
    # Function help
        print(Fore.YELLOW, Style.BRIGHT + "")
        print(	''' 1. Выберете в меню с каким языковым текстом из буфера обмена вы хотите работать.
                2. Скопируйте его в буфер обмена.
                3. выберет из меню русский или английский язык и нажмите "\Enter\"
                4. Посмотрите на результат.''')
            
    def enClipPaste():
    # Function insert english text
        count_w = 0
        count_c = 0
        text = pyperclip.paste()
        print(text)
        text = text.lower()
        consonants = set("bcdfghjklmnpqrstvwxyz")
        wowels = set("aeiou")
        for letter in text:
            if letter in wowels:
                count_w +=1
                print(f"count of wowels is {count_w}")
        for letter in text:
           if  letter in consonants:
            count_c +=1
        for letter in text:
            if (letter not in text and letter not in consonants and letter != text.isdigit()):
                print('Пожалуйста, выберете правильный язык текста для буфера обмена')
                softMenu()
        print(f"count of consonants is {count_c}") 
        print ("Length (simbols) : %d" % len (text))
        print(f"All words in buffer text is {len(text.split())}")
        

    def ruClipPaste():
    # Function insert russian text
        count_w = 0
        count_c = 0
        text = pyperclip.paste()
        print(text)
        text = text.lower()
        consonants = set("бвгджзйклмнпрстфхцчшщ")
        wowels = set("аоуыэяёюие")
        for letter in text:
            if letter in wowels:
                count_w +=1
                print(f"Число гласных - {count_w}")
        for letter in text:
            if  letter in consonants:
                count_c +=1
        for letter in text:
            if (letter not in text and letter not in consonants and letter != text.isdigit()):
                print('Пожалуйста, выберете правильный язык текста для буфера обмена')
                softMenu()
        print(f"Число согласных - {count_c}") 
        print ("Length (simbols) : %d" % len (text))
        print(f"Всего слов в тексте из буфера {len(text.split())}")

    def animationLoad():
    # Function animation Load
        start = ['L', 'o', 'a', 'd', 'i', 'n', 'g', '.', '.', '. ']
        print(Fore.RED + ' ')
        sleep(0.1)
        for i in range(0, len(start)):
            sleep(0.1)
            print(Fore.CYAN, Style.BRIGHT + " ", start[i], end="")

    def animationShut():
    # Function animation Shutdown
        start = ['S', 'h', 'u', 't', 'd', 'o', 'w', 'n ', '.', '.', '. ']
        print(Fore.RED + ' ')
        sleep(0.1)
        for i in range(0, len(start)):
            sleep(0.1)
            print(Fore.RED, Style.BRIGHT + " ", start[i], end="")

    # Function clear of screen
    def clearScreen():
        if (os.name == 'nt'):
            sleep(2)
            os.system('cls')
        elif (os.name == 'posix'):
            sleep(2)
            os.system('clear')
        else:
            print(Fore.WHITE, Back.RED + 'Other OS NOT SUPPORTED!')
            clearScreen()
            sys.exit()

    def sartSoft():
    # Function Start Software
        animationLoad()
        softMenu()
        
    def softMenu():
    # Function main menu
        clearScreen()
        print(Fore.GREEN, Style.BRIGHT + 'Добро пожаловать в меню программы. \nВыберете один из пунктов менюЖ')
        print()
        help()
        switch = int(input('1 - Работать с программой \n 2 - Выйти из программы \n>>> '))
        if (switch < 1) or (switch > 2):
            errorInputMessage()
        elif switch == 2:
            confirmForExit()
        elif switch == 1:
            langMenu()
            
    def langMenu():
    # Function language text menu 
        clearScreen()
        print(Fore.GREEN, Style.BRIGHT + 'Выдерете язык текста буфера обмена') 
        print()
        switch = int(input('1 - Русский \n 2 - Английский \n 3 - Вернуться к началу программы\n>>> '))
        if (switch < 1) or (switch > 3):
            errorInputMessage()
        elif switch == 3:
            softMenu()
        elif switch == 2:
            enClipPaste()
        elif switch == 1:
            ruClipPaste()
            confirmForExit()
            
    def confirmForExit():
    # Function language text menu 
        print('Вы точно хотите выйти из программы?')
        print()
        switch = int(input('Нажмите 2, что бы выйти \n1 - что бы работать с текстом.\n>>> '))
        if (switch < 1) or (switch > 2):
            errorInputMessage()
        elif switch == 2:
            exitSoft()
        elif switch == 1:
            softMenu()
            
    def exitSoft():
    # Function exit program
        print(Fore.RED, Style.BRIGHT + 'До свидания!')
        animationShut()
        clearScreen()
        sys.exit()
        
    def errorInputMessage():
    # Function error message 
        print(Fore.RED, Style.BRIGHT + 'Выбрано некорректное значение, пожалуйста, исправьте ошибку!')
        softMenu()
except ValueError:
    print("Некоректное вводимое значение!")
except TypeError:
    print("Ошибка типа данных!")
except SystemError:
    print("Общая системная ошибка!")
except BufferError:
    print("Ошибка работы буфера обмена!")
