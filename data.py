# Definert en liste med kontaktinformasjon for kantinen.
# Hver kontakt er en ordbok med navn, nummer, epost og rolle.
KONTAKT_INFO = [
    {"navn": "Marcus",
     "nummer": "+47 456 456 45",
     "epost": "kantine@akdemiet.no",
     "rolle": "Innkjøper"},

    {"navn": "Emma",
     "nummer": "+47 912 345 67",
     "epost": "emma.hansen@akademiet.no",
     "rolle": "Kantineleder"},

    {"navn": "Jonas",
     "nummer": "+47 987 654 32",
     "epost": "jonas.larsen@akademiet.no",
     "rolle": "Assistent"},
    
    {"navn": "Sofie",
    "nummer": "+47 401 223 89",
    "epost": "sofie.nilsen@akademiet.no",
    "rolle": "Kokk"
    }
]


#Definert en liste med menyelementer for hver dag i uken.
#Hvert element er en ordbok med dag navn på retten, pris og bilde.
MENY_ITEMS = [
    {"dag": "Mandag", "navn": "Lasagne med salat", "pris": 85, "bilde": "/static/images/Lasagne.jpg"},
    {"dag": "Tirsdag", "navn": "Kyllingwok med ris", "pris": 90, "bilde": "/static/images/Kyllingwok.jpg"},
    {"dag": "Onsdag", "navn": "Pasta Bolognese", "pris": 80, "bilde": "/static/images/pasta_bolognese.jpg"},
    {"dag": "Torsdag", "navn": "Kjøttboller med potetmos", "pris": 85, "bilde": "/static/images/Kjottboller.jpg"},
    {"dag": "Fredag", "navn": "Kyllingwrap", "pris": 65, "bilde": "/static/images/Kyllingwrap.jpg"},

]

#definert en liste med varer som er i kantina
# Hvert element er en ordbok med navn på varen, pris og bilde.
VARER_ITEMS = [
    {"navn": "Toast", "pris": 35, "bilde": "/static/images/Toast.jpg"},
    {"navn": "Cola Zero", "pris": 30, "bilde": "/static/images/cola_zero.jpg"},
    {"navn": "Baguette Kylling", "pris": 55, "bilde": "/static/images/baguette_kylling.jpg"},
    {"navn": "Salatboks", "pris": 60, "bilde": "/static/images/salat.jpg"},
    {"navn": "Yoghurt", "pris": 25, "bilde": "/static/images/yoghurt.jpg"},
    {"navn": "Kaffe", "pris": 20, "bilde": "/static/images/kaffe.jpg"},
    {"navn": "Smoothie Jordbær", "pris": 45, "bilde": "/static/images/smoothie_jordbaer.jpg"},
    {"navn": "Muffins Sjokolade", "pris": 30, "bilde": "/static/images/muffins.jpg"}
]
