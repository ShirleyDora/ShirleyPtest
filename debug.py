import allure
import pytest
import os
if __name__ == '__main__':
    pytest.main(['scripts/', '-s', '-q', '--alluredir', './result'])
    os.system('allure generate ./result -o ./report --clean')
    os.system("allure open ./report")
