from django.contrib.auth import forms, get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django import forms
from django.shortcuts import render, redirect
from django.views import generic, View
from django.http.response import HttpResponseRedirect, HttpResponse

from .tokens import account_activation_token
from posts.models import Post, Comment

# Create your views here.
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

@login_required()
class ProfileView(generic.TemplateView):

    def profile(request, username):
        all_posts = Post.objects.filter(author = request.user).order_by('pub_date')
        user_details = User.objects.get(pk=request.user.pk)
        
        context = {
            'all_posts': all_posts,
            'user_details': user_details,
        }
        
        return render(request, 'accounts/profile.html', context=context)



def registerView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # to_email = form.cleaned_data.get('email')
            user = form.save()
            # user.is_Active = False
            user.save()
            # current_site = get_current_site(request)
            # mail_subject = 'BSPForum: Verify your email'
            # message = render_to_string(['activate_email.html'], {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.username)),
            #     'token': account_activation_token.make_token(user)
            # })
            # to_email = form.cleaned_data.get('email')
            # send_mail(mail_subject, message, 'youremail', [to_email])
            return redirect('login_url')
            # return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# def activateUser(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         # return redirect('home')
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')