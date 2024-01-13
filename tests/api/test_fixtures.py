def test_change_name():
    user = User()
    user.create()

    assert user.name == 'Sergii'
    user.remove()

def test_change_second_name():
    user = User()
    user.create()

    assert user.second_name == 'Butenko'
    user.remove()


    