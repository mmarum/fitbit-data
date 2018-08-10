import base64

consumer_key = "22CTVJ"

consumer_secret = "e1793f999a271f160d6e16163894e45a"

# https://dev.fitbit.com/build/reference/web-api/oauth2/
# Authorization Header
# The Authorization header must be set to Basic followed by a space, then the 
# Base64 encoded string of your application's client id and secret concatenated with a colon. 
# For example, the Base64 encoded string, Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ=, is decoded as [client_id]:[client_secret]

# https://docs.python.org/3/library/base64.html

encoded = base64.b64encode(b'22CTVJ:e1793f999a271f160d6e16163894e45a')

print(encoded)

#b'ZGF0YSB0byBiZSBlbmNvZGVk'
#data = base64.b64decode(encoded)
#data
#b'data to be encoded'

# Getting a new refresh token:
# The following worked:
# curl -XPOST "https://api.fitbit.com/oauth2/token?grant_type=refresh_token&refresh_token=b1481afc07e12a16c8ddd387606a21c43c55a313407cc657e942a7db128f14ef" -H "Host: api.fitbit.com" -H "Authorization: Basic MjJDVFZKOmUxNzkzZjk5OWEyNzFmMTYwZDZlMTYxNjM4OTRlNDVh" -H "Content-Type: application/x-www-form-urlencoded"
# Response:
# {"access_token":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2NzlONUciLCJhdWQiOiIyMkNUVkoiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNTMxNDcwMTE4LCJpYXQiOjE1MzE0NDEzMTh9.HaQyToXqVD8gMBH2xFWKHVLN63y99SeIVcAMj-kqbOc","expires_in":28800,"refresh_token":"7dff75bb5855fc131758d841edcd8f23ff2eb7a2b48de8351c4458c7c9780dea","scope":"activity social weight heartrate location settings profile nutrition sleep","token_type":"Bearer","user_id":"679N5G"}
