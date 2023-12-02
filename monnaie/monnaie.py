import tkinter as tk
from tkinter import ttk, messagebox

class ConvertisseurDeDevises:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        fenetre.title("Convertisseur de Devises")
        fenetre.configure(bg='light gray')

        # Styles
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 12), background='light gray')
        style.configure('TButton', font=('Helvetica', 12))
        style.configure('TEntry', font=('Helvetica', 12))
        style.configure('TCombobox', font=('Helvetica', 12))

        # Taux de change (exemple statique)
        self.taux_de_change = {
            "USD": 1.0,  # Dollar Américain
            "EUR": 0.85,  # Euro
            "GBP": 0.75,  # Livre Sterling
            "JPY": 110.0  # Yen Japonais
        }

        # Interface utilisateur
        self.montant_label = ttk.Label(fenetre, text="Montant:", background='light gray')
        self.montant_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.montant_entry = ttk.Entry(fenetre, width=20)
        self.montant_entry.grid(row=0, column=1, padx=10, pady=10)

        self.devise_depart_label = ttk.Label(fenetre, text="Devise de départ:", background='light gray')
        self.devise_depart_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.devise_depart_combobox = ttk.Combobox(fenetre, values=list(self.taux_de_change.keys()), width=18)
        self.devise_depart_combobox.grid(row=1, column=1, padx=10, pady=10)

        self.devise_cible_label = ttk.Label(fenetre, text="Devise cible:", background='light gray')
        self.devise_cible_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.devise_cible_combobox = ttk.Combobox(fenetre, values=list(self.taux_de_change.keys()), width=18)
        self.devise_cible_combobox.grid(row=2, column=1, padx=10, pady=10)

        self.convertir_button = ttk.Button(fenetre, text="Convertir", command=self.convertir)
        self.convertir_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.resultat_label = ttk.Label(fenetre, text="Résultat:", background='light gray')
        self.resultat_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.resultat_value = ttk.Label(fenetre, text="", font=('Helvetica', 12, 'bold'), background='light gray')
        self.resultat_value.grid(row=4, column=1, padx=10, pady=10)

    def convertir(self):
        try:
            montant = float(self.montant_entry.get())
            devise_depart = self.devise_depart_combobox.get()
            devise_cible = self.devise_cible_combobox.get()

            taux_depart = self.taux_de_change[devise_depart]
            taux_cible = self.taux_de_change[devise_cible]

            montant_en_usd = montant / taux_depart
            montant_converti = montant_en_usd * taux_cible

            self.resultat_value.config(text=f"{montant_converti:.2f} {devise_cible}")
        except KeyError:
            messagebox.showerror("Erreur", "Devise non prise en charge.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")

fenetre = tk.Tk()
app = ConvertisseurDeDevises(fenetre)
fenetre.mainloop()
