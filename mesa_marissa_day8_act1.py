class Cellphone:
    color = "pink"
    manufacturer = "Samsung"
    model = "S20"

cp = Cellphone()
print('CP Color: ', cp.color)
print('CP Manufacturer: ', cp.manufacturer)
print('CP Model: ', cp.model)

cp1= Cellphone()
cp1.color = "yellow"
cp1.manufacturer = "Samsung"
cp1.model = "S21"

cp3 = Cellphone()
cp3.color = "blue"
cp3.manufacturer = "Oppo"
cp3.model = "F21"

cp4 = Cellphone()
cp4.color = "red"
cp4.manufacturer = "Apple"
cp4.model = "iphone*"

cp5 = Cellphone()
cp5.color = "black"
cp5.manufacturer = "Samsung"
cp5.model = "s9"

print('CP Color: ', cp.color)
print('CP2 Color: ', cp1.color)
print('CP3 Color: ', cp3.color)
print('CP4 Color: ', cp4.color)
print('CP5 Color: ', cp5.color)

print('CP Manufacturer: ', cp.manufacturer)
print('CP2 Manufacturer: ', cp1.manufacturer)
print('CP3 Manufacturer: ', cp3.manufacturer)
print('CP4 Manufacturer: ', cp4.manufacturer)
print('CP5 Manufacturer: ', cp5.manufacturer)

print('CP Model: ', cp.model)
print('CP2 Model: ', cp1.model)
print('CP3 Model: ', cp3.model)
print('CP4 Model: ', cp4.model)
print('CP5 Model: ', cp5.model)