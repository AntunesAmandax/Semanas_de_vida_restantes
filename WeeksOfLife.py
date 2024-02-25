print("Vamos descobrir quantas semanas de vida você ainda possui, considerando que viva até 90 anos?")
age = input("Quantos anos você tem?")
ageAsInterger = int(age)

LifeTime = (90 * 52) - (ageAsInterger * 52)

print(f"Você possui {LifeTime} semanas de vida restantes, aproveite com sabedoria. ")
