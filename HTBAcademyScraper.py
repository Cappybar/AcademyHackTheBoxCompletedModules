import requests as req

diff = ("Fundamental","Easy","Medium","Hard")
base_url = 'https://academy.hackthebox.com/achievement/'
cappybara_id = '89408'
module_amount = 400
result_map = {"Fundamental":[],"Easy":[],"Medium":[],"Hard":[]}

def scrap(r):
    index = r.text.find('content="Completed') + 19
    result = r.text[index:]
    result = result[:result.find('"')]
    return result
def difficulty(r):
    for d in diff:
        if r.find('>'+d+'<') > -1:
            return d

def createREADME(module_map):
    with open("README.md","w") as f:
        f.write("""# AcademyHackTheBoxCompletedModules
list of completed modules on Hack The Box Academy website

also included python script that scraps for completed achievements

""")
        for d in diff:
            f.write("## " + d + "\n\n")
            for module in result_map[d]:
                f.write(module+"\n\n")


for i in range(module_amount):
    request_link = base_url+cappybara_id+"/"+str(i)
    res = req.get(request_link)
    if res.status_code == 200:
        result_map[difficulty(res.text)].append(f"[{scrap(res)}]({request_link})")
        output_text = f"[!] {scrap(res)}: \n- {request_link}"
        print(output_text)

createREADME(result_map)

        
