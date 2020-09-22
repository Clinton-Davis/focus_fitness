# Testing

----

## Manual Testing

The manual testing is done for each user story and categorised into the different departments of the webpage.

#### Responsiveness

- **User story**
*As a user, I want to access the website from any device.*
- **Test**:
  - Open each page of the website from multiple devices and multiple browsers
  - Open with Chrome and Firefox Developer Tools. and click on "Responsive" to check all pages
- **Results**: Fail: On the Home page in ‘Landscape orientation’, Section 2 was covering section 1’s on small screen sizes.
- **Bug**: ‘Landscape orientation’
- **Verdict**: The issues were fixed, the test passed.

#### Navbar and Footer

- **User story**
*As a user, I want to easily navigate between the pages
As a user, I want to link to the social pages of the company.*
- **Test:**
Click on all the links in the navbar, to check if they work properly pointing to the correct pages
Make the navbar collapses on mobile and nav links are visible.
Make sure the Navbar is Fixed at the top of the page
Make sure the Login/Signup is visible if the user is not logged in.
Make sure the Cart and username are always visible.
Check the footer logo goes under section 2 and 3 of the footer.
Check when a product is added to the cart, ‘Empty’ is replaced with the Grand Total, and changes colour to green.
Results:
All link are working as expected
Navbar collapses on screen size 994px burger bar appears and links visible when clicked
Navbar is Fixed at the top of each page
Login/Signup is visible if the user is not logged in
Cart and username are always visible.
Products added, Empty was replaced with a correct grand total in green.
Footer Logo did go beneath section 2 and 3 of the footer
Test passed.
 Verdict: All the functionality works as expected.
 

 
 
 
 
 
 
 
 
 

Home
As a user, I want to be able to see there special offers
As a user, I would like to see if blogs are featured
As a user, I would like to see the Professional programs they have to offer
Tests:
Check the home page has a list of all the special offers
Check the home page to see if featured blogs are shone
Check the home page for a list of Training Programs
Results:
Special offers wherein section 4 of the home page
Featured blogs wherein section 5 of the home page
Training Programs wherein section 2 of the home page.
All tests Passed
Verdict: All the functionality works as expected.



Shop, Cart, Checkout
As a user, I want to be able to browse their products
As a user, I want to be able to read the details of a product.
As a user, I would like to be able to review and rate products
As a user, I would like to be able to search for a Product
As a user, I would like to be able to purchase an item from the shop without having to log in.
As a user, I would expect to receive a confirmation email about my orders
Test:
Check the shop has a list of all the products
Check when a product is clicked, the user is redirected to the product detail page with all the information. Star rating, Catogeys, Price, and image.
Check users can not rate or review products if not logged in.
Check the user is not logged in, add the product to cart and checkout using Stripe.
Check the adjust and remove button in the cart.
Check validation on the checkout form.
Check emails for an email confirmation.
Check if the user is logged in and is able to rate and review products
Results:
Clicked on the shop button and was redirected to the products as expected
After clicking on a product was redirected to the product details page.  Star rating, Catogeys, Price, and image were in the right places as expected.
User not logged in, Tried to add a review but the button said ‘login in to review’
Use not logged in, selected a product, was redirected to product detail page, added product to cart, redirected to cart page with the success message.
Order summary was correct with all the correct information.
Changed the qty and removed a product form the adjust cart button, they work as expected.
Clicked Checkout button and redirected to check out page with all the correct placeholders are in place
Got validation error when didn’t fill out all the forms fields, as expected
Checkout order using Stripe test card number 4242 42424 24242
Redirected to a checkout success page with a list of all the order details
Clicked on the ‘View Receipts’ link in the checkout success page and redirected to a new page with the receipt being shown.
Checked Stripe Dashboard for payment_intent.succeeded  webhook, success as expected
Check email and have received the confirmation email.
All Tests Passed
Verdict: All the functionality works as expected.
 
 
Blogs
As a user, I want to be able to browse the blogs list
As a user, I want to be able to read the blog post I'm interested in.
As a user, I would like to be able to search for a blog post
As a user, I would like only other logged-in users to see my members blog posts.
As a user, I would like to be able to comment on other members' blogs posts
Tests
Check to see if blog posts are being shown.
Check when blog post is clicked it goes to the blog post detail page
Check the search blog search bar is working.
Check to see if the right page is shown when no search results are found.
Check to see if the right blogs are shown when searched.
Click on members category, Check the right response is shown.
Check the user is logged in and click on the members category.
Click the write a comment button and check the comment is posted in the comment section of the blog post.
Results:
Clicked the Blogs button on the main page and redirected to the blogs list as expected.
Clicking on blogs redirects to the blog's detailed page as expected.
Searching a word that is not in any title or content redirects to the No search results found page.
Searching a known search result redirects to the blog posts as expected.
Checked user is logged out, Clicked  members in the categories block and the right response is shown as expected.
Logged in and clicked the members category again and members blogs are shown.
Clicked a comment button and a comment form pop up as expected and a comment was posted in the comment section as expected.
All Tests Passed
Verdict: All the functionality works as expected.
 
 
 
 
 
 
 
