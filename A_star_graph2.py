t = {'S': [['A', 6], ['B', 5], ['C', 10]],
        'A': [['S', 6], ['D', 6], ['E', 3]],
        'B': [['S', 5], ['D', 6], ['E', 7]],
        'C': [['S', 10], ['D', 3], ['E', 6]],
        'D': [['A', 6], ['B', 6], ['C', 4], ['G', 4]],
        'E': [['A', 3], ['B', 7], ['C', 6], ['G', 6]],
        }

heu = {'S': 14, 'A': 7, 'B': 10, 'C': 4, 'D': 2,'E': 4, 'G': 0}

c = {'S': 0}            


def astr(): 
    global t, heu
    clsd = []            
    opnd = [['S', 8]]    

    while True:
        fun = [i[1] for i in opnd]    
        chsn_in = fun.index(min(fun))
        n = opnd[chsn_in][0] 
        clsd.append(opnd[chsn_in])
        del opnd[chsn_in]
        if clsd[-1][0] == 'G':      
            break
        for itm in t[n]:
            if itm[0] in [cls_itm[0] for cls_itm in clsd]:
                continue
            c.update({itm[0]: c[n] + itm[1]})           
            fn_node = c[n] + heu[itm[0]] + itm[1]     
            temp = [itm[0], fn_node]
            opnd.append(temp)                                   

    
    t_n = 'G'                       
    opt_seq = ['G']               
    for i in range(len(clsd)-2, -1, -1):
        ch_n = clsd[i][0]           
        if t_n in [children[0] for children in t[ch_n]]:
            chld_c = [temp[1] for temp in t[ch_n]]
            chld_n = [temp[0] for temp in t[ch_n]]

            if c[ch_n] + chld_c[chld_n.index(t_n)] == c[t_n]:
                opt_seq.append(ch_n)
                t_n = ch_n
    opt_seq.reverse()             

    return clsd, opt_seq


if __name__ == '__main__':
    vstd_n, opt_n = astr()
    print('The travarsal path for this algorithem is: ' + str(vstd_n))
    print('The exact(optimal) path for this algorithem is: ' + str(opt_n))