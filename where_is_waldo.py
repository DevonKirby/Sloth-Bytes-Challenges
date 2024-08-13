from collections import defaultdict

def where_is_waldo(map):
    distinct_items = defaultdict(int)

    for row in map:
        for item in row:
            distinct_items[item] += 1

    key = ''

    for item, value in distinct_items.items():
        if value == 1:
            key = item

    coord = []

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == key:
                print('found match')
                coord = [y+1, x+1]

    return coord


result = where_is_waldo([
  ["A", "A", "A"],
  ["A", "A", "A"],
  ["A", "B", "A"]
])
print(result)

result = where_is_waldo([
  ["c", "c", "c", "c"],
  ["c", "c", "c", "d"]
])
print(result)

result = where_is_waldo([
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["P", "O", "O", "O"],
  ["O", "O", "O", "O"]
])
print(result)
