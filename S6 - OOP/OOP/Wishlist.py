# lesson 16: operators overloading
class Wishlist:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, item):
        return self.items[item]

    def __add__(self, other):
        return self.items.append(other)

    def __str__(self):
        wishlist = []
        for index, item in enumerate(self.items):
            wishlist.append(f'{index + 1}. {item}')
        print('List of items in your wishlist: ')
        print('-' * 30)
        return '\n'.join(wishlist)


my_wishlist = Wishlist(['pro programmer', 'miauu miauuu', 'abdulquddusss'])
print(len(my_wishlist))
print(my_wishlist[2])
my_wishlist + 'chinggg changgg😼😼'
print(my_wishlist)
