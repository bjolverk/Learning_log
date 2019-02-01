from django.db import models

# Create your models here.

class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200, verbose_name = "Название темы")  # Перевод добавил я
    date_added = models.DateTimeField(auto_now_add=True)

    #  Чтобы заголовки отображались на русском
    class Meta:
        """Выводимое имя"""
        verbose_name = "Тему"
        verbose_name_plural = "Темы"

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Выводимое имя"""
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        """Возвращает строковое представление модели"""
        if len(self.text) >= 50:
            return self.text[:50] + "..."
        else:
            return self.text
