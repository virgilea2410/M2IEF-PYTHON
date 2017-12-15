# Pricing Methods ...

# Main

RUN = 'RUN'
TEST = 'TEST'
HELP = 'HELP'
TEST_ASKED = 1

# Features
NONE = "NONE"
VANILLA = "VANILLA"
ASIAN = "ASIAN"
BARRIER = "BARRIER"
AMERICAN = "AMERICAN"
FEATURE = "FEATURE"

# ... Index tuples

BLACKSCHOLES = (0,)
MONTECARLO = (1,)
BINOMIAL = (2,)

# ... Names

BSM_NAME = "Black & Scholes"
MC_NAME = "Monte Carlo"
BINOM_NAME = "Arbre Binomial"

# Option types

CALL = 'CALL'
PUT = 'PUT'

# Changes rates

EUREUR = 1.00
EURUSD = 1.1744
EURGBP = 0.8820
EURCHF = 1.1641
EURJPY = 133.37
EURAUD = 1.5536
EURCAD = 1.5107
EURBTC = 1/14557.2
EURNZD = 1.6936
EURCNY = 7.7773
EURBRL = 3.8820
EURCZK = 25.6383
EURSEK = 9.8865

# list of disponible currencies

AVAIL_CCY = []
AVAIL_CCY.append('EUR')
AVAIL_CCY.append('USD')
AVAIL_CCY.append('GBP')
AVAIL_CCY.append('CHF')
AVAIL_CCY.append('JPY')
AVAIL_CCY.append('AUD')
AVAIL_CCY.append('CAD')
AVAIL_CCY.append('BTC')
AVAIL_CCY.append('NZD')
AVAIL_CCY.append('CNY')
AVAIL_CCY.append('BRL')
AVAIL_CCY.append('CZK')
AVAIL_CCY.append('SEK')

# index of disponible currencies

EUR = 0
USD = 1
GBP = 2
CHF = 3
JPY = 4
AUD = 5
CAD = 6
BTC = 7
NZD = 8
CNY = 9
BRL = 10
CZK = 11
SEK = 12

# Button Constants

RETRY = 'retry'
QUIT = 'quit'
VALIDATE = 'validate'
NBSIMUL = 'nbSimul'
CONVERT = 'convert'

BUTTON_ON = "#%02x%02x%02x" % (254, 167, 158)
BUTTON_OFF = 'black'

ENTRY_ON = "#%02x%02x%02x" % (217, 233, 251)
ENTRY_OFF = 'white'

RETURN_KEY = 'Return'
ESCAPE_KEY = 'Escape'

# Graphical options

BACKGROUND_COLOR = 'lightgrey'

BORDER_WIDTH = 3

TITLE_COLOR = 'red'
TITLE_FONT = 'Helvetica 20 bold'

NORMAL_COLOR = 'black'
NORMAL_FONT = 'Helvetica 10 bold'

FRAME_WIDTH = 780
FRAME_HEIGHT = 480

# Aggregate number of instances

NUM_INSTANCE = 0