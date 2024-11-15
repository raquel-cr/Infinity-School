# Salário

salario = float(input("Qual o seu salário mensal: "))

horasSem = float(input("Quantas horas foram trabalhadas essa semana: "))

horasMes = horasSem * 4.33

salarioHora = salario / horasMes

print(horasMes)

print(f"O seu salário por hora é: R${salarioHora:.2f}")