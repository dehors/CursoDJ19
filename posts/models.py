from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from markdown_deux import markdown
from comments.models import Comment
# Create your models here.
def upload_location(instance, filename):
	filebase, extension = filename.split(".")
	return "%s/%s.%s" %("post",instance.id, extension )
	
class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title

	@property
	def comments(self):
		instance = self
		qs = Comment.objects.filter_by_instance(self)
		return qs
	
	class Meta:
		ordering = ["-timestamp", "-updated"]

	def get_markdown(self):
		content = self.content
		return mark_safe(markdown(content))
		