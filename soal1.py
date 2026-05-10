temperatures = [25, 28, 30, 22, 35, 40, 18, 24]

#jawaban
temp_fahrenheit = [(c * 9/5) + 32 for c in temperatures]

print("Data Fahrenheit:")
print(temp_fahrenheit)

print("3 data terakhir:")
print(temp_fahrenheit[-3:])