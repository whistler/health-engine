import unittest
import fixtures


class TestRecommender(unittest.TestCase):
    
    def test_recommender(self):
        import instance_recommendations
        print instance_recommendations.process(fixtures.input)