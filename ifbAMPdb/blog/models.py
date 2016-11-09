from django.db import models
from django.utils import timezone
from django.conf import settings

def markdown_to_html( markdownText, images ):
	image_ref = ""

	for image in images:
		image_url = settings.MEDIA_URL + image.image.url
		image_ref = "%s\n[%s]: %s" % ( image_ref, image, image_url )

	md = "%s\n%s" % ( markdownText, image_ref )
	html = markdown.markdown( md )

	return html

class Image( models.Model ):
	name = models.CharField( max_length=100 )
	image = models.ImageField( upload_to="image" )

	def __unicode__(self):
		return self.name

	def __str__(self):
		return str(self.name)

class Post( models.Model ):
	title = models.CharField( max_length=100 )
	body = models.TextField()
	description = models.CharField(max_length=200, blank=True)
	images = models.ManyToManyField( Image, blank=True )
	author = models.ForeignKey('auth.User')
	created_date = models.DateTimeField( default = timezone.now)
	published_date = models.DateTimeField( blank = True, null= True)

	def body_html( self ):
		return markdown_to_html( self.body, self.images.all() )

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
