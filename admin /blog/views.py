from django.shortcuts import render
from .models import Blog

def home(request):
    # 모델로부터 전달받은 객체 목록을 쿼리셋이라 한다.
    # 쿼리셋을 어떤식으로 기능들을 처리하거나 정렬할 수 있게끔 해주는 방법 중 하나가 메소드이다.
    blogs = Blog.objects  #블로그 클래스 안에 있는 객체return  모델로 부터 객체를 전달 받을 수 있겠ㄱ금 한다- 
    return render(request,'blog/home.html', {'blogs' : blogs})

    # 쿼리셋과 메소드 표기 방식
    # 모델.퀘리셋(objects).메소드