import fitbit

consumer_key = "22CTVJ"
consumer_secret = "e1793f999a271f160d6e16163894e45a"

# Docs:
# http://python-fitbit.readthedocs.io/en/latest/

#access_token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2NzlONUciLCJhdWQiOiIyMkNUVkoiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNTI4MjU5MTcwLCJpYXQiOjE1MjgyMzAzNzB9.o00FA7g4RDJEic-LJRowC73UzjHusVpuHK8zsy8n0aY"
#refresh_token = "b1481afc07e12a16c8ddd387606a21c43c55a313407cc657e942a7db128f14ef"

# July 12 2018:
access_token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2NzlONUciLCJhdWQiOiIyMkNUVkoiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNTMxNDcwMTE4LCJpYXQiOjE1MzE0NDEzMTh9.HaQyToXqVD8gMBH2xFWKHVLN63y99SeIVcAMj-kqbOc"
refresh_token = "7dff75bb5855fc131758d841edcd8f23ff2eb7a2b48de8351c4458c7c9780dea"

authd_client = fitbit.Fitbit(consumer_key, consumer_secret, access_token=access_token, refresh_token=refresh_token)

sleep_data = authd_client.sleep()
#heart_data = authd_client.heart()

print(sleep_data['sleep'])
print("= = = = = = = = = = = = = =")
#print(heart_data['activities-heart'])
