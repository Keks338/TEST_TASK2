from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CashFlowRecord, Status, Type, Category, SubCategory
from .forms import CashFlowRecordForm, StatusForm, CategoryForm, TypeForm, SubCategoryForm

def cashflow_create_view(request):
    if request.method == 'POST':
        form = CashFlowRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Запись успешно создана")
            return redirect('cash:cashflow_list')
    else:
        form = CashFlowRecordForm()
    return render(request, 'cashflow_form.html', {'form': form})

def cashflow_update_view(request, pk):
    record = get_object_or_404(CashFlowRecord, pk=pk)
    if request.method == 'POST':
        form = CashFlowRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Запись успешно обновлена")
            return redirect('cash:cashflow_list')
    else:
        form = CashFlowRecordForm(instance=record)
    return render(request, 'cashflow_form.html', {'form': form})

def cashflow_delete_view(request, pk):
    record = get_object_or_404(CashFlowRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, "Запись удалена")
        return redirect('cash:cashflow_list')
    return render(request, 'cashflow_confirm_delete.html', {'object': record})

def directories_manage_view(request):
    if request.method == 'POST':
        status_form = StatusForm(request.POST, prefix='status')
        type_form = TypeForm(request.POST, prefix='type')
        category_form = CategoryForm(request.POST, prefix='category')
        subcategory_form = SubCategoryForm(request.POST, prefix='subcategory')

        if status_form.is_valid():
            status_form.save()
            messages.success(request, "Статус добавлен")
            return redirect('cash:directories_manage')

        if type_form.is_valid():
            type_form.save()
            messages.success(request, "Тип добавлен")
            return redirect('cash:directories_manage')

        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Категория добавлена")
            return redirect('cash:directories_manage')

        if subcategory_form.is_valid():
            subcategory_form.save()
            messages.success(request, "Подкатегория добавлена")
            return redirect('cash:directories_manage')
    else:
        status_form = StatusForm(prefix='status')
        type_form = TypeForm(prefix='type')
        category_form = CategoryForm(prefix='category')
        subcategory_form = SubCategoryForm(prefix='subcategory')

    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    return render(request, 'directories_manage.html', {
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
        'status_form': status_form,
        'type_form': type_form,
        'category_form': category_form,
        'subcategory_form': subcategory_form
    })

def cashflow_list_view(request):
    records = CashFlowRecord.objects.all()
    return render(request, 'cashflow_list.html', {'records': records})