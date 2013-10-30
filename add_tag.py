def add_tag(input_string):
    return '\Bla-bla{' + input_string + '}'

def process_me(my_text):
    search = 'чтобы'
    return my_text.replace(search, add_tag(search))
