# from django.shortcuts import render
# from .forms import *
# from django.http import JsonResponse
# from collections import defaultdict
# from django.shortcuts import get_object_or_404, redirect
# def rezerve_view(request):
#     return render(request,'rezerve_page.html')
# def admin_panel_view(request):
#     if request.method=="GET":
#         return render(request,'admin_panel/index.html')
#
#
#
# def add_plan_salon_ejtamaat_view (request):
#     if request.method=="GET":
#         AvailableTime_pure_form = AvailableTime_form()
#         available_time_object=AvailableTime.objects.all().order_by('id')
#         # group the period of time
#         # defaultdict(list) : create pure dictonary , that if dont have the key we searched create that key
#         # and add value for this key
#         grouped_periods = defaultdict(list)
#         for period in available_time_object:
#             grouped_periods[str(period.day_of_week)].append(period)
#         print(grouped_periods)
#         return render(request,'admin_panel/planing_page.html',{"AvailableTime_pure_form":AvailableTime_pure_form,"grouped_periods": grouped_periods})
#     # add and edit plan by ajax
#     elif request.method == "POST":
#         form = AvailableTime_form(request.POST)
#
#         if form.is_valid():
#             day_number = request.POST.get("day_of_week")
#
#             new_time = form.save(commit=False)
#             new_time.day_of_week = int(day_number)
#             new_time.Hall_id = 2  # 👈 اینجا هال رو 2 گذاشتیم
#             new_time.save()
#
#             return JsonResponse({"status": "success","id": new_time.id,"day": new_time.day_of_week,"start": new_time.start_time.strftime("%H:%M"),
# "end": new_time.end_time.strftime("%H:%M"),})
#
#         return JsonResponse({"status": "error", "errors": form.errors})
#
# def delete_available_time(request, pk):
#     obj = get_object_or_404(AvailableTime, pk=pk)
#
#     if request.method == "POST":
#         obj.delete()
#
#     return redirect('reservation:add_plan_salon')
