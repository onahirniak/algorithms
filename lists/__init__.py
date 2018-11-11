from .linked_list import LinkedList

class ListsRunner():
    @staticmethod
    def run():
        linked_list = LinkedList()

        linked_list.push(0)
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.push(0)

        linked_list.printList()

        linked_list.reverse()

        linked_list.printList()

        linked_list.search_and_print(1)
        linked_list.search_and_print(0)
        linked_list.search_and_print(100)

        linked_list.remove(3)
        linked_list.remove(0)
        linked_list.remove(0)
        linked_list.remove(0)
        linked_list.printList()