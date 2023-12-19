from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_caption = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.tag_caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.last_name}, {self.first_name}"

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    post_title = models.CharField(max_length=256)
    post_excerpt = models.CharField(max_length=256)
    post_image = models.ImageField(upload_to="posts", null=True)
    post_slug = models.SlugField(unique=True, null=False, db_index=True)
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
    post_content = models.TextField()
    post_date = models.DateField(auto_now=True)
    post_tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.post_title}"

class PostComments(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    comment = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
