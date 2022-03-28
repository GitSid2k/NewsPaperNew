from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from django.template.loader import render_to_string
from .models import Post


@receiver(post_save, sender=Post)
def send_sub_mail(sender, instance, created, **kwargs):
    current_cats = instance.postCategory.all()
    print(current_cats)
    subs_list = []
    cat_list = []
    for cat in current_cats:
        cat_list.append(cat.categoryName)
        subs_list.extend([user for user in cat.subscribers.all()])
    print(subs_list)
    # рассылка на все категории из новости
    cat_mess = ",".join(cat_list)
    print(cat_mess)
    for sub_user in subs_list:

        html_content = render_to_string(
            'news_update_mail.html', {'user': sub_user, 'cat_mess': cat_mess, 'post': instance})
        # instance - только созданный экземпляр класса post
        if created:
            msg = EmailMultiAlternatives(
                subject=f'Здравствуй, Новая статья из категории(-ий){cat_mess}',
                from_email='projects-mail-sf@yandex.ru',
                to=[sub_user.email]
            )

            msg.attach_alternative(html_content, 'text/html')
            msg.send()