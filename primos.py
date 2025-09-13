def es_primo_filter(num):
	if(num < 2):
		return False
	for i in range(2,num):
		if num % i == 0:
			return False
	return True

def primos(max):
	for num in range(max):
		primo = True
		if(num < 2):
			primo = False
		else:
			for i in range(2,num):
				if num % i == 0:
					primo = False
		if(primo is True):
			yield num


print(list(filter(es_primo_filter,range(100))))

print(list(primos(100)))