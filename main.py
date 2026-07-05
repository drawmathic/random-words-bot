#necessary for random letter and word length selection
import random

#list of all the letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

vowels = [0, 4, 8, 14,20]

def ai(w_count):
	w_list =[] #words list
	
	#create words and fill words list with them
	for i in range(w_count):
		
		#this affects the probability distribution of numbers from 1 to 8, thus helping in getting reasonable(still flawed) length of words from 1 to 8 with 1 and 8 being the most unlikely
		W = [random.randint(1,8),random.randint(2,7),random.randint(3,6),random.randint(4,5)]
		
		w_len = W[random.randint(0,3)] #word length
		word = ""
		for j in range(0,w_len):
			L = [random.randint(0,25), vowels[random.randint(0,4)]]
			word = f"{word}{letters[L[random.randint(0,1)]]}"
		w_list.append(word)
		
	#form the sentence string with words list
	sentence=""
	for i in range(w_count):
		sentence = f"{sentence} {w_list[i]}"
		
	return sentence
	
print(ai(1000))
