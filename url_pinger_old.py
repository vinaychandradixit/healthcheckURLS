import requests
from tabulate import tabulate
import yaml
import time
import os

# Assume this list is in database
def getURLs():
    
    with open('C:\\Users\\Vinay\\Dev\\Python\\PythonPrograms\\AdvancedPython\\url_pinger\\urls.yaml', 'r') as urls_file:
        urls = yaml.safe_load(urls_file)
    
    return urls["urls"]

def check_site(site):
    
    '''
    Input: Receives a website name
    output: return response object [{site: UP/DOWN}]
    '''

    if site is None:
        return [];

    req = requests.get(site);
    if req.status_code == 200:
        return {"site": site, "status": "UP", "response_time": "{:.2f} seconds".format(req.elapsed.total_seconds())}
        
    else:
        return {"site": site, "status" :"DOWN", "response_time": "{:.2f} seconds".format(req.elapsed.total_seconds())}
    
    return response

def print_table(data):
    if data is None:
        print("Invalid input value");
        return

    header = data[0].keys()
    rows = [ row.values() for row in data ]
    print(tabulate(rows, header))
    return 

if __name__ == "__main__":
        os.system('clear')      
        sites = getURLs()
        result = map(check_site, sites)
        print_table(list(result))