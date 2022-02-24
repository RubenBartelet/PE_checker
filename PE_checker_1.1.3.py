# Made by Ruben Bartelet on 2-2022
#version 1.1.3 (first fully working version)

import itertools#used to get all binary combinations

#the periodic table of elements symbols.
PE = ['H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F', 'NE' , 'NA', 'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR', 'K', 'CA', 'SC' ,'TI' , 'V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR', 'RB', 'SR', 'Y', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE', 'I', 'XE', 'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF', 'TA', 'W', 'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TL', 'PB', 'BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC', 'TH', 'PA', 'U', 'NP', 'PU', 'AM', 'CM', 'BK', 'CF', 'ES', 'FM', 'MD', 'NO', 'LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT']
PE.append(' ')#this way spaces are allowed

List = []#contains the specific elements

def check_1(string):#checks if the first character is in the PE and removes it 
    for a in range(0, len(PE)):
        if string[0:1] == PE[a]:
            string = string[1:len(string)]
            List.append(PE[a])   
            return string
    return string

def check_2(string):#checks if the first two character is in the PE and removes it 
    for b in range(0, len(PE)):
        if string[0:2] == PE[b]:
            string = string[2:len(string)]
            List.append(PE[b])
            return string
    return string

def execute():
    input_ = input('Text: ').upper()
    string = input_
    for c in range(2,len(input_)+1):
        bin_comb = list(itertools.product([0, 1], repeat=c))#checks every possible combination of check 1 and check 2 (binary). If one of this combonations is true the word can be made with the PE. INA for example cant be made with 2 and 1 (INA --> A --> False) but with 1 2 it can be made (INA --> NA --> True)
        for d in range(0,len(bin_comb)):
            temp_list = bin_comb[d]
            string = input_
            for e in range (0,c):
                if temp_list[e] == 0:
                    string = check_1(string)
                else:
                    string = check_2(string)
                if string == '':#if nothing is left it can be made
                    print('True')
                    end = List
                    numbers = []#turns the element symbol into the number in the PE
                    for f in range(0,len(end)):
                        if PE.index(end[f]) != len(PE)-1:#the space
                            numbers.append(str(PE.index(end[f])+1))#gives the number in the PE
                        else: 
                            numbers.append('0')#a space has number 0
                    print(', '.join(end), end=': ')
                    print(', '.join(numbers))
                    List.clear()
                    execute()
            List.clear()
    print('False')
    List.clear()
    execute()

execute()