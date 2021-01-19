import requests
import json

#--------

# Make sure that your file path has two '\' in it and ends with '\\'

# Example: C:\\Users\\Fevers\\Desktop\\AES-Bot\\

filepath = 'XXXXXXXXXX'

# You can leave this blank if you want, but if it doesnt work then put the filepath in.

#--------

print('Grabbing aes keys Keys...\n')

# Grabs version
response = requests.get('https://benbotfn.tk/api/v1/status')
version = response.json()['currentFortniteVersionNumber']

# Grabs the AES endpoint provided by Fortnite-API
response = requests.get('https://fortnite-api.com/v2/aes')
json = response.json()['data']

# Filters AES endpoint
main = json['mainKey']
dynamic = response.json()['data']['dynamicKeys']

print('Main keys grabbed!')

# Opens our txt file and writes content
f= open(f'{version}0 - aes.txt', 'w')

f.write(f'Current Main AES Key for v{version}0:\n0x{main}\n\n\nDynamic Keys:\n\n')

print('\nGrabbing the dynamic keys...')

# Loops for each dynamic key
for dynamickeys in dynamic:
    key = dynamickeys['key']
    pak = dynamickeys['pakFilename']
    f.write(f'{pak}: \n0x{key}\n\n')

# Grabs number of dynamic keys
x = len(dynamic)

# Ending print statement:
print('\nDynamic keys grabbed!')

print(f'\nThere are {x} Dynamic Keys detected. Writing all {x} keys to file...')

f.write('AES Generator made by Fevers')

print(f'\nGrabbed and wrote all AES keys for version v{version}0.')

bruh = x + 1

response1 = requests.get('https://benbotfn.tk/api/v1/status')

alldynamic = response1.json()['dynamicPakCount']

print(f'\nGrabbed {bruh}/{alldynamic} non-encrypted paks.')

f.close()
