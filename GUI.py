from tkinter import *
from fonctions import *
from tkinter.ttk import *

# fonction qui calcule les côuts et les affiches


def calculer():

    M = montant_var.get()
    t = taux_var.get()
    d = duree_var.get()
    mode_input = var_mode.get()
    type_input = type_var.get()
    diff_input = diff_var.get()

    var_cout1.set(cout_amort_cst(M, d, t, mode_input,
                                 type_input, diff_input)+" MAD")
    var_cout2.set(cout_annui_cst(M, d, t, mode_input,
                                 type_input, diff_input)+" MAD")
    var_cout3.set(cout_infine(M, d, t, mode_input,
                              type_input, diff_input)+" MAD")

# fonction qui affiche le tableau d'amortissement(amort cst)


def table_amort_cst():
    window = Tk()
    window.title("Tableau d'amortissement")

    n = duree_var.get()
    M = montant_var.get()
    M = float(M)
    i = taux_var.get()
    diff_input = diff_var.get()

    type_input = type_var.get()
    mode_input = var_mode.get()
    if (type_input == 1):
        if(mode_input == "Mensuelle"):
            i_f = i/1200
            d = n*12
        if(mode_input == "Trimestrielle"):
            i_f = i/400
            d = n*4
        if(mode_input == "Semestrielle"):
            i_f = i/200
            d = n*2
        if(mode_input == "Annuelle"):
            i_f = i/100
            d = n
    if(type_input == 2):
        if(mode_input == "Mensuelle"):
            i_f = i/100
            i_f = (1+i_f)**(1./12.) - 1
            d = n*12
        if(mode_input == "Trimestrielle"):
            i_f = i/100
            i_f = (1+i_f)**(1./4.) - 1
            d = n*4
        if(mode_input == "Semestrielle"):
            i_f = i/100
            i_f = (1+i_f)**(1./2.) - 1
            d = n*2
        if(mode_input == "Annuelle"):
            i_f = i/100
            d = n
    amort = M/d

    # creation et initialisation des colonnes du tableau
    tableau = Treeview(window, height=d+diff_input)
    tableau["columns"] = ("one", "two", "three", "four", "five")
    tableau.column("#0", width=50, minwidth=50, stretch=NO)
    tableau.column("one", width=100, minwidth=100, stretch=NO)
    tableau.column("two", width=100, minwidth=100, stretch=NO)
    tableau.column("three", width=100, minwidth=100, stretch=NO)
    tableau.column("four", width=100, minwidth=100, stretch=NO)
    tableau.column("five", width=100, minwidth=100, stretch=NO)

    tableau.heading("#0", text="Période", anchor=W)
    tableau.heading("one", text="Restant dû", anchor=W)
    tableau.heading("two", text="Intérêt", anchor=W)
    tableau.heading("three", text="Amortissement", anchor=W)
    tableau.heading("four", text="Annuité", anchor=W)
    tableau.heading("five", text="CFP", anchor=W)
    # remplir le tableau
    inter = M*i_f
    for j in range(diff_input):
        tableau.insert('', 'end', text=str(j+1), values=(str("%.2f" % M),
                                                         str("%.2f" % inter), str(0), str("%.2f" % inter), str(M)))

    for j in range(d):
        A = M-amort
        tableau.insert('', 'end', text=str(j+diff_input+1), values=(str("%.2f" % M),
                                                                    str("%.2f" % (M*i_f)), str("%.2f" % amort), str("%.2f" % (amort + (M*i_f))), str("%.2f" % A)))
        M = M - amort

    texte = Label(window, text="Amortissement constant",
                  font=("Arial", 16, "bold"), borderwidth=6, relief=GROOVE)
    if(type_input == 1):
        texte1 = Label(window, text="Periodicité : " +
                       mode_input+"              Taux : Proportionnel", font=("Times New Roman ", 10, "bold"))
    if(type_input == 2):
        texte1 = Label(window, text="Periodicité : " +
                       mode_input+"              Taux : Equivalent", font=("Times New Roman", 10, "bold"))
    # positionner les widgets avec pack
    texte.pack(pady=10, ipady=10)
    texte1.pack(pady=10, ipady=10)
    tableau.pack(side=BOTTOM, fill=X)

    window.mainloop()

