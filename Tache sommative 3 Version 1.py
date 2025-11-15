# NOM : Kamgueu Tagne 
# PRENOM : Ange Nael
# Et une infos que vous ne connaissez sans doute pas c'est que j'ai beaucoup d'experience en HTML,CSS,JS,C++ 
#Donc pour moi c'est juste la syntaxe d'Ecriture de python qui est differente
# Description: J'ai ecrit un programme avec tkinter a base de la consigne de l'unité. 
# J'ai créer une Platerforme AEC(Aide Ecole Canada), qui propose 2 jeux educatifs en interface graphique et donc la difficulté varie en fonction du niveau
# J'ai essayé de mettre le plus d'outils qui nous été appris pendant l'unite et ce que j'ai appris de mes recherches personnelles
# Entre autre:des infos bulles, Frames, l'etat du bouton,multi fenetre....
# Et de ce que j'ai appris de mes recherches personnelles : Canva, Integrer les images comme arrieres plans, executer plusieurs commande en une fois

# Premiere fonction qui sert a prendre des informations sur l'utilisateur 
def info_users():
    # fonction qui recupere les infos de l'utilisateur
    def soumettreinfos():
        global nom, prenom, age, niveau #global sert a signifier que j'utilise toujours les memes variables gloabales localement
        
        nom = entnon.get()  #nom recois ce que l'utilisateur entre dans entry
        prenom = entprenon.get()    #prenom recois ce que l'utilisateur entre dans entry
        age = entage.get()  #age recois ce que l'utilisateur entre dans entry
        niveau = int(radioniveau.get())      #niveau recois ce que l'utilisateur a coche comme radibox
        
        print(f"Infos: {nom} {prenom}, {age} ans, niveau {niveau}")     #affiche les infos de l'utilisateurs dans le terminal
        def afficherinfos():
            aff_infos = tk.Toplevel(fenetre_principale,background="#fff") #creer une fenetre secondaire pour afficher les infos
            aff_infos.geometry("400x300") #taille de la fenetre
            aff_infos.title("Vos Informations")   #titre de la fenetre
            aff_infos.resizable(False,False)   #taille immodifiable
            titreaffinfos = tk.Label(aff_infos, text="Vos Informations", font="Arial 20 bold", bg="#fff",fg=couleur_textegeneral)  #creer le titre h1 de la fenetre
            titreaffinfos.pack(pady=10)     #afficher le titre
            lblnomaff = tk.Label(aff_infos,text=f"NOM : {nom}",font="Arial 15 bold",bg="#fff",fg=couleur_textegeneral)      #creer le label nom
            lblnomaff.pack(pady=5) #afficher le label nom
            lblprenomaff = tk.Label(aff_infos,text=f"PRENOM : {prenom}",font="Arial 15 bold",bg="#fff",fg=couleur_textegeneral)    #creer le label du prenom
            lblprenomaff.pack(pady=5) #afficher le label du prenom
            lblageaff = tk.Label(aff_infos,text=f"AGE : {age} ans",font="Arial 15 bold",bg="#fff",fg=couleur_textegeneral)       #creer le label de l'Age
            lblageaff.pack(pady=5)        #afficher le label de l'
            lblniveauaff = tk.Label(aff_infos,text=f"NIVEAU : {niveau}",font="Arial 15 bold",bg="#fff",fg=couleur_textegeneral)   #creer le label du niveau
            lblniveauaff.pack(pady=5)     #afficher le label du niveau
        afficherinfos()
        
        # En fonction du niveau j'assigne des parametres de difficultés differentes 
        if niveau in [1, 2]:
            btncommencer.config(command=lambda:n12jeux_1(dn12,n12,n12))
        elif niveau in [3, 4]:
            btncommencer.config(command=lambda:n12jeux_1(dn34,n34,n34))
        elif niveau in [5, 6]:
            btncommencer.config(command=lambda:n12jeux_1(dn56,n56,n56))
        
        # Activer le bouton et fermer la fenêtre d'infos
        btncommencer.config(state="normal")
        fenetre_infos.destroy()#.destroy sert a detruire les widgets donc les fenetres secondaires
        
    # creer la fenetre secondaire
    fenetre_infos = tk.Toplevel(fenetre_principale,background="#fff")#creer la fenetre secondaires de recuperation des infos
    fenetre_infos.geometry("720x510") #taille
    fenetre_infos.resizable(False,False)    #taille immodifiable
    titreinfos = tk.Label(fenetre_infos, text="A propos de vous", font="Arial 20 bold", bg="#fff",fg=couleur_textegeneral)  #creer le titre h1 de la fenetre
    titreinfos.pack(pady=10)     #afficher le titre
    lblnom = tk.Label(fenetre_infos,text="NOM : ",font="Arial 20 bold",bg="#fff",fg=couleur_textegeneral)      #creer le label nom
    lblnom.place(x=50,y=100) #afficher le label nom
    
    #creer l'entry pour recevoit la valeur du nom
    entnon = tk.Entry(fenetre_infos,font="Arial 20",
                    bd = 1,
                    highlightthickness=1,
                    highlightbackground="#000",
                    fg=couleur_textegeneral
                    )
    entnon.place(x= 200, y= 100)
    lblprenom = tk.Label(fenetre_infos,text="PRENOM : ",font="Arial 20 bold",bg="#fff",fg=couleur_textegeneral)    #creer le label du prenom
    lblprenom.place(x=50,y=170) #afficher le label du prenom
    entprenon = tk.Entry(fenetre_infos,font="Arial 20",     #creer le entry du prenom
                        bd = 1,
                    highlightthickness=1,
                    highlightbackground="#000",
                    fg=couleur_textegeneral)
    entprenon.place(x= 200, y= 170)        #afficher le entry du prenom
    lblage = tk.Label(fenetre_infos,text="Age : ",font="Arial 20 bold",bg="#fff",fg=couleur_textegeneral)       #creer le label de l'Age
    lblage.place(x=50,y=240)        #afficher le label de l'age
    entage = tk.Entry(fenetre_infos,font="Arial 20",    #creer le entry de l'Age
                    bd = 1,
                    highlightthickness=1,
                    highlightbackground="#000",
                    fg=couleur_textegeneral)
    entage.place(x= 200, y= 240)    #afficher le entry de l'age
    radioniveau = tk.StringVar()    # creer la variable des radiobox pour que le programme reconnaisse que l'utilisateur ne doit choisir qu'1 seul avec cette variable
    radioniveau.set("1")   #par defaut le niveau 1 est selectionné
    niveau1 = tk.Radiobutton(fenetre_infos, text="Niveau 1", variable=radioniveau, value="1", #creer le bouton radiobox
                            bg="#fff",
                            fg=couleur_textegeneral,
                            font="Arial 15 bold",
                            selectcolor="#fff",         #la couleur du cercle
                            activebackground="#FFF",   #la couleur du background lors du cercle
                            activeforeground = couleur_textegeneral, # la couleur du texte lors du clique 
                            bd=0,
                            highlightthickness=0,       
                            indicatoron=True,   #permet de rendre le cercle visible
                            )
    niveau1.place(x=200,y=300)  #afficher le bouton et place sert a modifier les positions comme le souhaite 
    niveau2 = tk.Radiobutton(fenetre_infos, text="Niveau 2", variable=radioniveau, value="2",
                            bg="#fff",
                            fg=couleur_textegeneral,
                            font="Arial 15 bold",
                            selectcolor="#fff",         #la couleur du cercle
                            activebackground="#FFF",   #la couleur du background lors du cercle
                            activeforeground = couleur_textegeneral, # la couleur du texte lors du clique 
                            bd=0,
                            highlightthickness=0,       
                            indicatoron=True,   #permet de rendre le cercle visible
                            )
    niveau2.place(x=200,y=350)
    niveau3 = tk.Radiobutton(fenetre_infos, text="Niveau 3", variable=radioniveau, value="3",
                            bg="#fff",
                            fg=couleur_textegeneral,
                            font="Arial 15 bold",
                            selectcolor="#fff",         #la couleur du cercle
                            activebackground="#FFF",   #la couleur du background lors du cercle
                            activeforeground = couleur_textegeneral, # la couleur du texte lors du clique 
                            bd=0,
                            highlightthickness=0,       
                            indicatoron=True,   #permet de rendre le cercle visible
                            )
    niveau3.place(x=200,y=400)
    niveau4 = tk.Radiobutton(fenetre_infos, text="Niveau 4", variable=radioniveau, value="4",
                            bg="#fff",
                            fg=couleur_textegeneral,
                            font="Arial 15 bold",
                            selectcolor="#fff",         #la couleur du cercle
                            activebackground="#FFF",   #la couleur du background lors du cercle
                            activeforeground = couleur_textegeneral, # la couleur du texte lors du clique 
                            bd=0,
                            highlightthickness=0,       
                            indicatoron=True,   #permet de rendre le cercle visible
                            )
    niveau4.place(x=370,y=300)
    niveau5 = tk.Radiobutton(fenetre_infos, text="Niveau 5", variable=radioniveau, value="5",
                            bg="#fff",
                            fg=couleur_textegeneral,
                            font="Arial 15 bold",
                            selectcolor="#fff",         #la couleur du cercle
                            activebackground="#FFF",   #la couleur du background lors du cercle
                            activeforeground = couleur_textegeneral, # la couleur du texte lors du clique 
                            bd=0,
                            highlightthickness=0,       
                            indicatoron=True,   #permet de rendre le cercle visible
                            )
    niveau5.place(x=370,y=350)
    niveau6 = tk.Radiobutton(fenetre_infos, text="Niveau 6", variable=radioniveau, value="6",
                            bg="#fff",
                            fg=couleur_textegeneral,
                            font="Arial 15 bold",
                            selectcolor="#fff",         #la couleur du cercle
                            activebackground="#FFF",   #la couleur du background lors du cercle
                            activeforeground = couleur_textegeneral, # la couleur du texte lors du clique 
                            bd=0,
                            highlightthickness=0,       
                            indicatoron=True,   #permet de rendre le cercle visible
                            )
    niveau6.place(x=370,y=400)
    #bouton soumettre qui rattache a la fonction soumettreinfos et qui donnera les informations enregistrer aux variables assignes comme vu plus haut
    btnsoumettre = tk.Button(fenetre_infos,text="Soumettre",font="Arial 20 bold",
                            bg=couleur_textegeneral,
                            fg="#fff",
                            highlightcolor=couleur_textegeneral,
                            command=soumettreinfos)
    btnsoumettre.place(x=250,y=440)

