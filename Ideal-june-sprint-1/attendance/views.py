from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Attendance
from .serializers import AttendanceSerializer
from django.utils import timezone

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_in(request):
    user = request.user
    today = timezone.now().date()

    # Prevent multiple check-ins in one day
    if Attendance.objects.filter(user=user, date=today).exists():
        return Response({'message': 'Already checked in today.'}, status=400)

    attendance = Attendance.objects.create(user=user)
    serializer = AttendanceSerializer(attendance)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_out(request):
    user = request.user
    today = timezone.now().date()

    try:
        attendance = Attendance.objects.get(user=user, date=today)
    except Attendance.DoesNotExist:
        return Response({'message': 'No check-in record found for today.'}, status=400)

    if attendance.check_out:
        return Response({'message': 'Already checked out.'}, status=400)

    attendance.check_out = timezone.now()
    attendance.save()
    serializer = AttendanceSerializer(attendance)
    return Response(serializer.data)
