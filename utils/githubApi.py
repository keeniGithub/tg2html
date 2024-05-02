from github import Github

def commit_to_gh(token, name, path_to_json, commit_desc, content):
    g = Github(token)
    repo_name = name
    repo = g.get_user().get_repo(repo_name)

    file = repo.get_contents(path_to_json)

    repo.update_file(path_to_json, commit_desc, content, file.sha)