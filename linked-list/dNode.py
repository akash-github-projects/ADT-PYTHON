class ListNode:
    def __init__(self, data):

        # store data
        self.data = data

        # store reference of next node (default None)
        self.next = None

        # store reference of prev node (default None)
        self.prev = None

        return

    def has_value(self, value):

        if self.data == value:
            return True
        else:
            return False

