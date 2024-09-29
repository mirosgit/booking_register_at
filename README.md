
---
## Install Python v3.8
1. Go to [SITE](https://www.python.org/downloads/release/python-380/)
2. Install **Python v3.8** from this site
---

## GIT Setup Guide
1. Go to [GIT Setup Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
---

## Allure Setup Guide
1. Go to [Allure Setup Guide](https://allurereport.org/docs/install-for-windows/)
---

## Clone a repository from GitHub
1. Create Folder
2. Open **PowerShell**/**Terminal**
3. Input in **Terminal** way to your **Folder** (ex. `cd D:\Git\{name_your_folder}`)
4. Input to **Terminal** this command: `https://github.com/mirosgit/booking_register_at.git`
5. **Wait until all files are installed**

---
## Install and Run Tests
1. Input in **Terminal** way to your **Folder** (ex. `cd D:\Git\{name_your_folder}\booking_register_at`)
2. Input to **Terminal** this command: `pip install -r requirements.txt`
3. **Wait until all files are installed**
4. In File **TestData.xlsx** mark what tests you want to run
5. Save File 
6. Input to **Terminal** this command: `pytest -n auto -s -v --alluredir=allure-results`
7. After Tests Success Finished Input to **Terminal** this command: `allure generate allure-results -o allure-report --clean`
8. Input to **Terminal** this command: `allure open allure-report`

