from django.shortcuts import redirect, render

from User.models import UserProfile
from Vlog.models import Vlog

# Create your views here.
def Vlog_written(request):
    return render(request,'Vlog/Vlog.html')

#////////////////////////////////////////////////////////////////////////////////////////////////


def add_vlog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user_id = request.POST['user_id']

        user = UserProfile.objects.get(id=user_id)

        vlog = Vlog.objects.create(
            title=title,
            content=content,
            user=user
        )
        vlog.save()

        return redirect('Vlog:vlog_list')

    users = UserProfile.objects.all() 
    return render(request, 'Vlog/add_vlog.html', {'users': users})

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def vlog_list(request):
    vlogs = Vlog.objects.all() 
    return render(request, 'Vlog/vlog_list.html', {'vlogs': vlogs})
