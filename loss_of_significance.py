import matplotlib.pylab as plt

number = 0
real = 0
count = 0

error_list = []
number_list = []
real_list = []

for i in range(10000):
	number += 1/3	
	count += 1
	if count == 3:
		real += 1
		count = 0
		error = (100*(real - number)/real)
		error_list.append(error)
		real_list.append(real)
		print("Numero Supuesto: " + str(real) + "  Numero real: " + str(number))

plt.plot(real_list, error_list)
plt.xlabel("Tamano numeros")
plt.ylabel("Error relativo")
plt.show()