#petite fonction qui sert juste a faire la somme de 2 nombres et retourne le resultat  
def corriger(a, b, r):
    return a + b == r

def n12jeux_1(diff,no1,no2):
    def quitter_et_ouvrir():
        jeux1.destroy()  # Ferme la fenetre actuelle
        n12jeux_2(diff) #ouvre une nouvelle fenetre pour le 2eme jeux
    global score, i
    i = 0  # Compteur de questions
    score = 0  # Réinitialiser le score
    
    # Créer UNE SEULE fenetre
    jeux1 = tk.Toplevel(fenetre_principale, background=couleur_fondgeneral)
    jeux1.title("Jeux 1 : Quizz Mathématiques")
    jeux1.geometry("500x500")
    jeux1.resizable(False,False)
    
    # LAbel de presentation du jeux
    presentationj1 = tk.Label(jeux1, text="Repondez aux \n Questions",
                            font="rubik 20 bold",
                            fg=couleur_textegeneral,
                            bg=couleur_fondgeneral)
    presentationj1.pack()#afficher le label
    
    # Variables globales pour cette fenêtre
    num1 = tk.IntVar(value=0)
    num2 = tk.IntVar(value=0)
    
    # Widgets qui doivent être accessibles partout
    # label pour la question
    lblquestion = tk.Label(jeux1, text="",
                        font="Arial 45",
                        fg=couleur_textegeneral,
                        bg=couleur_fondgeneral)
    lblquestion.place(x=50,y=170)
    # label pour entre la reponse
    entreponse = tk.Entry(jeux1,
                        font="Arial 40 bold",
                        fg=couleur_textegeneral,
                        bd=1, highlightthickness=1,
                        width=3)
    entreponse.place(x=350, y=170)
    lbl_image =tk.Label()
    
    # Fonction pour la fin du jeux 
    def afficher_fin():
        
        # Masquer les widgets
        lblquestion.place_forget()  #
        entreponse.place_forget()
        btnquestion.pack_forget()
        btncorriger.place_forget()
        presentationj1.pack_forget()
        
        zone = tk.Label(jeux1, width=160,height=160,bg=couleur_fondgeneral)
        zone.place(x=175,y=335)
        
        
        # Afficher résultat final
        # Message de fin
        lblfin = tk.Label(jeux1, text="JEU TERMINÉ !", 
                         font="Rubik 40 bold",
                         fg="#fff",
                         bg=couleur_fondgeneral)
        lblfin.pack(pady=50)
        # Score de Fin
        lblscore_final = tk.Label(jeux1, text=f"Score Final :\n {score}/{diff}", 
                                 font="Arial 50 bold",
                                 fg=couleur_textegeneral,
                                 bg=couleur_fondgeneral)
        lblscore_final.pack(pady=30)
        # Bouton pour quitter et ouvrir le 2eme jeux
        btnquitter = tk.Button(jeux1, text="Suivant", 
                              font="Arial 20 bold",
                              bg="#D9D4D4",
                              fg=couleur_textegeneral,
                              command=quitter_et_ouvrir
                              )
        
        btnquitter.pack(pady=20)
    
    #Focntion qui s'occupe des calculs 
    def calculj1():
        global i
        
        i = i + 1
        
        # Vérifier si on a atteint le nombre question recquise
        if i > diff:
            afficher_fin()
            return
        
        # Générer une nouvelle question
        no1 = rand.randint(0,diff)
        no2 = rand.randint(0,diff)
        # Mettre à jour les variables
        num1.set(no1)
        num2.set(no2)
        
        # Afficher la question
        lblquestion.config(text=f"{num1.get()} + {num2.get()} = ")
        
        # Effacer l'ancienne réponse
        entreponse.delete(0, tk.END)
        entreponse.focus()
        
        lblscore.config(text=f"SCORE : {score}/{diff} ")
        
        btnquestion.config(state=tk.DISABLED)   #desactive le bouton question
        btncorriger.config(state=tk.NORMAL)     #active le bouton corriger
    
    #Fonction qui corrige le calcul
    def corriger_reponse():
        global score,lbl_image
        #pour s'assurer que l'utilisateur entre bien quelque chose j'ai inserer un try et expect
        try:
            
            reponse = int(entreponse.get())#recuperer la valeur entrée
            #verifie si le calcul est vrai ou pas
            if corriger(num1.get(), num2.get(), reponse):
                #si c'est vrai alors le score est incremente de 1
                score = score + 1
                lblscore.config(text=f"SCORE : {score}/{diff}")
                #BONNE RÉPONSE
                img_correct = Image.open("True.png")
                img_correct = img_correct.resize((160, 160))
                photo_correct = ImageTk.PhotoImage(img_correct)
                
                lbl_image = tk.Label(jeux1, image=photo_correct, bg=couleur_fondgeneral)
                lbl_image.image = photo_correct
                lbl_image.place(x=175,y=335)
            #sinon il ne bouge pas
            else:
                #MAUVAISE RÉPONSE
                img_correct = Image.open("false.png")
                img_correct = img_correct.resize((160, 160))
                photo_correct = ImageTk.PhotoImage(img_correct)
                
                lbl_image = tk.Label(jeux1, image=photo_correct, bg=couleur_fondgeneral)
                lbl_image.image = photo_correct
                lbl_image.place(x=175,y=335)
        # si l'utilisateur n'entre pas un nombre valide   
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide !")
            entreponse.delete(0, tk.END)
            entreponse.focus()
            return
        
        btnquestion.config(state=tk.NORMAL)
        btncorriger.config(state=tk.DISABLED)
        
    
    # Label qui affiche le score
    lblscore = tk.Label(jeux1, text=f"SCORE : 0/{diff} ", 
                        font="Rubik 10 bold",
                        fg=couleur_textegeneral,
                        bg=couleur_fondgeneral)
    lblscore.place(x=5,y=5)
    
    # Bouton qui appele la fonction calculj1 pour creer des question
    btnquestion = tk.Button(jeux1, text=f"Question", font="Arial 25 bold",
                        fg=couleur_textegeneral,
                        bg="#D9D4D4",
                        command=calculj1)
    aidequestion = infobulle.Hovertip(btnquestion,"Cliquer pour afficher une nouvelle question")
    #afficher le bouton
    btnquestion.pack(pady=10)
    
    #bouton qui sert a appeler la fonction corriger pour verifier si l'utilisateur a trouver ou pas
    btncorriger = tk.Button(jeux1, text="Corriger", font="Arial 25 bold",
                        fg=couleur_textegeneral,
                        bg="#D9D4D4",
                        command=corriger_reponse,
                        state=tk.DISABLED)
    aidercorriger = ""
    if btncorriger['state'] == tk.NORMAL:
        aidercorriger = infobulle.Hovertip(btncorriger,"Cliquer pour corriger votre réponse")
    btncorriger.place(x=170,y=250)
    
