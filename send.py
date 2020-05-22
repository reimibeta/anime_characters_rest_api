import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkwMTMwNzU4LCJqdGkiOiJhMGQzOWViYWVlZTA0NjNhYjQwNzE0YmRiNDcyMGY2YiIsInVzZXJfaWQiOjF9.vfoBdWEk1mI8yVPm4Ne_CIAYRLWuQQrFK8fZW6oVBQw'

request = requests.get('http://127.0.0.1:8000/characters/', headers=headers)

print(request.text)
