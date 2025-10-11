s = set(range(10))
it = iter(s)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
print("done")

while (line := input()) != "":
    print(line)
