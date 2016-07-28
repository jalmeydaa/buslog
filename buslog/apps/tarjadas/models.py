# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from pygments.lexers import get_all_lexers,get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Chofer(models.Model):
	nombre = models.CharField('Nombre',max_length=100)
	owner = models.ForeignKey(User, related_name='choferes',null=True)
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
	highlighted = models.TextField()

	class Meta:
		verbose_name='Chofer'
		verbose_name_plural='Choferes'

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		"""
		Use the `pygments` library to create a highlighted HTML
		representation of the code snippet.
		"""
		lexer = get_lexer_by_name(self.language)
		linenos = self.linenos and 'table' or False
		options = self.nombre and {'nombre': self.nombre} or {}
		formatter = HtmlFormatter(style=self.style, linenos=linenos,full=True, **options)
		self.highlighted = highlight(self.code, lexer, formatter)
		super(Chofer, self).save(*args, **kwargs)


class Carga(models.Model):
	descripcion = models.TextField('Descripcion')

	class Meta:
		verbose_name='Carga'
		verbose_name_plural='Cargas'

	def __str__(self):
		return self.descripcion


class Camion(models.Model):
	placa = models.CharField('Placa',max_length=50)
	chofer = models.OneToOneField(Chofer,related_name='camion_chofer')
	cargas = models.ManyToManyField(Carga,related_name='camion_cargas')


	class Meta:
		verbose_name=u'Camión'
		verbose_name_plural='Camiones'

	def __str__(self):
		return '%s - C: %s' % (self.placa, self.chofer)