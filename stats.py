def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents


def get_num_words(text):
        words = text.split()
        return len(words)
        

def character_count(text):
	text = text.lower()
	count = {}
	for char in text:
		if char in count:
			count[char] += 1
		else: 
			count[char] = 1
	return count
		
def sort_on(items):
    return items["num"]

def sorted_list(char_dict):
	list_of_dicts = []
	for char in char_dict:
		list_of_dicts.append({"char": char, "num": char_dict[char]})
	list_of_dicts.sort(reverse=True, key=sort_on)
	return list_of_dicts

