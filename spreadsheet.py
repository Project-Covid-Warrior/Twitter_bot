import gspread
import states_dist

gc = gspread.service_account(filename="credentials.json")


string = "I need oxygen in Junagadh"

sheets = {'assam' : "1p5NBBhcic0u9tFLCiZW51cQEVt8qu11YEFumtlCPOC8", 'rajasthan' : "13OTTPng2ETyfBeAgFkpM1ZHfOulh6glm0Fw6qBh5ne8"}


"""
for state in states:
    if state in string:
        state_name = gc.open_by_key(s[state])
        state_wks = state_name.sheet1
        state_result = state_wks.get_all_records()
        print(state_result)"""

def open_file(state):
    available = []
    worksheet = gc.open_by_key(sheets[state.lower()]).sheet1

    length = len(worksheet.col_values(1))
 
    for i in range(2, length + 1):
        temp = worksheet.row_values(i)
        
        if temp[4] == 'Available':
            available.append(temp[:4])
    print(available)

open_file('Assam')