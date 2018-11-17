errno = 50159747054
name = 'Bob'

print(">>OLD METHOD")
print('Hello %s' % name)
print("Hello %s, there is a Ox%x error!" % (name, errno))
print("Hey %(name)s there is a Ox%(error)x error!" % {'name':name, 'error':errno})

print(">>NEW METHOD")
print("Hello {}".format(name))
print("Hey {name}, there is a Ox{error:x} error".format(name=name, error = errno))

print(">>LATEST METHOD")
print(f'Hello {name}')

a = 5
b = 10
print(f'The sum of {a} and {b} is {a+b}')

def greet(name, question):
    print(f'Hi {name}, {question}')

greet("Bob", "how are you")