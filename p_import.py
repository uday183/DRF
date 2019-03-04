from play import PlayAdopter,MP3, DOC


def test_play():
    inputs_from_user = "doc"
    result = eval('PlayAdopter().'+inputs_from_user)
    return eval(result).play()
print (test_play())