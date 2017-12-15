#!python3

import tkinter
import tkinter.messagebox as msgbox
import PricerConstants as cst
import sys

class ParamInterface(tkinter.Frame):
# class ParamInterface(tkinter.Tk):

    def __init__(self):

        # Master class initialisation

        self.Tk = tkinter.Tk()
        self.Tk.title("My Option Pricer ©")

        if cst.NUM_INSTANCE > 0:
            self.Tk.withdraw()

        self.fenetre = tkinter.Frame.__init__(self, self.Tk, name="mypricer")

        # Main application frame

        self.cadre1 = tkinter.Frame(self.fenetre, width=cst.FRAME_WIDTH, height=cst.FRAME_HEIGHT, borderwidth=3, background=cst.BACKGROUND_COLOR, relief=tkinter.GROOVE)

        # Title and validate/quit buttons

        self.mainMessage = tkinter.Label(self.cadre1, text='--- My Option Pricer ---', background=cst.BACKGROUND_COLOR, foreground=cst.TITLE_COLOR, font=cst.TITLE_FONT, border= cst.BORDER_WIDTH, relief=tkinter.GROOVE)
        self.validateButton = tkinter.Button(self.cadre1, text='Valider', background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT, name=cst.VALIDATE, relief=tkinter.RAISED, padx=5, pady=5)
        self.quitButton = tkinter.Button(self.cadre1, text='Quitter', background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT, name=cst.QUIT, relief=tkinter.RAISED, padx=5, pady=5)

        # Empty lines
        self.empty_line_1 = tkinter.Label(self.cadre1, background=cst.BACKGROUND_COLOR)
        self.empty_line_2 = tkinter.Label(self.cadre1, background=cst.BACKGROUND_COLOR)
        self.empty_line_3 = tkinter.Label(self.cadre1, background=cst.BACKGROUND_COLOR)
        self.empty_line_4 = tkinter.Label(self.cadre1, background=cst.BACKGROUND_COLOR)

        # Option Type
        self.productMessage = tkinter.Label(self.cadre1, text="Type d'option : ",background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)

        self.var_product = tkinter.StringVar()
        self.product_frame = tkinter.Frame(self.cadre1)
        self.radio_product_call = tkinter.Radiobutton(self.product_frame, text="Call", variable=self.var_product, value=cst.CALL, background=cst.BACKGROUND_COLOR, borderwidth=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, font=cst.NORMAL_FONT, indicatoron=0)
        self.radio_product_put = tkinter.Radiobutton(self.product_frame, text="Put", variable=self.var_product, value=cst.PUT, background=cst.BACKGROUND_COLOR, borderwidth=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, font=cst.NORMAL_FONT, indicatoron=0)

        # Option Features
        self.featureMessage = tkinter.Label(self.cadre1, text="Caractéristiques : ",background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
        self.var_feature = tkinter.StringVar()

        self.feature_frame = tkinter.Frame(self.cadre1)
        self.feature_frame2 = tkinter.Frame(self.cadre1)
        self.radio_feature_vanilla = tkinter.Radiobutton(self.feature_frame, text=cst.VANILLA, variable=self.var_feature,value=cst.VANILLA, background=cst.BACKGROUND_COLOR,borderwidth=cst.BORDER_WIDTH, relief=tkinter.SUNKEN,font=cst.NORMAL_FONT, name = cst.VANILLA.lower())
        #self.radio_feature_american = tkinter.Radiobutton(self.feature_frame, text=cst.AMERICAN, variable=self.var_feature,value=cst.AMERICAN, background=cst.BACKGROUND_COLOR,borderwidth=cst.BORDER_WIDTH, relief=tkinter.SUNKEN,font=cst.NORMAL_FONT, name = cst.AMERICAN.lower())
        self.radio_feature_barrier = tkinter.Radiobutton(self.feature_frame2, text=cst.BARRIER, variable=self.var_feature, value=cst.BARRIER, background=cst.BACKGROUND_COLOR, borderwidth=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, font=cst.NORMAL_FONT, name = cst.BARRIER.lower())
        self.radio_feature_asian = tkinter.Radiobutton(self.feature_frame2, text=cst.ASIAN, variable=self.var_feature, value=cst.ASIAN, background=cst.BACKGROUND_COLOR, borderwidth=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, font=cst.NORMAL_FONT, name = cst.ASIAN.lower())

        # Currency Conversion
        self.check_Convert = tkinter.IntVar()
        self.widg_Convert = tkinter.Checkbutton(self.cadre1, text="Devise de conversion (base : EUR) ?", variable=self.check_Convert, background=cst.BACKGROUND_COLOR, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, font=cst.NORMAL_FONT)

        # Paramètres de l'option...

        # ... Strike
        self.msgStrike = tkinter.Label(self.cadre1, text="Strike de l'option (% du spot) : ", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
        # self.strike = tkinter.Entry(self.cadre1, width= 30)

        self.strikeVal = tkinter.DoubleVar
        self.strike = tkinter.Scale(self.cadre1, variable=self.strikeVal, orient=tkinter.HORIZONTAL, from_=50, to=150, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN)

        # ... Spot
        self.msgSpot = tkinter.Label(self.cadre1, text="Spot du sous-jacent : ", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
        self.spot = tkinter.Entry(self.cadre1, width=30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN)
        default_spot = 100
        self.spot.insert(tkinter.END, default_spot)

        # ... Maturité
        self.msgMaturite = tkinter.Label(self.cadre1, text="Maturité de l'option : ", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
        self.maturite = tkinter.Entry(self.cadre1, width= 30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN)
        default_matu = 1
        self.maturite.insert(tkinter.END, default_matu)

        # ... Risk free rate
        self.msgTauxSansRisque = tkinter.Label(self.cadre1, text="Taux sans risque : ", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
        self.taux_sans_risque = tkinter.Entry(self.cadre1, width= 30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN)
        default_rf = 0.02
        self.taux_sans_risque.insert(tkinter.END, default_rf)

        # ... Volatilité
        self.msgVolat = tkinter.Label(self.cadre1, text="Volatilité du sous jacent : ", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
        self.volat = tkinter.Entry(self.cadre1, width=30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN)
        default_volat = 0.05
        self.volat.insert(tkinter.END, default_volat)

        # Méthode de pricing
        self.listMessage = tkinter.Label(self.cadre1, text='Méthode de pricing : ', background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
        self.pricingMethod = tkinter.Listbox(self.cadre1, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, height=5)
        self.pricingMethod.insert(tkinter.END, cst.BSM_NAME)
        self.pricingMethod.insert(tkinter.END, cst.MC_NAME )
        self.pricingMethod.insert(tkinter.END, cst.BINOM_NAME)

        if self.pricingMethod.curselection() == cst.BLACKSCHOLES:
            self.pricingMethod.activate(cst.BLACKSCHOLES[0])
        elif self.pricingMethod.curselection() == cst.MONTECARLO:
            self.pricingMethod.activate(cst.MONTECARLO[0])
        elif self.pricingMethod.curselection() == cst.BINOMIAL:
            self.pricingMethod.activate(cst.BINOMIAL[0])

        # Add Params functions : Events Management

        self.txtNbSimul = tkinter.Label(self.fenetre, text="Nombres de simulations à effectuer :", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
        self.nbSimul = tkinter.Entry(self.fenetre, width=30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, name=cst.NBSIMUL)
        default_simul = 200
        self.nbSimul.insert(tkinter.END, default_simul)

        self.convert_devise = tkinter.Entry(self.cadre1, width=30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, name=cst.CONVERT)
        self.convert_message = tkinter.Label(self.cadre1, text="Merci d'indiquez laquelle : ", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
        default_devise = "CHF"
        self.convert_devise.insert(tkinter.END, default_devise)

        # Bind Events

        self.radio_product_call.bind('<Enter>', func=self.button_highlight)
        self.radio_product_call.bind('<Leave>', func=self.button_offlight)
        self.radio_product_put.bind('<Enter>', func=self.button_highlight)
        self.radio_product_put.bind('<Leave>', func=self.button_offlight)

        self.radio_product_call.bind('<ButtonPress>', func=self.button_click)
        self.radio_product_put.bind('<ButtonPress>', func=self.button_click)
        self.radio_product_call.bind('<ButtonRelease>', func=self.button_offclick)
        self.radio_product_put.bind('<ButtonRelease>', func=self.button_offclick)

        self.pricingMethod.bind("<ButtonRelease>", func=self.addParamsPricing)
        self.widg_Convert.bind("<ButtonRelease>", func=self.addParamsConvert)

        self.cadre1.bind("<KeyRelease>", func=self.enter)
        self.cadre1.bind("<Button-1>", func=self.focus_on)

        self.quitButton.bind("<Enter>", func=self.button_highlight)
        self.validateButton.bind("<Enter>", func=self.button_highlight)
        self.quitButton.bind("<Leave>", func=self.button_offlight)
        self.validateButton.bind("<Leave>", func=self.button_offlight)

        self.quitButton.bind("<ButtonPress>", func=self.button_click)
        self.validateButton.bind("<ButtonPress>", func=self.button_click)
        self.quitButton.bind("<ButtonRelease>", func=self.button_offclick)
        self.validateButton.bind("<ButtonRelease>", func=self.button_offclick)

        self.spot.bind("<Enter>", func=self.entry_highlight)
        self.maturite.bind("<Enter>", func=self.entry_highlight)
        self.taux_sans_risque.bind("<Enter>", func=self.entry_highlight)
        self.volat.bind("<Enter>", func=self.entry_highlight)

        self.spot.bind("<Leave>", func=self.entry_offlight)
        self.maturite.bind("<Leave>", func=self.entry_offlight)
        self.taux_sans_risque.bind("<Leave>", func=self.entry_offlight)
        self.volat.bind("<Leave>", func=self.entry_offlight)

        self.radio_feature_vanilla.bind("<ButtonRelease>", func=self.add_feature)
        self.radio_feature_barrier.bind("<ButtonRelease>", func=self.add_feature)
        self.radio_feature_asian.bind("<ButtonRelease>", func=self.add_feature)
        #self.radio_feature_american.bind("<ButtonRelease>", func=self.add_feature)

        # Pack
        self.mainMessage.pack(side="top")
        self.cadre1.pack(side="top", fill=tkinter.BOTH)
        self.productMessage.pack()
        self.product_frame.pack()
        self.radio_product_call.pack(side=tkinter.LEFT)
        self.radio_product_put.pack(side=tkinter.RIGHT)
        self.featureMessage.pack()
        self.feature_frame.pack()
        self.feature_frame2.pack()
        self.radio_feature_vanilla.pack(side=tkinter.TOP)
        #self.radio_feature_american.pack(side=tkinter.LEFT)
        self.radio_feature_asian.pack(side=tkinter.RIGHT)
        self.radio_feature_barrier.pack(side=tkinter.LEFT)
        self.widg_Convert.pack()
        self.msgStrike.pack()
        self.strike.pack()
        self.msgSpot.pack()
        self.spot.pack()
        self.msgMaturite.pack()
        self.maturite.pack()
        self.msgTauxSansRisque.pack()
        self.taux_sans_risque.pack()
        self.msgVolat.pack()
        self.volat.pack()
        self.listMessage.pack()
        self.pricingMethod.pack()

        self.validateButton.pack(side="bottom")
        self.quitButton.pack(side="bottom")

        cst.NUM_INSTANCE += 1

    def add_feature(self, event):

        if str(event.widget).split(".")[-1].upper() == cst.VANILLA or str(event.widget).split(".")[-1].upper() == cst.AMERICAN :
            try:
                self.feature_val_barrier.pack_forget()
            except:
                pass
            try:
                self.feature_val_asian.pack_forget()
            except:
                pass
            try:
                self.feature.pack_forget()
            except:
                pass
        elif str(event.widget).split(".")[-1].upper() == cst.ASIAN or str(event.widget).split(".")[-1].upper() == cst.BARRIER:
            try:
                try:
                    self.widg_Convert.pack_forget()
                    self.convert_devise.pack_forget()
                    self.convert_message.pack_forget()
                    self.msgStrike.pack_forget()
                    self.strike.pack_forget()
                    self.msgSpot.pack_forget()
                    self.spot.pack_forget()
                    self.msgMaturite.pack_forget()
                    self.maturite.pack_forget()
                    self.msgTauxSansRisque.pack_forget()
                    self.taux_sans_risque.pack_forget()
                    self.msgVolat.pack_forget()
                    self.volat.pack_forget()
                    self.listMessage.pack_forget()
                    self.pricingMethod.pack_forget()
                    self.txtNbSimul.destroy()
                    self.nbSimul.destroy()
                    self.quitButton.pack_forget()
                    self.validateButton.pack_forget()

                    try:
                        self.feature_val_asian.pack_forget()
                    except:
                        pass
                    try:
                        self.feature_val_barrier.pack_forget()
                    except:
                        pass
                    try:
                        self.feature.pack_forget()
                    except:
                        pass
                except:
                    pass

                self.feature_val_asian = tkinter.Label(self.cadre1, text="Nombres de jours :",background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
                self.feature_val_barrier = tkinter.Label(self.cadre1, text="Barrière (% du strike) :",background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
                self.feature = tkinter.Entry(self.cadre1, width=30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN)

                self.convert_devise = tkinter.Entry(self.cadre1, width=30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, name=cst.CONVERT)
                self.convert_message = tkinter.Label(self.cadre1, text="Merci d'indiquez laquelle : ", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
                default_devise = "CHF"
                self.convert_devise.insert(tkinter.END, default_devise)

                self.txtNbSimul = tkinter.Label(self.cadre1, text="Nombres de simulations à effectuer :", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
                self.nbSimul = tkinter.Entry(self.cadre1, width=30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, name=cst.NBSIMUL)
                default_simul = 200
                self.nbSimul.insert(tkinter.END, default_simul)

                self.nbSimul.bind("<Enter>", func=self.entry_highlight)
                self.nbSimul.bind("<Leave>", func=self.entry_offlight)
                self.convert_devise.bind("<Enter>", func=self.entry_highlight)
                self.convert_devise.bind("<Leave>", func=self.entry_offlight)
                self.feature.bind("<Enter>", func=self.entry_highlight)
                self.feature.bind("<Leave>", func=self.entry_offlight)

                if str(event.widget).split(".")[-1].upper() == cst.ASIAN:
                    self.feature_val_asian.pack(side="top")
                else:
                    self.feature_val_barrier.pack(side="top")

                self.feature.pack()
                self.widg_Convert.pack()

                if self.check_Convert.get() == 1:
                    self.convert_message.pack()
                    self.convert_devise.pack()

                self.msgStrike.pack()
                self.strike.pack()
                self.msgSpot.pack()
                self.spot.pack()
                self.msgMaturite.pack()
                self.maturite.pack()
                self.msgTauxSansRisque.pack()
                self.taux_sans_risque.pack()
                self.msgVolat.pack()
                self.volat.pack()
                self.listMessage.pack()
                self.pricingMethod.pack()

                if self.pricingMethod.curselection() == cst.MONTECARLO or self.pricingMethod.curselection() == cst.BINOMIAL:
                    self.txtNbSimul.pack()
                    self.nbSimul.pack()

                self.validateButton.pack(side="bottom")
                self.quitButton.pack(side="bottom")
            except:
                pass
        else:
            try:
                self.convert_devise.destroy()
                self.convert_message.destroy()
            except:
                pass

    def addParamsPricing(self, event):
        if self.pricingMethod.curselection() == cst.MONTECARLO or self.pricingMethod.curselection() == cst.BINOMIAL:
            try:
                try:
                    self.validateButton.destroy()
                    self.quitButton.destroy()
                    self.txtNbSimul.destroy()
                    self.nbSimul.destroy()
                except:
                    pass

                self.txtNbSimul = tkinter.Label(self.cadre1, text="Nombres de simulations à effectuer :", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
                self.nbSimul = tkinter.Entry(self.cadre1, width=30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, name=cst.NBSIMUL)
                default_simul = 200
                self.nbSimul.insert(tkinter.END, default_simul)

                self.nbSimul.bind("<Enter>", func=self.entry_highlight)
                self.nbSimul.bind("<Leave>", func=self.entry_offlight)

                self.validateButton = tkinter.Button(self.cadre1, text='Valider', background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT,name=cst.VALIDATE, relief=tkinter.RAISED, padx=5, pady=5)
                self.quitButton = tkinter.Button(self.cadre1, text='Quitter', background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT, name=cst.QUIT, relief=tkinter.RAISED, padx=5, pady=5)

                self.quitButton.bind("<Enter>", func=self.button_highlight)
                self.validateButton.bind("<Enter>", func=self.button_highlight)
                self.quitButton.bind("<Leave>", func=self.button_offlight)
                self.validateButton.bind("<Leave>", func=self.button_offlight)

                self.quitButton.bind("<ButtonPress>", func=self.button_click)
                self.validateButton.bind("<ButtonPress>", func=self.button_click)
                self.quitButton.bind("<ButtonRelease>", func=self.button_offclick)
                self.validateButton.bind("<ButtonRelease>", func=self.button_offclick)

                self.txtNbSimul.pack()
                self.nbSimul.pack()
                self.validateButton.pack(side="bottom")
                self.quitButton.pack(side="bottom")

            except:
                pass
        else:
            try:
                self.txtNbSimul.destroy()
                self.nbSimul.destroy()
            except:
                pass

    def addParamsConvert(self, event):
        if self.check_Convert.get() == 0:
            try:
                try:
                    self.convert_devise.pack_forget()
                    self.convert_message.pack_forget()
                    self.msgStrike.pack_forget()
                    self.strike.pack_forget()
                    self.msgSpot.pack_forget()
                    self.spot.pack_forget()
                    self.msgMaturite.pack_forget()
                    self.maturite.pack_forget()
                    self.msgTauxSansRisque.pack_forget()
                    self.taux_sans_risque.pack_forget()
                    self.msgVolat.pack_forget()
                    self.volat.pack_forget()
                    self.listMessage.pack_forget()
                    self.pricingMethod.pack_forget()
                    self.txtNbSimul.destroy()
                    self.nbSimul.destroy()
                    self.quitButton.pack_forget()
                    self.validateButton.pack_forget()
                except:
                    pass

                self.convert_devise = tkinter.Entry(self.cadre1, width=30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, name=cst.CONVERT)
                self.convert_message = tkinter.Label(self.cadre1, text="Merci d'indiquez laquelle : ", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
                default_devise = "CHF"
                self.convert_devise.insert(tkinter.END, default_devise)

                self.txtNbSimul = tkinter.Label(self.cadre1, text="Nombres de simulations à effectuer :", background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)
                self.nbSimul = tkinter.Entry(self.cadre1, width=30, border=cst.BORDER_WIDTH, relief=tkinter.SUNKEN, name=cst.NBSIMUL)
                default_simul = 200
                self.nbSimul.insert(tkinter.END, default_simul)

                self.nbSimul.bind("<Enter>", func=self.entry_highlight)
                self.nbSimul.bind("<Leave>", func=self.entry_offlight)
                self.convert_devise.bind("<Enter>", func=self.entry_highlight)
                self.convert_devise.bind("<Leave>", func=self.entry_offlight)

                self.convert_message.pack(side="top", fill=tkinter.X)
                self.convert_devise.pack()
                self.msgStrike.pack()
                self.strike.pack()
                self.msgSpot.pack()
                self.spot.pack()
                self.msgMaturite.pack()
                self.maturite.pack()
                self.msgTauxSansRisque.pack()
                self.taux_sans_risque.pack()
                self.msgVolat.pack()
                self.volat.pack()
                self.listMessage.pack()
                self.pricingMethod.pack()

                if self.pricingMethod.curselection() == cst.MONTECARLO or self.pricingMethod.curselection() == cst.BINOMIAL:
                    self.txtNbSimul.pack()
                    self.nbSimul.pack()

                self.validateButton.pack(side="bottom")
                self.quitButton.pack(side="bottom")
            except:
                pass
        else:
            try:
                self.convert_devise.destroy()
                self.convert_message.destroy()
            except:
                pass

    def validate(self):

        if msgbox.askyesno("Valider", "Les paramètres sont ils corrects ?\nVous ne pourrez plus les modifier"):
            self.quit()
        else:
            pass

    def quitter(self):

        if msgbox.askyesno("Quitter", "Etes vous sûr de vouloir quitter ? "):
            self.quit()
            sys.exit()
        else:
            pass

    def enter(self, event):

        touche = event.keysym

        if touche == cst.RETURN_KEY:
            self.validate()
        if touche == cst.ESCAPE_KEY:
            self.quitter()

    def focus_on(self, event):
        self.cadre1.focus_set()

    def button_highlight(self, event):

        if str(event.widget).split(".")[-1] == cst.VALIDATE:

            self.quitButton.configure(foreground=cst.BUTTON_OFF)
            self.validateButton.configure(foreground=cst.BUTTON_ON)

            self.validateButton.update()
            self.quitButton.update()

        elif str(event.widget).split(".")[-1] == cst.QUIT:

            self.quitButton.configure(foreground=cst.BUTTON_ON)
            self.validateButton.configure(foreground=cst.BUTTON_OFF)

            self.validateButton.update()
            self.quitButton.update()

        elif str(event.widget).split(".")[-1] == "!radiobutton":
            self.radio_product_call.configure(foreground=cst.BUTTON_ON)
            self.radio_product_call.update()

        elif str(event.widget).split(".")[-1] == "!radiobutton2":
            self.radio_product_put.configure(foreground=cst.BUTTON_ON)
            self.radio_product_put.update()

    def button_offlight(self, event):

        if str(event.widget).split(".")[-1] == cst.VALIDATE:

            self.quitButton.configure(foreground=cst.BUTTON_ON)
            self.validateButton.configure(foreground=cst.BUTTON_OFF)

            self.validateButton.update()
            self.quitButton.update()

        elif str(event.widget).split(".")[-1] == cst.QUIT:

            self.quitButton.configure(foreground=cst.BUTTON_OFF)
            self.validateButton.configure(foreground=cst.BUTTON_ON)

            self.validateButton.update()
            self.quitButton.update()

        elif str(event.widget).split(".")[-1] == "!radiobutton":
            self.radio_product_call.configure(foreground=cst.BUTTON_OFF)
            self.radio_product_call.update()

        elif str(event.widget).split(".")[-1] == "!radiobutton2":
            self.radio_product_put.configure(foreground=cst.BUTTON_OFF)
            self.radio_product_put.update()

    def entry_highlight(self, event):

        if str(event.widget).split(".")[-1] == '!entry':
            self.spot.configure(background=cst.ENTRY_ON)
            self.spot.update()
        elif str(event.widget).split(".")[-1] == '!entry2':
            self.maturite.configure(background=cst.ENTRY_ON)
            self.maturite.update()
        elif str(event.widget).split(".")[-1] == '!entry3':
            self.taux_sans_risque.configure(background=cst.ENTRY_ON)
            self.taux_sans_risque.update()
        elif str(event.widget).split(".")[-1] == '!entry4':
            self.volat.configure(background=cst.ENTRY_ON)
            self.volat.update()
        elif str(event.widget).split(".")[-1] == cst.CONVERT:
            self.convert_devise.configure(background=cst.ENTRY_ON)
            self.convert_devise.update()
        elif str(event.widget).split(".")[-1] == cst.NBSIMUL:
            self.nbSimul.configure(background=cst.ENTRY_ON)
            self.nbSimul.update()
        elif str(event.widget).split(".")[-1] == cst.FEATURE:
            self.nbSimul.configure(background=cst.ENTRY_ON)
            self.nbSimul.update()
        elif str(event.widget).split(".")[-1] == cst.BARRIER:
            self.feature.configure(background=cst.ENTRY_ON)
            self.feature.update()
        elif str(event.widget).split(".")[-1] == cst.ASIAN:
            self.feature.configure(background=cst.ENTRY_ON)
            self.feature.update()
        elif '!entry' in str(event.widget).split(".")[-1]:
            self.feature.configure(background=cst.ENTRY_ON)
            self.feature.update()

    def entry_offlight(self, event):

        if str(event.widget).split(".")[-1] == '!entry':
            self.spot.configure(background=cst.ENTRY_OFF)
            self.spot.update()
        elif str(event.widget).split(".")[-1] == '!entry2':
            self.maturite.configure(background=cst.ENTRY_OFF)
            self.maturite.update()
        elif str(event.widget).split(".")[-1] == '!entry3':
            self.taux_sans_risque.configure(background=cst.ENTRY_OFF)
            self.taux_sans_risque.update()
        elif str(event.widget).split(".")[-1] == '!entry4':
            self.volat.configure(background=cst.ENTRY_OFF)
            self.volat.update()
        elif str(event.widget).split(".")[-1] == cst.CONVERT:
            self.convert_devise.configure(background=cst.ENTRY_OFF)
            self.convert_devise.update()
        elif str(event.widget).split(".")[-1] == cst.NBSIMUL:
            self.nbSimul.configure(background=cst.ENTRY_OFF)
            self.nbSimul.update()
        elif str(event.widget).split(".")[-1] == cst.BARRIER:
            self.feature.configure(background=cst.ENTRY_OFF)
            self.feature.update()
        elif str(event.widget).split(".")[-1] == cst.ASIAN:
            self.feature.configure(background=cst.ENTRY_OFF)
            self.feature.update()
        elif '!entry' in str(event.widget).split(".")[-1]:
            self.feature.configure(background=cst.ENTRY_OFF)
            self.feature.update()

    def button_click(self, event):
        if str(event.widget).split(".")[-1] == cst.VALIDATE:
            self.validateButton.configure(relief=tkinter.SUNKEN)
            self.validateButton.update()
            self.validate()
        if str(event.widget).split(".")[-1] == cst.QUIT:
            self.quitButton.configure(relief=tkinter.SUNKEN)
            self.quitButton.update()
            self.quitter()
        if str(event.widget).split(".")[-1] == "!radiobutton":
            self.radio_product_call.select()
        if str(event.widget).split(".")[-1] == "!radiobutton2":
            self.radio_product_put.select()

    def button_offclick(self, event):
        if str(event.widget).split(".")[-1] == cst.VALIDATE:
            self.validateButton.configure(relief=tkinter.RAISED)
            self.validateButton.update()
        if str(event.widget).split(".")[-1] == cst.QUIT:
            self.quitButton.configure(relief=tkinter.RAISED)
            self.quitButton.update()


class ResultInterface(tkinter.Frame):

    def __init__(self, oneOptionPricer, methodPricing, prix):

        # Init
        self.Tk = tkinter.Tk()
        self.Tk.title("My Option Pricer ©")

        if cst.NUM_INSTANCE > 1:
            self.Tk.withdraw()

        self.fenetre = tkinter.Frame.__init__(self, width=cst.FRAME_WIDTH, height=cst.FRAME_HEIGHT, background=cst.BACKGROUND_COLOR)
        self.optionPricer = oneOptionPricer
        self.end = True

        # Widgets ...

        # ... Cadres
        self.cadre1 = tkinter.Frame(self.fenetre, width=cst.FRAME_WIDTH, height=cst.FRAME_HEIGHT, borderwidth=cst.BORDER_WIDTH, background=cst.BACKGROUND_COLOR)
        self.cadreParam = tkinter.LabelFrame(self.cadre1, text="Paramètres du pricing", width=cst.FRAME_WIDTH, height=cst.FRAME_HEIGHT, borderwidth=cst.BORDER_WIDTH, background=cst.BACKGROUND_COLOR, relief=tkinter.SUNKEN, padx=5, pady=5)
        self.cadreResult = tkinter.LabelFrame(self.cadre1, text="Résultat du pricing", width=cst.FRAME_WIDTH, height=cst.FRAME_HEIGHT, borderwidth=cst.BORDER_WIDTH, background=cst.BACKGROUND_COLOR, relief=tkinter.SUNKEN, padx=5, pady=5)

        # ... Title
        self.mainMessage = tkinter.Label(self.cadre1, text='--- My Option Pricer ---', background=cst.BACKGROUND_COLOR, foreground=cst.TITLE_COLOR, font=cst.TITLE_FONT, border= cst.BORDER_WIDTH, relief=tkinter.GROOVE)

        # ... Buttons
        self.quitButton = tkinter.Button(self.cadre1, text='Quitter', command=self.quitter, background=cst.BACKGROUND_COLOR, name=cst.QUIT, padx=5, pady=5)
        self.retryButton = tkinter.Button(self.cadre1, text="Recommencer", command=self.retry, background=cst.BACKGROUND_COLOR, name=cst.RETRY, padx=5, pady=5)

        # ... Result Messages
        self.params = "Type d'Option :                  " + self.optionPricer.optionType + \
                      "\nCaractéristique :                " + self.optionPricer.feature

        if self.optionPricer.feature != cst.VANILLA :
            if self.optionPricer.feature == cst.BARRIER:
                self.params += "\nBarrière :                            " + str(self.optionPricer.barrier)
            elif self.optionPricer.feature == cst.ASIAN:
                self.params += "\nMéthode de calcul :           Strike-moyen " + str(self.optionPricer.asian_days) + "J"

        try:
            self.params += "\nDevise :                              " + self.optionPricer.devise + \
                           "\nMéthode de Pricing :         " + methodPricing + \
                           "\nStrike :                               " + str(self.optionPricer.strike) + \
                           "\nSpot :                                 " + str(self.optionPricer.spot) + \
                           "\nMaturité :                           " + str(self.optionPricer.maturite) + " an(s) " + \
                           "\nVolatilité :                           " + str(self.optionPricer.volat) + \
                           "\nTaux sans risque :             " + str(self.optionPricer.taux_sans_risque)
        except:
            self.params = "LOADING PARAMS FAILED"

        self.msgParams = tkinter.Label(self.cadreParam, text=self.params, background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT, justify=tkinter.LEFT)

        try:
            self.result = "\nPrix du " + str(self.optionPricer.optionType) + " :        " + str(round(prix, 4)) + \
                          " " + self.optionPricer.devise + \
                          "\nDelta :     " + str(round(self.optionPricer.delta,4)) + \
                          "\nVega :      " + str(round(self.optionPricer.vega,4)) + \
                          "\nGamma : " + str(round(self.optionPricer.gamma,4))
        except:
            self.result = "PRICING FAILED"

        self.msgResult = tkinter.Label(self.cadreResult, text=self.result, background=cst.BACKGROUND_COLOR, font=cst.NORMAL_FONT)

        # Bind

        self.cadre1.bind("<Button-1>", func=self.focus_on)
        self.cadreParam.bind("<Button-1>", func=self.focus_on)
        self.cadreResult.bind("<Button-1>", func=self.focus_on)

        self.cadre1.bind("<KeyRelease>", func=self.enter)
        self.cadreParam.bind("<KeyRelease>", func=self.enter)
        self.cadreResult.bind("<KeyRelease>", func=self.enter)

        self.quitButton.bind("<Enter>", func=self.button_highlight)
        self.retryButton.bind("<Enter>", func=self.button_highlight)
        self.quitButton.bind("<Leave>", func=self.button_offlight)
        self.retryButton.bind("<Leave>", func=self.button_offlight)

        # Pack
        self.mainMessage.pack()
        self.cadre1.pack(side="top", fill=tkinter.BOTH)
        self.cadreParam.pack(side="top", fill=tkinter.BOTH)
        self.cadreResult.pack(side="top", fill=tkinter.BOTH)
        self.msgParams.pack(fill=tkinter.BOTH,expand=tkinter.TRUE)
        self.msgResult.pack(fill=tkinter.BOTH,expand=tkinter.TRUE)

        self.quitButton.pack(side="bottom")
        self.retryButton.pack(side="bottom")

    def retry(self):

        if msgbox.askyesno("Réessayer", "Etes vous sûr de vouloir recommencer ? "):
            self.mainMessage.destroy()
            self.cadre1.destroy()
            self.msgParams.destroy()
            self.msgResult.destroy()
            self.quitButton.destroy()
            self.retryButton.destroy()
            self.end = False
            self.quit()
        else:
            pass

    def quitter(self):

        if msgbox.askyesno("Quitter", "Etes vous sûr de vouloir quitter ? "):
            self.quit()
            exit(0)
        else:
            pass

    def focus_on(self, event):
        self.cadre1.focus_set()

    def enter(self, event):

        touche = event.keysym

        if touche == cst.RETURN_KEY:
            self.retry()
        if touche == cst.ESCAPE_KEY:
            self.quitter()

    def button_highlight(self, event):

        if str(event.widget).split(".")[-1] == cst.RETRY:

            self.quitButton.configure(foreground=cst.BUTTON_OFF)
            self.retryButton.configure(foreground=cst.BUTTON_ON)

            self.retryButton.update()
            self.quitButton.update()

        elif str(event.widget).split(".")[-1] == cst.QUIT:

            self.quitButton.configure(foreground=cst.BUTTON_ON)
            self.retryButton.configure(foreground=cst.BUTTON_OFF)

            self.retryButton.update()
            self.quitButton.update()

    def button_offlight(self, event):

        self.quitButton.configure(foreground=cst.BUTTON_OFF)
        self.retryButton.configure(foreground=cst.BUTTON_OFF)

        self.retryButton.update()
        self.quitButton.update()
