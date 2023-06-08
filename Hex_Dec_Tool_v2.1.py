'''
This is a tool to convert between Binary, Hexadecimal, and decimal.
Also it does have Logic operations Menu for AND, OR, NOT, XOR operations.
And Addition, Subtraction Menu for + and - operations.
Option 7 in the main menu will print all the numbers in binary, hexadecimal, and decimal.
''' 
import os

os.system("") # enables ansi escape characters in terminal

class TerminalColors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    RESET = '\033[0m'

binary_size = 32
dec_1_calc, j = 0, 0
binary_1 = []

print(TerminalColors.BRIGHT_GREEN + '\nThis is a tool where you can print\n')

def Hex_to_Dec(): # convert hex to dec
    try:
        hex_1 = hex(int(input(TerminalColors.BRIGHT_WHITE + 'Enter a hex number: ' + TerminalColors.BRIGHT_GREEN), 16))
        print('\n' + TerminalColors.BRIGHT_WHITE + hex_1,'=', int(hex_1, 16))
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid hexadecimal numbers. Try again' + TerminalColors.RESET)    
    print(TerminalColors.BRIGHT_CYAN + '\n-------Main Menu-------\n')

def convert_binary(dec_1): # this function is used to convert to binary 
    global binary_size, dec_1_calc, j, binary_1
    dec_1_calc = dec_1
    binary_1 = []
    print(TerminalColors.BRIGHT_WHITE, end = '')
    for i in range(binary_size):
        if(dec_1_calc % 2 == 0):
            binary_1.append(0)
        else:   
            binary_1.append(1) 

        dec_1_calc = dec_1_calc // 2

    for i in range(binary_size):
        if j == 4:
            print(' ', end = '')
            print(binary_1[binary_size - i - 1], end = '')
            j = 1
        else:        
            print(binary_1[binary_size - i - 1], end = '')     
            j += 1

def Sum_Hex(): # add two hex numbers
    try:
        hex_1 = hex(int(input(TerminalColors.BRIGHT_WHITE + 'Enter the first hexadecimal number: ' + TerminalColors.BRIGHT_GREEN), 16))
        hex_2 = hex(int(input(TerminalColors.BRIGHT_WHITE + 'Enter the second hexadecimal number: ' + TerminalColors.BRIGHT_GREEN), 16))
        total = hex(int(hex_1,16) + int(hex_2, 16))
        print('\n' + TerminalColors.BRIGHT_WHITE + hex_1, '+', hex_2, '=', total)
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid hexadecimal numbers. Try again' + TerminalColors.RESET)     

def Sub_Hex(): # Subtract two hex numbers
    try:
        hex_1 = hex(int(input(TerminalColors.BRIGHT_WHITE + 'Enter the first hexadecimal number: ' + TerminalColors.BRIGHT_GREEN), 16))
        hex_2 = hex(int(input(TerminalColors.BRIGHT_WHITE + 'Enter the second hexadecimal number: ' + TerminalColors.BRIGHT_GREEN), 16))
        total = hex(int(hex_1,16) - int(hex_2, 16))
        print('\n' + TerminalColors.BRIGHT_WHITE + hex_1, '-', hex_2, '=', total)
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid hexadecimal numbers. Try again' + TerminalColors.RESET)     

def Sum_Dec(): # add two dec numbers
    try:
        dec_1 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the first decimal number: ' + TerminalColors.BRIGHT_GREEN))
        dec_2 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the second decimal number: ' + TerminalColors.BRIGHT_GREEN))
        total = dec_1 + dec_2
        print('\n' + TerminalColors.BRIGHT_WHITE + str(dec_1), '+', str(dec_2), '=', str(total))
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid decimal numbers. Try again' + TerminalColors.RESET)     

def Sub_Dec(): # Subtract two dec numbers
    try:
        dec_1 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the first decimal number: ' + TerminalColors.BRIGHT_GREEN))
        dec_2 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the second decimal number: ' + TerminalColors.BRIGHT_GREEN))
        total = dec_1 - dec_2
        print('\n' + TerminalColors.BRIGHT_WHITE + str(dec_1), '-', str(dec_2), '=', str(total))
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid decimal numbers. Try again' + TerminalColors.RESET)       

