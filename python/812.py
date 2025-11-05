# Prog. 812
# Write a function to abbreviate 'road' as 'rd.' in a given string.

# References:
# - https://stackoverflow.com/questions/22190064/difference-between-find-and-index


def abbreviate(string: str, word: str, abbreviation: str) -> str:
    start_index = 0
    ret_string = str()

    while start_index < len(string):
        word_index = string.find(word, start_index)

        if word_index == -1:
            ret_string += string[start_index:]
            break

        leading_str = string[start_index : word_index]
        ret_string += leading_str + abbreviation
        
        start_index += len(leading_str) + len(word)

    return ret_string

if __name__ == "__main__":
    string = "This sentence contains the word road everywhere. The word road is being abbreviated."
    word = "road"
    abbreviation = "rd."

    print(abbreviate(string, word, abbreviation))