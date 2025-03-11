from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView

from mysite import settings

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm  # forms.pyのSignupFormを適用している
    template_name = "accounts/signup.html"  # ここに代入したhtmlが表示される
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]  # passwordではキーエラー
        user = authenticate(self.request, username=username, password=password)  # passwardはおかしい
        login(self.request, user)
        return response


class UserProfileView(TemplateView):
    template_name = "accounts/user_profile.html"

    def get_context_data(self, **kwargs):  # 動的なコンテキストを扱う
        context = super().get_context_data(**kwargs)  # 親クラスのメソッドを実行
        context["username"] = User.username  # 新しいデータの追加
        return context
