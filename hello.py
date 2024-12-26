import requests

# URL of the raw file in the GitHub repository
url = "https://raw.githubusercontent.com/anuraam/OpenUniGit001/main/SourceCodeForDashboard.txt"

# The local path where you want to save the file
local_filename = "SourceCodeForDashboard.txt"

# Send a GET request to fetch the file content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open the local file in write mode and save the content
    with open(local_filename, 'w') as f:
        f.write(response.text)
    print(f"File successfully downloaded and saved as {local_filename}")
else:
    print(f"Failed to download file. HTTP Status code: {response.status_code}")
