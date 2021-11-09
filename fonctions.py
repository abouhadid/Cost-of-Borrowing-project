


def actualiser(M, n, i):
    i = i/100
    v = M/((1+i) ** n)
    return v

# fonction qui retourne le côut pour une emprunt In-finie


def cout_infine(M, n, i, mode, type, diff):
    C = 0
    if (type == 1):
        if(mode == "Mensuelle"):
            i_f = i/1200
            d = n*12
        if(mode == "Trimestrielle"):
            i_f = i/400
            d = n*4
        if(mode == "Semestrielle"):
            i_f = i/200
            d = n*2
        if(mode == "Annuelle"):
            i_f = i/100
            d = n
    if(type == 2):
        if(mode == "Mensuelle"):
            i_f = i/100
            i_f = i_f**(1./12.) - 1
            d = n*12
        if(mode == "Trimestrielle"):
            i_f = i/100
            i_f = i_f**(1./4.) - 1
            d = n*4
        if(mode == "Semestrielle"):
            i_f = i/100
            i_f = i_f**(1./2.) - 1
            d = n*2
        if(mode == "Annuelle"):
            i_f = i/100
            d = n
    inter = M*i_f
    C += diff*inter
    C += inter*d
    C += M
    return "%.2f" % C

# fonction qui retourne le côut pour une emprunt avec ammortissement cst


def cout_amort_cst(M, n, i, mode, type, diff):
    C = 0
    A = M
    if (type == 1):
        if(mode == "Mensuelle"):
            i_f = i/1200
            d = n*12
        if(mode == "Trimestrielle"):
            i_f = i/400
            d = n*4
        if(mode == "Semestrielle"):
            i_f = i/200
            d = n*2
        if(mode == "Annuelle"):
            i_f = i/100
            d = n
    if(type == 2):
        if(mode == "Mensuelle"):
            i_f = i/100
            i_f = (1+i_f)**(1./12.) - 1
            d = n*12
        if(mode == "Trimestrielle"):
            i_f = i/100
            i_f = (1+i_f)**(1./4.) - 1
            d = n*4
        if(mode == "Semestrielle"):
            i_f = i/100
            i_f = (1+i_f)**(1./2.) - 1
            d = n*2
        if(mode == "Annuelle"):
            i_f = i/100
            d = n
    amort = M/d
    x = M*i_f
    C += x*diff
    for j in range(d):
        inter = A*i_f
        annui = inter + amort
        C += annui
        A -= amort
    return "%.2f" % C

# fonction qui retourne le côut pour une emprunt avec annuités cst


def cout_annui_cst(M, n, i, mode, type, diff):
    C = 0
    A = M
    if (type == 1):
        if(mode == "Mensuelle"):
            i_f = i/1200
            d = n*12
        if(mode == "Trimestrielle"):
            i_f = i/400
            d = n*4
        if(mode == "Semestrielle"):
            i_f = i/200
            d = n*2
        if(mode == "Annuelle"):
            i_f = i/100
            d = n
    if(type == 2):
        if(mode == "Mensuelle"):
            i_f = i/100
            i_f = (1+i_f)**(1./12.) - 1
            d = n*12
        if(mode == "Trimestrielle"):
            i_f = i/100
            i_f = (1+i_f)**(1./4.) - 1
            d = n*4
        if(mode == "Semestrielle"):
            i_f = i/100
            i_f = (1+i_f)**(1./2.) - 1
            d = n*2
        if(mode == "Annuelle"):
            i_f = i/100
            d = n
    x = M*i_f
    C += x*diff
    b = 1-((1+i_f)**(-d))
    annui = M * (i_f/b)
    for j in range(n-1):
        C += annui
        A = A - (annui - (A*i_f))
    annui = A + A*i_f
    C += annui
    return "%.2f" % C

