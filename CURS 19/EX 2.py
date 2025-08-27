class MyList:
    def __init__(self):
        self.items = []

    def add_item(self,item,*args):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self,index):
        return self.items[index]

    def __contains__(self,item):
        return item in self.items



if __name__ == "__main__":
    list1 = MyList()
    list1.add_item(1,)
    list1.add_item(2,)
    list1.add_item(3,)
    list1.add_item("Mihai",)
    print(list1.__len__())
    print(list1.__getitem__(3))
    print(list1.__contains__("Mihai"))




