import requests

api_names_endpoint = 'http://127.0.0.1:5000/names/'
api_search_endpoint = 'http://127.0.0.1:5000/search/'

#### Test fish names ####
fish_names_response = requests.get(api_names_endpoint)
print("---Testing names endpoint---")
if fish_names_response.ok:
    print("[OK] Got fish names!")
else:
    print("[FAIL] An error occurred")
    raise Exception()

fish_names = fish_names_response.json()
print("---Testing number of fish names (must be > 50)")
if len(fish_names) > 50:
    print("[OK] We have a lot of names!")
else:
    print("[FAIL] An error occurred")
    raise Exception()

#### Test fish search ####
five_fish = fish_names[:5]
for name in five_fish:
    print("---Searching for {}---".format(name))
    fish_names_response = requests.get(api_search_endpoint + name)
    if not fish_names_response.ok:
        print("[FAIL] An error occurred")
        raise Exception()
    
    decoded = fish_names_response.json()[0]
    if decoded.get("Biology", None) == None:
        print("[FAIL] Could not identify Biology")
        raise Exception()
    if decoded.get("Population", None) == None:
        print("[FAIL] Could not identify Population")
        raise Exception()

print("[OK] All tests have passed!")