def Sum_Binary():
    dec_total_1, dec_total_2 = 0, 0
    try:
        binary_1 = input(TerminalColors.BRIGHT_WHITE + 'Enter the first a binary number: ' + TerminalColors.BRIGHT_GREEN)
        binary_1_length = len(binary_1)
        binary_2 = input(TerminalColors.BRIGHT_WHITE + 'Enter the second binary number: ' + TerminalColors.BRIGHT_GREEN)
        binary_2_length = len(binary_2)
        for i in range(binary_1_length): 
            dec_total_1 += int(binary_1[binary_1_length - i - 1]) * 2**i
        for i in range(binary_2_length): 
            dec_total_2 += int(binary_2[binary_2_length - i - 1]) * 2**i  
        total = dec_total_1 + dec_total_2 
        print('\n' + TerminalColors.BRIGHT_WHITE + binary_1, '+', binary_2, '= ', end = '') 
        convert_binary(total)    
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid binary number. Try again' + TerminalColors.RESET)      

def Sub_Binary():
    dec_total_1, dec_total_2 = 0, 0
    try:
        binary_1 = input(TerminalColors.BRIGHT_WHITE + 'Enter the first a binary number: ' + TerminalColors.BRIGHT_GREEN)
        binary_1_length = len(binary_1)
        binary_2 = input(TerminalColors.BRIGHT_WHITE + 'Enter the second binary number: ' + TerminalColors.BRIGHT_GREEN)
        binary_2_length = len(binary_2)
        for i in range(binary_1_length): 
            dec_total_1 += int(binary_1[binary_1_length - i - 1]) * 2**i
        for i in range(binary_2_length): 
            dec_total_2 += int(binary_2[binary_2_length - i - 1]) * 2**i  
        total = dec_total_1 - dec_total_2 
        print('\n' + TerminalColors.BRIGHT_WHITE + binary_1, '-', binary_2, '=', end = '') 
        convert_binary(total)     
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid binary number. Try again' + TerminalColors.RESET)         

def Dec_to_Hex(): # convert dec to hex
    try:
        dec_1 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter a decimal number: ' + TerminalColors.BRIGHT_GREEN)) 
        print('\n' + TerminalColors.BRIGHT_WHITE + str(dec_1), '=', hex(dec_1))
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid decimal numbers. Try again' + TerminalColors.RESET)    
    print(TerminalColors.BRIGHT_CYAN + '\n-------Main Menu-------\n') 

def print_dec_binary_hex(): # print the number system of dec, hex, binary
    print(TerminalColors.RESET + ' 0 = 0000 = 0x0\n 1 = 0001 = 0x1\n 2 = 0010 = 0x2\n 3 = 0011 = 0x3\n 4 = 0100 = 0x4\n 5 = 0101 = 0x5\n 6 = 0110 = 0x6\n 7 = 0111 = 0x7\n 8 = 1000 = 0x8\n 9 = 1001 = 0x9\n10 = 1010 = 0xa\n11 = 1011 = 0xb\n12 = 1100 = 0xc\n13 = 1101 = 0xd\n14 = 1110 = 0xe\n15 = 1111 = 0xf')
    print(TerminalColors.BRIGHT_CYAN + '\n-------Main Menu-------\n')    

def Dec_to_Binary(): #convert dec to binary
    try: 
        dec_1 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter a decimal number: ' + TerminalColors.BRIGHT_GREEN))
        print('\n' + TerminalColors.BRIGHT_WHITE + 'The binary number for', str(dec_1),'is ',end = '')
        convert_binary(dec_1)
        print(TerminalColors.BRIGHT_CYAN + '\n\n-------Main Menu-------\n')  
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid decimal numbers. Try again' + TerminalColors.RESET)         

def Hex_to_Binary():
    try:
        hex_1 = hex(int(input(TerminalColors.BRIGHT_WHITE + 'Enter a hex number: ' + TerminalColors.BRIGHT_GREEN), 16))
        dec_1 = int(hex_1, 16)
        print('\n' + TerminalColors.BRIGHT_WHITE + 'The binary number for', hex(dec_1),'is ',end = '')
        convert_binary(dec_1)
        print(TerminalColors.BRIGHT_CYAN + '\n\n-------Main Menu-------\n')  
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid hexadecimal numbers. Try again' + TerminalColors.RESET)    

