''' This document has a function to convert all sentences to start with a capital letter.'''

def sentence_case(text):
    ''' Takes in a text and coverts all the sentences into proper casing'''
    #splitting text into individual sentences
    text_list = text.split('.')

    #defining an empty variable
    result = ''

    #capitalizing each sentence and merging it to the execute_result

    for element in text_list:
        #remove white spaces before or after each sentence
        element = element.strip()
        result +=element.capitalize()+'.'

    # Removing the execess period at the end of last lines
    result = result[:-1]
    return result

if __name__ == '__main__':

    text1 = '''this is to test the function.Here i'm not using the capitalization.the function should take care of it.'''

    print(f"Original text:\n{text1}")
    print(f"Corrected text:\n{sentence_case(text1)}")

