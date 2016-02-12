from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager

# Create your models here.

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager)
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user





class User(AbstractBaseUser):
	objects=UserManager()
	"""
	Custom user class.
	"""
	email = models.EmailField('email address', unique=True, db_index=True)
	joined = models.DateTimeField(auto_now_add=True)
	usertype=models.CharField(max_length=2)
	USERNAME_FIELD ='email'
	def __unicode__(self):
		return self.email
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	def get_full_name(self):
		return self.email
	def get_short_name(self):
		return self.email
	def __unicode__(self):
		return self.email
	def has_perm(self, perm, obj=None):
		return True
	def has_module_perms(self, app_label):
		return True
	def is_staff(self):
		return self.is_admin   

class article(models.Model):
	image=models.ImageField(upload_to='c:/Python27/desitomato/media/None', height_field=None, width_field=None, max_length=100)
	heading=models.CharField(max_length=90)
	level=models.IntegerField()
	summary=models.TextField()
	content=models.TextField()
	politics='1'
	sports='2'
	science='3'
	entertainment='4'
	world='5'
	nation='6'
	environment='7'
	businessandcommerce='8'
	genre_choices=(('', '---------'),(politics,'politics'),
		(sports,'sports'),
		(science,'science'),(entertainment,'entertainment'),(world,'world'),(nation,'nation'),(environment,'environment'),(businessandcommerce,'businessandcommerce'),)
	genre=models.CharField(max_length=2,choices=genre_choices,default='')
	def __unicode__(self):
		return str("id")+str(":")+str(self.id)+str(" ")+str("heading")+str(":")+str(self.heading)
	






class question(models.Model):
	article_id=models.ForeignKey(article)
	question_text=models.CharField(max_length=50)
	vocab='1'
	grammar='2'
	comp='3'
	genre_choices=(('', '---------'),(vocab,'vocabulary'),
		(grammar,'grammar'),
		(comp,'comprehension'),)
	genre=models.CharField(max_length=2,choices=genre_choices)
	choice1=models.CharField(max_length=50)
	choice2=models.CharField(max_length=50)
	choice3=models.CharField(max_length=50)
	choice4=models.CharField(max_length=50)
	choice1o='1'
	choice2o='2'
	choice3o='3'
	choice4o='4'
	choice_choices=(('', '---------'),(choice1o,'choice1'),
		(choice2o,'choice2'),
		(choice3o,'choice3'),(choice4o,'choice4'),)
	right_choice= models.CharField(max_length=2,choices=choice_choices,default='')
	def __unicode__(self):
		return str("id")+str(":")+str(self.id)+str(" ")+str("question_text")+str(":")+str(self.question_text)


	

class comment(models.Model):
	article_id=models.ForeignKey(article)
	user_id=models.ForeignKey(User)
	comment_text=models.CharField(max_length=999)
	time=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return str(self.id)


class performance(models.Model):
	question_id2=models.ForeignKey(question)
	user_id=models.ForeignKey(User)
	response=models.CharField(max_length=2,default='')
	key=models.BooleanField(default=False)
	def __unicode__(self):
		return str(self.id)
	


class word(models.Model):
	word_name=models.CharField(max_length=99)
	def __unicode__(self):
		return str(self.id)


class word_meaning(models.Model):
	word_id=models.ForeignKey(word)
	word_meaning=models.CharField(max_length=99)
	def __unicode__(self):
		return str(self.id)
















# Create your models here.
