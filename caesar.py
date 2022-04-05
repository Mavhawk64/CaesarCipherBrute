alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dictionary = open('english3.txt','r').read().split('\n')
def encrypt(word,n,alphabet):
	return convert_ints_to_str(add_arr_by_n_mod(convert_to_ints_mod(word,alphabet),n,len(alphabet)),alphabet)
def decrypt(word,n,alphabet):
	return encrypt(word,-n,alphabet)
def force_decrypt(word,alphabet):
	possibilities = []
	for i in range(0,len(alphabet)):
		words = decrypt(word,i,alphabet).split(' ')
		# print(words)
		for x in words:
			if x in dictionary:
				possibilities.append(' '.join(words))
				break
	# make this return best-fit word
	return possibilities
def force_best_decrypt(word,alphabet):
	poss = force_decrypt(word,alphabet)
	for i in poss:
		is_word = True
		for j in i.split(' '):
			is_word &= j in dictionary
			# print(j,is_word)
		if is_word:
			return i
	return 'No best string found. Here are some possibilities: [' + ', '.join(poss) + ']'
def convert_to_ints_mod(word,alphabet):
	word = word.lower()
	a = []
	for i in word:
		if i in alphabet:
			a.append(alphabet.index(i))
		elif i == ' ':
			a.append(-1)
	return a

def add_arr_by_n_mod(arr,n,m):
	for i in range(0,len(arr)):
		if arr[i] != -1:
			arr[i] += n
			arr[i] %= m
	return arr

def convert_ints_to_str(arr,alphabet):
	word = ''
	for i in arr:
		if i != -1:
			word += alphabet[i]
		else:
			word += ' '
	return word

# use: 

# encrypt obvious - pass in word, shift amt, and alphabet

# decrypt obvious - pass in word, shift amt, and alphabet

# force_decrypt - pass in word and alphabet - runs through all of the possible shifts and returns an array of all of the possibilites - a possibility is defined to have at least one english word in the phrase

# force_best_decrypt - pass in word and alphabet - calls force_decrypt to get all possibilites, runs through each possibility and checks to see if each word in that phrase is in the dictionary - returns phrase if all words are in dictionary or returns all possibilites as a string if not

# convert_to_ints_mod - pass in word and alphabet - does a lookup in the alphabet, sets array to index of letter in alphabet, and sets all spaces to be -1

# add_arr_by_n_mod - pass in int array, shift amount, and modular base - shifts all numbers in array by n : C = (P + n) mod m

# convert_ints_to_str - pass in nt array and alphabet - builds and returns a string from each index of alphabet, specified in the int array.



print(force_best_decrypt(encrypt('the quick brown fox jumps over a lazy dog',23,alphabet),alphabet))