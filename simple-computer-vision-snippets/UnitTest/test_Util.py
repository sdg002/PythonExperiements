import unittest
from  Common import Util
import math

class Test_test_Util(unittest.TestCase):
    def test_GenerateGaussianClusterOfPoints(self):
        center_x=2
        center_y=1
        count=100000
        stddev=3
        np_points=Util.GenerateClusterOfRandomPointsAroundXY(center_x,center_y,stddev,count)
        self.assertEqual(np_points.shape[0],count)
        self.assertEqual(np_points.shape[1],2)

        lst_distances=list()
        for index in range(0,count):
            x=np_points[index,0]
            y=np_points[index,1]
            dsquare=(center_x-x)**2 + (center_y-y)**2
            d=math.sqrt(dsquare)
            lst_distances.append(d)

        tolerance_3sigma=3*stddev
        lst_withintolerance3sigma=list(filter(lambda d:d <=tolerance_3sigma,lst_distances))
        self.assertTrue(len(lst_withintolerance3sigma) <= 0.9980 * count)

        tolerance_1sigma=1*stddev
        lst_withintolerance1sigma=list(filter(lambda d:d <=tolerance_1sigma,lst_distances))
        count1sigma=len(lst_withintolerance1sigma)
        self.assertTrue( count1sigma <= 0.7 * count)

if __name__ == '__main__':
    unittest.main()
