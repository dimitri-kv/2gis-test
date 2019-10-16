export PATH=$PATH:/
pytest ./test/test_api.py --alluredir=./tests/allure
./allure-2.12.1/bin/allure generate ./tests/allure -o ./allure-report --clean
