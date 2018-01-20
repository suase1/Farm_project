from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, FormView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from farmapp.models import Order
from .forms import OrderForm, DateSearchForm
from django.utils import timezone
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from enum import Enum

class grade(Enum):
    A = 30000
    B = 20000
    C = 10000

class delivery(Enum):
    onebox = 3000
    twobox = 4000

def caculate_price(order):
    if order.grade == 'A':
        grade_price = grade.A.value
    elif order.grade == 'B':
        grade_price = grade.B.value
    else: grade_price = grade.C.value
    if order.quantity == 1 :
        delivery_price = delivery.onebox.value
    else: delivery_price = delivery.twobox.value
    total_price = grade_price + delivery_price
    return total_price


def OrderFV(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.price = caculate_price(order)
            order.order_date = timezone.now()
            order.save()
            return redirect('ordercheck', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'farmapp/order.html', {'form': form})



def OrderCheck(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'farmapp/ordercheck.html', {'order': order})

def OrderEdit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.price = caculate_price(order)
            order.order_date = timezone.now()
            order.save()
            return redirect('ordercheck', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'farmapp/orderedit.html', {'form': form})

class OrderConfirm(TemplateView):
    template_name = 'farmapp/orderconfirm.html'



class OrderList(LoginRequiredMixin, FormView):
    form_class = DateSearchForm
    template_name = 'farmapp/orderlist.html'
    def form_valid(self, form):
        schDate = '%s' % self.request.POST['search_date']

        # order_list = Order.objects.filter(farmer_phone__iexact=str(self.request.user).strip()).filter(order_date__lte=schDate)
        order_list = Order.objects.filter(farmer_phone__iexact=str(self.request.user).strip()).filter(order_date__contains=schDate)

        orderlist = {}
        orderlist['farmer_number'] = str(self.request.user).strip()
        orderlist['form'] = form
        orderlist['search_date'] = schDate
        orderlist['object_list'] = order_list

        # if self.request.POST['search_date']:
        #     search_date = '%s' % self.request.POST['search_date']
        # order_list = Order.objects.filter(farmer_phone__iexact=str(self.request.user).strip()).filter(order_date__lte=search_date).order_by('-order_date')
        return render(self.request, self.template_name, orderlist)


# class OrderList(LoginRequiredMixin, ListView):
#     template_name = 'farmapp/orderlist.html'
#
#     def get_queryset(self):
#         search_date = timezone.now()
#         return Order.objects.filter(farmer_phone__iexact=str(self.request.user).strip()).filter(order_date__lte=search_date).order_by('-order_date')



# def OrderList(request):
#     farmer_phone = request.user.get_username()
#     orders = Order.objects.filter(farmer_phone__iexact=farmer_phone).order_by('-order_date')
#     return render(request, 'farmapp/orderlist.html', {'orders': orders})


#
# class OrderFV(CreateView):
#     model = Order
#     template_name = 'farmapp/order.html'
#     form_class = OrderForm
#     success_url = 'http://127.0.0.1:8000/order/check/1/'
#
# class OrderCheck(DetailView):
#     template_name = 'farmapp/ordercheck.html'
#     queryset = Order.objects.all()

# class OrderFV(FormView):
#     template_name = 'farmapp/order.html'
#     form_class = OrderForm
#     success_url = 'http://127.0.0.1:8000/order/check/'
#
#
# def OrderCheck(request):
#     order = request.POST
#     return render(request, 'farmapp/ordercheck.html', {'order':order})
#
#
#
# def OrderConfirm(request):
#     order2 = request.POST
#     return render(request, 'farmapp/orderconfirm.html', {'order2':order2})

# class OrderLV(User, ListView):
#     # username = User.get_username()
#     # farmer_phone='01037837071'
#     farmer_phone = request.POST.get('username','')
#
#     queryset = Order.objects.filter(farmer_phone__iexact=farmer_phone).order_by('order_date')
#     template_name = 'farmapp/orderlist.html'
#     context_object_name = 'orders'
#     paginate_by = 20
