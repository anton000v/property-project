from .utils import rus_alphabet

# ----------Default values:
NOT_COMPLETED = ''
DEFAULT = 'Не заполнено'
HUMAN_ORIENTED_DEFAULT = 'Упс, пока не можем найти'

# -------------selection items for field 'class':
ECONOM = 'ec'
COMFORT = 'co'
BUSINESS = 'bu'
PREMIUM = 'pr'
ELITE = 'el'
DELUXE = 'de'
TOWNHOUSE = 'to'

THE_CLASS_CHOICES = (
    (NOT_COMPLETED, DEFAULT),
    (ECONOM, 'Эконом'),
    (COMFORT, 'Комфорт'),
    (BUSINESS, 'Бизнес'),
    (PREMIUM, 'Премиум'),
    (ELITE, 'Элит'),
    (DELUXE, 'Делюкс'),
    (TOWNHOUSE, 'Townhouse')
)

# -------------selection items for field 'administrativeDistrict'

# MOSCOVSKII = 'mo'
# KIEVSKII = 'ki'
# SHEVCHENCOVSKII = 'sh'
# SLOBODSKOI = 'sl'
# OSNOVYANSKII = 'os'
# NEMISHLYANSKII = 'ne'
# HOLODNOGORSKII = 'ho'
# NOVOBAVARSKII = 'no'
# INDUSTRIALNII = 'in'

# THE_ADMINISTRATIVE_DISTRICT_CHOICES = (
#     (NOT_COMPLETED, DEFAULT),
#     (MOSCOVSKII, 'Московский'),
#     (KIEVSKII, 'Киевский'),
#     (SHEVCHENCOVSKII, 'Шевченковский'),
#     (SLOBODSKOI, 'Слободской'),
#     (OSNOVYANSKII, 'Основянский'),
#     (NEMISHLYANSKII, 'Немышлянский'),
#     (HOLODNOGORSKII, 'Холодногорский'),
#     (NOVOBAVARSKII, 'Новобоварский'),
#     (INDUSTRIALNII, 'Индустриальный')
# )

# -------------Selection items for field 'heating':
CENTRAL = 'ce'
AUTONOMOUS_GAS = 'ag'
AUTONOMOUS_ELECTRIC = 'ae'
AUTONOMOUS_AT_HOME = 'ah'

THE_HEATING_CHOICES = (
    (NOT_COMPLETED, DEFAULT),
    (CENTRAL, 'Центральное'),
    (AUTONOMOUS_GAS, 'Автономное газовое'),
    (AUTONOMOUS_ELECTRIC, 'Автономное электрическое'),
    (AUTONOMOUS_AT_HOME, 'Автономное на дом'),

)

# -------------Selection items for field 'parking':
UNDERGROUND = 'un'
GROUND = 'gr'
GUEST = 'gu'
BIKE_PARKING = 'bk'

THE_PARKING_CHOICES = (
    (NOT_COMPLETED, DEFAULT),
    (UNDERGROUND, 'Подземный'),
    (GROUND, 'Наземный'),
    (GUEST, 'Гостевой'),
    (BIKE_PARKING, 'Велопарковки')
)

# ------------Selection items for field 'Walls type':
BRICK = 'br'
GAS_BLOCK = 'gb'
PORCELAIN_BLOCK = 'pb'

THE_WALLS_TYPE_CHOICES = (
    (NOT_COMPLETED, DEFAULT),
    (BRICK, 'Кирпич'),
    (GAS_BLOCK, 'Газоблок'),
    (PORCELAIN_BLOCK, 'Керамоблок')

)

# -----------Selection items for field 'constructionTechnology':
BRICKWORK = 'br'
MONOLITHIC_FRAME = 'mf'
PANEL = 'pa'

THE_CONSTRUCTION_TECHNOLOGY_CHOICES = (
    (NOT_COMPLETED, DEFAULT),
    (BRICKWORK, 'Кирпичная кладка'),
    (MONOLITHIC_FRAME, 'Монолитно-каркасная'),
    (PANEL, 'Панельная')

)
# -----------Selection items for field 'warming':
STYROFOAM = 'st'
EXPANDED_POLYSTYRENE = 'ep'
MINERAL_WOOL = 'mw'
OTHER = 'ot'

