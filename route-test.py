import requests

fish_watch_api = 'https://www.fishwatch.gov/api/species/'

print("Making request...")
resp = requests.get(fish_watch_api)

# Make sure we recieve a proper response
if resp.ok:
    print("We got a response")
else:
    print("There was an error!")
    raise Exception()

# Convert response (json string) to usable structure (dictionary)
decoded = resp.json()

# Print the first five results
first_result = decoded[0]
print("All possible keys")
for k in first_result.keys():
    print("Key: " + k)

print("---Species Name---")
print(first_result['Species Name'])
print("---Location---")
print(first_result['Location'])
print("---Population---")
# Trying printing a different key! (Hint: Look at the output for choices)
print(first_result['Population'])
print("---Biology---")
# Experiment some more!
print(first_result['Biology'])