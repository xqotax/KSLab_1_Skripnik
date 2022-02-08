# Python 3.10
import bz2
import functions as func
import base64 as bs
from colorama import Fore
from colorama import init
init(autoreset=True)

def main_1():
    with open('Izdruk.txt', encoding="utf-16") as f:
        Izdruk = f.read()
    with open('Kolobok.txt', encoding="utf-16") as f:
        Kolobok = f.read()
    with open('Upiter.txt', encoding="utf-16") as f:
        Upiter = f.read()
    # Izdruk = Izdruk.lower().replace("\n", "")
    # Kolobok = Kolobok.lower().replace("\n", "")
    # Upiter = Upiter.lower().replace("\n", "")


    print(Fore.BLUE + "Izdruk")
    IzdrukSymbol = func.find_symbol(Izdruk)
    IzdrukProbability = func.probability_of_symbols(IzdrukSymbol)
    IzdrukEntropy = func.entropy(IzdrukProbability)
    func.information_size(IzdrukEntropy, len(Izdruk), 'Izdruk.txt')
    func.xlsxFileWrite('Izdruk.xlsx', IzdrukSymbol, IzdrukProbability)

       
    print("\n\n" + Fore.BLUE + "Kolobok")
    KolobokSymbol = func.find_symbol(Kolobok)
    KolobokProbability = func.probability_of_symbols(KolobokSymbol)
    KolobokEntropy = func.entropy(KolobokProbability)
    func.information_size(KolobokEntropy, len(Kolobok), 'Kolobok.txt')
    func.xlsxFileWrite('Kolobok.xlsx', KolobokSymbol, KolobokProbability)

    print("\n\n" + Fore.BLUE + "Upiter")
    UpiterSymbol = func.find_symbol(Upiter)
    UpiterProbability = func.probability_of_symbols(UpiterSymbol)
    UpiterEntropy = func.entropy(UpiterProbability)
    func.information_size(UpiterEntropy, len(Upiter), 'Upiter.txt')
    func.xlsxFileWrite('Upiter.xlsx', UpiterSymbol, UpiterProbability)

def main_2():
    with open('Izdruk.txt', encoding="utf-16") as f:
        Izdruk = f.read()
    with open('Kolobok.txt', encoding="utf-16") as f:
        Kolobok = f.read()
    with open('Upiter.txt', encoding="utf-16") as f:
        Upiter = f.read()

    # print(Fore.BLUE + bs.base64("Студент_3-го_Курсу_СА_Скрипник_Юрій"))
    izdrukBase64 = bs.base64(Izdruk)
    kolobolBase64 = bs.base64(Kolobok)
    upiterBase64 = bs.base64(Upiter)

    with open('IzdrukBase64.txt', "w") as f:
        f.write(izdrukBase64)
    with open('KolobokBase64.txt', "w") as f:
        f.write(kolobolBase64)
    with open('UpiterBase64.txt', "w") as f:
        f.write(upiterBase64)

    print(Fore.BLUE + "IzdrukBase64")
    IzdrukSymbol = func.find_symbol(izdrukBase64)
    IzdrukProbability = func.probability_of_symbols(IzdrukSymbol)
    IzdrukEntropy = func.entropy(IzdrukProbability)
    func.information_size(IzdrukEntropy, len(izdrukBase64), 'IzdrukBase64.txt')
    func.xlsxFileWrite('IzdrukBase64.xlsx', IzdrukSymbol, IzdrukProbability)

    print("\n\n" + Fore.BLUE + "KolobokBase64")
    KolobokSymbol = func.find_symbol(kolobolBase64)
    KolobokProbability = func.probability_of_symbols(KolobokSymbol)
    KolobokEntropy = func.entropy(KolobokProbability)
    func.information_size(KolobokEntropy, len(kolobolBase64), 'KolobokBase64.txt')
    func.xlsxFileWrite('KolobokBase64.xlsx', KolobokSymbol, KolobokProbability)

    print("\n\n" + Fore.BLUE + "UpiterBase64")
    UpiterSymbol = func.find_symbol(upiterBase64)
    UpiterProbability = func.probability_of_symbols(UpiterSymbol)
    UpiterEntropy = func.entropy(UpiterProbability)
    func.information_size(UpiterEntropy, len(upiterBase64), 'UpiterBase64.txt')
    func.xlsxFileWrite('UpiterBase64.xlsx', UpiterSymbol, UpiterProbability)

def main_2_4():
    with bz2.open("Izdruk.txt.bz2", "rt") as f:
        Izdruk = f.read()
    with bz2.open('Kolobok.txt.bz2', "rt") as f:
        Kolobok = f.read()
    with bz2.open('Upiter.txt.bz2', "rt") as f:
        Upiter = f.read()

    izdrukArchivedBase64 = bs.base64(Izdruk)
    kolobolArchivedBase64 = bs.base64(Kolobok)
    upiterArchivedBase64 = bs.base64(Upiter)


    with open('IzdrukBase64AfterArchived.txt', "w") as f:
        f.write(izdrukArchivedBase64)
    with open('KolobokBase64AfterArchived.txt', "w") as f:
        f.write(kolobolArchivedBase64)
    with open('UpiterBase64AfterArchived.txt', "w") as f:
        f.write(upiterArchivedBase64)

    IzdrukSymbol = func.find_symbol(izdrukArchivedBase64)
    IzdrukProbability = func.probability_of_symbols(IzdrukSymbol)
    print(Fore.BLUE + "IzdrukArchivedBase64")
    IzdrukEntropy = func.entropy(IzdrukProbability)
    func.information_size(IzdrukEntropy, len(izdrukArchivedBase64), 'IzdrukBase64AfterArchived.txt', True)

    KolobokSymbol = func.find_symbol(kolobolArchivedBase64)
    KolobokProbability = func.probability_of_symbols(KolobokSymbol)
    print("\n\n" + Fore.BLUE + "KolobokArchivedBase64")
    KolobokEntropy = func.entropy(KolobokProbability)
    func.information_size(KolobokEntropy, len(kolobolArchivedBase64), 'KolobokBase64AfterArchived.txt', True)

    UpiterSymbol = func.find_symbol(upiterArchivedBase64)
    UpiterProbability = func.probability_of_symbols(UpiterSymbol)
    print("\n\n" + Fore.BLUE + "UpiterArchivedBase64")
    UpiterEntropy = func.entropy(UpiterProbability)
    func.information_size(UpiterEntropy, len(upiterArchivedBase64), 'UpiterBase64AfterArchived.txt', True)



if __name__ == '__main__':
    print("Розкоментуйте блок, який необхідно виконати в блоці if __name__ == '__main__'")
    main_1()
    # main_2()
    # main_2_4()