def Binary_to_Hex():
    dec_total_1 = 0
    try:
        binary_1 = input(TerminalColors.BRIGHT_WHITE + 'Enter a binary number: ' + TerminalColors.BRIGHT_GREEN)
        binary_1_length = len(binary_1)
        for i in range(binary_1_length): 
            dec_total_1 += int(binary_1[binary_1_length - i - 1]) * 2**i 
        print('\n' + TerminalColors.BRIGHT_WHITE + 'The binary number',binary_1, '=', hex(dec_total_1))
        print(TerminalColors.BRIGHT_CYAN + '\n-------Main Menu-------\n')     
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid binary numer. Try again' + TerminalColors.RESET)

def Binary_to_Dec():
    dec_total_1 = 0
    try:
        binary_1 = input(TerminalColors.BRIGHT_WHITE + 'Enter a binary number: ' + TerminalColors.BRIGHT_GREEN)
        binary_1_length = len(binary_1)
        for i in range(binary_1_length): 
            dec_total_1 += int(binary_1[binary_1_length - i - 1]) * 2**i
        print('\n' + TerminalColors.BRIGHT_WHITE + 'The binary number', binary_1, '=',dec_total_1)    
        print(TerminalColors.BRIGHT_CYAN + '\n-------Main Menu-------\n') 
    except Exception:
        print(TerminalColors.BRIGHT_RED + 'Not a valid binary number. Try again' + TerminalColors.RESET)

def options2(user_input2):
    match(user_input2):
        case 1:
            print(TerminalColors.BRIGHT_CYAN +'\n-------Decimal Addition-------\n')  
            Sum_Dec()
        case 2:
            print(TerminalColors.BRIGHT_CYAN +'\n-------Decimal Subtraction-------\n')
            Sub_Dec()
        case 3:   
            print(TerminalColors.BRIGHT_CYAN +'\n-------Hexadecimal Addition-------\n') 
            Sum_Hex()
        case 4:
            print(TerminalColors.BRIGHT_CYAN +'\n-------Hexadecimal Subtraction-------\n')  
            Sub_Hex()
        case 5:
            print(TerminalColors.BRIGHT_CYAN +'\n-------Binary Addition-------\n')
            Sum_Binary()
        case 6:   
            print(TerminalColors.BRIGHT_CYAN +'\n-------Binary Subtraction-------\n') 
            Sub_Binary()   
        case _:
            print(TerminalColors.BRIGHT_RED +'\n-------', user_input2,'Is not a valid option-------\n')

def Addition_Subtraction(): #second menu for addition and subtraction operations
    while(True):
        print(TerminalColors.BRIGHT_YELLOW + '1)' + TerminalColors.BRIGHT_MAGENTA + ' Decimal Addition\n' + TerminalColors.BRIGHT_YELLOW + '2)' + TerminalColors.BRIGHT_MAGENTA + ' Decimal Subtraction\n' + TerminalColors.BRIGHT_YELLOW + '3)' + TerminalColors.BRIGHT_MAGENTA + ' Hexadecimal Addition\n' + TerminalColors.BRIGHT_YELLOW + '4)' + TerminalColors.BRIGHT_MAGENTA + ' Hexadecimal Subtraction\n' + TerminalColors.BRIGHT_YELLOW + '5)' + TerminalColors.BRIGHT_MAGENTA + ' Binary Addition\n' + TerminalColors.BRIGHT_YELLOW + '6)' + TerminalColors.BRIGHT_MAGENTA + ' Binary Subtractio\n' + TerminalColors.BRIGHT_YELLOW + '0)' + TerminalColors.BRIGHT_RED + ' Go Back to The Main Menu\n'+ TerminalColors.RESET)
        try:
            user_input2 = int(input(TerminalColors.BRIGHT_CYAN + 'Enter option:' + TerminalColors.BRIGHT_YELLOW + ' 1,2,3,4,5,6 or 0: '+ TerminalColors.BRIGHT_GREEN))
            if user_input2 == 0:
                break
            options2(user_input2)
            print(TerminalColors.BRIGHT_CYAN +'\n-------Addition, Subtraction Menu-------\n')
        except Exception:
            print(TerminalColors.BRIGHT_RED +'\n-------not a valid option-------\n')    
    print(TerminalColors.BRIGHT_CYAN + '\n-------Main Menu-------\n') 

