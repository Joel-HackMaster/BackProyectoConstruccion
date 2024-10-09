from django.db import models
from apps.Base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.

class CategoryService(BaseModel):
    description = models.CharField('Descripcion', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoria de Servicio'
        verbose_name_plural = 'Categorias de servicio'

    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'CategoriaServicio'
    
class Indicator(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Indicador de ofertas'
        verbose_name_plural = 'Indicadores de oferta'

    def __str__(self):
        return f'Oferta del servicio: {self.descount_value}%'
    
    class Meta:
        db_table = 'Indicator'

class ImagesService(BaseModel):
    description= models.CharField('Nombre Servicio', max_length=150, unique=True, blank=False, null=False)
    image = models.CharField('Imagen de servicio', max_length=300, blank=False, null=False, default='')
    historical= HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    
class Service(BaseModel):
    name = models.CharField('Nombre de servicio', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripcion del servicio', blank=False, null=False)
    image = models.CharField('Imagen de servicio', max_length=300, blank=False, null=False, default='')
    category_service = models.ForeignKey(CategoryService, on_delete=models.CASCADE, verbose_name='Categoria de servicio', null=False)
    indicator_service = models.ForeignKey(Indicator, on_delete=models.SET_NULL,verbose_name='Indicador de descuento', null=True, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Service."""
        db_table = 'Servicios'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        """Unicode representation of service."""
        return self.name
        





