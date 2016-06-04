#-*-coding: utf8 -*-
class SimpleCashCard:
    """
    SimpleCashCard class
    deposit, withdraw, and check_balance methods
    """

    def __init__(self):
       print("SimpleCashCard __init__()") #함수 호출 표식
       #클래스 생성자 (컨스터럭터)
       #멤버 변슈 초기화
       #각 카드 별로 따로 잔고를 기록한다
       self, balance_won = 0

    #메소드 methods #객체에 어떤 신호를 전달하는 역할을 한다
    def deposit(selfself, amount_won):
        """
        입금
        :param amount_won: 입금 액수:
        :return:
        """
        print "SimpleCashCard deposit()"