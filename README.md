Тестовое задание

** Структура проекта: ** \
[test] \
 содержит кейсы с наборами тестовых данных \
[docker] \
-docker-entrypoint.sh скрипт выполняемый при запуске докер-контейнера \
[allure-2.12.1] бинарная сборка аллюра для генерации тест-отчета \
[root_dir] \
-conftest.py - содержит реализации этапов взаимодействия с api \
-Dockerfile - инструкция с установкой всех необходимых зависимостей для запуска тестов \
-requirements.txt - файл с библиотеками-зависимостими для установки через pip  

**Для работы через докер: \**
(Требуется установленный docker актуальной версии) \
1.сбилдить проект \
``` docker build -t 2gis-test .``` \
2.запустить образ \
```docker run -v [path-to-project]/allure-report:/tests/allure-report 2gis-test``` \
3.для просмотр отчета открыть в браузере(предпочтительно Firefox) файл: \
```[path-to-project]/allure-report/index.html``` \
или если через аллюр(Для открытия тест-отчета через аллюр необходима java 1.8+ ): \
```/allure-2.12.1/bin/allure open ./tests/allure-report/```

**При запуске тестов из проекта: \**
Тестам необходим интерпретатор Python-3.7 и выше, \
python-pytest, \
(```sudo apt install python-pytest```)
зависимости указаные в requirements.txt \
(```pip3 install --trusted-host pypi.python.org -r requirements.txt)``` \


1.Для запуска тестов выполнить команду: \
```pytest ./test/test_api.py --alluredir=./tests/allure``` \

2.Запуск генерации(Для генерации тест-отчета через аллюр необходима java 1.8+): \
```./allure-2.12.1/bin/allure generate ./tests/allure -o ./tests/allure-report --clean``` \
3.Для просмотр отчета открыть в браузере(предпочтительно Firefox) файл: \
```./tests/allure-report/index.html``` \ 
(если отчет не открывается с бесконечным ...loading следует изменить в about:config параметр privacy.file_unique_origin) \
или если через аллюр(Для открытия тест-отчета через аллюр необходима java 1.8+): \
```/allure-2.12.1/bin/allure open ./tests/allure-report/```



