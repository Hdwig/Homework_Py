def pers_data(name, sec_name, old, city, email, numb):
    print(f"имя - {name}; фамилия - {sec_name}; год рождения - {old}; город проживания - {city}; email - {email}; "
          f"телефон - {numb}")


n = input("Введите Ваше имя:")
sn = input("Введите Вашу фамилию:")
o = input("Введите Ваш возраст:")
c = input("Введите Ваш город:")
e = input("Введите Вашу почту:")
numb = input("Введите Ваш телефон:")
pers_data(name=n, sec_name=sn, old=o, city=c, email=e, numb=numb)
