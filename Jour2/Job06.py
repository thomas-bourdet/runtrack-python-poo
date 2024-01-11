class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}
        self._statut_commande = "en cours"

    def ajouterPlat(self, nom_plat, prix):
        if self._statut_commande == "en cours":
            if nom_plat not in self._plats_commandes:
                self._plats_commandes[nom_plat] = {"prix": prix, "statut": "en cours"}
                print(f"Plat '{nom_plat}' ajouté à la commande.")
            else:
                print(f"Le plat '{nom_plat}' est déjà dans la commande.")
        else:
            print("Impossible d'ajouter un plat, la commande n'est plus en cours.")

    def annulerCommande(self):
        if self._statut_commande == "en cours":
            self._statut_commande = "annulée"
            print("La commande a été annulée.")
        else:
            print("Impossible d'annuler la commande, elle est déjà terminée ou annulée.")

    def _calculerTotal(self):
        total = sum(plat["prix"] for plat in self._plats_commandes.values() if plat["statut"] == "en cours")
        return total

    def afficherCommande(self):
        total = self._calculerTotal()
        print(f"\nCommande #{self._numero_commande} - Statut: {self._statut_commande}")
        print("Plats commandés:")
        for nom_plat, plat_info in self._plats_commandes.items():
            print(f"- {nom_plat}: {plat_info['prix']} € - Statut: {plat_info['statut']}")
        print(f"Total à payer: {total} €\n")

    def calculerTVA(self, taux_tva):
        total_tva = self._calculerTotal() * taux_tva
        return total_tva

commande1 = Commande(numero_commande=1)

commande1.ajouterPlat("Pizza", 10)
commande1.ajouterPlat("Burger", 8)

commande1.afficherCommande()

taux_tva = 0.1 
tva = commande1.calculerTVA(taux_tva)
print(f"TVA à payer: {tva} €")

commande1.annulerCommande()

commande1.ajouterPlat("Salade", 5)

commande1.afficherCommande()