THE_WARMING_CHOICES = (
    (NOT_COMPLETED, DEFAULT),
    (STYROFOAM, 'Пенопласт'),
    (EXPANDED_POLYSTYRENE, 'Пенополистирол'),
    (MINERAL_WOOL, 'Минеральная вата'),
    (OTHER, 'Другое')
)

# ----------------------------DISTRICT CHOICES:
# ----------CENTER:
CENTER = 'ce'
GOSPROM = 'gos'
NAGORNII = 'nag'
SOSNOVAYA_GORKA = 'sog'
SOKOLNIKI = 'sok'
SHATILOVKA = 'sha'
NAUCHAYA_METRO = 'nam'
NIJNII_CENTER = 'nic'
PLOSHAD_CONSTITUCII_METRO = 'pcm'
PUSHKINSKAYA_METRO = 'pum'

# ----------adjacent to the center
UJD = 'ujd'
CENTRALNII_RINOK = 'cer'

# -----------GAGARINA(LEVADA)
GAGARINA_METRO = 'gam'
SPORTIVNAYA_METRO = 'spm'
NOVII_CIRK = 'noc'
KONNII_RINOK = 'kor'
ZASCHITNIKOV_UKRAINI_METRO = 'zum'

# -----------ODESSA DISTRICTS
ODESSKAYA = 'ode'
OSNOVA = 'osn'
AEROPORT = 'aer'
ARTEMA_PARK = 'arp'
ZAVOD_MALISHEVA_METRO = 'zmm'
UJNOPROEKTNAYA = 'ujn'

# ----------HOLODNOGORSKOE DIRECTION
HOLODNAYA_GORA = 'hog'
LISAYA_GORA = 'lig'
ZALUTINO = 'zal'
BAVARIYA = 'bav'
NOVOSELOVKA = 'nov'
PESOCHIN = 'pes'

# ---------NOVOJANOVSKOYE DIRECTION
NOVOJANOVO = 'nov'
ZAVOD_SHEVCHENKO = 'zam'
MOSKALEVKA = 'mos'

# --------ROGANKOYE DIRECTION
HTZ = 'htz'
INDUSTRIALNAYA_METRO = 'inm'
HTZ_METRO = 'htm'
VOSTOCHNII_POSELOK = 'vop'
ROGAN = 'rog'
GORIZONT = 'gor'
SOLNECHNII = 'sol'
NOVOZAPADNII_POSELOK = 'nop'

# --------PYATIHATSKOE DIRECTION
JUKOVSKOGO_POSELOK = 'jup'
LESOPARK = 'les'
PYATIHATKI = 'pya'

# --------SALTOVSKOYE DIRECTION
SALTOVKA = 'sal'
SEVERNAYA_SALTOVKA = 'ses'
STARAYA_SALTOVKA = 'sts'
SABUROVA_DACHA = 'sad'
FRANCUZKII_BOULEVAR = 'frb'
KIROVA_POSELOK = 'kip'
KULINICHI = 'kul'
TURINKA = 'tur'
BOLSHAYA_DANILOVKA = 'bod'
NEMISHLYA = 'nem'
JURAVLEVKA = 'jur'
KIEVSKAYA_METRO = 'kim'
SHISHKOVKA = 'shi'
MJK = 'mjk'  # ??????????????????????

# ---------ALEXEYEVSKOE DIRECTION
ALEKSEEVKA = 'ale'
PAVLOVOE_POLE = 'pap'
PAVLOVKA = 'pav'
SORTIRIVKA = 'sor'
IVANOVKA = 'iva'

# -------NOVIE DOMA
NOVIE_DOMA = 'nod'
KOMMUNALNII_RINOK = 'kor'
DVOREC_SPORTA = 'dvs'
BOLNICA22 = '22b'
MASELSKOGO_METRO = 'mam'
ARMEYSKAYA_METRO = 'arm'
MOSKOVSKII_PROSPECT_METRO = 'mpm'