# fonction qui affiche le tableau d'amortissement(annui cst)


def table_annui_cst():
    window = Tk()
    window.title("Tableau d'amortissement")

    n = duree_var.get()
    M = montant_var.get()
    M = float(M)
    i = taux_var.get()
    diff_input = diff_var.get()

    type_input = type_var.get()
    mode_input = var_mode.get()
    if (type_input == 1):
        if(mode_input == "Mensuelle"):
            i_f = i/1200
            d = n*12
        if(mode_input == "Trimestrielle"):
            i_f = i/400
            d = n*4
        if(mode_input == "Semestrielle"):
            i_f = i/200
            d = n*2
        if(mode_input == "Annuelle"):
            i_f = i/100
            d = n
    if(type_input == 2):
        if(mode_input == "Mensuelle"):
            i_f = i/100
            i_f = (1+i_f)**(1./12.) - 1
            d = n*12
        if(mode_input == "Trimestrielle"):
            i_f = i/100
            i_f = (1+i_f)**(1./4.) - 1
            d = n*4
        if(mode_input == "Semestrielle"):
            i_f = i/100
            i_f = (1+i_f)**(1./2.) - 1
            d = n*2
        if(mode_input == "Annuelle"):
            i_f = i/100
            d = n
    A = M

    # creation et initialisation des colonnes du tableau
    tableau = Treeview(window, height=d+diff_input)
    tableau["columns"] = ("one", "two", "three", "four", "five")
    tableau.column("#0", width=50, minwidth=50, stretch=NO)
    tableau.column("one", width=100, minwidth=100, stretch=NO)
    tableau.column("two", width=100, minwidth=100, stretch=NO)
    tableau.column("three", width=100, minwidth=100, stretch=NO)
    tableau.column("four", width=100, minwidth=100, stretch=NO)
    tableau.column("five", width=100, minwidth=100, stretch=NO)

    tableau.heading("#0", text="Période", anchor=W)
    tableau.heading("one", text="Restant dû", anchor=W)
    tableau.heading("two", text="Intérêt", anchor=W)
    tableau.heading("three", text="Amortissement", anchor=W)
    tableau.heading("four", text="Annuité", anchor=W)
    tableau.heading("five", text="CFP", anchor=W)

    # remplir le tableau
    inter = M*i_f
    for j in range(diff_input):
        tableau.insert('', 'end', text=str(j+1), values=(str("%.2f" % M),
                                                         str("%.2f" % inter), str(0), str("%.2f" % inter), str(M)))

    b = 1-((1+i_f)**(-d))
    annui = M * (i_f/b)
    for j in range(d):
        A = A - (annui - (M*i_f))
        tableau.insert('', 'end', text=str(j+1+diff_input), values=(str("%.2f" % M),
                                                                    str("%.2f" % (M*i_f)), str("%.2f" % (annui - (M*i_f))), str("%.2f" % annui), str("%.2f" % A)))
        M = M - (annui - (M*i_f))

    texte = Label(window, text="Annuités constantes",
                  font=("Arial", 16, "bold"), borderwidth=6, relief=GROOVE)
    if(type_input == 1):
        texte1 = Label(window, text="Periodicité : " +
                       mode_input+"            Taux : Proportionnel", font=("Times New Roman ", 10, "bold"))
    if(type_input == 2):
        texte1 = Label(window, text="Periodicité : " +
                       mode_input+"              Taux : Equivalent", font=("Times New Roman ", 10, "bold"))
    # positionner les widgets avec pack
    texte.pack(pady=10, ipady=10)
    texte1.pack(pady=10, ipady=10)
    tableau.pack(side=BOTTOM, fill=X)

    window.mainloop()

# fonction qui affiche le tableau d'amortissement(in-finie)


