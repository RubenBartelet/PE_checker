# Made by Ruben Bartelet on 2-2022
#version 1.2 

import itertools#used to get all binary combinations
from pathlib import Path

#the directory to the map
PROJECT_ROOT = Path(__file__).parent.parent

raw_text = PROJECT_ROOT / "PE_Checker_1.2/English_words.txt"
PE_text_file = PROJECT_ROOT / "PE_Checker_1.2/PE_Test.txt"
PE_text = PE_text_file

with open (raw_text, "r") as raw_text:
    raw_text_list = raw_text.read().splitlines()

#the periodic table of elements symbols.
PE = ['H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F', 'NE' , 'NA', 'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR', 'K', 'CA', 'SC' ,'TI' , 'V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR', 'RB', 'SR', 'Y', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE', 'I', 'XE', 'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF', 'TA', 'W', 'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TL', 'PB', 'BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC', 'TH', 'PA', 'U', 'NP', 'PU', 'AM', 'CM', 'BK', 'CF', 'ES', 'FM', 'MD', 'NO', 'LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT']
PE.append(' ')#this way spaces are allowed

List = []#contains the specific elements

def check(string, length_):#checks if the first or/and second character is in the PE and removes it 
    for a in range(0, len(PE)):
        if string[0:length_] == PE[a]:
            string = string[length_:len(string)]
            List.append(PE[a])   
            return string
    return string

def execute():
    global PE_text
    PE_text_ = open(PE_text, "w")
    for g in range(0, len(raw_text_list)):
        continue_ = True
        PE_word = raw_text_list[g]
        input_ = raw_text_list[g].upper()
        string = input_
        for c in range(2,len(input_)+1):
            bin_comb = list(itertools.product([0, 1], repeat=c))#checks every possible combination of check 1 and check 2 (binary). If one of this combonations is true the word can be made with the PE. INA for example cant be made with 2 and 1 (INA --> A --> False) but with 1 2 it can be made (INA --> NA --> True)
            for d in range(0,len(bin_comb)):
                if continue_:
                    temp_list = bin_comb[d]
                    string = input_
                    for e in range (0,c):
                        if temp_list[e] == 0:
                            string = check(string,1)
                        else:
                            string = check(string,2)
                        if string == '':#if nothing is left it can be made
                            PE_text_.writelines([PE_word + ': '])
                            print(PE_word)
                            continue_ = False
                            end = List
                            numbers = []#turns the element symbol into the number in the PE
                            for f in range(0,len(end)):
                                if PE.index(end[f]) != len(PE)-1:#the space
                                    numbers.append(str(PE.index(end[f])+1))#gives the number in the PE
                                else: 
                                    numbers.append('0')#a space has number 0
                            PE_text_.writelines([', '.join(end)+ ': '+ ', '.join(numbers)+'\n'])
                            List.clear()
                List.clear()
        
    PE_text_.close

    PE_text = PE_text_file
    with open (PE_text, "r") as PE_text_:
        PE_text_ = PE_text_.read().splitlines()

    print(len(raw_text_list))
    print(len(PE_text_))

    answer = len(PE_text_) * 100 / len(raw_text_list)
    result = str(round(answer))
    print('~'+result+'%')

execute()