DISTRICT_CHOICES = [
    (NOT_COMPLETED, DEFAULT),
    ('Центр', (
        (CENTER, 'Центр'),
        (GOSPROM, 'Госпром'),
        (NAGORNII, 'Нагорный'),
        (SOSNOVAYA_GORKA, 'Сосновая горка'),
        (SOKOLNIKI, 'Сокольники'),
        (SHATILOVKA, 'Шатиловка'),
        (NAUCHAYA_METRO, 'Научная метро'),
        (NIJNII_CENTER, 'Нижний центр'),
        (PLOSHAD_CONSTITUCII_METRO, 'Площадь Конституции метро'),
        (PUSHKINSKAYA_METRO, 'Пушкинская метро'),
    )
     ),
    ('Прилегающие к центру', (
        (UJD, 'ЮЖД'),
        (CENTRALNII_RINOK, 'Центральный рынок'),
    )
     ),
    ('Гагарина (Левада)', (
        (GAGARINA_METRO, 'Спортивная метро'),
        (SPORTIVNAYA_METRO, 'Спортивная метро'),
        (NOVII_CIRK, 'Новый цирк'),
        (KOMMUNALNII_RINOK, 'Конный рынок'),
        (ZASCHITNIKOV_UKRAINI_METRO, 'Защитников Украины метро'),
    )
     ),
    ('Одесская районы', (
        (ODESSKAYA, 'Одесская'),
        (OSNOVA, 'Основа'),
        (AEROPORT, 'Аэропорт'),
        (ARTEMA_PARK, 'Артема парк'),
        (ZAVOD_MALISHEVA_METRO, 'Завод Малышева метро'),
        (UJNOPROEKTNAYA, 'Южнопроэктная'),
    )
     ),
    ('Холодногорское направление', (
        (HOLODNAYA_GORA, 'Холодная гора'),
        (LISAYA_GORA, 'Лысая гора'),
        (ZALUTINO, 'Залютино'),
        (BAVARIYA, 'Бавария'),
        (NOVOSELOVKA, 'Новоселовека'),
        (PESOCHIN, 'Песочин'),
    )
     ),
    ('Новожановское направление', (
        (NOVOJANOVO, 'Новожаново'),
        (ZAVOD_SHEVCHENKO, 'Завод Шевченко'),
        (MOSKALEVKA, 'Москалевка'),
    )
     ),
    ('Роганское направление', (
        (HTZ, 'ХТЗ'),
        (INDUSTRIALNAYA_METRO, 'Индустриальная метро'),
        (HTZ_METRO, 'ХТЗ метро'),
        (VOSTOCHNII_POSELOK, 'Восточный поселок'),
        (ROGAN, 'Рогань'),
        (GORIZONT, 'Горизонт'),
        (SOLNECHNII, 'Солнечный'),
        (NOVOZAPADNII_POSELOK, 'Новозападный поселок'),
    )
     ),
    ('Пятихатское направление', (
        (JUKOVSKOGO_POSELOK, 'Жуковского поселок'),
        (LESOPARK, 'Лесопарк'),
        (PYATIHATKI, 'Пятихатки'),
    )
     ),
    ('Салтовское направление', (
        (SALTOVKA, 'Салтовка'),
        (SEVERNAYA_SALTOVKA, 'Северная Салтовка'),
        (STARAYA_SALTOVKA, 'Старая Салтовка'),
        (SABUROVA_DACHA, 'Сабурова Дача'),
        (FRANCUZKII_BOULEVAR, 'Французский Бульвар'),
        (KIROVA_POSELOK, 'Кирова поселок'),
        (KULINICHI, 'Кулиничи'),
        (TURINKA, 'Тюринка'),
        (BOLSHAYA_DANILOVKA, 'Большая Даниловка'),
        (NEMISHLYA, 'Немышля'),
        (JURAVLEVKA, 'Журавлевка'),
        (KIEVSKAYA_METRO, 'Киевская метро'),
        (SHISHKOVKA, 'Шишковка'),
        (MJK, 'МЖК'),
    )
     ),
    ('Алексеевское направление', (
        (ALEKSEEVKA, 'Алексеевка'),
        (PAVLOVOE_POLE, 'Павловое Поле'),
        (PAVLOVKA, 'Павловка'),
        (SORTIRIVKA, 'Сортировка'),
        (IVANOVKA, 'Ивановка'),
    )
     ),
    ('Новые Дома', (
        (NOVIE_DOMA, 'Новые Дома'),
        (KOMMUNALNII_RINOK, 'Коммунальный Рынок'),
        (DVOREC_SPORTA, 'Дворец Спорта'),
        (BOLNICA22, '22 Больница'),
        (MASELSKOGO_METRO, 'Масельского метро'),
        (ARMEYSKAYA_METRO, 'Армейская метро'),
        (MOSKOVSKII_PROSPECT_METRO, 'Московский Проспект метро'),
    )
     ),
]