def table_infinie():
    window = Tk()
    window.title("Tableau d'amortissement")

    n = duree_var.get()
    M = montant_var.get()
    M = float(M)
    i = taux_var.get()
    diff_input = diff_var.get()

    type_input = type_var.get()
    mode_input = var_mode.get()
    if (type_input == 1):
        if(mode_input == "Mensuelle"):
            i_f = i/1200
            d = n*12
        if(mode_input == "Trimestrielle"):
            i_f = i/400
            d = n*4
        if(mode_input == "Semestrielle"):
            i_f = i/200
            d = n*2
        if(mode_input == "Annuelle"):
            i_f = i/100
            d = n
    if(type_input == 2):
        if(mode_input == "Mensuelle"):
            i_f = i/100
            i_f = (1+i_f)**(1./12.) - 1
            d = n*12
        if(mode_input == "Trimestrielle"):
            i_f = i/100
            i_f = (1+i_f)**(1./4.) - 1
            d = n*4
        if(mode_input == "Semestrielle"):
            i_f = i/100
            i_f = (1+i_f)**(1./2.) - 1
            d = n*2
        if(mode_input == "Annuelle"):
            i_f = i/100
            d = n
    inter = M*i_f

    # creation et initialisation des colonnes du tableau
    tableau = Treeview(window, height=d+diff_input)
    tableau["columns"] = ("one", "two", "three", "four", "five")
    tableau.column("#0", width=50, minwidth=50, stretch=NO)
    tableau.column("one", width=100, minwidth=100, stretch=NO)
    tableau.column("two", width=100, minwidth=100, stretch=NO)
    tableau.column("three", width=100, minwidth=100, stretch=NO)
    tableau.column("four", width=100, minwidth=100, stretch=NO)
    tableau.column("five", width=100, minwidth=100, stretch=NO)

    tableau.heading("#0", text="Période", anchor=W)
    tableau.heading("one", text="Restant dû", anchor=W)
    tableau.heading("two", text="Intérêt", anchor=W)
    tableau.heading("three", text="Amortissement", anchor=W)
    tableau.heading("four", text="Annuité", anchor=W)
    tableau.heading("five", text="CFP", anchor=W)

    # remplir le tableau
    for j in range(diff_input):
        tableau.insert('', 'end', text=str(j+1), values=(str("%.2f" % M),
                                                         str("%.2f" % inter), str(0), str("%.2f" % inter), str(M)))

    for j in range(d-1):
        tableau.insert('', 'end', text=str(j+1+diff_input), values=(str("%.2f" % M),
                                                                    str("%.2f" % inter), str(0), str("%.2f" % inter), str(M)))

    tableau.insert('', 'end', text=str(d+diff_input), values=(str("%.2f" % M), str(
        "%.2f" % inter), str("%.2f" % M), str("%.2f" % (M+inter)), str(0)))
    texte = Label(window, text="In-fine", font=("Arial",
                                                14, "bold"), borderwidth=6, relief=GROOVE)

    if(type_input == 1):
        texte1 = Label(window, text="Periodicité : " +
                       mode_input+"    Taux : Proportionnel", font=("Times New Roman ", 10, "bold"))
    if(type_input == 2):
        texte1 = Label(window, text="Periodicité : " +
                       mode_input+"              Taux : Equivalent", font=("Times New Roman ", 10, "bold"))
    # positionner les widgets avec pack
    texte.pack(pady=10, ipady=10)
    texte1.pack(pady=10, ipady=10)
    tableau.pack(side=BOTTOM, fill=X)

    window.mainloop()


# definir la fenêtre
main = Tk()
main.geometry('{}x{}'.format(940, 350))
main.title("Calcul du coût d'emprunt")

# definir des labels
L_montant = Label(main, text="Montant : (MAD)")
L_taux = Label(main, text="Taux annuel : (%)")
L_duree = Label(main, text="Dureé : (années)")
L_diff = Label(main, text="Nombre de périodes avant le premier paiement : ")

