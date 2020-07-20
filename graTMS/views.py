from graTMS.models import Complaint
from django.http import HttpResponse
from django.core.files.base import ContentFile
import re
from PIL import Image
from io import BytesIO
import base64
from django.shortcuts import render
from django.views.generic.list import ListView
from .filters import ComplaintFilter

# Create your views here.


def home(request):
    complaint = Complaint.objects.filter().order_by('-date')
    myFilter = ComplaintFilter()
    context = {
        'complaint': complaint,
        'myFilter': myFilter,
    }
    return render(request, 'graTMS/index.html', context)


def add_coplaint(request):
    office = request.POST.get('office')
    room = request.POST.get('room')
    complaint = request.POST.get('complaint')
    additional_Info = request.POST.get('additional_Info')
    solution = request.POST.get('solution')
    status = request.POST.get('status')
    signatory = request.POST.get('signatory')
    signature = request.POST.get('signature')
    format, imgstr = signature.split(',')
    ext = format.split('/')[1]
    data = ContentFile(base64.b64decode(
        imgstr), name='iVBORw0KGgoAAAANSUhEUgAAASwAAADICAYAAABS39xVAAAgAElEQVR4Xu2dCfR321jHH7lEkpIMmYpEpsrNkEulqwzpFuumMlWiDEkZolLmLkIlaUKDkEQjEa3+.' + ext)
    data = Complaint.objects.create(office=office, room=room, complaint=complaint, additional_Info=additional_Info,
                                    solution=solution, status=status, signatory=signatory, signature=data)
    return render(request, 'graTMS/modal.html')


def viewCompliant(request, id):
    comv = Complaint.objects.get(id=id)
    context = {
        'comv': comv,
    }
    return render(request, 'graTMS/modal.html', context)


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True
        books = Book.objects.all()
        data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string(
            'books/includes/partial_book_delete.html', context, request=request)
    return JsonResponse(data)
