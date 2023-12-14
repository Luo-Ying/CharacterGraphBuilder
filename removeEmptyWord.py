import string

def remove_punctuation(input_file, output_file):

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    translator = str.maketrans('', '', string.punctuation)
    content_without_punctuation = content.translate(translator)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content_without_punctuation)

input_filename = 'test.txt'
output_filename = 'test_output.txt'

remove_punctuation(input_filename, output_filename)