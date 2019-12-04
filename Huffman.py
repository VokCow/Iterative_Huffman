import copy

def lowest_pair(source):
  # find the lowest two less probable symbols in the source distribution
  symbols,values=np.array(list(source.keys())),np.array(list(source.values()))
  ais=symbols[np.argsort(values)]
  # print(ais[0],ais[1])
  return ais[0],ais[1]

def Huffman(source):

# all the encoding versions will be stored in this list X
  X=[source]
  t_source=copy.deepcopy(source)

# iteratively merge the two less probable symbols until encoding consist in just one
# symbol with probability 1
  while(True):
    
    a1,a2=lowest_pair(t_source)
    # print(t_source)
    # print(a1,a2)
    p1,p2=t_source.pop(a1),t_source.pop(a2)
    t_source[a1+a2]=p1+p2

    X.append(t_source)
    t_source=copy.deepcopy(t_source)

    if len(t_source)==2: break

  code=dict(zip(t_source.keys(),['1','0']))

# reverse the list containing encodings 
  X_r = X[::-1]

# reconstruct the codes starting with the symbols in the last encoding version
  for i in range(len(X_r)-1):

    a_old=set(X_r[i].keys())-set(X_r[i+1].keys())
    a_new=set(X_r[i].keys()).symmetric_difference(set(X_r[i+1].keys()))-a_old

    # print(f'a_old: {a_old}, a_new: {a_new}')

    a_old=list(a_old)[0]
    a_new=list(a_new)
    
    if a_old[0] == a_new[0]:
      a1,a2=a_new[0],a_new[1]
    else:
      a1,a2=a_new[1],a_new[0]

    # print(f'a_old: {a_old}, a1: {a1} a2: {a2}')

    code_old=code.pop(a_old)
    code[a1]=code_old + '1'
    code[a2]=code_old + '0'

  return  code


source1 = {'A': 0.25, 'B': 0.25 , 'C': 0.2, 'D':0.2,'E':0.1}
source2  = {'A': 0.1, 'B': 0.2 , 'C': 0.1, 'D':0.3,'E':0.3}
code1,code2 = Huffman(source1),Huffman(source2)
print(f'Source 1 Huffman encoding: {code1}\nSource 2 Huffman encoding: {code2}')
