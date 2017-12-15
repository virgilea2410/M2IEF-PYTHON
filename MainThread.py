#!python3

from ApplicationPricer import ApplicationPricer
import time
import threading
import PricerConstants as cst

global input_test
input_test = ""

class MainThread:

    def __init__(self):
        pass

    @staticmethod
    def ask_input_test(arg1, stop_event):

        global input_test

        while not stop_event.is_set() and input_test == "":

            input_test = str(input("Souhaitez vous :\n1 - Effectuer le test unitaire du module Option Pricer ?\n2 - Lancer l'application Option Pricer ?\n>"))

            stop_event.set()

    @staticmethod
    def main_thread():

        global input_test

        input_stop = threading.Event()
        input_thread = threading.Thread(target=MainThread.ask_input_test, args=(1, input_stop))
        input_thread.setDaemon(True)

        input_thread.start()

        i = 1
        while input_test == "" and not input_stop.is_set():
            time.sleep(1)
            i += 1

            if i > 5:
                input_stop.set()

        accepted_answers=['1', '2']

        if input_test in accepted_answers:
            if int(input_test) == cst.TEST_ASKED:
                print("Option 1 choisie !\nLancement des tests unitaires...")
                ApplicationPricer.test_pricing()

            else:

                print("Option 2 choisie !\nLancement de l'application...")
                ApplicationPricer.run_pricing()

        elif input_test == "":
            print("Out of time !\nLancement de l'application...")
            ApplicationPricer.run_pricing()
        else:
            print("No/Wrong input detected.\nLancement de l'application...")
            ApplicationPricer.run_pricing()

    @staticmethod
    def run():
        one_thread = threading.Thread(target=MainThread.main_thread)

        one_thread.run()