# ----------------microdistricts of 'SEVARNAYA SALTOVKA'
SS1 = 'ss1'
SS2 = 'ss2'
SS3 = 'ss3'
SS4 = 'ss4'
SS5 = 'ss5'
# ----------------microdistricts of 'SALTOVKA'
m601 = '601'
m602 = '602'
m603 = '603'
m604 = '604'
m605 = '605'
m606 = '606'
m606A = '606a'
m607 = '607'
m608 = '608'
m615 = '615'
m616 = '616'
m624 = '624'
m625 = '625'
m626 = '626'
m656 = '656'
m520 = '520'
m522 = '522'
m524 = '524'
m531 = '531'
m533 = '533'
m535 = '535'
HLEBZAVOD_8 = 'hl8'

MICRO_DISTRICT_DOES_NOT_EXIST = 'dne'

MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE = [
    (MICRO_DISTRICT_DOES_NOT_EXIST, "Не делится на микрорайоны"),
]

MICRO_DISTRICT_DEFAULT_CHOICE = [
    (NOT_COMPLETED, DEFAULT),
]
MICRO_DISTRICT_SALTOVKA_CHOICES = [
    (m601, '601'),
    (m602, '602'),
    (m603, '603'),
    (m604, '604'),
    (m605, '605'),
    (m606, '606'),
    (m606A, '606-A'),
    (m607, '607'),
    (m608, '608'),
    (m615, '615'),
    (m616, '616'),
    (m624, '624'),
    (m625, '625'),
    (m626, '626'),
    (m656, '656'),
    (m520, '520'),
    (m522, '522'),
    (m524, '524'),
    (m531, '531'),
    (m533, '533'),
    (m535, '535'),
    (HLEBZAVOD_8, '8 Хлебзавод'),
]

MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES = [
    (SS1, 'Северная Салтовка - 1'),
    (SS2, 'Северная Салтовка - 2'),
    (SS3, 'Северная Салтовка - 3'),
    (SS4, 'Северная Салтовка - 4'),
    (SS5, 'Северная Салтовка - 5'),
]
FULL_MICRO_DISTRICT_CHOICES = MICRO_DISTRICT_DOES_NOT_EXIST_CHOICE + MICRO_DISTRICT_DEFAULT_CHOICE + \
                              MICRO_DISTRICT_SALTOVKA_CHOICES + MICRO_DISTRICT_SEVERNAYA_SALTOVKA_CHOICES
# --------------------- Metro choices
SALTOVSKAYA_LINE = 'sl'
ALEXEEVSKAYA_LINE = 'al'
HOLODNOGORSKAYA_LINE = 'hl'

# --------------------- Saltovskaya Line
GEROYEV_TRUDA = 'gtr'
STUDENCHESKAYA = 'stk'
AKADEMINA_PAVLOVA = 'akp'
AKADEMINA_BARABASHOVA = 'akb'
KIEVSKAYA = 'kie'
PUSHKINSKAYA = 'psh'
UNIVERSITET = 'uni'
ISTORICHESKII_MUZEI = 'ism'

# ----------------------- Alekseevskaya Line
POBEDA = 'pob'
ALEXEEVSKAYA = 'ale'
AVGUSTA_23 = '23a'
BOTANICHESKII_SAD = 'bts'
NAUCHNAYA = 'nau'
GOSPROM = 'gos'
ARCHITECTORA_BIKETOVA = 'arb'
ZASCHITNIKOV_UKRAINI = 'zau'
METROSTROITELEY = 'met'

