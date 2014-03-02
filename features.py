class Features:
#class Features(object):
    """ Defines the features that are used to perform the recommendation. Features are generated by
    preprocessing input data from the API input and should be the inputs for the medical
    recommendations table """
    
    def __init__(self, bp_systolic_min, bp_systolic_max, bp_diastolic_min, bp_diastolic_max,
                 heartbeat_min, heartbeat_max, sleep_min, sleep_max, activity_min, activity_max,
                 age_min, age_max):

        self.bp_systolic_min = bp_systolic_min
        self.bp_systolic_max = bp_systolic_max
        self.bp_diastolic_min = bp_diastolic_min
        self.bp_diastolic_max = bp_diastolic_max
        self.heartbeat_min = heartbeat_min
        self.heartbeat_max = heartbeat_max
        self.sleep_min = sleep_min
        self.sleep_max = sleep_max
        self.activity_min = activity_min
        self.activity_max = activity_max
        self.age_min = age_min
        self.age_max = age_max  
        
    def __hash__(self):
            return hash((self.bp_systolic_min, self.bp_systolic_max, 
                         self.bp_diastolic_min, self.bp_diastolic_max,
                         self.heartbeat_min, self.heartbeat_max, 
                         self.sleep_min, self.sleep_max, 
                         self.activity_min, self.activity_max,
                         self.age_min, self.age_max))

    def __eq__(self, other):
            return (self.bp_systolic_min, self.bp_systolic_max, 
                    self.bp_diastolic_min, self.bp_diastolic_max,
                    self.heartbeat_min, self.heartbeat_max, 
                    self.sleep_min, self.sleep_max, 
                    self.activity_min, self.activity_max,
                    self.age_min, self.age_max) == (
                    other.bp_systolic_min, other.bp_systolic_max, 
                    other.bp_diastolic_min, other.bp_diastolic_max,
                    other.heartbeat_min, other.heartbeat_max, 
                    other.sleep_min, other.sleep_max, 
                    other.activity_min, other.activity_max,
                    other.age_min, other.age_max)
    
    def print_features(self):
        print 'bp_systolic_min: ' 
        print self.bp_systolic_min 
        print 'bp_systolic_max: ' 
        print self.bp_systolic_max
        print 'bp_diastolic_min: ' 
        print self.bp_diastolic_min 
        print 'bp_diastolic_max: ' 
        print self.bp_diastolic_max
        print 'heartbeat_min: ' 
        print self.heartbeat_min 
        print 'heartbeat_max: ' 
        print self.heartbeat_max 
        print 'sleep_min: ' 
        print self.sleep_min 
        print 'sleep_max: ' 
        print self.sleep_max 
        print 'activity_min: '
        print self.activity_min 
        print 'activity_max: '
        print self.activity_max 
        print 'age_min: ' 
        print self.age_min 
        print 'age_max: ' 
        print self.age_max 
        
        