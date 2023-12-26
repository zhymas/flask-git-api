import requests

def git_api(user):
    r = requests.get(f'https://api.github.com/users/{user}/repos')

    if r.status_code == 200:
        json_data = r.json()
        return [repo['name'] for repo in json_data]

    else:
        print(f'Error status code: {r.status_code}')