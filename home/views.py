from django.shortcuts import render, redirect , get_object_or_404
from home.models import contactFrom
from datetime import datetime
from .models import Notice
from django.utils.dateparse import parse_date
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
# For PDF
from io import BytesIO
from xhtml2pdf import pisa


#Home Page
def index(request):
    return render(request, 'Pages/index.html')

#Contact Us Page
def contactus(request):
    success = False  # flag for popup

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')

        # Saving to Database
        contact = contactFrom(
            name=name,
            email=email,
            phone=phone,
            comment=comment,
            date=datetime.today()
        )
        contact.save()

        success = True  # trigger popup in template

    return render(request, 'Pages/contactUs.html', {"success": success})

#About Us Page
def about(request):
    return render(request, 'Pages/about.html')

#Academics Page
def academics(request):
    return render(request, 'Pages/academics.html')


    #Admissions

#Admission Page
def admissions(request):
    return render(request, 'Pages/admissions.html')


    #Campus Life

#Campus Life Page
def campuslife(request):
    return render(request, 'Pages/campusLife.html')

#Dashboard Page
def dashboard(request):
    return render(request, 'Pages/dashboard.html')

#Write Notice Page

def writenotice(request):
    success = False
    notice = None   # yahan object rakhenge

    if request.method == "POST":
        subject = request.POST.get("subject")
        content = request.POST.get("content")

        # Checkbox list handle karna
        to_list = request.POST.getlist("to_list")
        copy_list = request.POST.getlist("copy_list")

        # Convert list into string for saving
        to_str = ", ".join(to_list)
        copy_str = ", ".join(copy_list)

        # Save to DB and store object
        notice = Notice.objects.create(
            subject=subject,
            content=content,
            to_list=to_str,
            copy_list=copy_str
        )

        success = True  # trigger popup in template

    return render(
        request,
        "Pages/writenotice.html",
        {"success": success, "notice": notice}  # 👈 yahan model object bhejna hai
    )

# Full notice page
def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    return render(request, "Pages/detailed-notice.html", {"notice": notice})



# Circular Page
def circulars(request):
    notices = Notice.objects.all().order_by("-created_at")

    # Filters
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    to_filter = request.GET.get("to_filter")

    if start_date:
        notices = notices.filter(created_at__date__gte=parse_date(start_date))
    if end_date:
        notices = notices.filter(created_at__date__lte=parse_date(end_date))
    if to_filter:
        notices = notices.filter(to_list__icontains=to_filter)

    return render(request, "Pages/circular.html", {"notices": notices})

#Circular Page API for JSON Response



def circulars_api(request):
    # Fetch all notice
    notices = Notice.objects.all().order_by("-created_at")

    data = []
    for notice in notices:
        data.append({
            "id": notice.id,
            "subject": notice.subject,
            "content": notice.content,
            "to_list": notice.to_list,
            "copy_list": notice.copy_list,
            "created_at": notice.created_at.strftime("%d %B %Y, %I:%M %p"),
        })

    return JsonResponse(data, safe=False)



# Download notice as PDF
def notice_download(request, pk):
    notice = get_object_or_404(Notice, pk=pk)

    # HTML template -> string
    html = render_to_string("notice_pdf.html", {"notice": notice})

    # Convert to PDF
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="notice_{notice.id}.pdf"'

    pisa_status = pisa.CreatePDF(
        html, dest=response, encoding="UTF-8"
    )

    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)

    return response
