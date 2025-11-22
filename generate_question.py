import random

president_refs = [
    "Rais wetu anasema nini",
    "Je Mheshimiwa Rais anatuelezea vipi",
    "Rais ana mpango gani",
    "Je Rais anajua kwamba",
    "Kwa nini Rais hasemi wazi"
]

gov_refs = [
    "serikali inafanya nini",
    "wabunge wamefikia wapi",
    "mawaziri wana mipango gani",
    "vyombo vya usalama vinafanya kazi gani",
    "serikali imejipangaje"
]

funny_bits = [
    "au ni masihara tu?",
    "ama tunadanganywa hadharani?",
    "au tumebaki kuwa watazamaji?",
    "ama ndo mambo yamewashinda?",
    "au tunachezewa kama sinema?"
]

topics = [
    "vurugu za baada ya uchaguzi",
    "malalamiko ya wananchi",
    "haki za binadamu",
    "fidia kwa waathiriwa",
    "uchunguzi huru",
    "watu waliopotea",
    "ukamataji usiofuata sheria",
    "matumizi ya nguvu kupita kiasi",
    "uwazi wa taarifa",
    "wajibu wa serikali"
]

def generate_questions():
    pres = random.choice(president_refs)
    gov = random.choice(gov_refs)
    top = random.choice(topics)
    funny = random.choice(funny_bits)
    q = f"{pres} kuhusu {top}, na {gov} juu ya hilo {funny}"
    return q

if __name__ == "__main__":
    print(generate_questions())
