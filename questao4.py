faturamentos_estados= {
'SP': 67836.43,
'RJ': 36678.66,
'MG': 29229.88,
'ES': 27165.48,
'Outros': 19849.53
}

total_faturamentos = sum(faturamentos_estados.values())
for estado, valor in faturamentos_estados.items():
    percentual = (valor / total_faturamentos) * 100
    print(f"{estado}: {percentual:.2f}% do faturamento total. ")