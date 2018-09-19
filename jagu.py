# #파이썬 기말 프로젝트 -학점계산-
# from tkinter import *
# import random
#
# win=Tk()
# win.title('파이썬 시험')
#
# #변수선언 및 초기화
# a, b, c = (0,0,0)
# class_A,class_B,class_C=([],[],[])#사용자와 다른 학생들의 점수가 들어감
# rank_A,rank_B,rank_C=(0,0,0)#순위
# credit,credit_A,credit_B,credit_C=(0,0,0,0)#학점
# grade_A,grade_B,grade_C=('','','')#등급(a+,a,b+....)
#
#
# def click():#버튼을 눌렀을때 실행하는 함수
#
#     #입력한 점수를 a,b,c에 저장
#    a=int(user_score_A.get())
#    b=int(user_score_B.get())
#    c=int(user_score_C.get())
#
#     #사용자 점수를 점수 리스트에 추가
#    class_A.append(a)
#    class_B.append(b)
#    class_C.append(c)
#     #거꾸로 점수 리스트를 정렬
#    class_A.sort(reverse=True)
#    class_B.sort(reverse=True)
#    class_C.sort(reverse=True)
#     #사용자점수(a,b,c)의
#    rank_A = class_A.index(a) + 1
#    rank_B = class_B.index(b) + 1
#    rank_C = class_C.index(c) + 1
#
#    lbl_rank_A = Label(win, text="수업(강) 순위(25명):           %d등"% rank_A)
#    lbl_rank_B = Label(win, text="수업(윤) 순위(29명):           %d등" % rank_B)
#    lbl_rank_C = Label(win, text="수업(최) 순위(33명):           %d등" % rank_C)
#    lbl_rank_A.grid()
#    lbl_rank_B.grid()
#    lbl_rank_C.grid()
#
#    # 학점
#    # 학점 강
#    if rank_A / 25 * 100 < 15:
#        credit_A = 4.5
#        grade_A='A+'
#    elif rank_A / 25 * 100 < 30:
#        credit_A = 4
#        grade_A='A'
#    elif rank_A / 25 * 100 < 45:
#        credit_A = 3.5
#        grade_A='B+'
#    elif rank_A / 25 * 100 < 60:
#        credit_A = 3
#        grade_A='B'
#    elif rank_A / 25 * 100 < 75:
#        credit_A = 2.5
#        grade_A='C+'
#    elif rank_A / 25 * 100 < 85:
#        credit_A = 2
#        grade_A='C'
#    elif rank_A / 25 * 100 < 90:
#        credit_A = 1.5
#        grade_A='D+'
#    elif rank_A / 25 * 100 < 95:
#        credit_A = 1
#        grade_A='D'
#    elif rank_A / 25 * 100 <= 100:
#        credit_A = 0.0
#        grade_A='F'
#
#    # 학점 윤
#    if rank_B / 29 * 100 < 15:
#        credit_B = 4.5
#        grade_B='A+'
#    elif rank_B / 29 * 100 < 30:
#        credit_B = 4
#        grade_B='A'
#    elif rank_B / 29 * 100 < 45:
#        credit_B = 3.5
#        grade_B='B+'
#    elif rank_B / 29 * 100 < 60:
#        credit_B = 3
#        grade_B='B'
#    elif rank_B / 29 * 100 < 75:
#        credit_B = 2.5
#        grade_B='C+'
#    elif rank_B / 29 * 100 < 85:
#        credit_B = 2
#        grade_B='C'
#    elif rank_B / 29 * 100 < 90:
#        credit_B = 1.5
#        grade_B='D+'
#    elif rank_B / 29 * 100 < 95:
#        credit_B = 1
#        grade_B='D'
#    elif rank_B / 29 * 100 <= 100:
#        credit_B = 0
#        grade_B='F'
#
#    # 학점 최
#    if rank_C / 33 * 100 < 15:
#        credit_C = 4.5
#        grade_C='A+'
#    elif rank_C / 33 * 100 < 30:
#        credit_C = 4
#        grade_C='A'
#    elif rank_C / 33 * 100 < 45:
#        credit_C = 3.5
#        grade_C='B+'
#    elif rank_C / 33 * 100 < 60:
#        credit_C = 3
#        grade_C='B'
#    elif rank_C / 33 * 100 < 75:
#        credit_C = 2.5
#        grade_C='C+'
#    elif rank_C / 33 * 100 < 85:
#        credit_C = 2
#        grade_C='C'
#    elif rank_C / 33 * 100 < 90:
#        credit_C = 1.5
#        grade_C='D+'
#    elif rank_C / 33 * 100 < 95:
#        credit_C = 1
#        grade_C='D'
#    elif rank_C / 33 * 100 <= 100:
#        credit_C = 0.0
#        grade_C='F'
#
#     #강,윤,최 학점 출력
#    lbl_credit_A = Label(win, text="수업(강) 학점:     %s   %.1f"%(grade_A,credit_A))
#    lbl_credit_B = Label(win, text="수업(윤) 학점:     %s   %.1f"%(grade_B,credit_B))
#    lbl_credit_C = Label(win, text="수업(최) 학점:     %s   %.1f"%(grade_C,credit_C))
#    lbl_credit_A.grid()
#    lbl_credit_B.grid()
#    lbl_credit_C.grid()
#
#    credit_pr = '20121234'  # 직전 학기 학점,따옴표안에 학점입력
#    credit_pr = 3.0 + float(credit_pr[-2:]) * 0.01
#    lbl_credit_pr = Label(win, text="진전 학기까지의 평균: %.2f" % credit_pr)
#    lbl_credit_pr.grid()
#
#    credit_now = (credit_A + credit_B + credit_C) / 3
#    lbl_credit_now = Label(win, text="이번학기 학점 평균: %.2f" % credit_now)
#    lbl_credit_now.grid()
#
#     #최종 학점
#    credit = (credit_now + credit_pr) / 2
#    credit = round(credit, 2)  # 최종 학점
#    lbl_credit = Label(win, text="6학기 학점 평균: %.2f" % credit)
#    lbl_credit.grid()
#
#
#
#
#
# for i in range(24):#수업A 점수 생성
#     class_A.append(random.randint(1,100))
# for i in range(28):#수업B 점수 생성
#     class_B.append(random.randint(1,100))
# for i in range(32):#수업C 점수 생성
#     class_C.append(random.randint(1,100))
#
# #사용자 점수 입력
# lbl1=Label(win,text="점수(강): 1~100 ")
# lbl2=Label(win,text="점수(윤): 1~100 ")
# lbl3=Label(win,text="점수(최): 1~100 ")
# lbl1.grid(row=0,column=0)
# lbl2.grid(row=1,column=0)
# lbl3.grid(row=2,column=0)
# user_score_A=Entry(win)
# user_score_B=Entry(win)
# user_score_C=Entry(win)
#
# btn=Button(win,text="점수 입력",command=click)#버튼
# user_score_A.grid(row=0,column=1)
# user_score_B.grid(row=1,column=1)
# user_score_C.grid(row=2,column=1)
# btn.grid()
#
# win.mainloop()
import re,operator
class grade:
    def __init__(self):
        self.sum={}
        self.aver=[]
        self.me =[]
        self.input()
        self.add()
        self.process()
        while True:
            b=input("출력=a,삭제=d,종료=e")
            if b=='a':
                self.output()
            elif b=='d':
                self.c=input("삭제할 이름:")
                self.delet()
            elif b=='e':
                break
    def input(self):
        self.student = []
        self.no = input("인원수를 입력해주시오: ")
        for i in range(int(self.no)):
            self.student.append([])
    def add(self):
        for i in range(int(self.no)):
            print("학번 이름 국어 영어 수학을 입력하시오(띄어쓰기 순서로 입력하시오) %d번째 학생"%(i+1))
            self.a = input().split(" ")
            for j in range(5):
                if len(self.a)!=5:
                    print("입력을 다시 해주십시오")
                    return self.add()
                else:
                    self.student[i].append(self.a[j])
    def process(self):
        for i in range(int(self.no)):
            sum=0
            for j in range(2,5):
                sum=int(self.student[i][j])+sum
            self.sum[self.student[i][1]]=sum
        self.sortedArr = sorted(self.sum.items(), key=operator.itemgetter(1, 0),reverse=True)
    def output(self):
        for i in range(int(self.no)):
            print("%s 합계=%d 평균=%d 석차=%d"%(self.sortedArr[i][0],self.sortedArr[i][1],self.sortedArr[i][1]/3,i+1))
    def delet(self):
        for i in range(len(self.sortedArr)):
            if re.findall("%s",self.c,self.sortedArr[i]):
                del(self.sortedArr[i])


a=grade()
