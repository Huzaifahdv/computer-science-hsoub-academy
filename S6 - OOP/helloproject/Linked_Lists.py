# U3 lesson 1: Linked lists
class Node:  # صنف العقدة
    def __init__(self, data):  # دالة تهيئة كائن العقدة
        self.data = data
        self.next = None


class LinkedList:  # صنف قائمة مترابطة يضم كائن العقدة
    def __init__(self):  # تهيئة رأس القائمة
        self.head = None

    def push(self, new_data):  # دالة لإدراج عقدة جديدة في بداية القائمة المترابطة
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):  # دالة لإدراج عقدة في موقع معين من القائمة المترابطة
        if prev_node is None:
            raise ValueError
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
# في الدالة لا يمكن إضافة عقدتين في نفس المكان لأنه لم يتم تعريف متغير حاول إصلاح المشكلة مع التجارب

    def apppend(self, new_data):  # دالة لإدراج عقدة في نهاية القائمة المترابطة
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_data
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
# الدالة يستطيع إدراج عقدة واحدة فقط ولا يستطيع إدراج عدة عقد

    # تمرين: أضف دالة تحذف عقدة معينة
    def delete(self, Node):  # أخذته من التعليقات
        if self.head == Node:
            self.head = Node.next
            del Node
            return
        item = self.head
        while item:
            if item.next == Node:
                item.next = Node.next
                break
            item = Node.next
        del Node

    def print_list(self):  # دالة طباعة عناصر القائمة المترابطة
        item = self.head
        while item:
            print(item.data)
            item = item.next


llist = LinkedList()
first = Node(1)
llist.head = first
second = Node(2)
llist.head.next = second
third = Node(3)
second.next = third
fifth = Node(5)
third.next = fifth
llist.apppend(6)
llist.apppend(7)
llist.delete(first)

llist.print_list()
print('-'*30)
llist.push(1)
llist.insert(third, 4)
llist.print_list()
