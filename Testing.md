## Testing 

### Manual Testing process

The manual testing of a website can be a simple procedure, involving the access of a web page or application within a controlled setting, systematically navigating through a set of predefined test scenarios, and documenting the results of each test in a spreadsheet. This fundamental method is often utilized by software teams as they first emphasize quality assurance.

Primarily, a foundational understanding of the Python environment and Django templating, along with knowledge of HTML elements and CSS properties, is advantageous for recognizing and resolving potential issues.

**Testing Process:**  
- *Tested Code*:  
- After every new function, variable or template tag, testing was provided through checking result with running server  
- Project was started as a Python code with Django framework to be used for templating and administration of applications  
![Django installed with success](Ωssets-readme/01-django-installation.png)  
- Setup of Project 'Boutique' and creating Superuser to be able to access Admin area  
![Django Admin Interface](Ωssets-readme/02-django-admin.png)  
- Installation of the Allauth app and required fields in the Admin area  
![Admin area with allauth fields](Ωssets-readme/03-django-admin-allauth.png)  

- *Tested Content*: 
- Before adding actual content, inserted some test content into HTML file and run it in web browser to ensure that the code is working as expected.  
- First draft of the Home page for Django e-commerce project to test functionality of the code, views, urls and related wireing in settings.py file  
![Home (Landing) page](Ωssets-readme/testing/home-page-first-draft.png)  

- *User Interface (UI)*:  
- Verified the layout, visual design, and overall user experience.  
- Checked for consistent formatting, proper image loading, and readability across different screen sizes.  

- *Readability*:  
- Examined displayed text (font family, font size, color contrast).  

- *Navigation*:  
- Tested all navigation elements like menus, buttons, and links. Ensured they lead to the correct destination pages and function smoothly.  
- Responsive top navigation elements, change smoothly into 'hamburger menu'

- *Forms & Functionality*:  
- Tested form (contact) to be sure it submit data correctly, provide clear error messages for invalid inputs, and follow expected functionalities, sending data.  

- *Content Accuracy*:  
- Reviewed all website content for accuracy, grammar, and spelling mistakes.  
- Verified that descriptions and other information are up-to-date and consistent.  

- *Responsiveness*:  
- Validated responsiveness of the website, with individual pages, loading Dev Tools option of split screen and resized the browser window across different browsers.  
- Working as expected, responsive containers, icons, images.  

- *Feature - email confirmation*   
- Email confirmation for the order, sent to Terminal   
![Terminal confirmation email](Ωssets-readme/testing/terminal-confirmation-email.png)  

- *Feature - Sign In/login*  
- User - login with success  
![Admin login successful](Ωssets-readme/testing/login-admin-success.png)  

- *Feature - Shopping*  
- Adding item to the cart  
![Adding item to the shopping cart](Ωssets-readme/testing/adding-item-to-cart.png)  

- *Feature - Product Management*  
- Add product feature for Admin raised Error message with too long price value  
![Raised Error msg in form validation](Ωssets-readme/testing/add-product-error-price-issue.png)  
- Add product feature - success message  
![Add product through Product Management success](Ωssets-readme/testing/add-product-success.png)  
- Edit product feature - success message  
![Edit product with success](Ωssets-readme/testing/edit-product-success.png)  
- Delete product feature - success message  
![Delete product with success](Ωssets-readme/testing/delete-product-success.png)  

- *Feature - Admin UI*  
- Add product/item with success through Admin interface/form   
![Add new item](Ωssets-readme/testing/admin-add-new-item.png)  

- Feature Stripe payment - webhooks events  
![Stripe payment event pass](Ωssets-readme/testing/stripe-webhook-event-endpoint.png)  
---


### Validator Testing 

