import urllib.request  # Note that we use urllib in Python 3.x but urllib2 in Python 2.x
import json
import ssl

# This suppresses the error that occurs when Python tries to verify the api.tp-iot.com
# SSL cert. This is a security hole, don't use this in production systems!
ssl._create_default_https_context = ssl._create_unverified_context

# Compose the REST request over HTTPS.
request = urllib.request.Request(
    method="PUT",
    url="https://api.tp-iot.com/devices/g88pi/led",
    data=str.encode('"on"'))

# Tell the server that the request data is JSON format.
request.add_header('Content-type', 'application/json')

# Make the REST request and read the response.  Decode as Unicode UTF-8.
result = urllib.request.urlopen(request).read().decode('utf-8')

# Show the response in JSON format with indentation.
print(json.dumps(json.loads(result), indent=2))
