'''
Dedicated towards returning the captial's found in a string
'''

import unittest

def capitals(word):
    results = []
    for char in word:
        if char.isupper():
            results.append(char)
    return results

#print (capitals1("AbCd eFgHIJKlMnoP"))


def captials_one(word):

    x = [char for char in word if char.isupper()]
    yield x

#print (next(captials_one("AbCd eFgHIJKlMnoP")))

print(capitals("AbCdEf"))

class TestCapitalMethod(unittest.TestCase):
    param_list = [("AbCdE", "ACE"), ("aBcDe", "BD")]

    def test_capitals(self):
        for p1, p2 in self.param_list:
            with self.subTest():
                str1 = "".join(capitals(p1))
                print("str1: ", str1, ", p2: ", p2)
                self.assertEqual(str1, p2)

if __name__ == '__main__':
    unittest.main()