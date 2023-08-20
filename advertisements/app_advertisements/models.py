from django.db import models


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

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
    # изображение

    # адрес

    # рейтинг продавца

    # похожие товары

    # кантакты продавца