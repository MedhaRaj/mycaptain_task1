def most_frequent():
	word = str(input("Enter your word:"))
	dict1 = {wrd:word.count(wrd) for wrd in word}
	sorted_x = sorted(dict1.items(), key= lambda t:t[1],reverse=True)
	for i in range(len(sorted_x)):
		for j in range(2):
			print(sorted_x[i][j],end=" ")
		print()
most_frequent()


