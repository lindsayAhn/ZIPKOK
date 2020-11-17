from django.http import HttpResponseRedirect

from user.models import User


def update(request):
    user = User.objects.get(id=request.session['authUser']['id'])
    # 인증
    authuser = request.session.get('authUser')
    if authuser is None or user.id != authuser['id']:
        return HttpResponseRedirect('/')
    user.photo = request.POST['photo']
    user.name = request.POST['name']
    # user.gender = request.POST['gender']

    if request.POST['password'] != '':
        user.password = request.POST['password']
    user.save()


    # 수정정보 다시 가져오기
    # request.session['authUser'] = model_to_dict(user)
    request.session['authUser']['name'] = user.name

    return HttpResponseRedirect('/user/updateform?result=success')