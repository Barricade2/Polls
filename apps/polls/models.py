from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

class Poll(models.Model):
    class Meta:
        db_table = 'poll'
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    title = models.CharField(_("Название"), max_length=256)
    plot = models.CharField(_("Описание"), max_length=512, blank=True)
    start_at = models.DateTimeField(_("Дата старта"), blank=True, null=True)
    end_at =  models.DateTimeField("Дата окончания", blank=True, null=True)
    is_published = models.BooleanField(_("Published"), default=True)

    def __str__(self):
        return '{}'.format(self.title)



class Question(models.Model):
    class Meta:
        db_table = 'question'
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    title = models.CharField(_("Название"), max_length=256, blank=True)
    plot = models.CharField(_("Описание"), max_length=512, blank=True)
    poll = models.ForeignKey(Poll, verbose_name=_("Опрос"), on_delete=models.CASCADE, related_name='poll', blank=True, null=True)
    class Type(models.TextChoices):
        INPUT = "Ввод", _("Ввод")
        ONE = "Один", _("Один")
        MANY = "Много", _("Много")
    type = models.CharField(_("Тип"), max_length=32, choices=Type.choices, blank=True)
    choice = models.ManyToManyField('Choice', verbose_name=_("Перечни"), blank=True)

    def __str__(self):
        return self.title



class Choice(models.Model):
    class Meta:
        db_table = 'сhoice'
        verbose_name = "Перечень"
        verbose_name_plural = "Перечни"

    text = models.CharField(verbose_name=_("Перечни"), max_length=256, blank=True)

    def __str__(self):
        return self.text


class UserChoiceID(models.Model):
    class Meta:
        db_table = 'myuser'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    poll = models.ForeignKey(Poll, verbose_name=_("Опрос"), on_delete=models.SET_NULL, blank=True, null=True)
    question = models.ForeignKey(Question, verbose_name=_("Вопрос"), on_delete=models.SET_NULL, blank=True, null=True)
    choice = models.ForeignKey(Choice, verbose_name=_("Выбор"), on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.uuid, self.choice)