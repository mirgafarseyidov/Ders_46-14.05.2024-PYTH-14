
"""
Salman müəllim 

Home Task  - 1 ci versiya 


Bir Packets adinda folder(Paket) yaradin. Icinde samitler adinda bir file (modul) olsun.
Onunda icinde samitleri_al adinda bir funksiya olsun.

Nece calisacaq ?:
Bu folderden colde yerlesen main.py faylimizda bu methodu cagirmali ve icine bir deyer (cumle) gondermeliyik.

Numune cagrilma:
'Salam necesen ... '

netice:
{'s', 'l', 'm', 'n', 'c'} >> heresinden bir dene olsa kifayetdir
"""

from Packets.samitler import samitleri_al

if __name__ == "__main__":
    cumle = 'Salam necesen'
    samitler = samitleri_al(cumle)
    print(samitler)