Member selection, Programs list, Subscription payment, email confirmation and invoice
As a user, I would like to be able to become a member by subscribing.
As a user, I would like to see the Professional programs they have to offer
As a member, I would like to be able to watch a video on how to do exercises.
Tests:
Check home page flow to become a subscriber
Check Programs list is displaying list.
Check only logged in users may see programs details.
Check email confirmation and invoice
Check logged in user flow to get to the member select page.
Check members can watch work out programs.
Results:
Click Training Programs and redirect to Programs page, as expected, checked that there is a list of programs to choose from.
When clicked on a Training programs redirected to the login page as expected.
Logged in, and clicked on Training Programs, redirected to Programs list, as expected.
Clicked on a program and redirected to the Upgrade membership page, as expected
Clicked on the ‘Select Membership’ button and redirected to the membership select page as expected.
Clicked ‘Select’ button in the Professional membership card redirected to Membership Payment page as expected.
Fill out the Stripe Card field with 424242 424242 424242 and click submit
Redirected to the programs page as expected. Clicked on a program redirected to the workout page as expected.
Clicked on workout redirected to the workout page where the video is able to play.
Check Stripe Dashboard for Webhook subscription_created received: customer.subscription.created. As expected.
Check email for confirmation and have one as expected.
All Tests Passed
Verdict: All the functionality works as expected.
 
 
 
 
Dashboard
As a user, I would like to have a place where I can see all my past orders
As a user, I would like to be able to change my password.
As a user, I would like to be able to change my shipping address
As a member, I would like to see when my next subscription payment is due
As a member, I would like to cancel my subscription any time
Tests:
Login in user and click on Dashboard link in navbar.
Check Dashboard is displayed correctly.
Check ‘Order History’ column is populated with the order history of the user
Check order history is ordered newest to oldest
Click on Order and test response.
Check ‘Profile Admin’ column has the user's email.
Check ‘Update password’ redirects to Password Reset Page.
Check ‘Shipping Details’ redirects to Shipping Details form with pre populated shipping address. 
Check ‘Subscription’ has the current user membership level in and redirects to subscriptions details
Check subscription information and Cancel subscription button
Check ‘Cancel Subscription’ button works
Results:
Logging in clicked to Dashboard and redirected to Dashboard page as expected.
Dashboard has 3 column Profile Admin, My Blogs, Order History. As expected.
Order History has a list of all previous orders ordered by date, Newest to oldest. As expected.
Clicked on a prevoirs order redirected to Order History page will all the information and stripe Receipt link opening up on a new page.
Profile Admin has users emails as expected.
Clicking on Shipping Details redirect to the shipping details page with all information pre populated as expected.
Clicking on Updated Password does redirect to password Reset Page as expected.
The Profile admin column has the membership level shown and clicking redirects to the Subscriptions page with Current Membership  members since date and Next payment due and a date.
Clicking Cancel Subscription redirects to cancel subscription confirmation page.
Failed. Clicking ‘Yes, Cancel my Subscription’ shows a NoReverseMatch error.
A success message was shown as expected.
Bug: ‘Yes, Cancel my Subscription’ button error. Name space was wrong.
Verdict: The issues were fixed, the test passed.
Login
As a user, I would like to be able to login with a social account.
Test
Check Social accounts Google 
Check Social accounts Facebook
Check Logout 
Check Login with email and password
Check Validation on email
Results:
Click the ‘Sign In with Google’ button and a google pop asked me which Google account to use, and redirected me to the home page as expected.
Clicked the ‘facebook’ button,redirected me to facebook password section, then redirected me back to the home page, as expected.
Clicked the logout button and redirected to the logout confirmation page, clicked the confirmation button and redirected to the home page.
Added wrong information into the email field and validation failed as expected.
Correct the information and login in, redirected to the home page, as expected.
Verdict: All the functionality works as expected.
 
The Admin
As the admin, I expect to be able to log in from any page.
As admin, I expect to be able to see all the different sections of the website.
As admin, I expect to be able to add, edit, delete products, blogs, programs as needed.
As admin, I expect to be able to change user memberships.
As admin, I expect to be able to put products out of stock and show this in the shop.
As admin, I expect to be able to put products on special offers.
As admin, I would like that if a staff member did not put the right ‘was’ price of the product that only the price would be shown.
As admin, I would like to be able to see what products have had the most views and heights 
As admin, I would like to be able to see all the orders that have taken place.
As admin, I expect to see a ‘No Image’ image if there is no image for a product.
Test:
Check the admin login icons are shown on all pages
Check in the admin area, all the different department are visible
Check the ability to add, edit, and delete products, blogs, programs
Check the ability to change user memberships
Check the product ‘In stock’ checkbox works and shows in the product list
Check if not in stock items are displayed in the special offers section.
Check the product special offers check box works and shows the special offers in the home page section.
Check the ‘was’ price is smaller that the price and if not check to ‘was’ price is not shown
Check the shop admin has the ability to filter by most views
Check the Shop orders are able to be seen. And order from newest to oldest with the name and shipping details.
Check the ‘No-image’ product image is shown if the product image is not there.
Results:
Pages throughout all the pages of the website and the admin icon was always there. As expected.
Login to the admin and all the different department are visible, as expected
Clicked on the ‘Products’ button and clicked on the products name, redirected to products details, I was able to edit, add, and delete a product. As expected.
Clicked on the ‘Blogs’ button and clicked on the blogs name, redirected to blogs details, I was able to edit, add, and delete the blog post. As expected.
Clicked on the ‘Programs’ button and clicked on the Programs name, redirected to program details, I was able to edit, add, and delete  the programs. As expected.
Clicked on the ‘Products’ button in the Shop section and was able to Uncheck the ‘in Stock’ check box.
Checked the products list in the shop and the ‘Out of Stock’ image was being shown.
Fail: Out of stock product was still being shown in special offers.
Fail: ‘was’ price is was shown
Checked the products page, could filter by rating and could filter. As expected
Checked Order in the Shop Order section and Order number, Date ordered, arranged from newest to oldest by default, able to filter by Date, Name, Order Total, Grand total or tax.
Clicked on an order number and all the orders details and address where as expected.
Cleared the image in the edit product section of the shop and no image was shown on the product in the shop and home page.
Bug:
Out of stock product was still being shown in special offers
‘was’ price is was shown
Verdict: The issues were fixed, the test passed.
