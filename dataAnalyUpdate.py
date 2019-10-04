data = []
max_count = 0
max_count_word = None
total_word_count = 0 
count = 0
length = 0
Total_length = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
	length = len(data)
	print('\n....................................')
	print(length, 'reviews in the file.')
	print('....................................\n')
	while count < length:
		print('\nreview ', count + 1,'\n')
		print(data[count])
		print('\n', len(data[count]))
		go = 'N'
		while True:
			if go == 'Y' or go == 'Q':
				break
			else:
				print('\n***************************************************************************\n')
				go = input('input Y for go to next review or Q for quit!......')
		if go == 'Q':
			print('Quit read!')
			break
		count += 1

words_dict = {}
for d in data:
	words = d.split()
	for word in words:
		if word in words_dict:
			words_dict[word] += 1
		else:
			words_dict[word] = 1
		total_word_count += 1
for word in words_dict:
	if words_dict[word] > 1000000:
		print(word, ' ', words_dict[word])
	if words_dict[word] > max_count:
		max_count = words_dict[word]
		max_count_word = word
print('maximun wording is "',max_count_word, '" by ', max_count, ' times!')
print('Total words count =', total_word_count)

while True:
	i = input('input a word! or Q123 to quit ')
	if i == 'Q123':
		break
	elif i in words_dict:
		print(i, ' is in words_dict for', words_dict[i], ' times')
	else:
		print(i, ' is not in words_dict!')









	
