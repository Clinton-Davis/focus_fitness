# focus_fitness

 MileStone 4

## Index Page

### Features

Index - Checks to see if the user is anomymous or a logged in  user.
If the user is anomymous.

- We offer the join up botton.

If the use has a login but not subcribed to the programs.

- We offer the subscribe botton.

If the user is a "Pro" subcriber and logged in.

- We offer the programs botton.
The section 3 "Subscribe Today" banners button will redirect the user to 'login' if not loged in and Membership select is logged in.
The Banner will not be shown if the user has a "Professional" membership.

### Programs Page

If a anomymous clickes on the Programs button in the Index page. They will be redirected to the Login Page

 Bugs:
 after adding a check to see if user is the same as the author, as to let the author edir or update post I have noticed the comments messages is chnaging as to how is logged it.

### deplyment

If you are starting with a new Database.
You will have to comment out all 'Blog categorys' forms views.
We have to do this because the catogery functions looking for blog_catogerys and throus a tabl does not exist. 

make migrations

then before you make superuser, you will have to comment out:
memberships.models - def post_save_usermembership_create
cart.context.py - def get_loged_user_discount(request): and the if request.user.is_authenticated:(the entire if statment).

profiles.models - create_or_update_user_profile.
Then you will be ok to make superuser.
Login to /admin/ and make memberships Fre/Pro and fill Stripe Products API id.
Then in UserMemberships, make the superuser a member.
Once that is done, uncomment everything, and you will be ready to go.
