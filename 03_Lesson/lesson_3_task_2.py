from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone", "+79991564534"),
    Smartphone("Samsung", "Galaxy", "+79884567845"),
    Smartphone("Sony", "Xperia", "+79315442897"),
    Smartphone("Motorola", "Razr", "+793154872897"),
    Smartphone("Vivo", "X", "+79315464897")
]

for phone in catalog:
    print(f"{phone.manufacturer} - {phone.model}.\
    Абонентский номер {phone.number}")
