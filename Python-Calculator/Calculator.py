print("***INFORMATION*** \n This calculator written @abdulkadirtoklu4's. In this calculator, you can also perform mode import and exponential operations other than normal calculators.\n")
print("***BİLGİLENDİRME*** \n Bu hesap makinesi @abdulkadirtkoklu4 tarafından yazılmıştır.Bu hesap makinesinde normal hesap makineleri dışında mod alma ve üs alma işlemlerini de yapabilirsiniz.\n")

print("Dil Seçin / Language Selection:")

language = input()

if language == "tr" or language == "Tr" or language == "Türkçe" :

    sayi1 = int(input("1. Sayıyı Girin: "))
    sayi2 = int(input("2. Sayıyı Girin: "))
    islem = input("İşlem Seçin (+,-,*,/,%,**): ")

    if islem == "+":
        sonuc = sayi1 + sayi2
        print("Sonuç: ",sonuc)

    elif islem == "-":
        sonuc = sayi1 - sayi2
        print("Sonuç: ",sonuc)

    elif islem == "*":
        sonuc= sayi1 * sayi2
        print("Sonuç: ",sonuc)

    elif islem == "/":
        sonuc = sayi1 / sayi2
        print("Sonuç: ",sonuc)

    elif islem == "%":
        sonuc = sayi1 % sayi2
        print("Sonuç: ",sonuc)

    elif islem == "**":
        sonuc = sayi1 ** sayi2
        print("Sonuç: ",sonuc)

    else:
        print("Yanlış Tuşa Bastınız, lütfen programı tekrar başlatın.")

if language == "en" or language == "En" or language == "English":

    number1 = int(input("1st Issue: "))
    number2 = int(input("2nd issue: "))
    action = input("Select an Action (+,-,*,/,%,**): ")

    if action == "+":
        result = number1 + number2
        print("Result: ",result)
    
    elif action == "-":
        result = number1 - number2
        print("Result: ",result)

    elif action == "*":
        result = number1 * number2
        print("Result: ",result)

    elif action == "/":
        result = number1 / number2
        print("Result: ",result)

    elif action == "%":
        result = number1 % number2
        print("Result: ",result)

    elif action == "**":
        result = number1 ** number2
        print("Result: ",result)

else: 
    print("Turkish: Yanlış Tuşa Bastınız. Programı Yeniden Başlatın. \n English: You pressed the wrong button. Restart the program.")
