from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager

# Create your models here.

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager)
from django.db import models
from multiselectfield.db.fields import MultiSelectField

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
	image=models.ImageField(upload_to='c:/pythondata/desitomato/media/None', height_field=None, width_field=None, max_length=100)
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
	parsed=models.BooleanField(default=False)
	grammar='1'
	comprehension='2'
	article_choices=(('', '---------'),(grammar,'grammar'),
		(comprehension,'comprehension'),)
	article_type=models.CharField(max_length=2,choices=article_choices,default='')
	
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
	


class wordmeaning(models.Model):
	word_name=models.CharField(max_length=99)
	word_meaning=models.CharField(max_length=99)
	def __unicode__(self):
		return str(self.word_name)


class sample_question(models.Model):
	article_id=models.ForeignKey(article)
	question_text=models.CharField(max_length=300)
	noun='1'
	pronoun='2'
	adjective='3'
	adverb='4'
	verb='5'
	conjunctionandinterjection='6'
	articels='7'
	determiners='8'
	vocabulary='9'
	choice_choices=(('', '---------'),(noun,'noun'),
		(pronoun,'pronoun'),
		(adjective,'adjective'),(adverb,'adverb'),(verb,'verb'),(conjunctionandinterjection,'conjunction or interjection'),(articels,'articels'),(determiners,'determiners'),(vocabulary,'vocabulary'),)
	subtopic= models.CharField(max_length=2,choices=choice_choices,default='')
	low='1'
	mid='2'
	high='3'
	level_choices=(('', '---------'),(low,'low'),
		(mid,'medium'),
		(high,'high'),)
	level=models.CharField(max_length=2,choices=level_choices,default='')
	mcq='1'
	morethanonechoice='2'
	truefalse='3'
	fillblank='4'
	edittext='5'
	matchit='6'
	question_type_choices=(('', '---------'),(mcq,'multiple choice questions'),
		(morethanonechoice,'more than one correct choice'),
		(truefalse,'true or false'),(fillblank,'fill in the blanks'),(edittext,'edit the sentence'),(matchit,'match the following'),)
	question_type=models.CharField(max_length=2,choices=question_type_choices,default='')
	manual='1'
	autogenerated='2'
	type_choices=((manual,'manual'),(autogenerated,'generated'),)
	question_type_type=models.CharField(max_length=2,choices=type_choices)
	paragraph_pos=models.IntegerField(null=True)
	sentence_pos=models.IntegerField(null=True)
	tag=models.BooleanField()
	word=models.CharField(blank=True,max_length=301)
	def __unicode__(self):
		return self.question_text+self.level



class mcq(models.Model):
	sample_question_id=models.ForeignKey(sample_question)
	choice1=models.CharField(max_length=30)
	choice2=models.CharField(max_length=30)
	choice3=models.CharField(max_length=30)
	choice4=models.CharField(max_length=30)
	choice1o='1'
	choice2o='2'
	choice3o='3'
	choice4o='4'
	choice_choices=(('', '---------'),(choice1o,'choice1'),
		(choice2o,'choice2'),
		(choice3o,'choice3'),(choice4o,'choice4'),)
	right_choice= models.CharField(max_length=2,choices=choice_choices,default='')
	def __unicode__(self):
		return str(self.sample_question_id)




class truefalse(models.Model):
	sample_question_id=models.ForeignKey(sample_question)
	true='1'
	false='2'
	choice_choices=(('', '---------'),(true,'true'),
		(false,'false'),)
	right_choice= models.CharField(max_length=2,choices=choice_choices,default='')

class morethanonechoice(models.Model):
	sample_question_id=models.ForeignKey(sample_question)
	choice1=models.CharField(max_length=30)
	choice2=models.CharField(max_length=30)
	choice3=models.CharField(max_length=30)
	choice4=models.CharField(max_length=30)
	choice1o='1'
	choice2o='2'
	choice3o='3'
	choice4o='4'
	MY_CHOICES = ((choice1o, 'choice1'),
              (choice2o, 'choice2'),
              (choice3o, 'choice3'),
              (choice4o, 'choice4'))
	right_choice= MultiSelectField(choices=MY_CHOICES)

class fillblank(models.Model):
	sample_question_id=models.ForeignKey(sample_question)
	right_choice=models.CharField(max_length=30)


class matchit(models.Model):
	sample_question_id=models.ForeignKey(sample_question)
	leftcol1=models.CharField(max_length=30)
	leftcol2=models.CharField(max_length=30)
	leftcol3=models.CharField(max_length=30)
	leftcol4=models.CharField(max_length=30)
	rightcol1=models.CharField(max_length=30)
	rightcol2=models.CharField(max_length=30)
	rightcol3=models.CharField(max_length=30)
	rightcol4=models.CharField(max_length=30)


class topic_score(models.Model):
	user_id=models.ForeignKey(User)

	noun_score=models.CharField(max_length=9)
	pronoun_score=models.CharField(max_length=9)
	adjective_score=models.CharField(max_length=9)
	adverb_score=models.CharField(max_length=9)
	verb_score=models.CharField(max_length=9)
	conjunction_score=models.CharField(max_length=9)
	article_score=models.CharField(max_length=9)
	determiner_score=models.CharField(max_length=9)


class sample_performance(models.Model):
	user_id=models.ForeignKey(User)
	sample_question_id=models.ForeignKey(sample_question)
	response=models.CharField(max_length=4)
	article_under=models.ForeignKey(article)
	paragraph_pos=models.IntegerField(null=True)
	sentence_pos=models.IntegerField(null=True)
	word=models.CharField(blank=True,max_length=301)


