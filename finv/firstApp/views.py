from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from firstApp.models import Employees,Craft
# Create your views here.


def index(request):
    return render(request,'firstApp/login.html')

def main(request):
    data = Employees.objects.all()
    data2 = Craft.objects.all()
    id_number = format(110, '05d')
    view_data = {"id_number": data,"id": data2,"test_is":id_number}

    
    return render(request,'firstApp/dashboard.html', view_data)

def create_employee(request):

    
    
    count = Employees.objects.all().count()

    if count == 0 :
        id_number = 1
        id_number = format(id_number, '08d')
        if request.method == 'POST':    
            first_name = request.POST['first_name']
            middle_name = request.POST['middle_name']
            last_name = request.POST['last_name']
            gender = request.POST['gender']
            emp_craft = request.POST['emp_craft']
            date_of_birth = request.POST['date_of_birth']
            address =request.POST['address']
            nationality = request.POST['nationality']
            religion = request.POST['religion']
            date_hired = request.POST['date_hired']
            educational_attainment = request.POST['educational_attainment']
            passport_no = request.POST['passport_no']
            residencial_id= request.POST['residencial_id']
            res_type= request.POST['res_type']
            res_id_date_issued= request.POST['res_id_date_issued']
            res_id_date_expires= request.POST['res_id_date_expires']    
            monthly_basic_salary= request.POST['monthly_basic_salary']
            add = Employees(id_number=id_number,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                gender=gender,
                emp_craft=emp_craft,
                date_of_birth=date_of_birth,
                address=address,
                nationality=nationality,
                religion=religion,
                date_hired=date_hired,
                educational_attainment=educational_attainment,
                passport_no=passport_no,
                residencial_id=residencial_id,
                res_type=res_type,
                res_id_date_issued=res_id_date_issued,
                res_id_date_expires=res_id_date_expires,
                monthly_basic_salary=monthly_basic_salary,
            )
            add.save()
            message = 'success'
        
        else:
            message = 'error'
    else:
        id_number = count+1 
        id_number = format(id_number, '08d')
        

        if request.method == 'POST':
            first_name = request.POST['first_name']
            middle_name = request.POST['middle_name']
            last_name = request.POST['last_name']
            gender = request.POST['gender']
            emp_craft = request.POST['emp_craft']
            date_of_birth = request.POST['date_of_birth']
            address =request.POST['address']
            nationality = request.POST['nationality']
            religion = request.POST['religion']
            date_hired = request.POST['date_hired']
            educational_attainment = request.POST['educational_attainment']
            passport_no = request.POST['passport_no']
            residencial_id= request.POST['residencial_id']
            res_type= request.POST['res_type']
            res_id_date_issued= request.POST['res_id_date_issued']
            res_id_date_expires= request.POST['res_id_date_expires']    
            monthly_basic_salary= request.POST['monthly_basic_salary']
            add = Employees(id_number=id_number,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                gender=gender,
                emp_craft=emp_craft,
                date_of_birth=date_of_birth,
                address=address,
                nationality=nationality,
                religion=religion,
                date_hired=date_hired,
                educational_attainment=educational_attainment,
                passport_no=passport_no,
                residencial_id=residencial_id,
                res_type=res_type,
                res_id_date_issued=res_id_date_issued,
                res_id_date_expires=res_id_date_expires,
                monthly_basic_salary=monthly_basic_salary,
            )
            add.save()
            message = 'success'
            
        else:
            message = 'error'
            
    data = {'message':message}
    return render(request,'firstApp/dashboard/create_employees.html', data)