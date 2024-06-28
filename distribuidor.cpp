#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric> // Add this header

int faturamento_diario(std::vector<int>& dias_faturamento) {
    // Ignore days without sales
    dias_faturamento.erase(std::remove(dias_faturamento.begin(), dias_faturamento.end(), 0), dias_faturamento.end());

    // Calculate total annual revenue
    int total_annual_revenue = std::accumulate(dias_faturamento.begin(), dias_faturamento.end(), 0);

    // Calculate average daily revenue
    double average_daily_revenue = static_cast<double>(total_annual_revenue) / dias_faturamento.size();

    // Count days with revenue above average
    int days_above_average = std::count_if(dias_faturamento.begin(), dias_faturamento.end(), [average_daily_revenue](int day) { return day > average_daily_revenue; });

    // Return minimum, maximum, and days above average
    return days_above_average;
}

int main() {
    // Input data manually
    int n;
    std::cout << "Digite o número de dias: ";
    std::cin >> n;
    std::vector<int> dias_faturamento(n);
    for (int i = 0; i < n; i++) {
        std::cout << "Digite o faturamento do dia " << i+1 << ": ";
        std::cin >> dias_faturamento[i];
    }

    int days_above_average = faturamento_diario(dias_faturamento);
    std::cout << "Dias acima da média: " << days_above_average << std::endl;

    return 0;
}