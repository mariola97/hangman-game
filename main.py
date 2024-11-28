rijec="baza"
pogoci=0
pogreske=0
while True:
    slovo=input("unesi slovo")
    if slovo in rijec:
        pogoci+=rijec.count(slovo)
        if pogoci==len(rijec):
            print(pogoci)
            print("pobijedili ste")
            break