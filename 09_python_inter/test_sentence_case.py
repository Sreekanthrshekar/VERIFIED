import unittest
import sentence_case

class Test_case(unittest.TestCase):
    
    def test_sentence_case(self):
        text1 = "this is a test. this will be used to test whether the sentence case module works porperly or not. if not necessary corrections are to be made. "
        result = sentence_case.sentence_case(text1)
        self.assertEqual(result,"This is a test.This will be used to test whether the sentence case module works porperly or not.If not necessary corrections are to be made.")

if __name__ == "__main__":
    unittest.main()
    
