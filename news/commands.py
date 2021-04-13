from news.models import Author, Category, Post, PostCategory, Comment
from django.contrib.auth.models import User
from django.db import models

# Создание пользователей
user1 = User.objects.create_user(username='User1', email='user1@user1',
                                 password='user1password')
user2 = User.objects.create_user(username='User2', email='user2@user2',
                                 password='user2password')

# Создание моделей Author
author1 = Author.objects.create(author=user1)
author2 = Author.objects.create(author=user2)

# Добавление категорий новостей Category.
category1 = Category.objects.create(category_name='Спорт')
category2 = Category.objects.create(category_name='Политика')
category3 = Category.objects.create(category_name='Наука')
category4 = Category.objects.create(category_name='Криминал')

# Добавить 2 статьи и 1 новость.
article1 = Post.objects.create(author=author1,
                               post_type=Post.article,
                               post_title='Заголовок статьи 1',
                               post_content='Текст статьи 1',
                               )
article2 = Post.objects.create(author=author1,
                               post_type=Post.article,
                               post_title='Заголовок статьи 2',
                               post_content='Текст статьи 2',
                               )
news1 = Post.objects.create(author=author2,
                            post_type=Post.news,
                            post_title='Заголовок новости 1',
                            post_content='Текст новости 1',
                            )

# Присвоение категории.
article1.post_category.add(category1)
article1.post_category.add(category2)
article2.post_category.add(category3)
news1.post_category.add(category4)

# Создание комментариев.
comment1 = Comment.objects.create(post=article1,
                                  user=user1,
                                  comment_text='Текст комментария 1')
comment2 = Comment.objects.create(post=article1,
                                  user=user2,
                                  comment_text='Текст комментария 2')
comment3 = Comment.objects.create(post=article2,
                                  user=user1,
                                  comment_text='Текст комментария 3')
comment4 = Comment.objects.create(post=news1,
                                  user=user2,
                                  comment_text='Текст комментария 4')

# Функции like() и dislike() для этих объектов.
comment1.like()
comment2.like()
comment3.like()
comment4.like()
comment1.like()
comment2.like()
comment3.like()
comment1.like()
comment2.like()
comment1.like()
comment1.dislike()
comment4.dislike()
comment3.dislike()
comment1.dislike()
article1.like()
article1.like()
article1.like()
article1.like()
article1.like()
article2.like()
article2.like()
article2.like()
news1.dislike()

# Обновление ревйтинга пользователей.
author1.update_rating()
author2.update_rating()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и
# возвращая поля первого объекта).

# Вывести дату добавления, username автора, рейтинг, заголовок и превью
# лучшей статьи, основываясь на лайках/дислайках к этой статье.

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.


Post.objects.all().values('author', 'post_title')
Post.objects.filter(author=author2)
Post.objects.filter(post_title='Заголовок статьи 1').values('author')
Comment.objects.filter(post=article1).values('comment_text')
Comment.objects.filter(comment_text='Текст комментария 2').values('comment_rating')
Author.objects.filter(id=1)
Author.objects.all().values('author', 'id')
Comment.objects.all().values('post', 'user')