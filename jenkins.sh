#! /bin/sh

pip install -r requerimientos.txt
autopep8 -ir .
flake8 --max-complexity=5 --exclude=*.txt,.gitignore --max-line-length=200 .
lettuce bdd
cd pruebasUnitarias
python TestMayor.py
coverage run --branch TestMayor.py
coverage report -m 
coverage html --title="Cobertura de código de Mayor"
