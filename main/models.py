from django.db import models

# class AuthorManager(models.Manager):
#     def author_validator(self, postData):
#         errors= {}
#         if len(postData['first_name']) < 2:
#             errors['first_name']= "First name must be at least 2 characters long!"
#         if len(postData['last_name']) < 2:
#             errors['last_name']= "Last name must be at least 2 characters long!"
#         if len(postData['notes']) < 5:
#             errors['notes']= "Notes must be at least 5 characters long!"
#         return errors
# Create your models here.
# class BookManager(models.Manager):
#     def book_validator(self, postData):
#         errors= {}
#         if len(postData['title']) < 2:
#             errors['title']= "Title must be at least 2 characters long!"
#         if len(postData['description']) < 2:
#             errors['description']= "Description must be at least 2 characters long!"
#         return errors


    
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __repr__(self):
    #     return "Title: {}".format(self.title)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="Authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # This was for use in the shell so that I could see the Auther and the book names instead of id!!
    # def __repr__(self):
    #     return "Name: {}".format(self.first_name, self.last_name)