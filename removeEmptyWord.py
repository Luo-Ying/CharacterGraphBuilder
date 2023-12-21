import string

code_of_special_character = [8212, 8217]

def remove_punctuation(content):
    
    content_without_punctuation = ''.join([' ' if ( ord(char) < 65 or (ord(char) > 90 and ord(char) < 97) or (ord(char) > 122 and ord(char) < 192) or ord(char) in code_of_special_character ) else char for char in content])

    return content_without_punctuation


def lemmatisation(input_filename, output_filename):
    
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content_without_punctuation = remove_punctuation(content)
    # print(content_without_punctuation)
    
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(content_without_punctuation)
    

lemmatisation('test.txt', 'test_output.txt')