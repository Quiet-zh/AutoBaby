from autobaby.foo import foo


def test_foo():
    assert foo("foo") == "foo"


if __name__ == "__main__":
    test_foo()
