def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    imc = peso / (altura ** 2)
    return imc

def verificar_imc_par_impar(imc):
    imc_inteiro = int(imc)
    if imc_inteiro % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

peso = float(input("Você pesa quantos kg: "))
altura = float(input("Qual sua altura em metros: "))

imc = calcular_imc(peso, altura)
resultado = verificar_imc_par_impar(imc)

print(f"O IMC é: {imc:.2f} e é {resultado}.")