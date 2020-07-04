## 정적메소드이다. ##
## 정적메소드란 클래스에서 직접 접근할 수 있는 메소드이다. ##

## classmethod()와 instancemethod()의 차이 ##
## instancemethod()는 특정 함수를 호출할 때 ##
## 객체를 지정해 주어야 한다. ##
## classmethod()는 그럴 필요 없이 바로 사용 가능 ##

class cnpz :
    
    def instance_method(self) :
        print("인스턴스")

    @classmethod
    def class_method(cls) :
        print("클래스")

    @staticmethod
    def static_method() :
        print("스테틱")
        
## cnpz.class_method() 입력시 클래스 출력 ##
## cnpz.static_method() 입력시 스테틱 출력 ##
## cnpz.instance_method() 입력시 오류 발생 ##
## a = cnpz() ##
## cnpz.instance_method() 이런 식으로 사용해야 함 ##
        
        
## classmethod()와 staticmethod()의 차이 ##
## 상속에서 차이가 난다. ##
## staticmethod()는 부모 클래스의 클래스 속성 값을 가져오지만 ##
## classmethod()는 cls 인자를 활용하여 cls의 클래스 속성을 가져온다. ## 

class Phone:
    default = "아이폰"

    def __init__(self):
        self.show = "나의 스마트폰은 " + self.default + "입니다."

    @classmethod
    def class_phone(cls) :      ## 생성할 때 인자로 cls를 넣어줘야 함 ##
        return cls()

    @staticmethod
    def static_phone() :      ## 생성할 때 인자를 비움. cls, self를 넣으면 오류 발생 ##
        return Phone()

    def print_phone(self) :
        print(self.show)

class Samsung(Phone):
    default = "갤럭시"
    
## Samsung.class_phone().print_phone() 입력시 ##
## 나의 스마트폰은 갤럭시입니다. 출력 ##
## Samsung.static_phone().print_phone() 입력시 ##
## 나의 스마트폰은 아이폰입니다. 출력 ##
