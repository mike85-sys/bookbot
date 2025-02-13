def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    lower_character_count = {}
    characters = list(file_contents)
    for character in characters:
        lower_character = character.lower()
        if lower_character not in lower_character_count:
            lower_character_count[lower_character] = 1
        else:
            lower_character_count[lower_character] += 1
    return lower_character_count

def sort_on(char_dict):
    return char_dict["num"]
    
def get_char_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"name": char, "num": count})
    return char_list

file_contents = main()
char_dict = character_count(file_contents)
char_list = get_char_list(char_dict)
char_list.sort(key=sort_on, reverse=True)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count(file_contents)} words found in the document\n")
for char in char_list:
    print(f"The '{char['name']}' character was found {char['num']} times")
print("--- End report ---")
