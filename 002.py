string = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24"

yaser = string.split(" ")
'''print for better see'''
#print(yaser)
answer = []
for i in range(len(yaser)):
    answer.append("&")
    
def print_string_from_list(x):
    
    print(("".join(x)))


for yas in yaser:
    #print(yas)
    c = yas[0]
    i = int(yas[1:])
    answer[i] = c
print(answer)
print_string_from_list(answer)
'''print for better see'''
    #print(f"c = {c} , i = {i}")