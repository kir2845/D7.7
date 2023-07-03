import django_filters
from django_filters import FilterSet
from .models import New
from django.forms import SelectDateWidget
import datetime


# Создаем свой набор фильтров для модели New. FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewFilter(django_filters.FilterSet):
#    time_in = django_filters.NumberFilter(field_name='time_in', lookup_expr='date')
#    time_in__gt = django_filters.NumberFilter(field_name='time_in', lookup_expr='date__gt')



   class Meta:                    # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
       model = New
       fields = {                  # В fields мы описываем по каким полям модели будет производиться фильтрация.
           'name': ['icontains'],  # поиск по названию
          # 'time_in':['date__gt'],
           'time_in': ['date__gte'],
           'author': ['exact'],
           }
       widget = SelectDateWidget(
           empty_label = ("Choose Year", "Choose Month", "Choose Day"),
       )