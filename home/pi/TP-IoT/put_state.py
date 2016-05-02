import urllib.request  # Note that we use urllib in Python 3.x but urllib2 in Python 2.x
import json

# Compose the REST request over HTTPS.
request = urllib.request.Request(
    method="PUT",
    url="https://1xt9kv75ii.execute-api.us-west-2.amazonaws.com/prod/devices/g88pi/led",
    data=str.encode('"on"'))  # b means convert the text to bytes.
# Tell the server that the request data is JSON format.
request.add_header('Content-type', 'application/json')

# Make the REST request and read the response.  Decode as Unicode UTF-8.
result = urllib.request.urlopen(request).read().decode('utf-8')
# Show the response in JSON format with indentation.
print(json.dumps(json.loads(result), indent=2))
