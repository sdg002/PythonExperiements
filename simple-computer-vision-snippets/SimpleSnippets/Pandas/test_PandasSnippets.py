import unittest
import pandas as pd
import numpy as np
import os

class Test_test_PandasSnippets(unittest.TestCase):
    def test_A(self):
        self.fail("Not implemented")


    def test_SimpleDataFrame_Creation(self):
        df = pd.DataFrame([
                            {'Price': 10, 'Cat': 'food', 'Qty': 2},
                            {'Price': 20, 'Cat': 'toy', 'Qty': 4},
                            {'Price': 15, 'Cat': 'food', 'Qty': 5},
                            {'Price': 12, 'Cat': 'food', 'Qty': 7}
                            ],
                            )
        print("Displaying columns")
        print(df.columns)
        print(df.head())
if __name__ == '__main__':
    unittest.main()
