from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        not_login = ["/special/list/", "/scoreline/list/", "/rate/list/", "/chart/list/",
                     "/chart/school_collection/",
                     "/login/", "/register/", "/", "/chart/school_score/","/admin/","/logout/",
                     "/chart/auto_school/","/chart/double_school/","/chart/total_school/",
                     ]
        # 0.排除那些不需要登录就能访问的页面
        # request.path_info 获取当前用户请求的URL /login/
        # print("path",request.path_info)
        # print(not_login)
        # print(request.path_info in not_login)
        if request.path_info in not_login:
            return

        # 1.读取当前访问的用户的session信息，如果能读到，说明已登陆过，就可以继续向后走。
        info_dict = request.session.get("info")
        # print(info_dict)
        if info_dict:
            return

        # 2.没有登录过，重新回到登录页面
        return redirect('/login/')
