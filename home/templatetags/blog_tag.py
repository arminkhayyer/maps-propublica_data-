from django import template
import datetime



def id(request):
    navigate_id = request.session['navigate.id']
    return  navigate_id - 1

register = template.Library()


#@register.filter(name='one_more')
#def one_more(fig, i):
 #   return fig, i

#@register.filter
#def employee_list(department_pk):
 #   depart = Departments.objects.get(pk = department_pk)
  #  job= Jobs.objects.filter(department=depart)
   # emp_list = Employee.objects.filter(job=job)
    #return emp_list


@register.filter
def numberofrepublic(data, state):
    for i in data:
        print(i)
    return data
