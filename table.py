
# My Intent: create a data entry system (table)

class Table:
    def __init__(self):
        # create an empty table
        self.data = []
        self.col_names = []

    def add(self, element):
        '''adds the element, where element is a dictionary
        takes O(c) on the average case'''
        if len(self.data) == 0:
            self.col_names = list(element.keys())
            self.data.append(element)
        else:
            if list(element.keys()) == self.col_names:
                self.data.append(element)

    def delete(self, index):
        '''deletes the element at that index
        takes O(n) time, where n is the length of the list'''
        del self.data[index]

    def delete_all(self, condition):
        '''deletes all elements that satisfy the condition
        condition is function that takes a dict and returns a boolean
        O(n^2) worst time'''
        # keep a list of elements to delete (they will be sorted) 
        to_be_deleted = []
        
        for i in range(len(self.data)):
            if condition(self.data[i]):
                to_be_deleted.append(i)

        # go through them in the opposite order to delete them
        for j in reversed(to_be_deleted):
            del self.data[j]

    def __iter__(self):
        return self.data.__iter__()

    def __getitem__(self, index):
        '''returns the element at the index'''
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def search_all(self, condition):
        '''returns a list of all indices that satisfy the condition
        O(n)'''
        indices = []
        for i in range(len(self.data)):
            if condition(self.data[i]):
                indices.append(i)
        return indices

    def __str__(self):
        a = ''
        for d in self.data:
            a += str(d) + '\n'
        return a

if __name__ == '__main__':
    t = Table()
    # fruit table
    # test add
    t.add({'fruit': 'banana', 'cost': 0.49, 'taste': 'exotic'})
    t.add({'fruit': 'orange', 'cost': 1.00, 'taste': 'sour'}) 
    t.add({'fruit': 'coconut', 'cost': 1.20, 'taste': 'sweet'})
    # don't add
    t.add({'fruit': 'coconut', 'cost': 1.20})
    print(t)

    # test remove
    t.delete(2)
    print(t)

    # test delete_all
    t.add({'fruit': 'coconut', 'cost': 1.20, 'taste': 'sweet'})
    t.add({'fruit': 'watermelon', 'cost': 10.00, 'taste': 'sweet'})
    print(t)
    t.delete_all(lambda d: d['taste'] == 'sweet')
    print(t)

    # test iter
    for i in t:
        print(i)

    # test getitem
    s = ''
    for i in range(len(t)):
        s += str(t[i]) + '\n'
    print(s)
    print(t.__str__() == s)

    # test search_all
    t.add({'fruit': 'coconut', 'cost': 1.20, 'taste': 'sweet'})
    t.add({'fruit': 'watermelon', 'cost': 10.00, 'taste': 'sweet'})
    t.add({'fruit': 'durian', 'cost': 4.00, 'taste': 'sweet'})
    print(t.search_all(lambda d: d['taste'] == 'sweet'))
        
