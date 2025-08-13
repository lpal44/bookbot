import sys
from stats import get_num_words, character_count, get_book_text, sort_on, sorted_list

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	char_counts = character_count(book_text)
	sorted_chars = sorted_list(char_counts)
	num_words = get_num_words(book_text)
	print_report(book_path, num_words, sorted_chars)
def print_report(book_path, num_words, sorted_chars):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in sorted_chars:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")

	print("============= END ===============")

main()
