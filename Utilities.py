import numpy as np
def glovevec():
    with open("glove.6B.50d.txt",'r',encoding='utf8') as f:
        words=set()
        word_to_vec_map={}
        for line in f:
            line=line.strip().split()
            curr_word=line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word]=np.array(line[1:],dtype=np.float64)
        
    return word_to_vec_map

def embedding(vocabulary_size,tk):
    emb_matrix = np.zeros((vocabulary_size, 50))

    word_to_vec_map=glovevec()
    for w, i in tk.word_index.items():
        temp= word_to_vec_map.get(w)
        if temp is not None:
            emb_matrix[i, :]=temp
    return emb_matrix