def options3(user_input3):
    match(user_input3):
        case 1:
            print(TerminalColors.BRIGHT_CYAN +'\n-------Hexadecimal AND-------\n')  
            try:
                hex_1 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the first hex number: ' + TerminalColors.BRIGHT_GREEN), 16)
                hex_2 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the second hex number: ' + TerminalColors.BRIGHT_GREEN), 16)
                hex_3 = hex(hex_1 & hex_2)
                print(TerminalColors.BRIGHT_WHITE + '\n     ', hex(hex_1), '\n', '    ', hex(hex_2), '\nAND =', hex_3)
            except Exception:
                print(TerminalColors.BRIGHT_RED + 'Not a valid hexadecimal numbers. Try again' + TerminalColors.RESET)   

        case 2:
            print(TerminalColors.BRIGHT_CYAN +'\n-------Hexadecimal OR-------\n')
            try:
                hex_1 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the first hex number: ' + TerminalColors.BRIGHT_GREEN), 16)
                hex_2 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the second hex number: ' + TerminalColors.BRIGHT_GREEN), 16)
                hex_3 = hex(hex_1 | hex_2)
                print(TerminalColors.BRIGHT_WHITE + '\n    ', hex(hex_1), '\n', '   ', hex(hex_2), '\nOR =', hex_3)
            except Exception:
                print(TerminalColors.BRIGHT_RED + 'Not a valid hexadecimal numbers. Try again' + TerminalColors.RESET)

        case 3:   
            print(TerminalColors.BRIGHT_CYAN +'\n-------Hexadecimal NOT-------\n') 
            try:
                hex_1 = input(TerminalColors.BRIGHT_WHITE + 'Enter a hex number: ' + TerminalColors.BRIGHT_GREEN)
                hex_result = hex(int(hex_1, 16) ^ int('F' * len(hex_1), 16))
                print(TerminalColors.BRIGHT_WHITE + '\n     ', hex(int(hex_1, 16)), '\nNOT =', hex_result)
            except Exception:
                print(TerminalColors.BRIGHT_RED + 'Not a valid hexadecimal numbers. Try again' + TerminalColors.RESET)
            
        case 4:
            print(TerminalColors.BRIGHT_CYAN +'\n-------Hexadecimal XOR-------\n')  
            try:
                hex_1 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the first hex number: ' + TerminalColors.BRIGHT_GREEN), 16)
                hex_2 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the second hex number: ' + TerminalColors.BRIGHT_GREEN), 16)
                hex_result = hex(hex_1 ^ hex_2)
                print(TerminalColors.BRIGHT_WHITE + '\n     ', hex(hex_1), '\n', '    ', hex(hex_2), '\nXOR =', hex_result)
            except Exception:
                print(TerminalColors.BRIGHT_RED + 'Not a valid hexadecimal numbers. Try again' + TerminalColors.RESET)

        case 5:
            print(TerminalColors.BRIGHT_CYAN +'\n-------Binary AND-------\n')
            try:    
                binary_1 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the first binary number: ' + TerminalColors.BRIGHT_GREEN), 2)
                binary_2 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the second binary number: ' + TerminalColors.BRIGHT_GREEN), 2)
                binary_3 = bin(binary_1 & binary_2)
                print(TerminalColors.BRIGHT_WHITE + '\n     ', bin(binary_1), '\n', '    ', bin(binary_2), '\nAND =', binary_3)
            except Exception:
                print(TerminalColors.BRIGHT_RED + 'Not a valid binary numbers. Try again' + TerminalColors.RESET)
        case 6:   
            print(TerminalColors.BRIGHT_CYAN +'\n-------Binary OR-------\n') 
            try:    
                binary_1 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the first binary number: ' + TerminalColors.BRIGHT_GREEN), 2)
                binary_2 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the second binary number: ' + TerminalColors.BRIGHT_GREEN), 2)
                binary_3 = bin(binary_1 | binary_2)
                print(TerminalColors.BRIGHT_WHITE + '\n    ', bin(binary_1), '\n', '   ', bin(binary_2), '\nOR =', binary_3)
            except Exception:
                print(TerminalColors.BRIGHT_RED + 'Not a valid binary numbers. Try again' + TerminalColors.RESET)   
        case 7:   
            print(TerminalColors.BRIGHT_CYAN +'\n-------Binary NOT-------\n') 
            try:
                binary_1 = input(TerminalColors.BRIGHT_WHITE + 'Enter a hex number: ' + TerminalColors.BRIGHT_GREEN)
                binary_result = ''.join(['1' if bit == '0' else '0' for bit in binary_1])
                print(TerminalColors.BRIGHT_WHITE + '\n     ', bin(int(binary_1, 2)), '\nNOT = 0b' + binary_result)
            except Exception:
                print(TerminalColors.BRIGHT_RED + 'Not a valid binary numbers. Try again' + TerminalColors.RESET)
        case 8:   
            print(TerminalColors.BRIGHT_CYAN +'\n-------Binary XOR-------\n') 
            try:    
                binary_1 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the first binary number: ' + TerminalColors.BRIGHT_GREEN), 2)
                binary_2 = int(input(TerminalColors.BRIGHT_WHITE + 'Enter the second binary number: ' + TerminalColors.BRIGHT_GREEN), 2)
                binary_3 = bin(binary_1 ^ binary_2)
                print(TerminalColors.BRIGHT_WHITE + '\n     ', bin(binary_1), '\n', '    ', bin(binary_2), '\nXOR =', binary_3)
            except Exception:
                print(TerminalColors.BRIGHT_RED + 'Not a valid binary numbers. Try again' + TerminalColors.RESET)       
        case _:
            print(TerminalColors.BRIGHT_RED +'\n-------', user_input3,'Is not a valid option-------\n')

