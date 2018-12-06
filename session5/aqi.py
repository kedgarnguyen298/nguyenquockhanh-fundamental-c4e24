from urllib.request import urlopen
import json

url = "https://wind.waqi.info/nsearch/full/hanoi?n=4&fbclid=IwAR1qnlKEEoqiGWmx139aulmukmDwqRu9VmxmTQrRG_C2inRTTIEQ0I0JBZE"

#1 Open connection
conn = urlopen(url)

#2 Read data
raw_data = conn.read()

#3 Decode data
text = raw_data.decode("utf-8")

#4 Convert data from str to dict
data = json.loads(text)

results = data["results"]

for result in results:
    print(result["s"]["a"])
    print(result["n"][0])

