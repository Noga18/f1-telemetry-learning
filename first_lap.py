
lap_times = [84.2, 83.5, 82.9, 83.1, 82.4, 85.0, 82.1]

fastest_lap = min(lap_times)
slowest_lap = max(lap_times)
average_lap = sum(lap_times) / len(lap_times)
delta = slowest_lap - fastest_lap


print(f"הקפה הכי מהירה: {fastest_lap} שניות")
print(f"הקפה הכי איטית: {slowest_lap} שניות")
print(f"ממוצע זמנים: {average_lap:.2f} שניות")
print(f"הפרש (Delta) בין הכי איטית למהירה: {delta:.2f} שניות")