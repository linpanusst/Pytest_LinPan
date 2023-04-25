import pytest
import time

@pytest.mark.smoke
def test_04():
    print("test 04")

class TestInterface:
    def test_03(self):
        print("test 03")

    @pytest.mark.run(order=1)
    def test_01(self):
        print("test 01")

