import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('OKorniichuk_qa_auto_2023')
    assert r['total_count'] == 1
    assert 'OKorniichuk_qa_auto_2023' in r['items'][0]['name']



@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_get_emojis(github_api):
    r = github_api.get_emojis('emojis')
    return(r)
    assert r == 'https://api.github.com/emojis'

@pytest.mark.api
def test_get_commits(github_api):
    owner = 'fromBEE2BEE'
    repo = 'OKorniichuk_qa_auto_2023'
    r = github_api.get_commits('fromBEE2BEE', 'OKorniichuk_qa_auto_2023')
    assert r == 'https://api.github.com/repos/fromBEE2BEE/OKorniichuk_qa_auto_2023/commits'
    

@pytest.mark.api
def test_get_list_branches_for_HEAD_commit(github_api):
    owner = 'fromBEE2BEE'
    repo = 'OKorniichuk_qa_auto_2023'
    commit_sha = '762abc94fb0fd5514170fc9c7af75a366a9fcde1'
    r = github_api.get_list_branches_for_HEAD_commit('fromBEE2BEE', 'OKorniichuk_qa_auto_2023', '762abc94fb0fd5514170fc9c7af75a366a9fcde1')
    assert r == 'https://api.github.com/repos/fromBEE2BEE/OKorniichuk_qa_auto_2023/commits/762abc94fb0fd5514170fc9c7af75a366a9fcde1/branches-where-head'
    

@pytest.mark.api
def test_get_a_commit(github_api):
    owner = 'fromBEE2BEE'
    repo = 'OKorniichuk_qa_auto_2023'
    ref = 'ebc9e97ae0437f90dddd52a64208c0baabdafd32'
    r = github_api.get_a_commit('fromBEE2BEE', 'OKorniichuk_qa_auto_2023', 'ebc9e97ae0437f90dddd52a64208c0baabdafd32')
    assert r == 'https://api.github.com/repos/fromBEE2BEE/OKorniichuk_qa_auto_2023/git/trees/ebc9e97ae0437f90dddd52a64208c0baabdafd32'   





