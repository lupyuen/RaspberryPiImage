import urllib.request  # Note that we use urllib in Python 3.x but urllib2 in Python 2.x
import json

# Compose the REST request over HTTPS.
request = urllib.request.Request(
    method="GET",
    url="https://api.tp-iot.com/prod/devices/g88pi")

# Make the REST request and read the response.  Decode as Unicode UTF-8.
result = urllib.request.urlopen(request).read().decode('utf-8')

# Show the response in JSON format with indentation.
print(json.dumps(json.loads(result), indent=2))