- HTML
  - [W3C validator](https://validator.w3.org/nu)  
  - Errors repeatedly raised from each page - need to be some template code
  - Error: Element 'li' not allowed as child of element 'nav' in this context
  - Error: Duplicate ID user-options
  - Error: A document must not include both a meta element with an http-equiv attribute

- CSS
  - [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
  - for files base.css, profiles.css
  - No errors were found when passing through the official validator  

- Lighthouse: **https://pagespeed.web.dev/**  
- Lighthouse is an open-source, automated Audit tool for improving the quality of web pages. You can run it against any web page, public or requiring authentication. It has audits for performance, accessibility, progressive web apps, SEO, and more. Lighthouse is integrated directly into the Chrome DevTools, under the "Lighthouse" panel.  
- Lighthouse metrics:
- Home page  
![Lighthouse Home page](Ωssets-readme/testing/ligthouse-home-page-mobile.png)  
- Products page  
![Lighthouse Product page](Ωssets-readme/testing/ligthouse-product-page.png)  
- Single Product page  
![Lighthouse Single product page](Ωssets-readme/testing/ligthouse-single-product-page.png)  
- Shopping Cart  
![Lighthouse Shopping Cart](Ωssets-readme/testing/ligthouse-shopping-cart.png)  
- Checkout page  
![Lighthouse Checkout page](Ωssets-readme/testing/ligthouse-checkout-page.png)  
- Sign in page  
![Lighthouse Sign in page](Ωssets-readme/testing/ligthouse-signin-page.png)  
- My profile page  
![Lighthouse My profile page](Ωssets-readme/testing/ligthouse-my-profile-page.png)  
- Product Management  
![Lighthouse product Management](Ωssets-readme/testing/ligthouse-product-management-page.png)  
- FAQs page  
![Lighthouse FAQs page](Ωssets-readme/testing/ligthouse-faqs-page.png)  


- JavaScript: **https://www.jshint.com/**
 - Files countryfield.js and stripe_elements.js results
 ![JS countryfield file](Ωssets-readme/testing/js-countryfield-image.png)
 ![JS stripe_elements file](Ωssets-readme/testing/js-stripe_elements-image.png)  

- Python: **https://pep8ci.herokuapp.com/**  
- file custom_storages.py
![Python Linter - custom_storages](Ωssets-readme/testing/py-custom_storages.png)  
- file profiles\views.py  
![Python Linter - profiles\views](Ωssets-readme/testing/py-profiles-views.png)  
- file profiles\models.py  
![Python Linter - profiles\models](Ωssets-readme/testing/py-profiles-models.png)  
- file profiles\forms.py  
![Python Linter - profiles\forms](Ωssets-readme/testing/py-profiles-forms.png)  
- file products\views.py  
![Python Linter - products\views](Ωssets-readme/testing/py-products-views.png)  
- file products\models.py  
![Python Linter - products\models](Ωssets-readme/testing/py-products-models.png)  
- file products\forms.py  
![Python Linter - products\forms](Ωssets-readme/testing/py-products-forms.png)  
- file  home\views.py  
![Python Linter - home\views](Ωssets-readme/testing/py-home-views.png)  
- file home\models.py  
![Python Linter - home\models](Ωssets-readme/testing/py-home-models.png)  
- file home\forms.py  
![Python Linter - home\forms](Ωssets-readme/testing/py-home-forms.png)  
- file faq\views.py  
![Python Linter - faq\views](Ωssets-readme/testing/py-faq-views.png)  
- file faq\models.py  
![Python Linter - faq\models](Ωssets-readme/testing/py-faq-models.py.png)  
- file checkout\webhooks.py  
![Python Linter - checkout\webhooks](Ωssets-readme/testing/py-checkout-webhooks.png)  
- file checkout\webhook_handler.py  
![Python Linter - checkout\webhook_handler](Ωssets-readme/testing/py-checkout-webhook_handler.png)  
- file checkout\views.py  
![Python Linter - checkout\views](Ωssets-readme/testing/py-checkout-views.png)  
- file checkout\models.py  
![Python Linter - checkout\models](Ωssets-readme/testing/py-checkout-models.png)  
- file checkout\forms.py
![Python Linter - checkout\forms](Ωssets-readme/testing/py-checkout-forms.png)  
- file cart\views.py  
![Python Linter - cart\views](Ωssets-readme/testing/py-cart-views.png)  
- file cart\contexts.py  
![Python Linter - cart\contexts](Ωssets-readme/testing/py-cart-contexts.png)  
- file cart_tools.py  
![Python Linter - cart_tools](Ωssets-readme/testing/py-cart_tools.png)


## Bugs and Fixtures

- Missing table to display 'Products' page, RESOLVED with migrations to create tables in DB.  
![Missing table to display 'Products' page](Ωssets-readme/bugs/missing-products-table.png)  
- Error because 'cart_tools' is not a registered as a tag library, when try to access 'checkout' page  
!['cart_tools' is not a registered](Ωssets-readme/bugs/not-registered-tag-library.png)  
- AttributeError 'cart' - event_handler event displays, even after processed order, RESOLVED changing view 'cache_checkout_data' wrong name  
![AttributeError 'cart'](Ωssets-readme/bugs/attributeerror-cart-eventhandler.png)  
- RelatedObjectDoesNotExist error - new app 'profiles' overrides existing superuser profile with try out of saving unknown profile  
- Error RESOLVED with created new superuser and deleted old one  
![Superuser login doesn't work](Ωssets-readme/bugs/RelatedObjectDoesNotExist.png)  
- Error 'The 'image' attribute has no file associated with it.' raised when try to open new added product without image  
- RESOLVED with replacing Django tags between 'image' and 'no-image' references  
![Error when open product page without image](Ωssets-readme/bugs/no-image-single-product-page.png)  
- Server error (500) - on Heroku when try to send email to newsletter table  
![Heroku newsletter issue](Ωssets-readme/bugs/heroku-newsletter-issue.png)  
- Resolved with access to Heroku Console and run migrations  
![Newsletter form Server Error resplved](Ωssets-readme/bugs/heroku-newsletter-issue-resolved.png)  

### Unfixed Bugs

- The About Page in the Django e-commerce site remains incomplete due to an unidentified issue preventing text from rendering or displaying properly.  