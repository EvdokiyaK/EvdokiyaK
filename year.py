def is_leap_year(year):
 if (year % 4) == 0:
   if (year % 100) == 0:
     if (year % 400) == 0:
       return 'Leap'
     else:
       return 'Not leap'
   else:
     return 'Leap'
 else:
   return 'Not leap'

# функцию можно переписать с помощью логических операторов `and` (И), `or` (ИЛИ) и `not` (НЕ)
def is_leap_year(year):
 # `\` используется для объединения нескольких строк кода
 # в один блок
 if (year % 4) == 0 and (year % 100) == 0 and (year % 400) == 0 \
 or (year % 4) == 0 and not (year % 100) == 0:
   return 'Leap'
 else:
   return 'Not leap'

print(
 is_leap_year(
   int(
     input('Year: ')
   )
 )
)
