nb= 0
s = 0
m_max = 0 
m_min = 20
while True:
    note = float(input("entrez la valeur de la note "))
    if note < 0 or note > 20:
        break

    s += note
    nb += 1

    if note > m_max:
        m_max = note

    if note < m_min:
        m_min = note

    print("nombre de notes entre :", nb)
    print("note  :",m_max)
    print("note :", m_min)
    print("moyenne :", s/nb)
