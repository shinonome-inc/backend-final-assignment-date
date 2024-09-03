from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy  # reverse_lazy関数を使いたい
from django.views.generic import CreateView

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm  # forms.pyのSignupFormを適用している
    template_name = "accounts/signup.html"  # ここに代入したhtmlが表示される
    success_url = reverse_lazy("tweets:home")  # 宣言をしないとエラー？

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]  # passwordではキーエラー
        user = authenticate(self.request, username=username, password=password)  # passwardはおかしい
        login(self.request, user)
        return response
