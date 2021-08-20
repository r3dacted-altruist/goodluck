import cryptocode
word = input('encrypted string: ')
key = input('key: ')

def solve(word, key):
    output = cryptocode.decrypt(word, key)
    print(output)

solve(word, key)

# keep this resource in mind 