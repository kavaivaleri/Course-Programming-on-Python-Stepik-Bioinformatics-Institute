```
Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов в сутки. Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.
```

recommend_low = int(input())
recommend_high = int(input())
real = int(input())

if recommend_low <= real <= recommend_high:
    print("Это нормально")
elif recommend_low > real:
    print("Недосып")
elif recommend_high < real:
    print("Пересып")

