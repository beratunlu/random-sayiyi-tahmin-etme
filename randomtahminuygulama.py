import random

sayi = random.randint(0,100)
Hak = 10

while Hak>0:
  tahmin = int(input("Lütfen Pozitif Tam Sayı Giriniz"))
  if tahmin < 0:
    print("Girdiğiniz sayı pozitif değil:")
    continue
  Hak-=1 
  if tahmin == sayi:
    print("Tebrikler Sayıyı Doğru Tahmin Ettiniz.") 
    break 
  elif (tahmin > sayi) and Hak!=0:
    print(f"Lütfen tahmin etmiş olduğunuz sayıyı düşürünüz Kalan Hakkınız:{Hak}")
  elif (tahmin < sayi) and Hak!=0:
    print(f"ütfen tahmin etmiş olduğunuz sayıyı arttırınız Kalan Hakkınız:{Hak}")
  if Hak ==0:
    print(f"Hakkınız Kalmamıştır. Doğru Sayı: {sayi} olacaktır.")
