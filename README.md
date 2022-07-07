# BSPForum: A demo Forum App backend on Django 
## Project for BSP, IITD Web Editor Recruitment 2022

### About
A barebones forum implemented in Django, which lets users sign up, post a new post and post comments on the existing posts. Admins can open Django admin panel, which is provided built-in by Django for admin functions like deleting or editing posts or comments or removing users from the forum.

### Features
1. Registration system allows users to register themselves using email id, username, first name, last name and password.
    - Email verification was implemented but commented out (code still present in the source) due to complications in sending emails.
    - Username field is unique.
    - Password field is minimum 8 characters long (Django enforces it by default, so cannot change it). So specified passwords of 'pwd1', 'pwd2' and 'pwd3' can't be set for users.
2. If logged out, the home page redirects to login page.
3. If logged in, home page loads.
4. Home page shows Recent posts as well as count of registered users and total posts.
5. Search feature on home screen lets user search through posts or users.
6. My profile link in the left pane links to the profile page of the logged-in user.
7. Login/Logout/Register links are self explanatory. 
8. Profile page of user shows profile details and posts by the user.
9. If the logged in user is admin, there is an extra link of Django admin internal site in the profile page.
    - Admin site provides admin with features of editing or deleting any post/comment.
    - Admins can also delete users from the forum app from here.
10. Post previews in the home page and profile page are clickable and on clicking opens in a full page.
11. Posts can optionally contain a single image. (Only single image implemented for now.)
12. Add post button available on home page to create a new post.
13. Add comment button available on each post's page to add comments.

### How to run locally
Requirements:
- Python 3.6+ (I had used 3.9.x)
- Django 3.0+ (I had used 3.2)

Steps:
1. Clone the repo or download the zip and exrtract it to your local machine.
2. Go to BSPForum directory (which contains the manage.py file ) and run the command from the terminal: `python manage.py runserver`
    - PS: On certain devices (mostly Windows), you may need to replace `python` with `python3` or `py` in the above command. Run `python --version` or `python3 --version` or `py --version` to check which command is working for you.

If the above command works, the server should be up and running on the default port. Go to the url shown in your terminal window (Generally: `127.0.0.1:8000`)