#Le second jeu affiche un nombre de pomme a l'Ecran et demande a l'utilisateur le nombre de pomme qu'il voit afficher a l'ecran
#il Y'a 3 propositions et l'eleve doit cliquer sur le bouton correspondant au nombre de pomme
def n12jeux_2(diff):    
    def bonnombre():
        jeux2 = tk.Toplevel(fenetre_principale, background=couleur_fondgeneral)    #creer la fenetre du second jeu
        jeux2.title("Bon Nombre")   #titre de la fenetre
        jeux2.geometry("500x600")   #taille de la fenetre
        jeux2.resizable(False, False)   # rendre la taille de la fenetre immodifiable
        
        # Initialiser les variables
        num = tk.IntVar(value=0)
        score = tk.IntVar(value=0)  
        questions_restantes = tk.IntVar(value=diff)#plus le niveau est grand et plus la diificulté sera augmenter
        
        def afficher_resultat_final():
            jeux2.destroy() #fermer la fentre jeux2
            
            # et ouvre la nouvelle Fenêtre des résultats
            fenetre_resultat = tk.Toplevel(fenetre_principale, background=couleur_fondgeneral)
            fenetre_resultat.title("Résultats")
            fenetre_resultat.geometry("400x300")
            fenetre_resultat.resizable(False, False)
            
            #label du titre jeu termine
            lbltitre = tk.Label(fenetre_resultat, text="Jeu Terminé!",
                               font="rubik 30 bold",
                               fg=couleur_textegeneral,
                               bg=couleur_fondgeneral)
            lbltitre.pack(pady=30)
            
            #label score final
            lblscore = tk.Label(fenetre_resultat, 
                               text=f"Ton score final:\n{score.get()} / {diff}",
                               font="arial 25 bold",
                               fg=couleur_textegeneral,
                               bg=couleur_fondgeneral)
            lblscore.pack(pady=20)
            
            # Message selon le score
            if score.get() == {diff}:
                message = "Parfait! "
            elif score.get() >= {diff-3}:
                message = "Bien joué"
            elif score.get() >= {diff/2}:
                message = "Bon travail!"
            else:
                message = "La prochaine fois tu feras mieux"
            
            lblmessage = tk.Label(fenetre_resultat, text=message,
                                 font="arial 20",
                                 fg=couleur_textegeneral,
                                 bg=couleur_fondgeneral)
            lblmessage.pack(pady=10)
            
            btnfermer = tk.Button(fenetre_resultat, text="Fermer",
                                 font="arial 18 bold",
                                 bg="#D9D4D4",
                                 fg=couleur_textegeneral,
                                 command=fenetre_resultat.destroy)
            btnfermer.pack(pady=20)
        
        # generation des choix aleatoirement 
        def choixs():
            # Générer le nombre aléatoire de pommes
            nombre_pommes = rand.randint(1, 6)
            num.set(nombre_pommes)
            
            # Créer 3 options différentes
            options = [nombre_pommes]  # La bonne réponse
            
            # J'ajoute 2 autres reponse mais je verifie d'abord qu'elles ne sont pas les vraies reponses grace not in
            while len(options) < 3:
                
                mauvaise_reponse = rand.randint(1, 6)
                
                if mauvaise_reponse not in options:
                    options.append(mauvaise_reponse)
            
            # Mélanger les options
            rand.shuffle(options)
            
            # Mettre à jour les boutons
            btnchoix1.config(text=options[0], state="normal")
            btnchoix2.config(text=options[1], state="normal")
            btnchoix3.config(text=options[2], state="normal")
            
            # Effacer les anciennes pommes
            for widget in zone.winfo_children():
                widget.destroy()
            
            # Afficher les nouvelles pommes
            for i in range(nombre_pommes):
                if i < 3:
                    row = 0
                    col = i
                else:
                    row = 1
                    col = i - 3
                
                lblpomme = tk.Label(zone, image=bgpomme, bg=couleur_fondgeneral)
                lblpomme.image = bgpomme
                lblpomme.grid(row=row, column=col, padx=5, pady=5)
            
            # Désactiver le bouton "Nouvelle Question"
            btnquestion.config(state="disabled")
        
        def verifier_reponse(reponse_choisie):
            # Vérifier la réponse
            if reponse_choisie == num.get():
                score.set(score.get() + 1)
                messagebox.showinfo("Bravo!", f"Bonne réponse! \nScore: {score.get()}/{diff}")
            else:
                messagebox.showerror("Oups!", f"Mauvaise réponse. C'était {num.get()}\nScore: {score.get()}/{diff}")
            
            # Décrémenter les questions restantes
            questions_restantes.set(questions_restantes.get() - 1)
            lblquestions.config(text=f"Questions restantes: {questions_restantes.get()}")
            
            # Désactiver les boutons de choix
            btnchoix1.config(state="disabled")
            btnchoix2.config(state="disabled")
            btnchoix3.config(state="disabled")
            
            # Vérifier si c'était la dernière question
            if questions_restantes.get() == 0:
                btnquestion.config(state="disabled")
                jeux2.after(1000, afficher_resultat_final)  # Attendre 1 seconde avant d'afficher les résultats
            else:
                # Réactiver le bouton "Nouvelle Question"
                btnquestion.config(state="normal")
        
        lblpresentation = tk.Label(jeux2, text="Combien de pommes \nvois-tu à l'écran ?",
                                fg=couleur_textegeneral,
                                bg=couleur_fondgeneral,
                                font="rubik 25 bold")
        lblpresentation.pack()
        
        # Label pour afficher les questions restantes
        lblquestions = tk.Label(jeux2, text=f"Questions restantes: {questions_restantes.get()}",
                               font="arial 16",
                               fg=couleur_textegeneral,
                               bg=couleur_fondgeneral)
        lblquestions.pack(pady=5)
        
        btnquestion = tk.Button(jeux2, text="Nouvelle Question", font="Arial 25 bold",
                        fg=couleur_textegeneral,
                        bg="#D9D4D4",
                        command=choixs)
        aidequestion = infobulle.Hovertip(btnquestion,"Cliquer pour afficher un nouveau nombre de pommes")
         #afficher le bouton
        btnquestion.pack(pady=10)
        
        # Inserer les images de pommes c'est la meme methode que pour le fond d'ecran image
        imgpomme = Image.open("pomme.png")
        imgpomme = imgpomme.resize((100, 100))
        bgpomme = ImageTk.PhotoImage(imgpomme)
        
        zone = tk.Frame(jeux2, width=400, height=250, bg=couleur_fondgeneral)
        zone.pack(pady=20)
        
        # creer 3 boutons qui vont recevoir les options de l'utilisateur
        btnchoix1 = tk.Button(jeux2, text="?",
                            font="arial 35 bold",
                            width=3, height=1,
                            background="#fff",
                            fg=couleur_textegeneral,
                            state="disabled",
                            command=lambda: verifier_reponse(int(btnchoix1.cget("text"))))
        btnchoix1.place(x=50, y=470)
        
        btnchoix2 = tk.Button(jeux2, text="?",
                            width=3, height=1,
                            font="arial 35 bold",
                            background="#fff",
                            fg=couleur_textegeneral,
                            state="disabled",
                            command=lambda: verifier_reponse(int(btnchoix2.cget("text"))))
        btnchoix2.place(x=190, y=470)
        
        btnchoix3 = tk.Button(jeux2, text="?",
                            font="arial 35 bold",
                            width=3, height=1,
                            background="#fff",
                            fg=couleur_textegeneral,
                            state="disabled",
                            command=lambda: verifier_reponse(int(btnchoix3.cget("text"))))
        btnchoix3.place(x=340, y=470)
        aidercorriger = infobulle.Hovertip(btnchoix1,"Cliquer sur le bouton correspondant au nombre de pommes affichées")
        aidercorriger = infobulle.Hovertip(btnchoix2,"Cliquer sur le bouton correspondant au nombre de pommes affichées")
        aidercorriger = infobulle.Hovertip(btnchoix3,"Cliquer sur le bouton correspondant au nombre de pommes affichées")
    bonnombre()