# definir des variables de contrôle
montant_var = IntVar()
taux_var = IntVar()
duree_var = IntVar()
diff_var = IntVar()

# definir des champs pour taper
entry_montant = Entry(main, textvariable=montant_var)
entry_taux = Entry(main, textvariable=taux_var)
entry_duree = Entry(main, textvariable=duree_var)
entry_diff = Entry(main, textvariable=diff_var)

# positionnement des widgets avec grid
L_montant.grid(row=0, column=0, sticky="e", pady=20, ipady=5)
entry_montant.grid(row=0, column=1, pady=20, ipady=5)
L_diff.grid(row=0, column=2, pady=20)
entry_diff.grid(row=0, column=3, pady=0, ipady=5)
L_taux.grid(row=1, column=0, sticky="e", pady=10, ipady=5)
entry_taux.grid(row=1, column=1, pady=10, ipady=5, sticky="ew")
L_duree.grid(row=1, column=2, sticky="e", pady=10, ipady=5)
entry_duree.grid(row=1, column=3, pady=10, ipady=5, sticky="ew")


# pour le reste c'est la même chose
# on definit des widgets, et on les positionnent dans la fenêtre principale
l_mode = Label(main, text="Périodicité :")
l_mode.grid(row=2, column=0, sticky="e")
var_mode = StringVar()
mode = Combobox(main, values=["Mensuelle",
                              "Trimestrielle", "Semestrielle", "Annuelle"], textvariable=var_mode)
mode.current(3)
mode.grid(row=2, column=1)

bu_calcul = Button(main, text="Calculer le coût", command=calculer)
bu_calcul.grid(row=3, column=2, columnspan=2,
               ipady=10, ipadx=75, pady=5)


l_type = Label(main, text="Taux :")
l_type.grid(row=2, column=2, sticky="e")
type_var = IntVar()
type_var.set(1)
prop = Radiobutton(main, text="Proportionnel", variable=type_var, value=1)
prop.grid(row=2, column=3)
equiv = Radiobutton(main, text="Equivalent", variable=type_var, value=2)
equiv.grid(row=2, column=4)

ligne = Separator(main, orient=HORIZONTAL)
ligne.grid(row=4, column=0, columnspan=6,
           sticky="ew", pady=10, padx=10)

var_cout1 = StringVar()
l_type1 = Label(main, text="Amortissement constant ",
                font=("Arial", 12, "bold"))
l_cout1 = Label(main, textvariable=var_cout1)
var_cout1.set("  ")

var_cout2 = StringVar()
l_type2 = Label(main, text="Annuités constantes ", font=("Arial", 12, "bold"))
l_cout2 = Label(main, textvariable=var_cout2)
var_cout2.set("  ")

var_cout3 = StringVar()
l_type3 = Label(main, text="In-fine", font=("Arial", 12, "bold"))
l_cout3 = Label(main, textvariable=var_cout3)
var_cout3.set("  ")


bu_amort = Button(main, text="Tableau d'amortissement",
                  command=table_amort_cst)
bu_amort.grid(row=7, column=0, columnspan=1, pady=10)

bu_annui = Button(main, text="Tableau d'amortissement",
                  command=table_annui_cst)
bu_annui.grid(row=7, column=2, columnspan=1, padx=20, pady=10)

bu_infinie = Button(main, text="Tableau d'amortissement",
                    command=table_infinie)
bu_infinie.grid(row=7, column=4, columnspan=1, padx=20, pady=10)


l_type1.grid(row=5, column=0, columnspan=1, pady=10, ipady=10, padx=15)
l_cout1.grid(row=6, column=0, columnspan=1, padx=10)
l_type2.grid(row=5, column=2, columnspan=1,
             pady=10, ipady=10, padx=20,)
l_cout2.grid(row=6, column=2, padx=10)
l_type3.grid(row=5, column=4, columnspan=1,
             pady=10, ipady=10, padx=20)
l_cout3.grid(row=6, column=4, padx=10)

# afficher la fenêtre principale (main)
main.mainloop()
