import inflect
p = inflect.engine()
answer = 0
print(p.number_to_words(342))
for i in range(1,1001):
	string = p.number_to_words(i)
	for j in string:
		if j.isalpha():
			answer+=1
			
print(answer)
