import unittest
import fixtures
import recommender


class TestRecommender(unittest.TestCase):
    
    def test_recommender(self):
        print recommender.recommend(fixtures.input)