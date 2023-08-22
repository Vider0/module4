from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Advertisement(models.Model):

    # небольшое текстовое поле
    title = models.CharField("Заголовок", max_length=128)

    # описание
    # большое текстовое поле
    description = models.TextField("Описание")

    # цена
    # число с фиксированной точностью
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    # уместен ли торг
    # логическое значение
    auction = models.BooleanField("Торг", help_text="Отметьте, если хотите торговаться")

    # дата создания
    created_at = models.DateTimeField(auto_now_add=True)

    # дата изменения
    updated_at = models.DateTimeField(auto_now=True)
    
    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone

        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.strftime("%H:%M:%S")
            return format_html("<span style='color:green; font-wight:bold;'> Сегодня в {}</span>", created_time)


        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone

        if self.created_at.date() == timezone.now().date():
            updated_time = self.created_at.strftime("%H:%M:%S")
            return format_html("<span style='color:red; font-wight:bold;'> Сегодня в {}</span>", updated_time)


        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
    # изображение

    # адрес

    # рейтинг продавца

    # похожие товары

    # кантакты продавца