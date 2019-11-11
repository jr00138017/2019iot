import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
LED_PIN=12
GPIO.setup(LED_PIN,GPIO.OUT)
def mos(list):
        if list == 1:
                GPIO.output(LED_PIN,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(LED_PIN,GPIO.LOW)
                time.sleep(0.5)
        elif list == 0:
                GPIO.output(LED_PIN,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(LED_PIN,GPIO.LOW)
                time.sleep(0.5)
_A=[0, 1]
_B=[1,0, 0, 0]
_C=[1, 0, 1, 0]
_D=[1, 0, 0]
_E=[0]
_F=[0, 0, 1, 0]
_G=[1, 1, 0]
_H=[0, 0, 0, 0]
_I=[0, 0]
_J=[0, 1, 1, 1]
_K=[1, 0, 1]
_L=[0, 1, 0, 0]
_M=[1, 1]
_N=[1, 0]
_O=[1, 1, 1]
_P=[0, 1, 1, 0]
_Q=[1, 1, 0, 1]
_R=[0, 1, 0]
_S=[0, 0, 0]
_T=[1]
_U=[0, 0, 1]
_V=[0, 0, 0, 1]
_W=[0, 1, 1]
_X=[1, 0, 0, 1]
_Y=[1, 0, 1, 1]
_Z=[1, 1, 0, 0]
_1=[0, 1, 1, 1, 1]
_2=[0, 0, 1, 1, 1]
_3=[0, 0, 0, 1, 1]
_4=[0, 0, 0, 0, 1]
_5=[0, 0, 0, 0, 0]
_6=[1, 0, 0, 0, 0]
_7=[1, 1, 0, 0, 0]
_8=[1, 1, 1, 0, 0]
_9=[1, 1, 1, 1, 0]
_0=[1, 1, 1, 1, 1]

str=raw_input("input:")
str = str.upper()
print(str)
for i in str:
        if i == 'A':
                map(mos, _A)
        elif i == 'B':
                map(mos, _B)
        elif i == 'C':
                map(mos, _C)
        elif i == 'D':
                map(mos, _D)
        elif i == 'E':
                map(mos, _E)
        elif i == 'F':
                map(mos, _F)
        elif i == 'G':
                map(mos, _G)
        elif i == 'H':
                map(mos, _H)
        elif i == 'I':
                map(mos, _I)
        elif i == 'J':
                map(mos, _J)
        elif i == 'K':
                map(mos, _K)
        elif i == 'L':
                map(mos, _L)
        elif i == 'M':
                map(mos, _M)
        elif i == 'N':
                map(mos, _N)
        elif i == 'O':
                map(mos, _O)
        elif i == 'P':
                map(mos, _P)
        elif i == 'Q':
                map(mos, _Q)
        elif i == 'R':
                map(mos, _R)
        elif i == 'S':
                map(mos, _S)
        elif i == 'T':
                map(mos, _T)
        elif i == 'U':
                map(mos, _U)
        elif i == 'V':
                map(mos, _V)
        elif i == 'W':
                map(mos, _W)
        elif i == 'X':
                map(mos, _X)
        elif i == 'Y':
                map(mos, _Y)
        elif i == 'Z':
                map(mos, _Z)
        elif i == '0':
                map(mos, _0)
        elif i == '1':
                map(mos, _1)
        elif i == '2':
                map(mos, _2)
        elif i == '3':
                map(mos, _3)
        elif i == '4':
                map(mos, _4)
        elif i == '5':
                map(mos, _5)
        elif i == '6':
                map(mos, _6)
        elif i == '7':
                map(mos, _7)
        elif i == '8':
                map(mos, _8)
        elif i == '9':
                map(mos, _9)

GPIO.cleanup()

