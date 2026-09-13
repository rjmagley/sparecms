from django.db import models
from django.contrib.auth import User


# Articles are written by users, potentially set to a specific AuthorProfile
# the body of the article itself is actually stored in a Markdown file outside
# the database, for export via Pelican
class Article(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    # listed_author lets you have a different displayed author name rather than
    # the actual author username; for fun jokes and goofs
    listed_author = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(AuthorProfile, null=True, on_delete=SET_NULL)
    # markdown_file will be a file name in the directory where Markdown content
    # is stored. By default I think this will be MEDIA_ROOT?
    # I'm not sure if it's smart at this point to try to divy up
    # Markdown files by category or some other way of sorting them,
    # so for now it'll just be a filename
    markdown_file = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    def get_author_display_name(self):
        if self.listed_author != "":
            return self.author.display_name
        return self.listed_author

    # this probably needs a much better translation table but this will do
    # for a prototype
    # https://docs.python.org/3/library/stdtypes.html#str.maketrans
    def update_slug(self):
        new_slug = self.title.translate(str.maketrans(
            {" ": "-",
            ":": "-",
            ";": "-"}
            ))
        self.slug = new_slug

    # Stub for override of .save() to handle automatic slug generation and the like
    # reference: https://docs.djangoproject.com/en/6.1/topics/db/models/#overriding-predefined-model-methods
    def save(self, **kwargs):
        self.update_slug()
        super().save(**kwargs)

    # Stub for write_article - writes article content to Markdown file on disk
    # reference for metadata format for writing: https://docs.getpelican.com/en/latest/content.html#file-metadata
    # presumably this will be called at some point during .save()? or maybe these files should be created en-masse
    # with some kind of "publish site" functionality?
    # maybe that's an option that can be set
    def write_article(self):
        return


# Tags
class Tags(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)


# do we want a custom user model?
# the default user model just has fields that we may or may not want
# https://docs.djangoproject.com/en/6.1/topics/auth/customizing/#specifying-a-custom-user-model
# reference for the default model is here:
# https://docs.djangoproject.com/en/6.1/ref/contrib/auth/#django.contrib.auth.models.User
# notably, the envisioned use case has a user whose login username may not be
# the same as the display name they'd like to be credited under
# would also be useful to have links to their social media and the like
# this could also be handled with an intermediary Author model?
# for now I'm going to go with that


# AuthorProfiles are bound to a specific user for now
# there may be a reason to make this not the case later, but for now,
# this feels like a good choice
class AuthorProfile(models.Model):
    display_name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_link = models.EmailField(null=True)
    website_link = models.URLField(null=True)
    bluesky_link = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)
