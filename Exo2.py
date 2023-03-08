
def solve(lines) :

    res = ""
    for l in lines.splitlines()[1:] :
        vals = {1:"0/36", 2:"1/36",3:"1/12",4:"1/6",5:"5/18",6:"5/12",7:"7/12",8:"13/18",9:"5/6",10:"11/12",11:"35/36",12:"1"}
        res += str(vals[int(l)]) +"\n" 

    return res 