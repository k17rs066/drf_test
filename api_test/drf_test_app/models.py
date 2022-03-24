from unicodedata import category, name
from django.db import models

# ユーザ情報を格納する
class User(models.Model):
    name = models.CharField(max_length=32)  # ユーザ名
    mail = models.EmailField()              # メールアドレス
    birth_day = models.DateField()          # 生年月日
    created_at = models.DateTimeField(auto_now_add=True) # 作成日時
    update_at = models.DateTimeField(auto_now=True)      # 更新日時
    
    
# お問合せフォームのデータを格納する
class Question(models.Model):
    title = models.CharField(max_length=128)    # タイトル
    question = models.TextField()               # 問い合わせ内容
    created_at = models.DateTimeField(auto_now_add=True) # 作成日時