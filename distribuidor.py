# Suponha que 'faturamentos' é o vetor com os valores de faturamento diário
faturamentos = [...]  # O vetor já está carregado com os valores

# Filtrar os dias com faturamento maior que zero
faturamentos_validos = [faturamento for faturamento in faturamentos if faturamento > 0]

# Calcular o menor e maior valor de faturamento
menor_faturamento = min(faturamentos_validos)
maior_faturamento = max(faturamentos_validos)

# Calcular a média anual (ignorando os dias sem faturamento)
media_anual = sum(faturamentos_validos) / len(faturamentos_validos)

# Contar o número de dias com faturamento acima da média anual
dias_acima_media = sum(1 for faturamento in faturamentos_validos if faturamento > media_anual)

print("Menor valor de faturamento do ano:", menor_faturamento)
print("Maior valor de faturamento do ano:", maior_faturamento)
print("Número de dias com faturamento acima da média anual:", dias_acima_media)
