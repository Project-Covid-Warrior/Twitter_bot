import gspread

gc = gspread.service_account(filename="credentials.json")


states = ['rajasthan', 'assam']

string = "I need oxygen in rajasthan".split()

s = {'assam' : "1p5NBBhcic0u9tFLCiZW51cQEVt8qu11YEFumtlCPOC8", 'rajasthan' : "13OTTPng2ETyfBeAgFkpM1ZHfOulh6glm0Fw6qBh5ne8"}

for state in states:
    if state in string:
        state_name = gc.open_by_key(s[state])
        state_wks = state_name.sheet1
        state_result = state_wks.get_all_records()
        print(state_result)