def Logic_operations(): #3rd menu for boolean algebra operations
    while(True):
        print(TerminalColors.BRIGHT_YELLOW + '1)' + TerminalColors.BRIGHT_MAGENTA + ' Hexadecimal AND\n' + TerminalColors.BRIGHT_YELLOW + '2)' + TerminalColors.BRIGHT_MAGENTA + ' Hexadecimal OR\n' + TerminalColors.BRIGHT_YELLOW + '3)' + TerminalColors.BRIGHT_MAGENTA + ' Hexadecimal NOT\n' + TerminalColors.BRIGHT_YELLOW + '4)' + TerminalColors.BRIGHT_MAGENTA + ' Hexadecimal XOR\n' + TerminalColors.BRIGHT_YELLOW + '5)' + TerminalColors.BRIGHT_MAGENTA + ' Binary AND\n' + TerminalColors.BRIGHT_YELLOW + '6)' + TerminalColors.BRIGHT_MAGENTA + ' Binary OR\n' + TerminalColors.BRIGHT_YELLOW + '7)' + TerminalColors.BRIGHT_MAGENTA + ' Binary NOT\n' + TerminalColors.BRIGHT_YELLOW + '8)' + TerminalColors.BRIGHT_MAGENTA + ' Binary XOR\n' + TerminalColors.BRIGHT_YELLOW + '0)' + TerminalColors.BRIGHT_RED + ' Go Back to The Main Menu\n' + TerminalColors.RESET)
        try:
            user_input3 = int(input(TerminalColors.BRIGHT_CYAN +'Enter option:' + TerminalColors.BRIGHT_YELLOW + ' 1,2,3,4,5,6,7,8 or 0: '+ TerminalColors.BRIGHT_GREEN))
            if user_input3 == 0:
                break
            options3(user_input3)
            print(TerminalColors.BRIGHT_CYAN + '\n-------Logic Operations Menu-------\n')
        except Exception:
            print(TerminalColors.BRIGHT_RED +'\n-------not a valid option-------\n')    
    print(TerminalColors.BRIGHT_CYAN + '\n-------Main Menu-------\n') 
    
