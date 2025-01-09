
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {} 

        arcs = [] 

 

        print("Configuration manuelle du réseau :") 

         

        # L'utilisateur choisi la position x et y du noeud d'entrée 

        while True: 

            try: 

                entree_x = int(input("Ligne du noeud d'entrée : ")) 

                entree_y = int(input("Colonne du noeud d'entrée : ")) 

                if t.cases[entree_x][entree_y] != Case.OBSTACLE: 

                    noeud_entree = 0 

                    noeuds[0] = (entree_x, entree_y) 

                    break 

                else: 

                    print("Position impratiquable") 

            except ValueError: 

                print("Entrez d'autres coordonnées") 

 

        # Ajout de noeuds 

        while True: 

            ajouter_noeud = input("Ajouter un noeud ? (o/n) : ").lower() 

            if ajouter_noeud == 'n': 

                break 

            try: 

                noeud_id = len(noeuds) 

                x = int(input("Ligne du noeud : ")) 

                y = int(input("Colonne du noeud : ")) 

                if (x, y) not in noeuds.values() and t.cases[x][y] != Case.OBSTACLE: 

                    noeuds[noeud_id] = (x, y) 

                else: 

                    print("Emplacement invalide ou occupé") 

            except ValueError: 

                print("Entrez d'autres coordonnées") 

 

        # Ajout d'arcs 

        while True: 

            ajouter_arc = input("Ajouter un arc ? (o/n) : ").lower() 

            if ajouter_arc == 'n': 

                break 

            try: 

                n1 = int(input("Identifiant du premier noeud : ")) 

                n2 = int(input("Identifiant du second noeud : ")) 

                if n1 in noeuds.keys() and n2 in noeuds.keys() and n1 != n2: 

                    arc = (min(n1, n2), max(n1, n2)) 

                    if arc not in arcs: 

                        arcs.append(arc) 

                    else: 

                        print("Noeuds déjà liés") 

                else: 

                    print("Noeuds invalides") 

            except ValueError: 

                print("Entrez d'autres identifiants") 

 

        return noeud_entree, noeuds, arcs 
        return -1, {}, []

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        return -1, {}, []

