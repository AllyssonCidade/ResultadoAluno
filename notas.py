while True:
    aluno = input("Digite o nome do aluno: ")
    faltas = int(input("Digite o número de faltas: "))

    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 5 and faltas <= 5:
        print(f"Aluno {aluno} aprovado.")
    else:
        print(f"Aluno {aluno} reprovado.")

    continuar = input("Deseja verificar mais um aluno? (s/n): ")
    if continuar.lower() == 'n':
        break
