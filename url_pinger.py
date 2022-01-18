import yaml
import requests
from tabulate import tabulate
import os

def getURLs():
        with open("C:\\Users\\Vinay\\Dev\\Python\\PythonPrograms\\AdvancedPython\\url_pinger\\urls.yaml", 'r') as urls_file:
            urls=yaml.safe_load(urls_file)
        return urls["urls"]
    
def check_site(site):
        if site is None:
            return []
        req=requests.get(site)
        if req.status_code==200:
            return {"site": site,"status":"UP","response_time":"%.2f seconds"%(req.elapsed.total_seconds())}
        else:
            return {"site": site,"status":"DOWN","response_time":req.elapsed.total_seconds()}
def printData(data):
        if data is None:
            return "invalid input"
        header=data[1].keys()
        row=[row.values() for row in data]
        return tabulate(row,header)
os.system("clear")
sites=getURLs()
result=map(check_site,sites)
table=(list(result))
print(table)
print(printData(table))

