# Prog. 102
# Write a function to convert snake case string to camel case string.

def snake_to_camel_case(string: str) -> str:
    words = string.split('_')
        
    for i, word in enumerate(words[1:]):
        if word == '':
            continue

        words[i + 1] = word.capitalize()

    return words[0].lower() + "".join(words[1:]) 


if __name__ == '__main__':
    print(snake_to_camel_case("aaron_mathew"))