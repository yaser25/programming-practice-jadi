string  ="T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24"
parts = string.split(" ")
#print(type(yas2))
#print(f"parts------------------->{parts}")
#-------------------------------------------
answer = []
for i in range(55):
    answer.append("*")
#-------------------------------------------
sum = 0
for p in parts:
    sum = sum + 1
    c = p[0]
    i = int(p[1:])
    answer[i] = c
    #print(answer)
    #print(f'answer i hast {answer[i]}')
    print(f'"\n"sum = {sum}p={p},c={c},i={i}')
#--------------------------------------------
def print_string(s):
    print("".join(s))
#--------------------------------------------
print_string(answer)
#print(i)
#print(answer[i])            
    