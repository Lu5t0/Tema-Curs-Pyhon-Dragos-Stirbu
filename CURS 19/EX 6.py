class IDGenerator:
    _counter = 0

    @staticmethod
    def next_id():
        IDGenerator._counter += 1
        return IDGenerator._counter

if __name__ == "__main__":


    print(IDGenerator.next_id())
    print(IDGenerator.next_id())
    print(IDGenerator.next_id())
    print(IDGenerator.next_id())
