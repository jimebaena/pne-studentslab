import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

conn = http.client.HTTPSConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")
    print(f"Response received!: {res.status} {res.reason}")
    print()

    response = json.loads(data)

    if response.get('ping') == 1:
        print("PING OK! The database is running!")
    else:
        print("PING Failed! The database might be down.")

except Exception as e:
    print(f"An error occurred: {e}")

conn.close()