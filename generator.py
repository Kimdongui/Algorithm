def generate():
    print("Now starting session 1...")
    yield 1
    print("Now starting session 2...")
    yield 2
    print("Now starting session 3...")
    yield 3

g = generate()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
