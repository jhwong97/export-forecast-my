import datetime as dt
import requests
import random
import time

# URL, csrf_token, headers from targeted url
url = "https://metsonline.dosm.gov.my/tradev2/product-coderesult"
csrf_token = 'dG5PZ09oay0nPiIMATBTeTsZHFAgKSJdRQQVKwRYJBQADRckHStGYA=='
headers = {
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 
"Cookie": "_ga_F8QG3XBL63=GS1.1.1679998862.1.1.1679998930.0.0.0; _ga_7Q47WMYPD5=GS1.1.1679998865.1.1.1679998930.0.0.0; _ga_HK905W412V=GS1.1.1679998865.1.1.1679998930.0.0.0; mp_f55a9b6a137ab21675ef8724f7864bde_mixpanel=%7B%22distinct_id%22%3A%20%2218727cb0e099da-0247f50f77e9aa-7a545471-144000-18727cb0e0a31%22%2C%22%24device_id%22%3A%20%2218727cb0e099da-0247f50f77e9aa-7a545471-144000-18727cb0e0a31%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__timers%22%3A%20%7B%7D%7D; _ga_TF34V4E8EM=GS1.1.1679999831.1.1.1680004133.0.0.0; _ga_XSB7QCQ0M9=GS1.1.1681551362.3.1.1681551368.0.0.0; _ga=GA1.1.324035783.1679998837; PHPSESSID=3oi1at9dfj4ugn6nno2bsqdd60; _csrf=193a3c282709e8f8d32929d94372b30d2cc2a5402306edc5e12c04ca098a1819a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22SPmkNX8TOwS7oAIp1jZLK0O9tcXCRC-M%22%3B%7D; BNES_PHPSESSID=fk0GuBGEQJmmIMfAn9TJ6EK+FW/oxjgTr2AAO+vNTw1JHh1+YzlOkigmNmbMOtjxuyDVXvBqWx9L6ZHOVdyK0Unb9r8ZsuhgKRw0f3zlmA8=; BNES__csrf=T1JRVt/fspwmarDUSua9ANdq7/OTqhlhu8lprfzaWWaQtpaDzljVNyJUL1Y65guWawDI8LDmCHrD6nlIXud7o3ytcCBG5TDvi4Kd94SBmSCx1ED1HWM0YV+ztPXAQ5AhjCkcJExisSE5tRQSObfAv0WAFW/4frqxEg4pTyBtkcJZTi4Amki6jSChfqJAyShFuYOrg/ZKI0IsB8ShUR5UFcxqa3a28w/OAICYVhchalmoAAhmCMY22tozvta3gpBJGC+pONVCkNPozWC+7XVzDC5ZciTE34Uq"
}

# To select targeted year for data extraction
starting_year = 2000
current_year = dt.date.today().year

# Specify the year interval
year_interval = 10

targeted_year = []

for year in range (starting_year, current_year + 1, year_interval):
    if year + year_interval == current_year:
        ending_year = current_year
        targeted_year.append(ending_year)
        break
    elif year + year_interval < current_year:
        ending_year = year + year_interval - 1
        targeted_year.append(ending_year)
    elif year + year_interval > current_year:
        ending_year = current_year
        targeted_year.append(ending_year)

print(targeted_year)