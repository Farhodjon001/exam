from django.shortcuts import render
from rest_framework import generics
from .models import Customer, RepairType, RepairRequest
from .serializers import CustomerSerializer, RepairTypeSerializer, RepairRequestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class RepairTypeList(generics.ListCreateAPIView):
    queryset = RepairType.objects.all()
    serializer_class = RepairTypeSerializer

class RepairRequestList(generics.ListCreateAPIView):
    queryset = RepairRequest.objects.all()
    serializer_class = RepairRequestSerializer

class RepairRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RepairRequest.objects.all()
    serializer_class = RepairRequestSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# class RepairRequestsByCustomer(APIView):
#     def get(self, request, customer_id):
#         try:
#             repair_requests = RepairRequest.objects.filter(customer_id=customer_id)
#             serializer = RepairRequestSerializer(repair_requests, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except RepairRequest.DoesNotExist:
#             return Response({"msg": "Customer has no repair requests."}, status=status.HTTP_404_NOT_FOUND)

class RepairRequestsByCustomer(APIView):
    def get(self, request):
        customer_id = request.query_params.get('customer_id')

        if customer_id is None:
            return Response({"msg": "Enter customer id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            repair_requests = RepairRequest.objects.filter(customer_id=customer_id)
            serializer = RepairRequestSerializer(repair_requests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RepairRequest.DoesNotExist:
            return Response({"msg": "NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)

class RepairRequestsByRepairType(APIView):
    def get(self, request):
        repair_type_id = request.query_params.get('repair_type_id')

        if not repair_type_id:
            return Response({"msg": "Enter repair id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            repair_requests = RepairRequest.objects.filter(repair_type_id=repair_type_id)
            serializer = RepairRequestSerializer(repair_requests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RepairRequest.DoesNotExist:
            return Response({"msg": "NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)
