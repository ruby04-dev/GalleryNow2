from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Gallery, ReadOnlyGalleryForm

# Create your views here.


def index(request):

    gallery_list = Gallery.objects.all()

    # object 가 없을 때 처리 로직
    if not gallery_list:
        messages.info(request, "현재 데이터가 없습니다.")
        return redirect('index')

    context = {
        'gallery_list': gallery_list,
    }
    return render(request, 'galleries/list.html', context)


def detail(request, gallery_id):

    # object 가 없을 때 처리 로직
    try:
        gallery_item = Gallery.objects.get(pk=gallery_id)
    # obj가 존재할 때 실행할 코드
    except ObjectDoesNotExist:
        # 객체가 존재하지 않을 때 실행할 코드
        print("아이템을 찾을 수 없습니다.")
        return redirect('index')
    # field_names = [field.name for field in Gallery._meta.fields]
    context = {
        'gallery_item': gallery_item,
    }
    return render(request, 'galleries/detail.html', context)


# legacy code
"""
# posts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Theme, Exhibition, Review, Artist, Gallery
from posts import api
from .forms import ReviewForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
# 첫 페이지 모든 theme의 list를 보여준다.
def index(request):
    theme_list = Theme.objects.all()
    context = {
        'theme_list': theme_list,
    }
    # return render(request, 'posts/test/now.html', context)
    return render(request, 'posts/index.html', context)


# 선택된 테마의 포함된 전시 리스트를 보여준다.
def post_list(request, theme_pk):
    theme = Theme.objects.get(pk=theme_pk)
    context = {
        'theme': theme,
    }
    return render(request, 'posts/post_list.html', context)


# 전시 detail 조회

def detail(request, post_pk):
    post = Exhibition.objects.get(pk=post_pk)
    review_form = ReviewForm()
    reviews = post.review_set.all()
    context = {
        'post': post,
        'review_form': review_form,
        'reviews': reviews
    }
    return render(request, 'posts/detail.html', context)

@login_required
def like(request, post_pk):
    post = Exhibition.objects.get(pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
        is_liked = False
    else:
        post.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)


# 리뷰 C
@login_required
def review_create(request, post_pk):
    exhibition = Exhibition.objects.get(pk=post_pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.exhibition = exhibition
        review.user = request.user
        review.save()
        return redirect('posts:detail', post_pk)
    context = {
        'exhibition': exhibition,
        'review_form': review_form,
    }
    return render(request, 'posts/detail.html', context)
    

@login_required
def review_update(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    review_form = ReviewForm(instance=review)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('posts:detail', post_pk)
    context = {
        'review_form': review_form,
        'review': review,
    }
    return render(request, 'posts/detail.html', context)


# 리뷰 D
@login_required
def review_delete(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('posts:detail', post_pk)


@login_required
def review_like(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    print(JsonResponse(context))
    return JsonResponse(context)


@login_required
def create_theme(request):
    context = {}
    return render(request, 'posts/test/create_theme.html', context)


@login_required
def staff(request):
    if request.user.is_admin:
        context = {
            'items': Exhibition.objects.all()
        }
        return render(request, 'posts/test/staff.html', context)


@login_required
def update_exhibition_list(request):
    if request.method == "POST":
        # admin user 일 때만 동작
        if request.user.is_admin:
            print(api.update())
    return redirect('posts:staff')


# 관리자의 테마 생성 플로우
0. 태그 관리자 페이지 에서 태그 통계 확인
1. 테마 생성하기 버튼 입력
"""