# ----------------------- Holodnogorsko zavodskaya Line
HOLODNAYA_GORA = 'hog'
UJNII_VOKZAL = 'ujv'
CENTRALNII_RINOK = 'cer'
PLOSHAD_KONSTITUCII = 'plk'
PROSPECT_GAGARINA = 'prg'
SPORTIVNAYA = 'spo'
ZAVOD_IMENI_MALISHEVA = 'zim'
MOSKOVSKII_PROSPECT = 'mop'
DVOREC_SPORTA = 'dvs'
ARMEISKAYA = 'arm'
IMENI_MASELSKOGO = 'imm'
TRAKTORNII_ZAVOD = 'trz'
INDUSTRIALNAYA = 'ind'

THE_METRO_CHOICES = [
    (NOT_COMPLETED, DEFAULT),
    ('Салтовская линия', (
        (GEROYEV_TRUDA, 'Героев Труда'),
        (STUDENCHESKAYA, 'Студенческая'),
        (AKADEMINA_PAVLOVA, 'Академика Павлова'),
        (AKADEMINA_BARABASHOVA, 'Академика Барабашова'),
        (KIEVSKAYA, 'Киевская'),
        (PUSHKINSKAYA, 'Пушкинская'),
        (UNIVERSITET, 'Университет'),
        (ISTORICHESKII_MUZEI, 'Исторический Музей'),
    )
     ),
    ('Алексеевская линия', (
        (POBEDA, 'Победа'),
        (ALEXEEVSKAYA, 'Алексеевская'),
        (AVGUSTA_23, '23 Августа'),
        (BOTANICHESKII_SAD, 'Ботанический сад'),
        (NAUCHNAYA, 'Научная'),
        (GOSPROM, 'Госпром'),
        (ARCHITECTORA_BIKETOVA, 'Архитектора Бикетова'),
        (ZASCHITNIKOV_UKRAINI, 'Защитников Украины'),
        (METROSTROITELEY, 'Метростроителей'),
    )
     ),
    ('Холодногорско-Заводская линия', (
        (HOLODNAYA_GORA, 'Холодная Гора'),
        (UJNII_VOKZAL, 'Южный Вокзал'),
        (CENTRALNII_RINOK, 'Центральный рынок'),
        (PLOSHAD_KONSTITUCII, 'Площадь Конституции'),
        (PROSPECT_GAGARINA, 'Проспект Гагарина'),
        (SPORTIVNAYA, 'Спортинвая'),
        (ZAVOD_IMENI_MALISHEVA, 'Завод имени Малышева'),
        (MOSKOVSKII_PROSPECT, 'Московский Проспект'),
        (DVOREC_SPORTA, 'Дворец Спорта'),
        (ARMEISKAYA, 'Армейская'),
        (IMENI_MASELSKOGO, 'Имени А.С. Масельского'),
        (TRAKTORNII_ZAVOD, 'Тракторный Завод'),
        (INDUSTRIALNAYA, 'Индустриальная'),
    )
     ),
]
# --------------------- Type of movement choices
ON_FOOT = 'of'
BY_CAR = 'bc'
THE_TYPE_OF_MOVEMENT_CHOICES = (
    (NOT_COMPLETED, DEFAULT),
    (ON_FOOT, 'Пешком'),
    (BY_CAR, 'На машине'),
)



#---------------------- House letter CHOICES

WITHOUT_LETTER = ''
WITHOUT_LETTER_FOR_HUMANS = 'Без бувы'
HOUSE_LETTER_CHOICES = [(WITHOUT_LETTER, WITHOUT_LETTER_FOR_HUMANS)] + [(k,k) for k in rus_alphabet]



#---------------------- HOUSING NUMBER choices
NOT_DIVIDED = ''
HOUSING_NUMBER_CHOICES = [(WITHOUT_LETTER, 'Не делится на корпуса')] + [(str(i),str(i)) for i in range(1, 11)]
