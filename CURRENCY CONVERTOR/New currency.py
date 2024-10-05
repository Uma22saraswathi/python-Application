from currency_converter import CurrencyConverter

amount = int(input("amount: "))
target_currency = input("Enter target currency code (e.g., USD, EUR, ): ")
c = CurrencyConverter()
converting = c.convert(amount,'INR',target_currency)

print(f" {amount} INR is equal to {converting} {target_currency}")
