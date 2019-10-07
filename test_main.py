import main

def test_main():
    # set up test
    a = [1,2,3]
    b = [4,5]
    assert main.concat_list(a,b) == [1,2,3,4,5]
    assert False