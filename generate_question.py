import random

president_refs = [
        "Rais wetu anasema nini",
        "Je Mheshimiwa Rais anaongeleaje",
        "Rais anatuambia nini kuhusu",
        "Je Rais anafahamu changamoto hizi za",
        "Kwa nini hatupati majibu ya wazi kuhusu",
        "serikali inafanya nini kuhusu",
        "wizara husika imefika wapi",
        "maafisa wanatoa majibu gani",
        "mchakato rasmi uko wapi",
        "ni hatua gani zimechukuliwa"
    ]

injecting_bits = [
        "au ndo maamuzi yamekula shifting?",
        "ama taarifa zenyewe zimepotea barabarani?",
        "au tunaambiwa tuvune matumaini tu?",
        "ama kila kitu kiko pending kama vibali vyenyewe?",
        "au tunapewa ahadi ambazo hazina stakabadhi?"
    ]

agri_topics = [
        "bei ya mbaazi",
        "vibali za kusafirisha nje mbaazi",
        "kero za wakulima wa korosho",
        "upatikanaji wa mbolea kwa wakati",
        "uhifadhi wa mazao vijijini",
        "usafirishaji wa mazao kuvuka mipaka",
        "miundombinu ya umwagiliaji",
        "ushuru usioeleweka kwa wakulima",
        "ufuatiliaji wa vyama vya ushirika",
        "changamoto za soko la ndani"
    ]

def generate_question():
    pres = random.choice(president_refs)
    top = random.choice(agri_topics)
    inj = random.choice(injecting_bits)
    q = f"{pres} {top},{inj}"
    return q

if __name__ == "__main__":
    print(generate_question())
        
