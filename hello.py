sumKgCandy = float(input("Введите цену 1кг  конфет : "))

for i in range(1, 11):
    print(f"{i/10} кг конфет будет стоить {i/10 * sumKgCandy} рублей")