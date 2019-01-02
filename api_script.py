import requests

r = requests.get('https://api.github.com/events')

if r.status_code == 200:
    print('Code: ' + str(r.status_code) + ' request successful!')
elif r.status_code == 301:
    print('Code: ' + str(r.status_code) + ' redirecting endpot!')
elif r.status_code == 401:
    print('Code: ' + str(r.status_code) + ' authentication error check credentials!')
elif r.status_code == 400:
    print('Code: ' + str(r.status_code) + ' bad request!')
elif r.status_code == 403:
    print('Code: ' + str(r.status_code) + ' access forbidden!')
elif r.status_code == 404:
    print('Code: ' + str(r.status_code) + ' not found on server!')
else:
    print('Code: ' + str(r.status_code) + ' unknown please search!')
	
with open('api_output.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)