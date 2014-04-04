import unittest
import fixtures
import recommender
import timeseries_recommendations


class TestRecommender(unittest.TestCase):
    
    def test_recommender(self):
        print recommender.recommend(fixtures.input)
        
    def test_ts_recommeder(self):
        print timeseries_recommendations.process(fixtures.input)