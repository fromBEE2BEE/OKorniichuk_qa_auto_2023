import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(
            'https://api.github.com/search/repositories',
            params={"q": name}
        )
        body = r.json()

        return body

    def get_emojis(self, emojis):
        r = requests.get(f'https://api.github.com/emojis')
        body = r.json()

        return body


    def get_commits(owner, repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
        body = r.json()

        return body

    def get_list_branches_for_HEAD_commit(owner, repo, commit_sha):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head')
        body = r.json()

        return body

    def get_a_commit(owner, repo, ref):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits/{ref}')
        body = r.json()

        return body

    
    











        


    