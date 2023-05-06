import requests

url = "https://zoom-pinecone-backend.onrender.com/qa"

payload = {
    "question": "hi ",
    "clientId": "12345",
    "transcript_ids": "1T1g8KNFkxzxhDgsxUjlYl2ow2YQoUc82" # "1T73I4uA3BpNPWuCppF664YncSVBJhVJs"
}

headers = {"content-type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.text)