import re 
url = "https://retosdeprogramacion.com?year=2023&challenge=0"
components = url.split("&")
for component in components:
    if "=" in component:
        param = component.split("=")
        if len(param) == 2 and param[1]:
            print (param[1])

expr = r"=([a-zA-Z0-9]+)"
params = re.findall(expr, url)
print(params)