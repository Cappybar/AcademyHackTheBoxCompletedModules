import requests as req

def scrap(r):
    index = r.text.find('content="Completed') + 9
    result = r.text[index:]
    result = result[:result.find('"')]
    return result

base_url = 'https://academy.hackthebox.com/achievement/'
cappybara_id = '89408'
module_amount = 500

for i in range(module_amount):
    request_link = base_url+cappybara_id+"/"+str(i)
    res = req.get(request_link)
    if res.status_code == 200:
        print(f"[!] {scrap(res)}: \n- {request_link}")


