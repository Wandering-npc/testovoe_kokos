import requests

from django.core.management.base import BaseCommand
from datetime import date

from currencies.models import Currency



class Command(BaseCommand):
    help = 'Обновление курса валют'

    def handle(self, *args, **kwargs):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            date_today = date.today()
            
            for charcode, value in data['Valute'].items():
                rate = value['Value']
                currency_rate, created = Currency.objects.get_or_create(charcode=charcode, date=date_today)
                currency_rate.rate = rate
                currency_rate.save()        
                
            self.stdout.write(self.style.SUCCESS('Курс валют обновлен'))
            
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при обновлении курса валют: {e}'))
