
import unittest
import xmlrunner

from Reseau import Reseau
from Terrain import Terrain, Case

class TestReseau(unittest.TestCase):

    def test_definition_entree(self):
        r = Reseau() 

        r.ajouter_noeud(0, (0, 0))  # On ajoute un nœud d'entrée 

        r.definir_entree(0)   

        self.assertEqual(r.noeud_entree, 0)  # On vérifie que l'entrée est bien définie  

 
        

    def test_ajout_noeud(self):
        r = Reseau() 

        r.ajouter_noeud(1, (0, 0))  # On ajoute un nouveau nœud 

        self.assertIn(1, r.noeuds)   

        self.assertEqual(r.noeuds[1], (0, 0))  # On vérifie que le nœud soit bien ajouté et avec les bonnes coordonnées 

 

        r.ajouter_noeud(1, (1, 1))  # On ajoute un nœud avec une clé déjà existante pour voir si il ne bouge pas 

        self.assertEqual(r.noeuds[1], (0, 0))  

        r.ajouter_noeud(-1, (2, 2))  # On essaye d'ajouter un nœud négatif 

        self.assertNotIn(-1, r.noeuds)  # Le nœud ne doit pas être ajouté si tout fonctionne 
       

    def test_ajout_arc(self):
        r = Reseau() 

        r.ajouter_noeud(0, (0, 0))   

        r.ajouter_noeud(1, (1, 0)) 

        r.ajouter_arc(0, 1)  # On ajoute un arc entre les deux nœuds 

        self.assertIn((0, 1), r.arcs)  # On vérifier son ajout 

 

        r.ajouter_arc(1, 0)   

        self.assertEqual(len(r.arcs), 1)  # Si on ajoute le meme arc dans l'autre sens il ne doit pas être dupliqué 

 

        r.ajouter_arc(0, 2)  # On essaye d'ajouter un arc vers un nœud non créé 

        self.assertNotIn((0, 2), r.arcs)  # L'arc ne doit pas se faire 

 

    def test_validation_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        self.assertTrue(r.valider_reseau())

    def test_validation_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)

        self.assertFalse(r.valider_reseau())

    def test_distribution_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.VIDE, Case.CLIENT],
        ]

        self.assertTrue(r.valider_distribution(t))

    def test_distribution_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]

        self.assertFalse(r.valider_distribution(t))

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

