def give_toy():
    yield "car"
    yield "pokemon"
    yield "crane"
    yield "bike"

toy = give_toy()

print(next(toy))
print(next(toy))
print(next(toy))
print(next(toy))