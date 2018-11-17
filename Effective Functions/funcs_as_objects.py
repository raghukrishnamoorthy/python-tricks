def yell(text):
    return text.upper() + '!'

def whisper(text):
    return text.lower() + "!"

bark = yell
funcs = [bark, str.lower, str.capitalize]

for item in funcs:
    print(f"The result of calling {item.__name__} is {item('raghu')}")

print(funcs[2]("raghu"))

def greet(func):
    greeting = func("hi me a python program")
    print(greeting)

greet(str.capitalize)
greet(whisper)

my_map = map(str.capitalize, ["water", "fire", "air"])
print(my_map)
for item in my_map:
    print(item)
print(list(my_map))

#Inner functions
def speak(text):
    
    def whisper(t):
        return t.lower() + ".."
    
    return whisper(text)

print(speak("Hello world"))


def get_speaker_func(text, volume):

    def whisper():
        return text.lower() + "..."
    def shout():
        return text.upper() + "!"
    
    if volume > 0.5:
        return shout
    else:
        return whisper

def make_adder(n):
    
    def add(x):
        return x + n
    return add

my_new_func = make_adder(4)
print(my_new_func(6))

speak_to_me = get_speaker_func("wanksta", 0.7)
print(speak_to_me())

class Adder:

    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return self.n + x

make_add = Adder(5)
print(make_add(6))
print(callable(make_add))