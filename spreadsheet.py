import gspread
import states_dist
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


def get_tweet(state, service):
    print(state)
    available = []
    worksheet = gc.open_by_key(sheets[state.lower()]).sheet1

    length = len(worksheet.col_values(1))
 
    for i in range(2, length + 1):
        temp = worksheet.row_values(i)
        service_need = temp[5].lower().strip()

        if service_need == service:
            available.append(temp[:10])
    
    data = random.choice(available)

    name = data[0].strip()
    contact = str(data[1]).strip()
    location = data[2].strip()
    last_verified = str(data[3]).strip()
    price = str(data[4]).strip()
    detail = data[6].strip()
    additional_info = data[7].strip()

    if service == "oxygen":
        tweet = f"{name}, contact info {contact}, location: {location}, price: {price}, refill: {refill}. \nLast verified by a Covid Warrior at {last_verified}"

    return tweet
