# BLOG PHOTO #
## A web project in Python, using Django ##

I. Authentication:
  1. Creation of a User model that implements AbstarctUser
  2. Creating a view for user to loggin with a LoginForm.
  3. Logout
  4. Restrict access to home page : only available for logged in users.
  5. Utilisation of generic view LoginView
  6. Signup page with a UserCreationForm
  7. Validators for password
  
II. Blog Photo
  1. Uploading images with a form
  2. Changing profile picture with a form
  3. Displaying feed on home page.
  4. Creating a Blog article with a Photo uploaded (BlogForm + PhotoForm)
  5. Viewing a Blog article
  6. Editing/Deleting a Blog article
  7. Uploading multiple image with a FormSet
  8. Resizing an image when saved, by overwritting save() method of Photo's model
  9. Using permissions on Groups to restrict access for some pages.
  10. Many to Many relation between users (to follow a user/creator)
 
