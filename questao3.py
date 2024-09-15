import json

with open('dados.json', 'r' ) as file:
    data = json.load(file)

faturamento_diario = [item['valor'] for item in data  if item['valor'] >0]

def calcular_faturametno(faturametonos):
    menor_fatrutamento = min(faturametonos)
    maior_faturametno = max(faturametonos)
    media_faturamentos = sum(faturametonos)/ len (faturametonos)
    return menor_fatrutamento, maior_faturametno, media_faturamentos

menor_fatrutamento,maior_faturametno,media_faturamentos = calcular_faturametno(faturamento_diario)

print(f"Menor faturamento: {menor_fatrutamento}")
print(f"Maior faturamento: {maior_faturametno}")
print(f"Media de faturamento: {media_faturamentos:.2f}")

