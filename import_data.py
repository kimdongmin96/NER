import json
import io

def load_corpus(file = 'train_data2_finish.json'):
    with io.open(file, 'r', encoding = 'utf-8-sig') as fp:
        corpus = json.load(fp)
    
    tagged_sentences = []
    pos_tags = []
    for sentence in corpus['sentence']:
        current_sentence = [[a['lemma'], 'O'] for a in sentence['morp']]
        current_pos_tags = [a['type'] for a in sentence['morp']]
        for named_entity in sentence['NE']:
            #print("NER :",named_entity['text'])
            NE_begin = int(named_entity['begin'])
            NE_end = int(named_entity['end'])
            NE_type = named_entity['type'][:2]
            for i in range(NE_begin, NE_end + 1): # 5 ~6
                current_sentence[i][1] = NE_type #5
        tagged_sentences.append(current_sentence)
        pos_tags.append(current_pos_tags)
    X = [[_[0] for _ in tagged_sentence] for tagged_sentence in tagged_sentences]
    #print("X : ",X)
    y = [[_[1] for _ in tagged_sentence] for tagged_sentence in tagged_sentences]
    #print("Y : ",y)
    return X, y, pos_tags
        
    
