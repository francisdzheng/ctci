import unittest

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    s1 = ''.join(sorted(str1))
    s2 = ''.join(sorted(str2))

    return s1 == s2

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = checkPermutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = checkPermutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()