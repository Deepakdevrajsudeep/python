
# class Parent:
#     def calculation(self):
#         print("This is a parent class")

# class Child(Parent):
#     def child_class(self):
#         print("This is a child class")

# p = Child()
# p.child_class()




# class grandfather():
#     def grand(self):
#         print("This is a grand class")
# class father(grandfather):
#     def further(self):
#         print("This is a father class")
# class child(father):
#     def children(self):
#         print("This is a child class")
# x = child()
# x.children()
# x.further()
# x.grand()


class brother():
    def sibling_1(self):
        print("first brother")
class brother_2():
    def sibling_2(self):
        print("second brother")
class sister(brother,brother_2):
    def sibling_3(self):
        print("third brother")
k=sister()
k.sibling_3()
k.sibling_2()
k.sibling_1()                     