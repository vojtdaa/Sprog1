# Základní kurzy (vůči 1 CZK)
def konvertor_men(hodnota, z_meny, na_menu, jiny_kurz = None):
    kurz = 0
    vychozi_kurzy = {
    "CZK": 1.0,
    "EUR": 0.04,
    "USD": 0.043,
    "GBP": 0.034,
    "JPY": 6.43
}   
    if jiny_kurz == None:
        kurz = vychozi_kurzy
    else: kurz = jiny_kurz

    if hodnota == 0:
        return 0

    if hodnota < 0 or z_meny not in vychozi_kurzy or na_menu not in vychozi_kurzy:
        return None

    vysledek = hodnota/kurz[z_meny]
    vysledek2 = vysledek*kurz[na_menu]
    return round(vysledek2, 2)


print(konvertor_men(1000, "CZK", "EUR"))  # 40.0
print(konvertor_men(50, "EUR", "CZK"))  # 1250.0
print(konvertor_men(100, "USD", "JPY"))  # 14953.49
print(konvertor_men(75, "GBP", "USD", {"GBP": 1.0, "USD": 1.26}))  # 94.5
print(konvertor_men(200, "CZK", "XYZ"))  # None
print(konvertor_men(0, "CZK", "JPY")) # 0
print(konvertor_men(20, "EUR", "EUR")) # 20
print(konvertor_men(100, "EUR", "CZK", {"EUR": 0.1, "CZK": 1})) # 1 EUR = 10 Kc => 1000