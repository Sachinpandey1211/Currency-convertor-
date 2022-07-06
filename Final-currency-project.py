# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:58:22 2021
@author: 100ry
"""
from forex_python.converter import CurrencyRates

curr = CurrencyRates()
print(curr.get_rates('INR'))  # Check the currency in this and change accordingly
print("_______________Welcome to python currency convertor________________")
print("\n")
print("\n")
print("         You can convert any currency given below to INR:        ")
print("\n")
print("1.  USD ")
print("2.  CHF ")
print("3.  JPY ")
print("4.  EUR ")
print("5.  GBP ")
print("6.  BGN ")
print("7.  CZN ")
print("8.  DKK ")
print("9.  HUF ")
print("10. PLN ")
print("11. ROK")
print("12. SEK ")
print("13. ISK ")
print("14. NOK ")
print("15. HRK")
print("16. RUK")
print("17. TRY")
print("18. AUD ")
print("19. BRL")
print("20. CAD")
print("21. CNY")
print("22. HKD ")
print("23. IDR ")
print("24. KRW ")
print("25. MXN ")
print("26. MYR")
print("27. NZD ")
print("28. PHP")
print("29. SGD ")
print("30. THB ")
print("31. ZAR ")
print("32. Sri lanka ruppes")
print("33. Pakistani rupees")
print("34. Icelandic krona")
print("35. Serbian dinar")
print("36. Argentine peso")
print("37. Central african")
print("38. Mexican peso")
print("39. Nepalese ruppes")
print("40. Indonesain rupiah")
print("\n")
print("\n")
print("___________Please enter the number of your choice as given_______")
print("\n")
print("\n")
c = int(input("Enter currency choice which you want to convert to INR:"))
print("\n")
if c == 1:
    a = int(input("Enter the USD amount to convert to INR:"))
    d = curr.get_rate('USD', 'INR')
    x = a * d
    print(f'{a} USD {x:.3f} INR')
elif c == 2:
    a = int(input("Enter the CHF amount to convert to INR:"))
    d = curr.get_rate('CHF', 'INR')
    x = a * d
    print(f'{a} CHF {x:.3f} INR')
elif c == 3:
    a = int(input("Enter the JPY amount to convert to INR:"))
    d = curr.get_rate('JPY', 'INR')
    x = a * d
    print(f'{a} JPY {x:.3f} INR')
elif c == 4:
    a = int(input("Enter the EUR amount to convert to INR:"))
    d = curr.get_rate('EUR', 'INR')
    x = a * d
    print(f'{a} EUR {x:.3f} INR')
elif c == 5:
    a = int(input("Enter the GBP amount to convert to INR:"))
    d = curr.get_rate('GBP', 'INR')
    x = a * d
    print(f'{a} GBP {x:.3f} INR')
elif c == 6:
    a = int(input("Enter the BGN amount to convert to INR:"))
    d = curr.get_rate('BGN', 'INR')
    x = a * d
    print(f'{a} BGN {x:.3f} INR')
elif c == 7:
    a = int(input("Enter the CZN amount to convert to INR:"))
    d = curr.get_rate('CZN', 'INR')
    x = a * d
    print(f'{a} CZN {x:.3f} INR')
elif c == 8:
    a = int(input("Enter the DKK amount to convert to INR:"))
    d = curr.get_rate('DKK', 'INR')
    x = a * d
    print(f'{a} DKK {x:.3f} INR')
elif c == 9:
    a = int(input("Enter the HUF amount to convert to INR:"))
    d = curr.get_rate('HUF', 'INR')
    x = a * d
    print(f'{a} HUF {x:.3f} INR')
elif c == 10:
    a = int(input("Enter the PLN amount to convert to INR:"))
    d = curr.get_rate('PLN', 'INR')
    x = a * d
    print(f'{a} PLN {x:.3f} INR')
elif c == 11:
    a = int(input("Enter the ROK amount to convert to INR:"))
    d = curr.get_rate('ROK', 'INR')
    x = a * d
    print(f'{a} ROK {x:.3f} INR')
elif c == 12:
    a = int(input("Enter the SEK amount to convert to INR:"))
    d = curr.get_rate('SEK', 'INR')
    x = a * d
    print(f'{a} SEK {x:.3f} INR')
elif c == 13:
    a = int(input("Enter the ISK  amount to convert to INR:"))
    d = curr.get_rate('ISK', 'INR')
    x = a * d
    print(f'{a} ISK  {x:.3f} INR')
elif c == 14:
    a = int(input("Enter the NOK amount to convert to INR:"))
    d = curr.get_rate('NOK', 'INR')
    x = a * d
    print(f'{a} NOK {x:.3f} INR')
elif c == 15:
    a = int(input("Enter the HRK amount to convert to INR:"))
    d = curr.get_rate('HRK', 'INR')
    x = a * d
    print(f'{a} HRK {x:.3f} INR')
elif c == 16:
    a = int(input("Enter the RUK amount to convert to INR:"))
    d = curr.get_rate('RUK', 'INR')
    x = a * d
    print(f'{a} RUK {x:.3f} INR')
elif c == 17:
    a = int(input("Enter the TRY amount to convert to INR:"))
    d = curr.get_rate('TRY', 'INR')
    x = a * d
    print(f'{a} TRY {x:.3f} INR')
elif c == 18:
    a = int(input("Enter the AUD   amount to convert to INR:"))
    d = curr.get_rate('AUD ', 'INR')
    x = a * d
    print(f'{a} AUD {x:.3f} INR')
elif c == 19:
    a = int(input("Enter the BRL amount to convert to INR:"))
    d = curr.get_rate('BRL', 'INR')
    x = a * d
    print(f'{a} BRL {x:.3f} INR')
elif c == 20:
    a = int(input("Enter the CAD amount to convert to INR:"))
    d = curr.get_rate('CAD', 'INR')
    x = a * d
    print(f'{a} CAD {x:.3f} INR')
elif c == 21:
    a = int(input("Enter the CNY amount to convert to INR:"))
    d = curr.get_rate('CNY', 'INR')
    x = a * d
    print(f'{a} CNY {x:.3f} INR')
elif c == 22:
    a = int(input("Enter the HKD amount to convert to INR:"))
    d = curr.get_rate('HKD', 'INR')
    x = a * d
    print(f'{a} HKD {x:.3f} INR')
elif c == 23:
    a = int(input("Enter the IDR amount to convert to INR:"))
    d = curr.get_rate('IDR', 'INR')
    x = a * d
    print(f'{a} IDR {x:.3f} INR')
elif c == 24:
    a = int(input("Enter the KRW  amount to convert to INR:"))
    d = curr.get_rate('KRW', 'INR')
    x = a * d
    print(f'{a} KRW {x:.3f} INR')
elif c == 25:
    a = int(input("Enter the MXN amount to convert to INR:"))
    d = curr.get_rate('MXN', 'INR')
    x = a * d
    print(f'{a} MXN {x:.3f} INR')
elif c == 26:
    a = int(input("Enter the MYR  amount to convert to INR:"))
    d = curr.get_rate('MYR', 'INR')
    x = a * d
    print(f'{a} MYR {x:.3f} INR')
elif c == 27:
    a = int(input("Enter the NZD amount to convert to INR:"))
    d = curr.get_rate('NZD', 'INR')
    x = a * d
    print(f'{a} NZD {x:.3f} INR')
elif c == 28:
    a = int(input("Enter the PHP amount to convert to INR:"))
    d = curr.get_rate('PHP', 'INR')
    x = a * d
    print(f'{a} PHP {x:.3f} INR')
elif c == 29:
    a = int(input("Enter the SGD  amount to convert to INR:"))
    d = curr.get_rate('SGD ', 'INR')
    x = a * d
    print(f'{a} SGD {x:.3f} INR')
elif c == 30:
    a = int(input("Enter the THB amount to convert to INR:"))
    d = curr.get_rate('THB', 'INR')
    x = a * d
    print(f'{a} THB {x:.3f} INR')
elif c == 31:
    a = int(input("Enter the ZAR amount to convert to INR:"))
    d = curr.get_rate('ZAR', 'INR')
    x = a * d
    print(f'{a} ZAR {x:.3f} INR')
elif c == 32:
    a = int(input("Enter the Sri lanka rupees amount to convert to INR:"))
    d = float(0.373)
    x = a * d
    print(a, "sri lanka rupees =", x, "INR")
elif c == 33:
    a = int(input("Enter the Pakistani rupees to convert to INR:"))
    d = float(0.462)
    x = a * d
    print(a, "Pakistani rupees =", x, "INR")
elif c == 34:
    a = int(input("Enter the Icelandic krona amount to convert to INR:"))
    d = float(0.588)
    x = a * d
    print(a, "Icelandic krona =", x, "INR")
elif c == 35:
    a = int(input("Enter the Serbian dinar amount to convert to INR:"))
    d = float(0.744)
    x = a * d
    print(a, "Serbian dinar =", x, "INR")
elif c == 36:
    a = int(input("Enter the Argentine peso amount to convert to INR:"))
    d = float(0.77)
    x = a * d
    print(a, "Argentine peso =", x, "INR")
elif c == 37:
    a = int(input("Enter the Central African France amount to convert to INR:"))
    d = float(0.1334)
    x = a * d
    print(a, "Central African France =", x, "INR")
elif c == 38:
    a = int(input("Enter the Mexican peso amount to convert to INR:"))
    d = float(3.69)
    x = a * d
    print(a, "Mexican peso =", x, "INR")
elif c == 39:
    a = int(input("Enter the Nepalese rupees to convert to INR: "))
    d = float(0.622)
    x = a * d
    print(a, "Nepalese rupees =", x, "INR")
elif c == 40:
    a = int(input("Enter the Indonesaih rupiah to convert to INR:"))
    d = float(0.00513)
    x = a * d
    print(a, "Indonesian rupiah =", x, "INR")
else:
    print("Sorry this currency is not avilable for converting:")

