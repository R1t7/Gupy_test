import json



def ler_dados(filename):
    with open(filename, 'r') as file:
        return json.load(file)



def calcular_faturamento(dados):
    valores = [d['valor'] for d in dados['faturamento'] if d['valor'] > 0]

    if not valores:
        return None, None, 0  # Não há faturamento

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_faturamento = sum(valores) / len(valores)

    dias_superiores_media = sum(1 for valor in valores if valor > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_superiores_media


dados = ler_dados('faturamento.json')
menor, maior, dias_superiores = calcular_faturamento(dados)

print(f'Menor faturamento: {menor}')
print(f'Maior faturamento: {maior}')
print(f'Dias com faturamento acima da média: {dias_superiores}')
