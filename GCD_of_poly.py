'''def __GCF_PP_P__(poly1,poly2):
    c=MOD_PP_P(poly1,poly2)
    while NZER_N_B(DEG_P_N(c)):
        poly1,poly2=poly2,c
        c=MOD_PP_P(poly1,poly2)
    return poly2'''
def GCF_PP_P(poly1,poly2):
    c=poly1%poly2
    while NZER_N_B(DEG_P_N(c)):
        poly1,poly2=poly2,c
        c=poly1%poly2
    return poly2