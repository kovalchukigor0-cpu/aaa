import pandas as pd

file1 = open('RULEVIE REIKI.txt', 'r', encoding="utf-8")

number = []
brand = []
price = []
price_final= []

name = []
zakup = []
srok = []
kolvo = []

for l in file1:
    x = l.split(';')
    number.append(x[0])
    brand.append(x[1])
    price.append(x[2])
    name.append(x[3])

    zakup.append('1000')
    srok.append('2')
    kolvo.append('5')

for i in price:
    i = i.replace(" ","")
    x = i.split('₽')
    p = int(x[0])
    p = p*80/100
    p = int(p)
    price_final.append(p)

df1 = pd.DataFrame({
    'Номер запчасти': number,
    'Производитель': brand,
    'Цена продажи': price_final,
    'Название детали': name,
    'Цена закупа': zakup,
    'Срок': srok,
    'Колличество': kolvo
})


with pd.ExcelWriter("sales_report.xlsx") as writer:
    df1.to_excel(writer, index=False)

