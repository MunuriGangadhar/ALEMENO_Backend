from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer, Loan
from .serializers import CustomerSerializer, LoanSerializer

@api_view(['POST'])
def register(request):
    data = request.data
    approved_limit = round(36 * data['monthly_income'], -5)
    customer = Customer.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        phone_number=data['phone_number'],
        monthly_salary=data['monthly_income'],
        approved_limit=approved_limit,
    )
    return Response(CustomerSerializer(customer).data)

@api_view(['POST'])
def check_eligibility(request):
    customer_id = request.data['customer_id']
    loan_amount = request.data['loan_amount']
    interest_rate = request.data['interest_rate']
    tenure = request.data['tenure']

    try:
        customer = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

    # Perform credit score calculation and eligibility checks here...
    # Placeholder response:
    return Response({'approval': True, 'corrected_interest_rate': 10.0})
