import sys
from pathlib import Path
from stats import count_words, count_chars, sort_by_count




def get_book_texty(filepath: str) -> str:
    with open(filepath, "r") as f:
        file_contents = f.read()
        
    return file_contents



def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = str(Path(sys.argv[1])) # str() to avoid typecheck errors
    book_text = get_book_texty(book_path)
    num_words = count_words(book_text=book_text)
    
    char_count = count_chars(book_text=book_text)
    sorted_count = sort_by_count(char_count=char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    
    for item in sorted_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
            
    print("============= END ===============")
    
    
if __name__ == "__main__":
    main()