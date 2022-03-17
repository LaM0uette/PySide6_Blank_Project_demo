import http.client

conn = http.client.HTTPSConnection("flaticon.p.rapidapi.com")

payload = "apikey=febcd634512d10152df637a57086f72c3ddc808c"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "flaticon.p.rapidapi.com",
    'x-rapidapi-key': "4ec0205882msh1de920897726356p163353jsn0288ca06b940"
    }

conn.request("POST", "/app/authentication", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))