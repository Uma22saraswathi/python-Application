currency_rates={
    "USD":{"INR":82.50,"EUR":0.94,"GBR":0.79},
    "INR":{"USD":0.012,"EUR":0.011,"GBR":0.0095},
    "EUR":{"USD":1.06,"INR":88.00, "GBR":0.85},
    "GBR":{"USD":1.27,"INR":103.50,"EUR":1.18}
}
def convert_currency(Amount,From_currency,To_currency):
    if From_currency in currency_rates and To_currency in currency_rates[From_currency]:
        rate = currency_rates[From_currency][To_currency]
        return Amount * rate 
    else:
        return None
Amount = float(input("enter the amount"))
From_currency=(input("enter the from currency : "))
To_currency=(input("enter the to currency"))

print(From_currency,"to",To_currency)

result=convert_currency(Amount,From_currency,To_currency)
if result is not None:  
    print(f"{Amount}{From_currency}To{To_currency}is{result}")
else:
    ("invalid currency")    
