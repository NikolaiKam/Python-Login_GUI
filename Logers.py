import re

def correct_logs(email,password):
    dic_logs={

        'nikolaink@abv.bg':'4567',
        'kamenov.nk@gmail.com':'1234',
        'emil.kamenov@abv.bg':'123456da',
        'nikolaikamenov@icloud.com':'0000'
    }

    count=0

    for i in dic_logs.keys():
        if i==email:
            if dic_logs[i]==password:
                return 'Welcome back!'
            else:
                return 'Wrong password... Try Again'
        else:
            count+=1
            if count==4:
                return 'Wrong email... Try Again'

def correct_email(email):
    
    match_abv=re.search(r'@abv.bg$',email)
    match_gmail=re.search(r'@gmail.com$',email)
    match_icloud=re.search(r'@icloud.com$',email)
    if match_abv or match_gmail or match_icloud:
        return 'Correct'
    else:
        return 'Incorrect'

        