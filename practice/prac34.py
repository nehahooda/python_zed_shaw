def rm(str,n):
    fp = str[:n]
    lp = str[n+1:]
    return fp +lp
print(rm('nehahooda',0))
print(rm('nehahooda',3))
print(rm('nehahooda',5))