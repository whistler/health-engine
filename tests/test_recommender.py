import unittest
import recommender

class TestRecommender(unittest.TestCase):
    
    def test_recommender(self):
        assert recommender.recommend(None) == None