import gspread
import states_dist
import random

gc = gspread.service_account(filename="credentials.json")


sheets = {'rajasthan' : "1p5NBBhcic0u9tFLCiZW51cQEVt8qu11YEFumtlCPOC8", 'temp' : "13OTTPng2ETyfBeAgFkpM1ZHfOulh6glm0Fw6qBh5ne8"}


def get_tweet(state, service):
    print(state)
    available = []
    worksheet = gc.open_by_key(sheets[state.lower()]).sheet1

    length = len(worksheet.col_values(1))
 
    for i in range(2, length + 1):
        temp = worksheet.row_values(i)
        status = temp[9].lower().strip()
        service_need = temp[8].lower().strip()

        if status == 'available' and service_need == service:
            available.append(temp[:10])
    
    data = random.choice(available)

    name = data[0].strip()
    contact = str(data[1]).strip()
    location = data[2].strip()
    last_verified = data[3].strip()
    price = str(data[4]).strip()
    refill = data[5].strip()
    bed_type = data[6].strip()
    additional_info = data[7].strip()

    if service == "oxygen":
        tweet = f"{name}, contact info {contact}, location: {location}, price: {price}, refill: {refill}. \nLast verified by a Covid Warrior at {last_verified}"

    return tweet
