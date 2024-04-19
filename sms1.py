from traceback import print_tb


def remplir_dic(fichier):
    dic_sms = {}
    f=open(fichier, 'r')
    for line in f:
        l=line.split()
        num=l[0]
        date=l[1]
        heure=l[2]
        msg=l[3:]
        continu =' '.join(msg)
        dic_sms[num]=[date,heure,continu]
    f.close()
    return dic_sms

def no_spam_sms(dic_sms):
    dic_sms_no_spam={}
    for cle,val in dic_sms.items():
        if not cle.startswith('0899'):
            dic_sms_no_spam[cle]=val
    return dic_sms_no_spam

def upper_pub(upper_char):
    nb =0
    for ch in upper_char:
        if ch.isupper():
            nb+=1
    return nb>len(upper_char)//2

def delete_pub(dic_sms):
    dic_sms_no_pub={}   
    for cle,val in dic_sms.items():
        if '$' not in val[2] and not upper_pub(val[2]):
            dic_sms_no_pub[cle] = val
    return dic_sms_no_pub

            
if __name__=="__main__":
    print("___________________________List___________________________")
    dic_sms=remplir_dic("sms.txt")
    print(dic_sms)
    print("______________________No Span Number______________________")
    print(no_spam_sms(dic_sms))
    print("______________________No pub______________________")
    print(delete_pub(dic_sms))