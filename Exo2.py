
def solve(lines) :

    res = ""
    for l in lines.splitlines()[1:] :
        vals = {1:0, 2:1,3:3,4:6,5:10,6:15,7:21,8:26,9:30,10:33,11:35,12:36}
        res += str(vals[int(l)]) +"\n" 

    return res