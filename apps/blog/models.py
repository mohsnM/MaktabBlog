# Core imports.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=128)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    content = models.TextField(_("Content"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True)
    draft = models.BooleanField(_("Draft"), default=True, db_index=True)
    image = models.ImageField(_("image"), upload_to='posts/images/', null=True, blank=True)
    category = models.ForeignKey(
        "Category",
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='posts',
        related_query_name='posts',
    )
    author = models.ForeignKey(
        User, verbose_name=_("Author"), on_delete=models.CASCADE, related_name="posts", related_query_name="children"
    )

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-publish_time']

    def __str__(self):
        return self.title

    def create_setting(self, comment=True, author=True, allow_discussion=False):
        return PostSetting.objects.create(post=self, comment=comment, author=author, allow_discussion=allow_discussion)

    def get_comments(self):
        comments = []
        for com in self.comments.filter(parent=None):
            comments.append((com, com.children.all()))
        return comments

    @property
    def comment_count(self):
        q = self.comments.all()
        return q.count()

    @property
    def convert_publish_date(self):
        converted_date = f"{self.publish_time.day} - {self.publish_time.month} - {self.publish_time.year}"
        return converted_date

    @property
    def convert_create_date(self):
        converted_date = f"{self.create_at.day} - {self.create_at.month} - {self.create_at.year}"
        return converted_date


class PostSetting(models.Model):
    post = models.OneToOneField(
        "Post", verbose_name=_("post"), on_delete=models.CASCADE, related_name='setting', related_query_name='setting'
    )
    comment = models.BooleanField(_("comment"), default=True)
    author = models.BooleanField(_("author"), default=False)
    allow_discussion = models.BooleanField(_("allow discussion"), default=False)

    class Meta:
        verbose_name = _("PostSetting")
        verbose_name_plural = _("PostSettings")


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        related_query_name='children',
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.slug

    def get_children(self):
        return self.children.all()


class CommentLike(models.Model):
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    comment = models.ForeignKey(
        'blog.Comment',
        verbose_name=_('Comment'),
        on_delete=models.CASCADE,
        related_name="comment_like",
        related_query_name="comment_like",
    )
    condition = models.BooleanField(_("Condition"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        unique_together = [['author', 'comment']]
        verbose_name = _("CommentLike")
        verbose_name_plural = _("CommentLikes")

    def __str__(self):
        return str(self.condition)


class Comment(models.Model):
    content = models.TextField(_("Content"))
    post = models.ForeignKey(
        "Post",
        verbose_name=_("Post"),
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comments',
    )
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(_("confirm"), default=True)
    parent = models.ForeignKey(
        'self',
        verbose_name=_('parent'),
        null=True,
        on_delete=models.CASCADE,
        blank=True,
        related_name='children',
        related_query_name='child',
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-create_at']

    def __str__(self):
        return self.content[:10]

    @property
    def like_count(self):
        q = CommentLike.objects.filter(comment=self, condition=True)
        return q.count()

    @property
    def dis_like_count(self):
        q = CommentLike.objects.filter(comment=self, condition=False)
        return q.count()

    @property
    def convert_create_date(self):
        converted_date = f"{self.create_at.day} - {self.create_at.month} - {self.create_at.year}"
        return converted_date
