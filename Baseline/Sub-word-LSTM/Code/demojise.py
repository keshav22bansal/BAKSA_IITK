import emoji
from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.dicts.emoticons import emoticons

text_processor = TextPreProcessor(
    # terms that will be normalized
    normalize=['url', 'email', 'percent', 'money', 'phone', 'user',
        'time', 'url', 'date', 'number'],
    # terms that will be annotated
    annotate={"hashtag", "allcaps", "elongated", "repeated",
        'emphasis', 'censored'},
    fix_html=True,  # fix HTML tokens
    
    # corpus from which the word statistics are going to be used 
    # for word segmentation 
    segmenter="twitter", 
    
    # corpus from which the word statistics are going to be used 
    # for spell correction
    corrector="twitter", 
    
    unpack_hashtags=True,  # perform word segmentation on hashtags
    unpack_contractions=True,  # Unpack contractions (can't -> can not)
    spell_correct_elong=False,  # spell correction for elongated words
    
    # select a tokenizer. You can use SocialTokenizer, or pass your own
    # the tokenizer, should take as input a string and return a list of tokens
    tokenizer=SocialTokenizer(lowercase=True).tokenize,
    
    # list of dictionaries, for replacing tokens extracted from the text,
    # with other expressions. You can pass more than one dictionaries.
    dicts=[emoticons]
)
import re
newfile = open("../Data/sem_eval_data_smileys_replaced_users_removed", "w")
with open("../Data/sem_eval_data.txt") as f:
    for line in f.readlines():
        modified_line = emoji.demojize(line, delimiters=('<', '> ')).strip()
        l = modified_line.split()
        l1=[]
        l2=[]
        for token in l:
            if token[0] == '<' and token[-1] == '>':
                l2.append(token)
            else:
                l1.append(token)
        ans1 = l1[0]+"\t"
        ans1 = ans1+" ".join(l1[1:])
        ans = ans1[:-4] +" "+ " ".join(l2)+" "+ ans1[-4:]+'\n'
        ans = list(ans)
        ans[-3] = '\t'
        ans[-5] = '\t'
        # print(ans)
        ans = "".join(ans)
        # print(ans)

        ##Modified by Keshav
        print(ans)
        ans = ans.replace('@ ','@').replace('# ','#').replace('<','').replace('>','').replace("_",' ').replace('  ',' ')
        string = ans.split('\t')[1]
        processed = text_processor.pre_process_doc(string)
        print(processed)
        new_ans = []
        for token in processed:
            if token.startswith(("<hash","<number","<")) or "user" in token:
                continue
            new_ans.append(token)
        
        arr = ans.split('\t')
        arr[1] = re.sub(r"http.*|…",""," ".join(new_ans))
        ans = "\t".join(arr)
        
        print(arr[2])
        print(ans)
        # break
        newfile.write(ans)
        # break