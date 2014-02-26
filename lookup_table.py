""" Reads recommendation table from disk and returns recommendations which meet the criteria 
described in the features"""

table = None # Stores all the recommendations

def lookup(features):
    
    recommendations = []
    
    # check if table is already loaded
    if 'table' in vars() or 'table' in globals():
        table = load_recommendations()
        
    #TODO: Loop over the recommendations table and append the ones the meet the criteria in features
    # to recommendations list
    
    stub = {'id': 1, 'recommendation': "Test recommendation" }
    recommendations.append(stub)
    
    return recommendations
    

def load_recommendations():
    """ Reads the recommendations table from disk and returns it """
    import gspread
    # Login with your Google account
    gc = gspread.login('account', 'password')
    
    # Open a worksheet from spreadsheet with one shot
    wks = gc.open("Medical Research").sheet1
    
    # Get all values from the first row
    # With label
    val = wks.acell('B1').value
    
    return val