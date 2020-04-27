import requests

# url = 'https://hooks.slack.com/services/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'

url = '' # Replace with slack webhook URL
data = {"text":"Hello, World."}
requests.post(url, json=data)
