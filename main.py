from functions import Processes
endpoint="https://api.genelpara.com/embed/doviz.json"

process=Processes(endpoint)
response = process.request(url=endpoint,method="GET",values={})
for x in range(5):
    print("*",end="")
print("Hoşgeldiniz",end="")
for x in range(5):
    print("*",end="")
print("\n")
print("Çevirebileceğiniz Para Birimleri Şunlar"),
for x in response:
    print(" | "+x+" | ",end="")

print("\n")
converted_type=input("Hangi Para Birimi ₺'ye  Çevirilsin:").upper()
process.check_that_there_is(key=converted_type)
try:
    tobe_converted=float(input("Çevirmek İstediğiniz  Miktarı Giriniz:"))
except:
    print("Miktar Algılanamadı")
    exit()

converted=float(response.get(converted_type).get('alis'))*tobe_converted
print("Sonuç :"+str(converted))
