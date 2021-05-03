# Python Instagram Bot
This project created with Python - Selenium. 

The project opens instagram.com in web browser whichone you chose in step 2-3 and enters your credentials to username and password fields. Then it clicks some noticitation links. Finally it opens profile page to get followers count. You can see the result in console. 

**Additional Note**

_In ilk_bot_uygulamasi.py file, you can see basic usage of selenium module._

# How to setup
**1.Install selenium module.**

You can find everything here [ https://selenium-python.readthedocs.io/ ] about installing selenium.
Shortly you can install with this command : 
`pip install selenium`

**2.Download webdriver which one you prefer Chrome, Firefox, Safari and etc.**

Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads

Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox:	https://github.com/mozilla/geckodriver/releases

Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

**3.Create bilgiler.py inside the project directory and create these three variables below ;

**_kullanici_adi_** = which holds Instagram username
 
**_parola_** = which holds Instagram password

**_webdriver_path_** = which holds  webdriver path where you have already downloaded at step 2

Then import it in instagram_bot.py file.**

_4.You're ready to start._

