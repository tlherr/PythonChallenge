import url
import string

# Question 2

def make_rot_n(n):
 lc = string.ascii_lowercase
 uc = string.ascii_uppercase
 trans = str.maketrans(lc + uc,
                          lc[n:] + lc[:n] + uc[n:] + uc[:n])
 return lambda s: str.translate(s, trans)

solve = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# K to M (2 chars)
rot2 = make_rot_n(2)
solve = rot2(solve)

print(solve)

url.format(rot2("274877906944"))