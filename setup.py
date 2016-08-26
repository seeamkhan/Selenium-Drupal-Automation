from distutils.core import setup
import py2exe

# Change the path in the following line for webdriver.xpi
# data_files = [('selenium/webdriver/firefox', ['D:/Python27/Lib/site-packages/selenium/webdriver/firefox/webdriver.xpi'])]
# data_files=[('Drivers', ['C:/Python27/Scripts/chromedriver.exe'])],

setup(
console=['general_test.py'],
# data_files=[('Drivers', ['C:/Python27/Scripts/chromedriver.exe'])],

options={
        "py2exe":{
                "skip_archive": True,
                "unbuffered": True,
                "optimize": 2
        }
}
)