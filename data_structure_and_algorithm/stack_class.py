class stack:

    # constructor for stack
    def __init__(self):
        self.items = []

    # method to find the size
    def size(self):
        return len(self.items)

    # method to insert an item to the stack
    def push(self, item):
        self.items.append(item)


def main():
    s = stack()
    # prints the size of the stack
    print(s.size())

    # inserts an item to the stack
    s.push(5)

# prints the size of the stack
    print(s.size())

    print(s)

main()

