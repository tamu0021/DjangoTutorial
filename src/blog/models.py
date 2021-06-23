from django.db import models
from django.utils import timezone

class Post(models.Model):
    # 多対一の関係を作成する。
    # 今回は、auth.Userから複数のPostがある関係
    # on_deleteには削除の方法を指定する。
    # models.CASCADEを指定したことにより、親(auth.User)のデータが削除された際に子(Post)のデータも削除する。
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