import tkinter as tk #importer tkinter sous le nom de tk
from tkinter import messagebox  #importer l'element de tkinter qui permet de creer des petites fenetres box
from PIL import Image, ImageTk #permet d'importer Image et Imagetk qui me permette de mettre une image en fond d'ecran
import random  as rand #importer random sous le nom de rand
import idlelib.tooltip as infobulle  #permet de creer les infos bulles pour guider l'utilisateurs


couleur_textegeneral = "#001F3F"   # variables qui contient la couleur de la plus part de mes textes
couleur_fondgeneral = "#00FFD0"    # variables qui contient la couleur de la plus part de mes fond

#En fonction du niveau j'ai etabli une difficulte pour le jeux 1 et jeux 2
dn12 = 10 #pour n1 et n2
dn34 = 15 #pour n3 et n4
dn56 = 20 #pour n5 et n6
n12 = rand.randint(0,dn12)      #n1 et n2
n34 = rand.randint(0,dn34)      #n3 et n4
n56 = rand.randint(0,dn56)      #n5 et n6
nom = ""        #nom
prenom = ""     #prenom
age = 0         #age
niveau = 0      #age

    
# creer la fenetre principale 
fenetre_principale = tk.Tk()    
fenetre_principale.title("Aide Ecole Canada")   #titre de la fenetre
fenetre_principale.geometry("1080x750")     #taille de la fenetre
fenetre_principale.resizable(False,False)   #rendre la fenetre immodifiable
fenetre_principale.config(background="#fff")      #Couleur du fond blanche

