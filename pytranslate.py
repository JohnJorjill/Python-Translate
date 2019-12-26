from translate import Translator 

translator = Translator(to_lang="zh") # Translator class-s translator object uusgej bna
try:
	with open('./test.txt', mode='r') as my_file: # ./test.txt file-g ongoilgood text variable dotor buh contentiin huulaad translate hiigeed test-zh.txt file dotor hadaglah
		text = my_file.read()
		translation = translator.translate(text)
		with open('./test-zh.txt', mode='w') as my_file2:
			my_file2.write(translation)
except FileNotFoundError as e: # FileNotFoundError aldaa zaaval doorh msg print hiih
	print('please check your path')
