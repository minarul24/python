class stack:

    # constructor for stack
    def __init__(self):
        self.items = []

    # method to find the size
    def size(self):
        return len(self.items)

    


def main():
    s = stack()
    print(s.size())


main()

