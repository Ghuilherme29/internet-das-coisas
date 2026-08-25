notas = []

for i in range(8):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)


media = sum(notas) / len(notas)
acima_da_media = [nota for nota in notas if nota > media]
print(f"\nMédia da turma: {media:.2f}")
print(f"Notas acima da média: {acima_da_media}")