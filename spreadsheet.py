import gspread
import states_dist
import random

gc = gspread.service_account(filename="credentials.json")


sheets = {'rajasthan' : "1p5NBBhcic0u9tFLCiZW51cQEVt8qu11YEFumtlCPOC8", 'temp' : "13OTTPng2ETyfBeAgFkpM1ZHfOulh6glm0Fw6qBh5ne8"}


def get_tweet(state, service_need):
    print(state)
    available = []
    worksheet = gc.open_by_key(sheets[state.lower()]).sheet1

    length = len(worksheet.col_values(1))
 
    for i in range(2, length + 1):
        temp = worksheet.row_values(i)
        status = temp[4].lower().strip()
        service = temp[3].lower().strip()

        if status == 'available' and service_need == service:
            available.append(temp[:4])
    
    data = random.choice(available)
    tweet = f"Supplier : {data[0]}, Service : {data[3]}, Contact Number : {data[1]}, Location : {data[2]}"

    return tweet
