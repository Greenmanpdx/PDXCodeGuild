# class node:
#     def __init__(self, character, previous, next):
#         self.character = character
#         self.previous = previous
#         self.next_node = next


class Initiative_list(list):
    

    def __getitem__(self, item):
        try:
            return super(Initiative_list, self).__getitem(item)
        except IndexError:
            pass

        try:
            index = int(item)
            index = index % self.__len__()
            return super(Initiative_list, self).__getitem__(index)
        except ValueError:
            raise TypeError
