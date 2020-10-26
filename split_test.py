'''
    split_test.py
    
    This file tests string.split(). In the real world, there's no need to test
    Python's library functions, but we're just doing this as an intro to unit
    tests.
'''

import unittest

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_LENGTH = "length"
KEY_FIRST_WORD = "first_word"
KEY_SECOND_WORD = "second_word"

class SplitTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "Childish Gambino",
                KEY_EXPECTED: {
                    KEY_LENGTH: 2,
                    KEY_FIRST_WORD: "Childish",
                    KEY_SECOND_WORD: "Gambino",
                }
            }
            ,
            
            {
                KEY_INPUT: "Bone Thigs N' Harmony",
                KEY_EXPECTED: {
                    KEY_LENGTH: 4,
                    KEY_FIRST_WORD: "Bone",
                    KEY_SECOND_WORD: "Thigs",
                }
            }
            ,
            {
                KEY_INPUT: "Batman Superman",
                KEY_EXPECTED: {
                    KEY_LENGTH: 2,
                    KEY_FIRST_WORD: "Batman",
                    KEY_SECOND_WORD: "Superman",
                }
            }
            
        ]
        
        self.failure_test_params = [
            {
                KEY_INPUT: "Nicki Minaj",
                KEY_EXPECTED: {
                    KEY_LENGTH: 1,
                    KEY_FIRST_WORD: "NickiMinaj",
                }
            },
            {
                KEY_INPUT: "Tupac Shakur",
                KEY_EXPECTED: {
                    KEY_LENGTH: 20,
                    KEY_FIRST_WORD: "Tupaacer",
                }
            },
            {
                KEY_INPUT: "cat dog",
                KEY_EXPECTED: {
                    KEY_LENGTH: 200,
                    KEY_FIRST_WORD: "goat",
                }
            }
            
        ]


    def test_split_success(self):
        for test in self.success_test_params:
            inp = test[KEY_INPUT].split()
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(len(inp), expected[KEY_LENGTH])
            self.assertEqual(inp[0], expected[KEY_FIRST_WORD])
            self.assertEqual(inp[1], expected[KEY_SECOND_WORD])
            
    def test_split_failure(self):
        for test in self.failure_test_params:
            inp = test[KEY_INPUT].split()
            expected = test[KEY_EXPECTED]
            
            self.assertNotEqual(len(inp), expected[KEY_LENGTH])
            self.assertNotEqual(inp[0], expected[KEY_FIRST_WORD])

