from django.shortcuts import render
from django.db.models import Sum
from Countapp.models import Record, Certification
from datetime import datetime


def record_list(request):
    month = request.GET.get('month', datetime.now().month)
    year = request.GET.get('year', datetime.now().year)
    user = request.user  # 현재 사용자의 기록만 가져오기

    # Filtering records by selected month and year
    records = Record.objects.filter(user=user, create_at__year=year, create_at__month=month)

    # Aggregating records by day
    daily_records = records.values('create_at__date').annotate(
        total_distance=Sum('distance'),
        total_time=Sum('msec')
    ).order_by('create_at__date')
    total_distance = sum(record['total_distance'] for record in daily_records)
    records_with_certifications = []
    for record in daily_records:
        date = record['create_at__date']
        # certification =Certification.objects.filter(record__user=user, record__create_at__date=date).order_by(
        #     '-create_at')
        certification = Certification.objects.filter(user=user).order_by('-create_at')
        print(certification)
        second_latest_certification = certification[1]
        #print(second_latest_certification.walk_image.url)
        records_with_certifications.append({
            'date': date,
            'total_distance': record['total_distance'],
            'total_time': record['total_time'],
            'certification': second_latest_certification
        })
    # Adding certifications to the records
    # records_with_certifications = [
    #     {
    #         'date': record['create_at__date'],
    #         'total_distance': record['total_distance'],
    #         'total_time': record['total_time'],
    #
    #     } for record in daily_records
    # ]

    years = range(2020, datetime.now().year + 1)

    context = {
        'month': int(month),
        'year': int(year),
        'total_distance': total_distance,
        'records': records_with_certifications,
        'years': years,
    }

    return render(request, 'historyapp/record_list.html', context)
