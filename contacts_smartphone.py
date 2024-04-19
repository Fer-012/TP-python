contacts = {'chloe': '0601020304', 'quentin': '0710203040', 'lyes': '0623344556', 'alex': '0412345678'}
print("cle  dictionnaire contact :", contacts.keys())
print("valeur dictionnaire contact :", contacts.values())
contacts['chloe'] = '0611223344'
print("nouveau numr de chloe :", contacts['chloe'])
contacts['sarah'] = '0145444342'
print(contacts['lyes'])
contacts.pop('chloe')
print("cle  dictionnaire contact :", contacts.keys())

