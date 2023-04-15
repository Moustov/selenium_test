EXAMPLES OF SELENIUM USAGES
=====
![Selenium Logo](https://selenium-python.readthedocs.io/_static/logo.png)

* The purpose of this repos is to demonstrate some [Selenium](https://selenium-python.readthedocs.io/) features with python.
* It is based on the [Page Object Model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/). To run the demo, see [Test Running](#Test Running) section.
* Those interfaces could be improved using the [ScreenPlay](https://screenpy-docs.readthedocs.io/en/latest/index.html) design pattern 
# Quick start...
## Requirements
Install requirements:

    pip install -r requirements. txt 

This will basically install the modules:
* selenium
* pytest

# Test Running
Run 

    python.exe -m pytest tests

# Page Object Models folder
## POM with pure HTML page
Based on the HTML page located at 

https://www.caipture.com/demo/samples.html

See [here](pom/caipture_com_demo_samples.py)

## POM with Angular 1.7 page
Based on the HTML page located at 

https://codesandbox.io/s/angularjs-17x-sandbox-5kdd3

See [here](pom/codesandbox.py)

# Tips

* https://www.reddit.com/r/QualityAssurance/comments/q5rsl8/in_your_experience_is_using_xpaths_a_bad_practice/:

>CSS selectors perform far better than Xpath and it is well documented in Selenium community. Here are some reasons,
>
>Xpath engines are different in each browser, hence make them inconsistent
>
>IE does not have a native xpath engine, therefore selenium injects its own xpath engine for compatibility of its API. Hence we lose the advantage of using native browser features that WebDriver inherently promotes.
>
>Xpath tend to become complex and hence make hard to read in my opinion
>
>Further more there was a benchmark that indicated css selectors to be faster - not by much but I guess it could add up to a minute or 2 for large scale projects.


