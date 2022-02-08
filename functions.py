
# Функції для дослідження ентропії, частоти появи символів та кількості інформації

import math
import os
import xlsxwriter
from colorama import Fore
from colorama import init
init(autoreset=True)
def find_symbol(text):
    array_of_symbols = []
    for symbol in text:
        dict = {symbol: text.count(symbol)}
        array_of_symbols.append(dict)
    unique_symbols = []
    for symbol in array_of_symbols:
        if symbol not in unique_symbols:
            unique_symbols.append(symbol)

    unique_symbols.append({'length': len(text)})
    print(unique_symbols)
    return unique_symbols
def probability_of_symbols(unique_sumbols):
    length_of_text = unique_sumbols[(len(unique_sumbols) - 1)]["length"]
    unique_sumbols = unique_sumbols[:-1]
    probability = []
    for symbol_count in unique_sumbols:
        probability.append(round(list(symbol_count.values())[0]/length_of_text, 5))
    print(probability)
    return probability

def entropy(probability_of_symbols):
    avar_entropy = 0
    for chance in probability_of_symbols:
        avar_entropy += chance * math.log(1/chance, 2)
    print(Fore.RED + "Ентропія: "+str(avar_entropy))
    return avar_entropy

def information_size(entopy, length, fileName, justInfo = False):
    fileSize = os.stat(fileName).st_size
    information = entopy * length / 8
    if (justInfo):
        print(Fore.LIGHTGREEN_EX +"Кількість інформації (в байтах): {}"
            .format(round(information)))
    else:
        print(Fore.LIGHTGREEN_EX + "Для файлу: {}\nДовжина тексту: {} символів\nЕнтропія: {}\nКількість інформації (в байтах): {}\nРозмір файлу (в байтах): {}"
            .format(fileName[:-4], length, round(entopy, 5), information, fileSize))

def xlsxFileWrite(fileName, symbols, probability):
    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    worksheet.write(row, col, "Символ")
    worksheet.write(row, col + 2, "Кількість повторень")
    worksheet.write(row, col + 1, "Ймовірність повторень")
    row += 1
    for i in range(len(probability)):
        worksheet.write(row, col, list(symbols[i].keys())[0])
        worksheet.write(row, col + 2, list(symbols[i].values())[0])
        worksheet.write(row, col + 1, probability[i])
        row += 1
    workbook.close()
