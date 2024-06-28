def faturamento_diario(dias_faturamento):
    # Ignore days without sales
    dias_faturamento = [day for day in dias_faturamento if day > 0]

    # Calculate total annual revenue
    total_annual_revenue = sum(dias_faturamento)

    # Calculate average daily revenue
    average_daily_revenue = total_annual_revenue / len(dias_faturamento)

    # Count days with revenue above average
    days_above_average = sum(1 for day in dias_faturamento if day > average_daily_revenue)

    # Return minimum, maximum, and days above average
    return min(dias_faturamento), max(dias_faturamento), days_above_average

# Input data manually
n = int(input("Digite o número de dias: "))
dias_faturamento = []
for i in range(n):
    day = int(input(f"Digite o faturamento do dia {i+1}: "))
    dias_faturamento.append(day)

min_sale, max_sale, days_above_average = faturamento_diario(dias_faturamento)
print("Faturamento diário mínimo:", min_sale)
print("Faturamento diário máximo:", max_sale)
print("Dias acima da média:", days_above_average)