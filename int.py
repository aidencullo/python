def startswith(prefix):
    def inner(word):
        return word.startswith(prefix)

    return inner

def doesntstartwith(prefix):
    does = startswith(prefix)
    def inner(word):
        return not does(word)

    return inner
    
dunder = '__'
int_attrs = dir(int)
dunders = list(filter(startswith(dunder), int_attrs))
not_dunders = list(filter(doesntstartwith(dunder), int_attrs))

print(dunders)
print(not_dunders)
