import requests
import os
import time

file = str(input("输入txt文件位置\n"))

final_f = str(input("输入输出txt位置\n"))

final_file = open(final_f, 'w')

result = []

final = []

with open(file, 'r') as f:
    results = f.readlines()
    for r in results:
        rr = r.replace('\n', '')
        result.append(rr)
print(result)

for code in result:
    parameter = {
                    'locate': code,
                    'region': 'SG',
                    'geoit': 'CSV',
                }
    '''
    headers = {"User-Agent": "PostmanRuntime/7.28.4",
               "Accept-Encoding": "gzip, deflate, br",
               "Connection": "Keep-alive",
               }
    response = requests.get("https://geocode.xyz/?locate=location", params=parameter, headers=headers)           
    '''
    response = requests.get("https://geocode.xyz/?locate=location", params=parameter)
    time.sleep(1.5)
    final.append(response.text)
    print(response.text)

print(final)
for hh in final:
    final_file.write(hh[-17:]+' \n')

f.close()
final_file.close()
os.system('pause')