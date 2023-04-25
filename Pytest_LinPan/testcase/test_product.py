import pytest
import time

class TestProduct:
    @pytest.mark.smoke
    def test_05(self):
        time.sleep(3)
        print("test 02")
        