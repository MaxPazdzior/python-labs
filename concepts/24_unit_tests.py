# ==============================================================================

import super_modul
import unittest

# ==============================================================================

# print(super_modul.dividiere(6,2))

class TestDividiere(unittest.TestCase):

    # Assert 1: Normalfall (Positive Zahlen)
    def test_normal(self):
        self.assertEqual(super_modul.dividiere(10,5),2,msg="A1 Failed") # --> die zwei hinter der Rechnung bedeutet, dass ich prüfen möchte, ob dies das Ergebnis der Rechnung ist


    # Asser 2: Negative Zahlen
    def test_negativ(self):
        self.assertEqual(super_modul.dividiere(6, -2), -3, msg="A2 Failed")

    # Asser 3: Null Werte -> Ergebnis
    def test_durch_numm(self):
        self.assertEqual(super_modul.dividiere(10,0), "Error", msg="A3 Failed")

unittest.main()

# ==============================================================================
