from django.http import JsonResponse
from currencies.models import Currency

def get_currency_rate(request):
    charcode = request.GET.get('charcode')
    date = request.GET.get('date')
    currency = Currency.objects.filter(charcode=charcode, date=date).first()
    if currency:
        data = {
            'charcode': currency.charcode,
            'date': str(currency.date),
            'rate': float(currency.rate)
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Currency not found'}, status=404)