#Comment j'Ai inserer l'image en fonc d'ecran
dessinclasse = Image.open("dessin_salle_classe.jpg")   #grace from pil j'ai importe Image qui me permet d'importer une image et dans l'assigner a une variable
dessinclasse = dessinclasse.resize((1080,750))  #maintenant je redimensionne la taille de l'image a volonté
zoneclasse = ImageTk.PhotoImage(dessinclasse)   # variable qui recoit l'image apres modifications de la taille 
lblzoneclasse = tk.Label(fenetre_principale, image= zoneclasse)     #Maintenant je cree le label qui affichera l'image
lblzoneclasse.image = zoneclasse
lblzoneclasse.place(x=0,y=0)   
#message de bienvenue
lblbienvenue = tk.Label(fenetre_principale,text="Bienvenue sur \nAEC",
                        font="Rubik 59 bold",
                        fg="#fff",
                        bg="#108310",
                        width=14,
                        height=3)
lblbienvenue.place(x=188,y=54)  #J'ai utilise une fois de plus .place pour pouvoir la mettre a la position souhaitée

#creation du boutons infos qui sert a activer la fenetre qui recuillera les infos 
btninfos = tk.Button(fenetre_principale, text=" Infos ",font="Arial 20 bold",
                    bg="#fff",
                    fg=couleur_textegeneral
                    ,command=info_users)
# Infosbulle pour dire a l'utilisateur ce que fera le bouton infos
aideinfos = infobulle.Hovertip(btninfos,"Cliquer sur le bouton Infos pour \n pour nous donner vos informations")
btninfos.place(x=480,y=430)
score = 0 #creation de la variable pour le score
i = 0   #creation de la variable pour le compteurs
# Elles me seront toutes 2 utiles plus tard
# Le premier jeu demande juste a l'utilisateur de faire la somme de nombre qui s'affiche a l'ecran et de l'entre
#puis on verifie si il a trouve ou pas
    

# Boutton commencer qui sert a lancer la partie  
btncommencer = tk.Button(fenetre_principale, text="Commencer", bg="#fff", fg=couleur_textegeneral,
                        font="rubik 20 bold",
                        state="disabled") 
# infos bulle qui dit a l'utilisateur a quoi sert le bouton  
aidecommencer = infobulle.Hovertip(btncommencer,"Cliquer sur le bouton Commencer\n pour commencer le jeux")
btncommencer.place(x=437,y=530)
    
# lancer la fenetre
fenetre_principale.mainloop()