class theory(models.Model):
	heading=models.CharField(max_length=50)
	short_summary=models.CharField(max_length=200)
	long_description=models.CharField(max_length=999)
	example=models.CharField(max_length=500) #    add tags for words representing example 
	noun='noun'
	pronoun='pronoun'
	adjective='adjective'
	adverb='adverb'
	verb='verb'
	conjunctionandinterjection='conjunctionandinterjection'
	articels='articels'
	determiners='determiners'
	no='no'
	choice_choices=(('', '---------'),(noun,'noun'),
		(pronoun,'pronoun'),
		(adjective,'adjective'),(adverb,'adverb'),(verb,'verb'),(conjunctionandinterjection,'conjunction or interjection'),(articels,'articels'),(determiners,'determiners'),(no,'no'),)
	is_subtopic= models.CharField(max_length=20,choices=choice_choices,default='')
	




class article_visited(models.Model):
	user_id=models.ForeignKey(User)
	article_id=models.ForeignKey(article)


class verb_form(models.Model):
	first_form=models.CharField(max_length=20)
	second_form=models.CharField(max_length=20)
	third_form=models.CharField(max_length=20)
	plural_form=models.CharField(max_length=20)
	ing_form=models.CharField(max_length=20)
	def __unicode__(self):
		return self.first_form


class common_words(models.Model):
	word_anurag=models.CharField(max_length=30)


class dictionary(models.Model):
	word=models.CharField(max_length=30)
	word_meaning=models.CharField(max_length=5000)
	

class bookmark(models.Model):
	user=models.ForeignKey(User)
	word=models.CharField(max_length=50)
	word_meaning=models.CharField(max_length=3000)
	


class adjective_form(models.Model):
	first_form=models.CharField(max_length=20)
	second_form=models.CharField(max_length=20)
	third_form=models.CharField(max_length=20)


class synonyms(models.Model):
	word_id=models.ForeignKey(dictionary)

	synonym_def=models.CharField(max_length=40)
	adjective='a'
	adverb='s'
	verb='v'
	noun='n'
	tag_choices=(('', '---------'),(adjective,'adjective'),
		(adverb,'adverb'),
		(verb,'verb'),(noun,'noun'),)
	tag= models.CharField(max_length=20,choices=tag_choices,default='')


class similars(models.Model):
	word_id=models.ForeignKey(dictionary)

	similar_def=models.CharField(max_length=40)
	adjective='a'
	adverb='s'
	verb='v'
	noun='n'
	tag_choices=(('', '---------'),(adjective,'adjective'),
		(adverb,'adverb'),
		(verb,'verb'),(noun,'noun'),)
	tag= models.CharField(max_length=20,choices=tag_choices,default='')


class relateds(models.Model):
	word_id=models.ForeignKey(dictionary)

	related_def=models.CharField(max_length=40)
	adjective='a'
	adverb='s'
	verb='v'
	noun='n'
	tag_choices=(('', '---------'),(adjective,'adjective'),
		(adverb,'adverb'),
		(verb,'verb'),(noun,'noun'),)
	tag= models.CharField(max_length=20,choices=tag_choices,default='')



class antonyms(models.Model):
	word_id=models.ForeignKey(dictionary)

	antonym_def=models.CharField(max_length=40)
	adjective='a'
	adverb='s'
	verb='v'
	noun='n'
	tag_choices=(('', '---------'),(adjective,'adjective'),
		(adverb,'adverb'),
		(verb,'verb'),(noun,'noun'),)
	tag= models.CharField(max_length=20,choices=tag_choices,default='')


class essay(models.Model):
	heading=models.CharField(max_length=200)

class essay_attempted(models.Model):
	user_id=models.ForeignKey(User)
	essay_id=models.ForeignKey(essay)
	essay_content=models.CharField(max_length=2000)
class user_essay_reviews(models.Model):
	reviewer_id=models.ForeignKey(User)
	
	essay_id=models.ForeignKey(essay)
	parameter1=models.IntegerField()
	parameter1_text=models.CharField(max_length=300)
	parameter2=models.IntegerField()
	parameter2_text=models.CharField(max_length=300)
	parameter3=models.IntegerField()
	parameter3_text=models.CharField(max_length=300)
	parameter4=models.IntegerField()
	parameter4_text=models.CharField(max_length=300)
	parameter4=models.IntegerField()
	parameter5_text=models.CharField(max_length=300)


class list1(models.Model):
	word_name=models.CharField(max_length=50)
	word_meaning=models.CharField(max_length=2000)
	word_example=models.CharField(max_length=4000)
	def __unicode__(self):
		return self.word_name


class bookmark_questions(models.Model):
	
	word_used=models.ForeignKey(bookmark)
	question_text=models.CharField(max_length=400)
	choice1=models.CharField(max_length=300)
	choice2=models.CharField(max_length=300)
	choice3=models.CharField(max_length=300)
	choice4=models.CharField(max_length=300)
	choice1o='1'
	choice2o='2'
	choice3o='3'
	choice4o='4'
	choice_choices=(('', '---------'),(choice1o,'choice1'),
		(choice2o,'choice2'),
		(choice3o,'choice3'),(choice4o,'choice4'),)
	right_choice= models.CharField(max_length=2,choices=choice_choices,default='')

class bookmark_attempted(models.Model):
	user_id=models.ForeignKey(User)
	question_id=models.ForeignKey(bookmark_questions)
	response=models.IntegerField()










		
	
	




























# Create your models here.

# Create your models here.
