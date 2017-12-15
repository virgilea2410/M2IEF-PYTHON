from MainThread import MainThread
from ApplicationPricer import ApplicationPricer
import sys
import PricerConstants as cst

args = sys.argv

if len(args) == 1:
     MainThread.run()

elif len(args) > 1:

    if str(args[1]).upper() == cst.RUN:
        print("Lancement de l'application ...")
        ApplicationPricer.run_pricing()

    elif str(args[1]).upper() == cst.TEST:
        print("Lancement des tests unitaires ...")
        ApplicationPricer.test_pricing()

    elif str(args[1]).upper() == cst.HELP:
        print("\nExecuter, dans une console, et au choix, l'un des commandes suivantes :\npython3 Main.py --> Pour lancer le programme principal")
        print("\npython3 Main.py run --> pour lancer uniquement l'application de pricing")
        print("\npython3 Main.py test --> pour lancer uniquement les tests unitaires du module de l'application de pricing\n")




