repo: odoo

=> 2 folders:
- [folder] addons <----- ******
- [folder] odoo
  - [folder] addons
    - [*] [folder] base
  - [*] models.py
  - [*] fields.py
  - [*] api.py
  - sql_db.py
  - http.py
  - ...


module: sale
- [*] __manifest__.py
- [*] __init__.py
- [folder] models
  - *.py
- [folder] views
  - *.xml
- [folder] security
  - *.xml
  - *.csv
  - [optional] *.py
- [folder] report
  - *.xml
  - *.py
- [folder] data
  - *.xml
  - *.py
- [folder] wizard
  - *.py
  - *.xml
- [folder] controllers
  - *.py
- [folder] i18n
  - *.po
- [folder] tests
  - *.py
- [folder] static
  - [*] [folder] src
    - [folder] css
    - [folder] img
    - [folder] js
    - [folder] scss
    - [folder] xml
