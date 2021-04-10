import requests

def main():
    URL = "https://resumetrigger.azurewebsites.net/api/resumecounter/b513d94b-d78e-4c4c-a916-a9d24e8fd32a"

    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()
    
    return int(data[0]['visitor_count'])
    

def test_main():
    assert main() == 71
