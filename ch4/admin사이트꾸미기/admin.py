from django.contrib import admin
from polls.models import Question,Choice

# Register your models here.

# 4.1 admin 사이트 꾸미기
# django admin 사이트는 db에 들어있는 데이터를 쉽게 관리할 수 있도록
# C.R.U.D 기능을 제공. (CREATE,READ,UPDATE,DELETE)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra =2 

#테이블 형식으로 보여주기
class ChoiceTabular(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    #필드 순서 변경
    # fileds= ['published_date','question_text']       
    
    #필드 분리해서 보여주기
    # fieldsets=[       
    #     ('Question Statement',{'fields':['question_text']}),
    #     ('Date Information',{'fields':['published_date'],'classes':['collapse']}),
    # ]

    #필드 접기,Question,Choice 같이 보기
    fieldsets=[
        ('None',{'fields':['question_text']}),
        ('Date Information',{'fields':['published_date'],'classes':['collapse']}),
    ]
    #inlines = [ChoiceInline]
    inlines = [ChoiceTabular]
    list_display =('question_text','published_date')        #컬럼(명) 지정하기.
    list_filter =['published_date']                         #filter 기능 추가.
    search_fields = ['question_text','published_date']                       #검색 박스 추가 : []에 지정된 필드에 해당하는 단어를 검색.
    

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

