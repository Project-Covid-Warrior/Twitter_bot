import gspread
import random

gc = gspread.service_account(filename="credentials.json")


sheets = {'rajasthan' : '1OWuwtd3eGZRHI4ODCSxKY6SNu9xCtcNCEC5NeSlDQ7k',
          'maharashtra' : '12csXtHJ-YtgsNTDIiWZNjwwRFR3ztt9FQ7YIYlDBdk0',
          'delhi' : '1CwE7_P4W_WZMkIPfTqBw9_17ESzlFJjC_ZdnU4F-CUo',
          'uttar pradesh' : '1SSF5TmpLEUXF7ia5Le_G6MjCt6I4TfBn_atvhDV1yiY',
          'tamil nadu' : '1Ke_C2DJNoiit7Ck9vAfbycPFBSoZzAgibFVBTESDraU',
          'bihar' : '1LAS0L6zOgTBIYNFclO0ycxweY54wSr1ChYje1HU67t0',
          'jharkhand' : '1poOvssfaN_KfVW7HKVcHUlk7dXHd67GR8ittEVMgMbk',
          'west bengal' : '1rJ5la05Yzq6djZsH1QpMKsUPdrfAp9XgSEaQo9qvVaE',
          'telangana' : '1Ffx7e5VwI3gfu1jgsZZWJ8Q4UbPbZaEAuOxF1mRM0pM',
          'karnatka' : '1JAmFwdb96AKlb5BCbY0nvHmY0ar0IPA0kvTi-DKaQ1M',
          'andhra pradesh' : '1fdjtxSVLw6KzicPzMIXzgkqt7cHGWsjW3DGr7Ue_2lA',
          'madhya pradesh' : '1Riip7cYKvoRlgrjPqNMCP585_t5hHAivdywtlVD4gUo',
          'odisha' : '1X7BYHrDI8Pmks5zrRCITDUEy3VtVTipdPmvb4nsHY78'
          }


def get_data(tweet_list, state, service_need, statewise=False):
    service_need = service_need.split()
    print(state)                        # For testing purpose
    available = []
    worksheet = gc.open_by_key(sheets[state.lower()]).sheet1

    length = len(worksheet.col_values(1))
 
    for i in range(1, length + 1):
        temp = worksheet.row_values(i)
        service = temp[5].lower().strip()
        location = temp[2]
        city = location.split()[-1]
        
        if statewise:
            if service_need[-1] == "bed" and service_need[0] == "oxygen":
                if temp[6] == "oxygen bed":
                    available.append(temp[:8])
            elif service_need[-1] == service:
                available.append(temp[:8])            
        elif city in tweet_list:
            if service_need[-1] == "bed" and service_need[0] == "oxygen":
                if temp[6] == "oxygen bed":
                    available.append(temp[:8])
            elif service_need[-1] == service:
                available.append(temp[:8])
    
    return available

def get_tweet(available, service_need):
    data = random.choice(available)
    name = data[0].strip()
    contact = str(data[1]).strip()
    last_verified = str(data[3]).strip()
    location = data[2].strip()
    price = str(data[4]).strip()
    detail = data[6].strip()
    try:
        additional_info = data[7].strip()
        is_additional = True
    except:
        is_additional = False

    if service_need == "oxygen":
        tweet = f"Name: {name}, contact: {contact}, location: {location}, price: ₹{price}, service: {detail}"

        if additional_info != "":
            tweet += f" {additional_info}. Last verified by a Covid Warrior at {last_verified}"
        else:
            tweet += f" Last verified by a Covid warrior at {last_verified}"
    else:
        tweet = f"Name: {name}, contact: {contact}, location: {location}, service: {detail}"

        if is_additional:
            tweet += f" {additional_info}. Last verified by a Covid Warrior at {last_verified}"
        else:
            tweet += f" Last verified by a Covid warrior at {last_verified}"

    return tweet
