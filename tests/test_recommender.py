import unittest
import fixtures
import recommender
import timeseries_recommendations


class TestRecommender(unittest.TestCase):
    
    def test_recommender(self):
        print "============================="
        print "Recommendations for high sleep high activities"
        print "============================="
        for recommendation in recommender.recommend(fixtures.input):
            if recommendation['severity'] >= 5:
                print recommendation['recommendation']

    def test_condition9(self):
        print "============================="
        print "Recommendations for Bloodpressure high"
        print "============================="
        for recommendation in recommender.recommend(fixtures.input9):
            if recommendation['severity'] >= 5:
                print recommendation['recommendation']
        
    def test_condition53(self):
        print "============================="
        print "Recommendations for Low activity"
        print "============================="
        for recommendation in recommender.recommend(fixtures.input53):
            if recommendation['severity'] >= 5:
                print recommendation['recommendation']
        
    def test_condition72(self):
        print "============================="
        print "Recommendations for Too much sleep"
        print "============================="
        
        for recommendation in recommender.recommend(fixtures.input72):
            if recommendation['severity'] >= 5:
                print recommendation['recommendation']