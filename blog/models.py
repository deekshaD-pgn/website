from django.db import models

class BlogItem(models.Model):

	date = models.DateTimeField(
		verbose_name='Blog entry', 
		auto_now_add = True,
		db_index=True,
	)


	owner = models.ForeignKey(
		verbose_name="Owner",
		to="auth.User",
		on_delete=models.PROTECT,
		)

	title = models.CharField(
		verbose_name= 'Title',
		max_length=100,
	)

	body = models.TextField(
		verbose_name='Body'
	)
