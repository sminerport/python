print()

# User input
sentence = input("Please enter some text: ")

# Remove Punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
noPunct = ""
for char in sentence:
	if char not in punctuations:
		noPunct += char
print()

# Split each word on a space
sentenceList = noPunct.split()

totalLetters = 0

if not sentenceList:
	print("List words   Length")
	print("----------   ------")

elif sentenceList:
	#get longest string in List
	longestWord = len(max(sentenceList, key = len))
	if longestWord < 13:
		# Calculate total word length
		print("List words   Length")
		print("----------   ------")
		for word in sentenceList:
			print("{: <12} {:^7}".format(word, len(word)))
			totalLetters += len(word)
	else:
		format = longestWord - 8
		print("List words" + ' ' * (longestWord - 8) + "Length")
		print("----------" + ' ' * (longestWord - 8) + "------")
		for word in sentenceList:
			print(("{w:<{m}} {l:^8}").format(w = word,m = longestWord,l = len(word)))
			totalLetters += len(word)

# Calculate total words
totalWords = len(noPunct.split())

# Print Total words and letters
print()
print("Total Letters   Total Words")
print("-------------   -----------")
print("{: ^13}   {: ^11}".format(totalLetters, totalWords))

# Calculate Average
print()
print("Average letters per word")
print("------------------------")

if totalWords > 0:
	average = totalLetters / totalWords
else:
	average = 0

#Print output
print('{0:d} / {1:d} = {2:.2f}'.format(totalLetters, totalWords, average))

print()

#Final Output
print('Result')
print('------')
if average == 0:
	print('An average of {0:.2f} means you did not input any words!'.format(average))
elif 0 < average < 5:
	print('{0:.2f} is less than 5 average letters per word.'.format(average))
elif 5 <= average < 10:
	print('{0:.2f} is between 5 and 10 average letters per word.'.format(average))
else:
	print(('{0:.2f} is greater than 10 average letters per word!'
	       ' You have a large vocabulary!').format(average))
