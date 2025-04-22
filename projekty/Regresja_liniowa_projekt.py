import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import linregress
matplotlib.use('TkAgg')

data = pd.read_csv("data.csv", skiprows=4, names=["Data", "Temperatura"])
data.dropna(inplace=True)
print(data.to_string())

# Usunięcie wartości z roku 1974 która wynosi -90
data = data[data["Temperatura"] >= -90]

# Pobranie tylko pierwszych 4 cyfr (roku) z kolumny "Data"
data["Data"] = data["Data"].astype(str).str[:4].astype(int)

# Zamiana temperatury z Fahrenheita na Celsjusza
data["Temperatura"] = (data["Temperatura"] - 32) * 5/9

# Zamiana temperatury na liczby zmiennoprzecinkowe
data["Temperatura"] = data["Temperatura"].astype(float)

print(data.head())
print(data.info())
print(data.describe())
print("------------------------------------------------------------")

# Obliczenie regresji liniowej
slope, intercept, r_value, p_value, std_err = linregress(data["Data"], data["Temperatura"])

print(f'Wartość współczynnika korelacji: {r_value:.2f}')
print(f'Wartość p: {p_value}')
print(f'Błąd standardowy nachylenia: {std_err:.5f}')
print("------------------------------------------------------------")

# Prognoza temperatury w 2025 roku
prognoza_2025 = slope * 2025 + intercept
print(f"Prognozowana temperatura w 2025 roku: {prognoza_2025:.2f}°C ///// Temperatura rzeczywista w styczniu 2025 to 8,5°C")

# Wizualizacja wyników
plt.figure(figsize=(10, 5))
sns.set(style="whitegrid")

# Scatter plot danych historycznych
sns.scatterplot(x=data["Data"], y=data["Temperatura"], label="Dane historyczne", color='blue', s=100, edgecolor='black', alpha=0.7)

# Linia regresji
plt.plot(data["Data"], slope * data["Data"] + intercept, color='red', label="Regresja liniowa", linewidth=2)

# Ustawienia etykiet
plt.xlabel("Rok", fontsize=14, weight='bold', color='darkblue')
plt.ylabel("Średnia temperatura w styczniu (°C)", fontsize=14, weight='bold', color='darkblue')

plt.title("Regresja liniowa temperatury w Las Vegas", fontsize=16, weight='bold', color='darkred')
plt.legend()
plt.show()
