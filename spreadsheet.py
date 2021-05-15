import gspread
import states_dist
import random

gc = gspread.service_account(filename="credentials.json")


string = "I need oxygen in Junagadh"

sheets = {'assam' : "1p5NBBhcic0u9tFLCiZW51cQEVt8qu11YEFumtlCPOC8", 'rajasthan' : "13OTTPng2ETyfBeAgFkpM1ZHfOulh6glm0Fw6qBh5ne8"}


def get_tweet(state):
    available = []
    worksheet = gc.open_by_key(sheets[state.lower()]).sheet1

    length = len(worksheet.col_values(1))
 
    for i in range(2, length + 1):
        temp = worksheet.row_values(i)
        
        if temp[4] == 'Available':
            available.append(temp[:4])
    
    data = random.choice(available)
    tweet = f"Supplier : {data[0]}, Service : {data[3]}, Contact Number : {data[1]}, Location : {data[2]}"

    return tweet

open_file('Assam')