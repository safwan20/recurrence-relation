# T(n) = a * T(n/b)  +   n^k (log n)^i
import math

# checking if the values are equal
# precision is upto 10^-9
def floatEquals(x,y):
    return abs(x-y)<10**(-9)

def calculate(e,f,g,h):
    p=math.log(e)/math.log(f)
    if floatEquals(p,g):
       h+=1
    if p>g:
        if floatEquals(round(p),p):
            g=round(p)
            h=0
        else:
            g=round(p,3)
            h=0
    else:
        g,h=g,h
    return [g,h]

def validation(s):
    try:
        #    eg:   s = " 4T ( n/ 2) + n2logn"

        fuction = s.replace(" ","")       #4T(n/2)+n2logn   -----> REMOVE ALL THE WHITE SPACES

        #print("recurrence relation is : ",fuction,"\n")

        arr = fuction.split('+')  # ---->SPLIT THE FUCTION WITH '+'

        part1 = arr[0]     # PART 1 : 4T(n/2)   , IT WILL HELP TO FIND a,b

        part2 = arr[1]     # PART 2 : n2logn     , IT WILL HELP TO FIND k,i

        #print(part1)
        #print(part2)


        # NOW THE JOURNEY BEGINS TO FIND a,b FROM PART1

        t = part1.split('T')        #SPLIT WITH 'T'

        print(t)                    #WE HAVE  ['4' , '(n/2)']

        f = t[0]                    # f = 4 , x = (n/2)
        x = t[1]

        print(x)

        x = x.split('/')           # SPLIT WITH '/'

        print(x)

        print(f)

        # work for a

        if f == '':               # means value of a is 1 if f is empty
            a = 1
        else:                      # else value of f is assign to a
            a = f

        # work for b

        if len(x) ==  1:           #if list of x is empty then b value is 1 which later captures by if condition(i.e it is invalid)
            b = 1
        else:                      # else value is assign to b
            b = x[1].replace(')', "")

        # WORK IS DONE OF FINDING a,b
        print("VALUE OF a and b is : ", a, b, "\n")



        # NOW THE JOURNEY BEGINS TO FIND k,i FROM PART2

        k = 0
        i = 0

        print(part2,"\n")

        if part2 == '1' :           #eg:   s = " 4T ( n/ 2) + 1"
            k = 0
            i = 0

        elif '/' in part2:

            '''
            7 cases can be possible with divide('/') operation
            
            eg:   s = " 4T ( n/ 2) + n2logn/2"
            eg:   s = " 4T ( n/ 2) + n/2logn2"
            eg:   s = " 4T ( n/ 2) + n/2logn/2"
            eg:   s = " 4T ( n/ 2) + n/2"
            eg:   s = " 4T ( n/ 2) + logn/2"
            eg:   s = " 4T ( n/ 2) + n/2logn"
            eg:   s = " 4T ( n/ 2) + nlogn/2"
            '''

            m = part2.split('/')

            print(m)

            if len(m) == 3:   #    s = " 4T ( n/ 2) + n/2logn/2"
                h = str(m[1])
                h = h[0]
                k = 1 / int(h)
                i = 1 / int(m[2])

            elif len(m) == 2:  #remaining 6 cases
                if m[0] == 'n':       # s = " 4T ( n/ 2) + n/logn"   or  s = " 4T ( n/ 2) + n/2logn2"   or s = " 4T ( n/ 2) + n/2logn  or s = " 4T ( n/ 2) + n/2

                    if 'logn' in m[1] :   # s = " 4T ( n/ 2) + n/logn  or  s = " 4T ( n/ 2) + n/2logn2"   or s = " 4T ( n/ 2) + n/2logn
                        f = m[1].split('logn')

                        if f[1] == '' :     # s = " 4T ( n/ 2) + n/logn  or   s = " 4T ( n/ 2) + n/2logn
                            k = 1/int(f[0])
                            i = 1
                        else :            #s = " 4T ( n/ 2) + n/2logn2
                            k = 1 / int(f[0])
                            i = f[1]

                    else :                  # s = " 4T ( n/ 2) + n/2
                        k = 1/int(m[1])
                        i = 0

                else:                       #s = " 4T ( n/ 2) + n2logn/2"  or   s = " 4T ( n/ 2) + nlogn/2"  or    s = " 4T ( n/ 2) + logn/2"


                    if 'nlogn' == m[0] :        #s = " 4T ( n/ 2) + nlogn/2"
                        k = 1
                        i = 1/int(m[1])
                    elif 'logn' == m[0]:        #s = " 4T ( n/ 2) + logn/2"
                        k = 0
                        i = 1/int(m[1])
                    else :                      ##s = " 4T ( n/ 2) + n2logn/2"
                        k = m[0][1]
                        i = 1/int(m[1])



        elif 'logn' not in part2 :

            '''
                   eg:   s = " 4T ( n/ 2) + n2"
                   eg:   s = " 4T ( n/ 2) + n "

                   '''

            h = part2.split('n')            # split with 'n'

            if h[1]!= '' :              #   if it is logn2 , logn566 etc the 2 , 256 etc will assign into i
                k = h[1]
            else :                      # else if it is only logn then 1 is assign into i
                k = 1

        else :
            '''
                            eg:   s = " 4T ( n/ 2) + nlogn"
                            eg:   s = " 4T ( n/ 2) + n2logn2" 
                            eg:   s = " 4T ( n/ 2) + logn2"
                            eg:   s = " 4T ( n/ 2) + nlogn2"
                            eg:   s = " 4T ( n/ 2) + logn"
                            
                            '''

            arr = part2.split('logn')

            print(arr)

            if arr[1] == '' and arr[0] == '':   # s = " 4T ( n/ 2) + logn"
                i = 1
                k = 0

            elif arr[1] == '' :                 # s = " 4T ( n/ 2) + nlogn
                i = 1
                h = arr[0].split('n')

                if h[0] == '' and h[1] == '' :
                    k =1
                else :
                    k = h[1]

            elif arr[0] == '' :             # s = " 4T ( n/ 2) + logn2
                i = arr[1]
                k = 0


            else :                         # s = " 4T ( n/ 2) + n2logn"      or      s = " 4T ( n/ 2) + nlogn2"
                i = arr[1]
                h = arr[0].split('n')

                if h[0] == '' and h[1] == '':
                    k = 1
                else:
                    k = h[1]


        print("VALUE OF k and p is : ",k," ",i)


       #NOW WE GOT ALL a,b,i k WHICH IS USED TO IDENTIFY WHICH CASE WILL COME INTO USE

        a = int(a)
        b = int(b)
        k = float(k)
        i = float(i)

        if a < 0:
            ans = "Value of a should be non-negative"
        elif b <= 1:
            ans = "Value of b should be greater than 1"
        elif k < 0:
            ans = "Value of k must be atleast 0"
        elif i < 0:
            ans = "Value of i must be atleast 0"
        else :
            ans = calculate(a, b, k, i)

    except:
        ans = "incorrect recurrence relation"

    return ans
