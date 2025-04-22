import pandas as pd
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')

# Wczytanie danych
df = pd.read_csv("csv.csv")

temperatures_sorted = df["TEMPERATURE_AVG"].dropna().sort_values()
print(temperatures_sorted.reset_index(drop=True))

pm10_sorted = df["PM10_AVG"].dropna().sort_values()
print(pm10_sorted.reset_index(drop=True))

pm25_sorted = df["PM25_AVG"].dropna().sort_values()
print(pm25_sorted.reset_index(drop=True))

pressure_sorted = df["PRESSURE_AVG"].dropna().sort_values()
print(pressure_sorted.reset_index(drop=True))

# Usunięcie błędnej wartości -40
df = df[df["TEMPERATURE_AVG"] != -40]

# Usunięcie 3 największych wartości z PM10_AVG
df = df.sort_values("PM10_AVG", ascending=False).iloc[3:]

# Usunięcie 3 największych wartości z PM25_AVG
df = df.sort_values("PM25_AVG", ascending=False).iloc[3:]

# Lista kolumn do analizy
columns_to_analyze = ["HUMIDITY_AVG", "PRESSURE_AVG", "TEMPERATURE_AVG", "PM10_AVG", "PM25_AVG"]

# Analiza statystyczna
for col in columns_to_analyze:
    print(f"\nAnaliza dla kolumny: {col}")
    data = df[col].dropna()

    try:
        mode_val = statistics.mode(data)
    except statistics.StatisticsError:
        mode_val = "Brak jednej dominanty"

    print(f"Średnia: {statistics.mean(data)}")
    print(f"Mediana: {statistics.median(data)}")
    print(f"Moda: {mode_val}")
    print(f"Wariancja: {statistics.variance(data)}")
    print(f"Odchylenie standardowe: {statistics.stdev(data)}")

# Wspólna siatka wykresów (2 wiersze, 3 kolumny)
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
axs = axs.flatten()

# Rysowanie histogramów
for i, col in enumerate(columns_to_analyze):
    data = df[col].dropna()
    sns.histplot(data, kde=True, bins=10, color="cornflowerblue", ax=axs[i])
    axs[i].set_title(f"{col}", fontsize=12)
    axs[i].set_xlabel("")
    axs[i].set_ylabel("")

# Usunięcie pustego subplotu jeśli jest nieparzysta liczba kolumn
if len(columns_to_analyze) < len(axs):
    for j in range(len(columns_to_analyze), len(axs)):
        fig.delaxes(axs[j])

plt.suptitle("Histogramy dla zmiennych środowiskowych", fontsize=16)
plt.tight_layout(rect=(0, 0.03, 1, 0.95))
plt.show()
