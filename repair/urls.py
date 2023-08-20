from django.urls import path
from .views import CustomerList, RepairTypeList, RepairRequestList, RepairRequestDetail,RepairRequestsByCustomer,RepairRequestsByRepairType

urlpatterns = [
    path('customers/', CustomerList.as_view()),
    path('repair/types/', RepairTypeList.as_view()),
    path('repair/requests/', RepairRequestList.as_view()),
    path('repair/requests/<int:pk>/', RepairRequestDetail.as_view()),
    path('customers/<int:customer_id>/repair_requests/',RepairRequestsByCustomer.as_view()),
    path('repair/requests/by_type/', RepairRequestsByRepairType.as_view())
]
