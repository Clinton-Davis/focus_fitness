# focus_fitness

 MileStone 4



 Bugs:
 after adding a check to see if user is the same as the author, as to let the author edir or update post 
 I have noticed the comments messages is chnaging as to how is logged it.

#### Bugs

 I was having a getting the right product_id in the idex.html. I was using 
 {% url 'product_detail' product.id %}, I was get a Error:  

~~~
Reverse for 'product_detail' with arguments '('',)' not found. 1 pattern(s) tried: ['products/(?P<product_id>[^/]+)/$']
~~~

Fix: Im my for loop I was using the word 'items' in sale_item so once I change the 
product.id for item.id it fixed the bug.

#### Bugs

There is a boostrap4 carousel in the blog#-list.html page that shows featured blogs. 
I was using a for loop to get the blog post to show. 
After that I was using a if statement to pick out the featured post from the others.
But it was not working.
When i tested the carousel to if that was the problem, it worked fine.
I then made sure the for loop was working with {{ blogs.featured }} 
True and False where being shown, that that was not the bug.
To make the carousel work with looped objects you have to loop the counter with 1 being active.
~~~
<div class="carousel-item {% if forloop.counter == 1 %}active{% endif %}"
                        id="slide{{ forloop.counter }} ">
~~~

When I had my {% if blog.featured == Ture %} the div's class if loop was cause an error and nothing was being shown.
Fix: in the bloglistview I added a quaryset with a filter to loop for featured blogs and passed them into the context. From there i just looped through them.

I had a form with in a form in the footer thats why is was not getting to the view
discount wasnt getting taken into account as the discount was not being added into the order model, So i added it from global context and saved

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


