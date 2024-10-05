from Currency_Converter= import CurrencyConverter
amount = int(input("amount:"))
converting = CurrencyConverter().convert(amount,'USD','EUR')
print(converting)