def options():
    global user_input
    match(user_input):
        case 1:
            print(TerminalColors.BRIGHT_CYAN + '\n-------Decimal to binary number-------\n')  
            Dec_to_Binary()
        case 2:
            print(TerminalColors.BRIGHT_CYAN + '\n-------Decimal to hexadecimal number-------\n')
            Dec_to_Hex() 
        case 3: 
            print(TerminalColors.BRIGHT_CYAN + '\n-------Hexadecimal to binary number-------\n') 
            Hex_to_Binary()       
        case 4:
            print(TerminalColors.BRIGHT_CYAN + '\n-------Hexadecimal to decimal number-------\n')
            Hex_to_Dec()
        case 5:
            print(TerminalColors.BRIGHT_CYAN + '\n-------Binary to decimal number-------\n') 
            Binary_to_Dec()
        case 6:
            print(TerminalColors.BRIGHT_CYAN + '\n-------Binary to hexadecimal number-------\n')       
            Binary_to_Hex()        
        case 7:
            print(TerminalColors.BRIGHT_CYAN + '\n-------decimal = binary = hexadecimal-------\n')
            print_dec_binary_hex()  
        case 8:
            print(TerminalColors.BRIGHT_CYAN + '\n-------Addition, Subtraction Menu-------\n')
            Addition_Subtraction()     
        case 9:
            print(TerminalColors.BRIGHT_CYAN + '\n-------Logic Operations Menu-------\n')
            Logic_operations()
        case 0:   
            print(TerminalColors.BRIGHT_RED + '\n-------Exit the program-------\n' + TerminalColors.RESET) 
            quit()
        case _:
            print(TerminalColors.BRIGHT_RED + '\n-------', user_input,'Is not a valid option-------\n'+ TerminalColors.RESET)

while(True):
    print(TerminalColors.BRIGHT_YELLOW + '1)' + TerminalColors.BRIGHT_MAGENTA + ' Decimal to binary number\n'+ TerminalColors.BRIGHT_YELLOW + '2)'+ TerminalColors.BRIGHT_MAGENTA + ' Decimal to hexadecimal number\n'+ TerminalColors.BRIGHT_YELLOW + '3)'+ TerminalColors.BRIGHT_MAGENTA + ' Hexadecimal to binary number\n'+ TerminalColors.BRIGHT_YELLOW + '4)' + TerminalColors.BRIGHT_MAGENTA + ' Hexadecimal to decimal number\n'+ TerminalColors.BRIGHT_YELLOW + '5)' + TerminalColors.BRIGHT_MAGENTA + ' Binary to decimal number\n'+ TerminalColors.BRIGHT_YELLOW + '6)' + TerminalColors.BRIGHT_MAGENTA + ' Binary to hexadecimal number\n'+ TerminalColors.BRIGHT_YELLOW + '7)' + TerminalColors.BRIGHT_MAGENTA + ' Print decimal, binary and hexadcimal number\n'+ TerminalColors.BRIGHT_YELLOW + '8)' + TerminalColors.BRIGHT_MAGENTA + ' Addition, Subtraction Menu\n'+ TerminalColors.BRIGHT_YELLOW + '9)' + TerminalColors.BRIGHT_MAGENTA + ' Logic operations Menu\n'+ TerminalColors.BRIGHT_YELLOW + '0)'+ TerminalColors.BRIGHT_RED + ' To Exit\n'+ TerminalColors.RESET)
    try:
        user_input = int(input(TerminalColors.BRIGHT_CYAN + 'Enter option:' + TerminalColors.BRIGHT_YELLOW + ' 1,2,3,4,5,6,7,8,9 or 0: ' + TerminalColors.BRIGHT_GREEN))
        if user_input == 0:
            print(TerminalColors.BRIGHT_RED + '\n-------Exit the program-------\n' + TerminalColors.RESET)
            break
        options()
    except Exception:
        print(TerminalColors.BRIGHT_RED + '\n-------not a valid option-------\n' + TerminalColors.RESET) 