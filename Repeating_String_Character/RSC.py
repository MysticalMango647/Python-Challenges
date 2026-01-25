'''
Fuction that passing a new string will with return string where
each original char has been repeated/dubplicated
sample use case:
hello -> hheellllo
'''

def double_char_2(str):
    result = ""
    for char in str:
        result = result + char + char
    return result

#print (double_char_2("hello"))

def dhouble_char_1(str):
    x = list(str)
    prep = []
    output = ""
    for i in range(len(x)):
        prep.append(x[i]*2)
        #prep.append(x[i])
        print("prep: ", prep)

    #for i in range(len(prep)):
    #    output += prep[i]
    #return output
    return "".join(prep)

#print(dhouble_char_1("hello"))

# Trying this with Generators

def double_char_3(str):
    for x in str:
        yield x *2

#print("".join(double_char_3("hello")))

#Trying another generator
def double_char_4(str):
    return "".join([x+x for x in str])

#print (double_char_4("hello"))

import unittest

class TestDoubleMethods(unittest.TestCase):
    param_list = [
        ('hello', 'hheelllloo'),
        ('world', 'wwoorrlldd')
    ]

    def test_double_char(self):
        for p1, p2 in self.param_list:
            with self.subTest():
                self.assertEqual(double_char_4(p1), p2)


if __name__ == '__main__':
    unittest.main()