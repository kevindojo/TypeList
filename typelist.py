#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# input
m = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"

# input
n = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"

def filter(l):
    string = ''
    total = 0

    for i in l:
        if isinstance(i, int) or isinstance(i, float):
            total += i
        elif isinstance(i, str):
            string += i
        
        if string and total:
            print "The array you entered is of mixed type"
            print "String:", string
            print "Total:", total

        elif string:
            print "The array you entered is of string type"
            print "String:", string

        else:
            print "The array you entered is of number(float or int) type"
            print "Total:", total

filter(l)