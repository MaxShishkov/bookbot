def count_words(book_text: str) -> int:
    words = book_text.split()

    return len(words)


def count_chars(book_text: str) -> dict[str, int]:
    char_count = {}
    
    for ch in book_text:
        ch = ch.lower()
        if ch not in char_count:
            char_count[ch] = 0
            
        char_count[ch] += 1
    
    return char_count
    
    
def _sort_on(items) -> int:
    return items["num"]


def sort_by_count(char_count: dict[str, int]) -> list[dict[str, int | str]]:
    result = []
    
    for char, count in char_count.items():
        result.append({"char": char, "num": count})
        
    result.sort(reverse=True, key=_sort_on)
    return result