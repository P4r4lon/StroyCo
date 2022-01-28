from django.db import models
from django.utils import timezone


class Employer(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    position = models.CharField(max_length=20, verbose_name='Должность')
    address = models.CharField(max_length=50, verbose_name='Адрес офиса')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    quantityOfDeals = models.CharField(max_length=5, verbose_name='Количество сделок')

    def publish(self):
        self.save()

    def __str__(self):
        str = self.position + " " + self.name
        return str

    def get_absolute_url(self):
        return f'/employers/{self.id}'

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


class CounterAgent(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    passport = models.CharField(max_length=10, verbose_name='Пасспортные данные')
    address = models.CharField(max_length=100, verbose_name='Адрес регистрации')
    date_of_birth = models.DateTimeField(default=timezone.now, verbose_name='Дата рождения')

    def publish(self):
        self.save()

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return f'/counteragents/{self.id}'

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Invoice(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер счёта')
    sum = models.IntegerField(default=25, verbose_name='Сумма к оплате')
    dateOfPayment = models.DateTimeField(default=timezone.now, verbose_name='Дата оплаты')
    dateOfIssue = models.DateTimeField(default=timezone.now, verbose_name='Дата выставления счёта')

    def publish(self):
        self.save()

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return f'/invoices/{self.id}'

    class Meta:
        verbose_name = 'Cчёт'
        verbose_name_plural = 'Счета'


class Apartment(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер квартиры')
    address = models.CharField(max_length=50, verbose_name='Адрес дома')
    floor = models.CharField(max_length=2, verbose_name='Этаж')
    square = models.IntegerField(default=5, verbose_name='Площадь')
    price = models.IntegerField(default=25, verbose_name='Цена')
    status = models.BooleanField(default=False, verbose_name='Продана')

    def publish(self):
        self.save()

    def __str__(self):
        str = self.address + " " + self.number
        return str

    def get_absolute_url(self):
        return '/apartments_search/-price'

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class Deal(models.Model):
    contract = models.IntegerField(default=0, verbose_name='Номер договора')
    price = models.IntegerField(default=0, verbose_name='Цена')
    dateOfReg = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации')
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='deal_manager',
                                 verbose_name='Менеджер')
    counteragent = models.ForeignKey(CounterAgent, on_delete=models.CASCADE, related_name='agent',
                                     verbose_name='Контрагент')
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice', verbose_name='Счёт')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apart', verbose_name='Квартира')
    dateOfCon = models.DateTimeField(default=timezone.now, verbose_name='Дата заключения')
    status_of_act = models.BooleanField(default=False, verbose_name='Статус акта приема-передачи')

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.contract)


    def get_absolute_url(self):
        return f'/deals/{self.id}'


    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
