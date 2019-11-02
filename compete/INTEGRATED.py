# T(n) = a * T(n/b)  +   n^k (log n)^i
import math

# checking if the values are equal
# precision is upto 10^-9
def floatEquals(x,y):
    return abs(x-y)<10**(-9)


def display(arr):
    print("\nn^" +str(arr[0])+"(log n)^"+str(arr[1]))


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

def validation():
    try:
        s = " 4T ( n/ 2) + nlogn"

        fuction = s.replace(" ","")

        print("recurrence relation is : ",fuction,"\n")

        arr = fuction.split('+')

        part1 = arr[0]

        part2 = arr[1]

        #print(part1)
        #print(part2)

        t = part1.split('T')

        f = t[0]
        x = t[1]

        x = x.split('/')

        if f == '':
            a = 1
        else:
            a = f

        if len(x) == 1:
            b = 1
        else:
            b = x[1].replace(')', "")

        #print("VALUE OF a and b is : ", a, b, "\n")

        k = 0
        i = 0

        #print(part2,"\n")

        if part2 == '1' :
            k = 0
            i = 0

        elif '/' in part2:

            m = part2.split('/')

            #print(m)

            if len(m) == 3:
                h = str(m[1])
                h = h[0]
                k = 1 / int(h)
                i = 1 / int(m[2])
            elif len(m) == 2:
                if m[0] == 'n':
                    h = str(m[1])
                    h = h[0]
                    k = 1 / int(h)
                    i = 1
                else:
                    k = 1
                    i = 1 / int(m[1])

        elif 'logn' not in part2 :
            h = part2.split('n')

            if h[1]!= '' :
                k = h[1]
            else :
                k = 1

        else :
            part2 = list(part2)
            part2.append('#')
            part2 = ''.join(part2)

            m = part2.split('logn')

            #print(m)

            if m[1] == '#' :
                i = 1
                if m[0] == '' :
                    k = 0
                else :
                    r = m[0].split('n')
                    if r[1] == '' :
                        k = 1
                    else :
                        k = r[1]
            else :
                i = m[1]
                if m[0] == '' :
                    k = 0
                else :
                    r = m[0].split('n')
                    if r[1] == '' :
                        k = 1
                    else :
                        k = r[1]


        if '#' in str(i) :
            i = i.replace('#','')

        #print("VALUE OF k and p is : ",k," ",i)

        a = int(a)
        b = int(b)
        k = float(k)
        i = float(i)

        if a < 0:
            print("Value of a should be non-negative")
        elif b <= 1:
            print("Value of b should be greater than 1")
        elif k < 0:
            print("Value of k must be atleast 0")
        elif i < 0:
            print("Value of i must be atleast 0")
        else :
            ans = calculate(a, b, k, i)
            display(ans)

    except:
        print("incorrect recurrence relation")




validation()

