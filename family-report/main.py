def kids (sentence_func):
    def assign(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f'{original_sentence} by the kids.'
    return assign

def mom (sentence_func):
    def assign(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f'{original_sentence} by mom.'
    return assign

def dad (sentence_func):
    def assign(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f'{original_sentence} by dad.'
    return assign

@kids
def laundry():
    return "The dirty laundry was cleaned"

@kids
def garbage():
    return "The garbage was taken out"

@mom
def dust():
    return "The house was dusted"

@dad
def groom():
    return "The dog was brushed"

print(laundry())
print(garbage())
print(dust())
print(groom())