import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Product": ["Latte", "Latte", "Mocha", "Latte", "Mocha", "Americano", "Latte"],
    "Cups_Sold": [120, 135, 98, 150, 110, 165, 142],
    "Revenue": [540, 610, 460, 690, 500, 720, 640],
}

df = pd.DataFrame(data)

cups_array = np.array(data["Cups_Sold"])
mean_cups = np.mean(cups_array)
max_cups = np.max(cups_array)
min_cups = np.min(cups_array)


sns.set_theme(style="whitegrid")
fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.plot(df["Day"], df["Cups_Sold"], marker='o', linestyle='-', color='b', linewidth=2)
ax1.set_title("Daily Cups Sold")
ax1.set_xlabel("Day of the Week")
ax1.set_ylabel("Number of Cups")
ax1.grid(True, linestyle='--', alpha=0.7)

plt.show()