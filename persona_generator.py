import json
import random
import mysql.connector

# device name, ua model, device os, os version, device platform, logical width, logical height, original width, original height, device pixel ratio, hardware concurrency, memory, gpu vendor name, webgl renderer, [language, color depth]

proxy_rack_country_cities_list = {"GD": ["Saint George's"], "DM": ["Roseau"],
                                  "LK": ["Colombo", "Dehiwala", "Galle", "Panadura", "Wattala"],
                                  "MN": ["Ulan Bator", "Nuga"],
                                  "PE": ["Trujillo", "Pucallpa", "Arequipa", "Viru", "Lima", "Cusco"],
                                  "XK": ["Pristina"], "MO": ["Macao"], "AM": ["Yerevan"],
                                  "TW": ["Chiayi County", "Hsinchu", "Yilan", "Kaohsiung City", "Taipei", "Yunlin",
                                         "Zhongli District",
                                         "Chang-hua", "Chiayi City", "Neipu", "Zhubei", "Jian", "Taoyuan District",
                                         "Taichung", "New Taipei",
                                         "Hualien City", "Xitun", "Bade District", "Luzhu", "Tainan City",
                                         "Pingtung City", "Hsinchu County"],
                                  "LY": ["Ajdabiya", "At Taj", "Tripoli", "Benghazi", "Zliten", "Misratah", "Awjilah",
                                         "Ghat", "Al Marj"],
                                  "SA": ["Makkah", "Jeddah", "Riyadh", "Dammam", "Medina", "Eastern Province"],
                                  "NG": ["Lagos", "Ilorin", "Benin City"], "GQ": ["Bicurga", "Malabo"],
                                  "BR": ["Sao Jose do Vale do Rio Preto", "Franca", "Chapadao Do Sul", "Araioses",
                                         "Teresina",
                                         "Belo Horizonte", "Curitiba", "Maceió", "Itapetininga", "Balneário Camboriú",
                                         "Rio Maria",
                                         "Ipatinga", "Santo André", "Pouso Alegre", "Praia Grande", "Brasília",
                                         "Fortaleza",
                                         "Jaboatao dos Guararapes", "Guaratuba", "Várzea Grande", "Dom Cavati",
                                         "Araguaína", "Aracaju",
                                         "Osasco", "Rio de Janeiro", "Novo Hamburgo", "Sangao", "Santos", "Viamão",
                                         "Saudades", "Betim",
                                         "Paracatu", "Garca", "Sao Jose do Rio Preto", "Sorocaba", "Paulista",
                                         "Vinhedo", "Uberaba",
                                         "Limeira", "Maringá", "Teotonio Vilela", "Vila Velha", "Manhuacu",
                                         "Jaraguá do Sul", "Vitória",
                                         "Ariquemes", "Nova Iguaçu", "Sao Jose de Piranhas", "João Pessoa",
                                         "Vitória da Conquista",
                                         "Virgem da Lapa", "Assis", "Serra", "Farroupilha", "Fazenda Rio Grande",
                                         "Guarulhos",
                                         "Santa Cruz do Sul", "Ijui", "Imperatriz", "Lencois", "Malta", "Cafelandia",
                                         "Porto Alegre",
                                         "Caxias do Sul", "Pintadas", "Campinas", "Jacunda", "São Paulo", "Irece",
                                         "Anápolis", "Lagarto",
                                         "Dois Irmaos", "Manaus", "Porto Velho", "Parobe", "Ourinhos", "Sumaré",
                                         "Boa Vista",
                                         "Ribeirão Preto", "Goiânia", "São Caetano do Sul"],
                                  "ID": ["Gresik", "Bengkulu", "Keputih", "Banjarmasin", "Magelang", "Kupang",
                                         "Balikpapan", "Palembang",
                                         "Pandeglang", "Karawang", "Bandar Lampung", "Cilegon", "Kalideres", "Subang",
                                         "Yogyakarta", "Demak",
                                         "Ambon City", "Temanggung", "Sragen", "Blora", "Brebes",
                                         "Karanganyar Wetankali", "Semarang",
                                         "Bekasi", "Jepara", "Cilacap", "Bintaro", "Manado", "Bukittinggi", "Pemalang",
                                         "Pangkalpinang",
                                         "Mojosongo", "Magetan", "Manggadua Selatan", "Buaran", "Jakarta", "Pontianak",
                                         "Tangerang",
                                         "Sumedang", "Pekanbaru", "Blitar", "Sleman", "Menteng", "Cibeber", "Rembangan",
                                         "Pati", "Sukabumi",
                                         "Prapattunggal", "Ciamis", "Kendari", "Ponorogo", "Natar", "Tanjung Pinang",
                                         "Mojokerto",
                                         "Pangandaran", "Lamongan", "Nabire", "Gorontalo", "Boyolali", "Sumbawa Besar",
                                         "Babakangarut",
                                         "Palu", "Wonogiri", "Tegal", "Palangkaraya", "Bogor", "Makassar",
                                         "South Tangerang", "Madiun",
                                         "Tuban", "Malang", "Perwira", "Jambi City", "Klaten", "Bulanbulan",
                                         "Purwokerto", "Merauke",
                                         "Cipulir", "Sidoarjo", "Bontang", "Bukit Duri", "Depok", "Tenggarong",
                                         "Jatimakmur", "Bedalipermai",
                                         "Tanjung Balai", "Mataram", "Serang", "Purbalingga", "Manokwari", "Papua",
                                         "Tasikmalaya", "Denpasar",
                                         "Ngawi", "Banyumas", "Samarinda", "Surabaya", "Sukoharjo", "Trenggalek",
                                         "Probolinggo",
                                         "Kebon Kelapa", "Ternate", "Kebumen Satu", "Indramayu", "Batam", "Padang",
                                         "Jember", "Selong",
                                         "Surakarta", "Lhokseumawe", "Pasuruan", "Pekalongan", "Sorong", "Bima",
                                         "Srengseng", "Lumajang",
                                         "Cirebon", "Kediri", "Banyuwangi", "Tarakan", "Medan", "Ancol Timur",
                                         "Jayapura", "Baru Ilir",
                                         "Banda Aceh", "Bandung", "Pondok Pinang", "Jati"],
                                  "DO": ["Santo Domingo Este", "Nagua", "San Francisco de Macorís",
                                         "La Boca de Mao Abajo", "Cabarete",
                                         "Santa Cruz de Barahona", "San Isidro", "Santo Domingo", "Cotui",
                                         "Las Terrenas", "San Cristobal",
                                         "Santiago de los Caballeros", "San Pedro de Macorís", "Sabaneta de Yasica",
                                         "Concepción de la Vega",
                                         "Dajabon", "Los Alcarrizos", "Puerto Plata", "Bonao", "Sosua, Cabarete",
                                         "Licey al Medio",
                                         "Washington", "Provincia de Barahona", "La Romana", "Santo Domingo Oeste",
                                         "Guananico",
                                         "Hato Mayor del Rey", "Gaspar Hernandez"], "PG": ["Lae"],
                                  "FR": ["Draveil", "Issy-les-Moulineaux", "Montevrain", "Strasbourg", "Rouen",
                                         "Montreuil-Juigne", "Metz",
                                         "Chatillon-sur-Loire", "Vire", "Eclance", "Marseille", "Cannes",
                                         "Dun-sur-Auron", "Bandol", "Saumur",
                                         "Sezanne", "Les Essarts-le-Roi", "Lyon", "Les Sables-d'Olonne",
                                         "Thonon-les-Bains", "Bordeaux",
                                         "Angais", "Vélizy-Villacoublay", "Sète", "Molsheim", "Choisy-le-Roi",
                                         "Bully-les-Mines",
                                         "Boulogne-Billancourt", "Roubaix", "Saint-Etienne", "Perpignan", "Sélestat",
                                         "Sainte-Geneviève-des-Bois", "Aubervilliers", "Cornas", "Noisy-le-Grand",
                                         "Paris",
                                         "Saint-Cheron-des-Champs", "Bouxieres-sous-Froidmont"],
                                  "CZ": ["Bilina", "Liberec", "Přerov", "Zbraslavice", "Kutná Hora", "Frýdek-Místek",
                                         "Zlín", "Prague",
                                         "Tábor", "Most", "Velke Brezno", "Sternberk"],
                                  "BY": ["Pinsk", "Gomel", "Vitebsk", "Mogilev", "Minsk", "Brest"],
                                  "DK": ["Esbjerg", "Aarhus", "Odense", "Frederiksberg"],
                                  "KR": ["Anseong", "Jecheon", "Uiwang", "Bucheon-si", "Mokpo", "Suyeong-gu",
                                         "Seodaemun-gu",
                                         "Yeongdeungpo-gu", "Namhae-gun", "Yangp'yong", "Jungnang-gu", "Daegu",
                                         "Seongdong-gu", "Busanjin-gu",
                                         "Geumjeong-gu", "Gunsan", "Uiseong-gun", "Kwangyang", "Bupyeong-gu",
                                         "Gyeongsan-si", "Yongheung",
                                         "Ulju-gun", "Dongjak-gu", "Muju-gun", "Pocheon-si", "Yeongcheon-si",
                                         "Yangyang-gun", "Tangjin",
                                         "Yangcheon-gu", "Hongseong-gun", "Gangdong-gu", "Taean-gun", "Dalseong-gun",
                                         "Gangneung",
                                         "Gwangmyeong", "Seongju-gun", "Nonsan", "Songpa-gu", "Suseong-gu", "Chinch'on",
                                         "Changnyeong",
                                         "Iksan", "Suncheon", "Sejong", "Gyeonggi-do", "Namyangju", "Yongsan-gu",
                                         "Yongin-si",
                                         "Dongdaemun-gu", "Seocho-gu", "Ansan-si", "Dalseo-gu", "Pohang", "Nowon-gu",
                                         "Yeonsu-gu", "Gwacheon",
                                         "Miryang", "Namdong-gu", "Anyang-si", "Osan", "Hanam", "Haeundae-gu", "Busan",
                                         "Pyeongtaek-si",
                                         "Siheung-si", "Gwangjin-gu", "Goseong-gun", "Sasang-gu", "Paju", "Mapo-gu",
                                         "Yuseong-gu",
                                         "Icheon-si", "Suwon", "Cheonan", "Yeonje-gu", "Hongch'on", "Gapyeong County",
                                         "Seogwipo",
                                         "Jongno-gu", "Yeongwol-gun", "Gimpo-si", "Areannamkwaengi", "Guro-gu",
                                         "Uijeongbu-si", "Cheongju-si",
                                         "Chungju", "Goyang-si", "Saha-gu", "Gangbuk-gu", "Daedeok-gu", "Ulsan",
                                         "Nam-gu", "Seongnam-si",
                                         "Chuncheon", "Gangseo-gu", "Seongbuk-gu", "Jeollabuk-do", "Eunpyeong-gu",
                                         "Jung-gu", "Seoul",
                                         "Gwangju", "Gwangmyeong-si", "Geoje", "Yeongdong-gun", "Yecheon", "Wanju",
                                         "Chilgok-gun", "Boryeong",
                                         "Gangnam-gu", "Gyeongju", "Goheung-gun", "Asan", "Donggu", "Buan-gun",
                                         "Hwaseong-si", "Taejeon",
                                         "Paju-si", "Dong-gu", "Dobong-gu", "Gyeyang-gu", "Andong", "Muan", "Jeonju",
                                         "Geumcheon-gu",
                                         "Gwangsan-gu", "Incheon", "Yangju", "Gimcheon", "Naju", "Seo-gu", "Gwanak-gu",
                                         "Tongyeong", "Jinju",
                                         "Pyeongchang", "Jeongseon-gun", "Pohang-si", "Dongducheon-si", "Wonju",
                                         "Jeju City", "Yeosu",
                                         "Yangsan", "Buk-gu", "Gimhae", "Gumi", "Gimje-si", "Seosan City", "Changwon",
                                         "Ganghwa-gun",
                                         "Gijang-gun", "Guri-si", "Yeoncheon-gun"], "CI": ["Abidjan"],
                                  "LB": ["Beirut", "Fanar"],
                                  "BZ": ["Belize City", "Orange Walk", "San Ignacio"], "CW": ["Willemstad"],
                                  "CO": ["Garzón", "Bucaramanga", "Envigado", "San Pelayo", "Arauca", "Supata",
                                         "Saravena", "Caucasia",
                                         "Bogotá", "San Gil", "Santiago de Cali", "Tuluá", "Barranquilla",
                                         "San José del Guaviare",
                                         "San Rafael", "Pereira", "Pasto", "Risaralda", "Jamundi",
                                         "Guadalajara de Buga", "Valledupar",
                                         "Cúcuta", "Ibague", "Agustin Codazzi", "Andalucia", "Aguachica",
                                         "San Andres de Palomo", "Cartagena",
                                         "Medellín", "Acacias", "Chia", "San Onofre", "Ipiales"],
                                  "ET": ["Nazret", "Gambela", "Harar", "Jijiga", "Addis Ababa", "Kuta Ber",
                                         "Dire Dawa"],
                                  "AD": ["Andorra la Vella"], "QA": ["Doha"], "UZ": ["Gurlan", "Tashkent", "Bukhara"],
                                  "TR": ["Sanliurfa", "Bayrampasa", "Bagcilar", "Edirne", "Izmir", "Denizli",
                                         "Zonguldak", "Antalya",
                                         "Diyarbakır", "Kosekoy", "Istanbul", "Bursa", "Ankara", "Adıyaman", "Antakya",
                                         "Adana"],
                                  "PR": ["Bayamón", "Manati", "Ciales", "San German", "San Juan"],
                                  "HT": ["Port-au-Prince"], "ZW": ["Harare"],
                                  "BB": ["Christ Church", "Bridgetown"],
                                  "SE": ["Spanga", "Sollentuna", "Ludvika", "Hultsfred", "Stockholm", "Sundsvall",
                                         "Bollnaes", "Karlstad"],
                                  "AT": ["Graz", "Hoechst", "Bregenz", "Kirchbichl", "Goestling an der Ybbs",
                                         "Ried im Innkreis", "Hard",
                                         "Sankt Johann in Tirol", "Innsbruck", "Dornbirn", "Vienna",
                                         "Kematen an der Ybbs", "Going",
                                         "Lustenau"], "AO": ["Luanda", "Lubango"], "AE": ["Dubai", "Abu Dhabi"],
                                  "ME": ["Rozaje", "Budva"],
                                  "IR": ["Tehran"], "NI": ["Managua"],
                                  "DE": ["Gelsenkirchen", "Elsterwerda", "Siegen", "Frankfurt am Main", "Trier",
                                         "Freudenstadt",
                                         "Bietigheim-Bissingen", "Dresden", "Cologne", "Bad Durrheim", "Hilden",
                                         "Bremen", "Namborn", "Kaaks",
                                         "Beckingen", "Cochem", "Kassel", "Kleve", "Lüneburg", "Borken",
                                         "Monheim am Rhein", "Landau",
                                         "Bingen am Rhein", "Leipzig", "Nuremberg", "Senftenberg", "Monschau",
                                         "Bad Salzungen", "Buechel",
                                         "Düsseldorf", "Hamburg", "Buedingen", "Essen", "Laichingen", "Fuerstenwalde",
                                         "Ibbenbueren",
                                         "Oberursel", "Pfaffenhofen an der Ilm", "Duisburg", "Ingolstadt", "Schwalbach",
                                         "Erfurt", "Soltau",
                                         "Zwickau", "Halberstadt", "Bad Pyrmont", "Osnabrück", "Fuldabruck",
                                         "Bad Bevensen", "Plattling",
                                         "Haltern am See", "Gottmadingen", "Ludwigshafen am Rhein", "Bendorf",
                                         "Brandenburg",
                                         "Bad Neuenahr-Ahrweiler", "Reutlingen", "Poessneck", "Oberhaching", "Uelzen",
                                         "Coburg", "Koblenz",
                                         "Bad Kreuznach", "Friedrichsdorf", "Olching", "Bardowick", "Kronberg",
                                         "Reinbek", "Bayreuth",
                                         "Gotha", "Mainz", "Bienenbuttel", "Schweinfurt", "Heilbronn", "Braunschweig",
                                         "Chemnitz", "Munich",
                                         "Buxtehude", "Ruppertsecken", "Bielefeld", "Alzenau in Unterfranken",
                                         "Inchenhofen", "Bretten",
                                         "Meiningen", "Bochum", "Augsburg", "Muehldorf", "Bonn", "Wiesbaden",
                                         "Bad Friedrichshall",
                                         "Rielasingen-Worblingen", "Loecknitz", "Nagold", "Rennertshofen",
                                         "Limburg an der Lahn",
                                         "Oberhausen", "Ettlingen", "Jena", "Bad Freienwalde", "Untergriesbach",
                                         "Magdeburg", "Asslar",
                                         "Karlsruhe", "Rostock", "Aschersleben", "Osterholz-Scharmbeck",
                                         "Rehlingen-Siersburg", "Mannheim",
                                         "Berlin", "Neu-Isenburg", "Kaiserslautern", "Gaildorf", "Neusass", "Gangkofen",
                                         "Gunzenhausen",
                                         "Leverkusen", "Remagen", "Krefeld", "Hanover"], "UY": ["Montevideo", "Aguada"],
                                  "JO": ["Irbid", "Amman", "Zarqa", "Salt", "Balqa"],
                                  "SI": ["Kamnik", "Trbovlje", "Semic", "Divača", "Maribor", "Domžale", "Ljubljana"],
                                  "BF": ["Ouagadougou"],
                                  "CD": ["Inongo"], "YE": ["Sanaa"],
                                  "ZA": ["Letaba", "Secunda", "Tzaneen", "Westonaria", "Ladybrand", "Stellenbosch",
                                         "Benoni", "Mafikeng",
                                         "Brits", "Grahamstown", "Polokwane", "Moorreesburg", "Sedgefield",
                                         "Hartswater", "Lephalale",
                                         "Cape Town", "Krugersdorp", "Springs", "Vanderbijlpark", "Rustenburg",
                                         "Thohoyandou", "East London",
                                         "Villiersdorp", "Paarl", "St Francis Bay", "Pretoria", "Bloemfontein",
                                         "Durban", "Worcester",
                                         "Kuruman", "Robertson", "Nelspruit", "Kranskop", "Rabie Ridge", "Centurion",
                                         "Johannesburg",
                                         "Potchefstroom", "Vredenburg", "Richards Bay", "Somerset West", "Kempton Park",
                                         "Cradock",
                                         "Port Elizabeth", "Pietermaritzburg", "Despatch", "Theunissen", "Atlantis",
                                         "Queenstown"],
                                  "GT": ["San Marcos", "Peten", "Quetzaltenango", "Villa Nueva", "Puerto Barrios",
                                         "Guatemala City",
                                         "Esquipulas", "Zacapa"], "SZ": ["Mbabane"],
                                  "BM": ["Hamilton", "Devonshire Parish"], "PW": ["Koror"],
                                  "HN": ["Tegucigalpa", "San Pedro Sula"], "MQ": ["Fort-de-France"],
                                  "IN": ["Ahmedabad", "Guntur", "Ghaziabad", "Vyara", "Bhubaneswar", "Varanasi",
                                         "Cherthala", "Kanpur",
                                         "Sikar", "Palakollu", "Sonipat", "Delhi", "Patna", "Kozhikode", "Deoria",
                                         "Bikaner", "Coimbatore",
                                         "Hubli", "Gurgaon", "Shillong", "Churu", "Kumily", "Dombivali", "Aurangabad",
                                         "Mohali", "Bharuch",
                                         "Ambala", "Visakhapatnam", "Warangal", "Alangad", "Mamit", "Morena",
                                         "Jamnagar", "Gondal",
                                         "Jalandhar", "Ongole", "Karaikal", "Dindigul", "Imphal", "Valsad",
                                         "Puducherry", "Mayapur", "Mumbai",
                                         "Thoothukudi", "Pune", "Bhopal", "Khammam", "Bahadurgarh", "Shimla", "Pilani",
                                         "Medinipur",
                                         "Navi Mumbai", "Kakinada", "Sambalpur", "Namakkal", "Bijnor", "Bengaluru",
                                         "Ramanathapuram",
                                         "Khandwa", "Vadodara", "Agra", "Baraut", "Jalalpore", "New Delhi", "Vaddangi",
                                         "Hyderabad",
                                         "Gonda City", "Bilimora", "Beed", "Asansol", "Nashik", "Amritsar", "Gondia",
                                         "Guwahati", "Madurai",
                                         "Thanjavur", "Chennai", "Jhajjar", "Anantapur", "Kumbakonam", "Kota",
                                         "Bareilly", "Panipat", "Jalna",
                                         "Vijayawada", "Dehradun", "Kochi", "Salem", "Vellore", "Jhansi", "Surat",
                                         "Thane", "Lucknow",
                                         "Kurnool", "Faridabad", "Ateli Mandi", "Nagpur", "Indore", "Ajmer",
                                         "Jamshedpur", "Krishnagiri",
                                         "Panvel", "Karur", "Jorhat", "Kolkata", "Malappuram", "Balasore", "Hisar",
                                         "Palladam", "Morvi",
                                         "Noida", "Thrissur", "Howrah", "Brahmapur", "Jaipur", "Ludhiana", "Ankleshwar",
                                         "Raipur", "Nellore",
                                         "Kollam", "Aizawl", "Virar", "Sitarganj", "Mitauli", "Dhanbad", "Erode",
                                         "Patan", "Raurkela",
                                         "Trivandrum", "Alappuzha", "Pathankot", "Kasaragod", "Mira Road", "Tiruchi",
                                         "Chandigarh", "Aligarh",
                                         "Rajkot", "Baddi", "Erumanur", "Greater Noida", "Churachandpur", "Meerut",
                                         "Kannur", "Deesa",
                                         "Udaipur"], "JM": ["May Pen", "Kingston", "Parish of Saint Ann"],
                                  "MR": ["Nouakchott"],
                                  "VE": ["Maracay", "Coro", "Yaritagua", "Ciudad Ojeda", "Miranda", "Biruaca",
                                         "Maiquetia", "Los Teques",
                                         "Maturín", "Anaco", "San Antonio de Los Altos", "San Bernardino", "Punto Fijo",
                                         "Cabimas",
                                         "Catia La Mar", "La Victoria", "Guatire", "Cua", "Duaca", "Sucre", "Maracaibo",
                                         "Los Dos Caminos",
                                         "Puerto Cabello", "Valera", "San Felipe", "Araure", "El Tigre", "Mariara",
                                         "Porlamar",
                                         "Ciudad Guayana", "La Asunción", "Barinas", "Catia", "Nueva Esparta",
                                         "Valencia", "Calabozo",
                                         "Trujillo", "Mérida", "Guanare", "Turmero", "Puerto Ordaz and San Felix",
                                         "Cagua", "Vargas", "Zulia",
                                         "San Carlos", "Ciudad Bolívar", "Caricuao", "Alto Barinas", "Abejales",
                                         "San Cristóbal",
                                         "Distrito Federal", "Barcelona", "Libertador", "El Pilar", "Cocote",
                                         "Carrizal", "Aragua", "Caracas",
                                         "La Guaira", "Ocumare", "Carúpano", "Cumaná", "Acarigua",
                                         "San Fernando de Apure", "Vigia",
                                         "San Juan de los Morros", "Nirgua", "Barquisimeto", "Puerto Cruz", "Lecherias",
                                         "Cabudare",
                                         "El Guarenal", "Tocuyito", "Guacara"],
                                  "GR": ["Athens", "Glyfada", "Marousi", "Thessaloniki", "Piraeus", "Nea Liosia",
                                         "Volos", "Thebes",
                                         "Rhodes"], "AL": ["Vlorë", "Lushnje", "Tirana", "Fier"], "IE": ["Dublin"],
                                  "SN": ["Thiès", "Dakar"],
                                  "PS": ["Salfit", "Hebron", "Bethlehem", "Palestine", "Nablus", "Tulkarm", "Gaza",
                                         "Khan Yunis", "Ramallah",
                                         "Jenin"],
                                  "TT": ["Williamsville", "Port of Spain", "Trincity", "Arima", "Fyzabad", "Gasparillo",
                                         "Preysal",
                                         "San Fernando", "Chaguanas", "Scarborough", "Saint Augustine"],
                                  "CR": ["Alajuela", "San José"],
                                  "TZ": ["Arusha", "Dodoma"], "RW": ["Kigali"],
                                  "RE": ["Sainte-Anne", "L'Etang-Sale", "Saint-Benoit", "Petite Ile"],
                                  "EG": ["Beheira", "6th of October City", "Al Amiriyah", "Al Hawamidiyah", "Mit Ghamr",
                                         "Bilqas", "Banha",
                                         "Agouza", "Kafr ash Shaykh", "Kafr ash Shaykh Hilal", "Arish", "Asyut",
                                         "Sohag", "Qina", "Hurghada",
                                         "Rosetta", "Al Ma`adi", "Al Qusiyah", "Baltim", "Al `Atabah",
                                         "Al 'Ashir min Ramadan", "Biyala",
                                         "Qalyubia", "Madinat an Nasr", "Faraskur", "Dokki", "Zefta", "Bani Mazar",
                                         "Awsim", "Tahta",
                                         "Sidi Bishr", "Heliopolis", "Esna", "Madinat as Sadat", "Helwan", "Al Haram",
                                         "Qus",
                                         "Al Mahallah al Kubra", "Juhaynah", "Kafr ad Dawwar", "Aswan", "Matay",
                                         "Cairo Governorate", "Giza",
                                         "Al Mansurah", "Talkha", "Shubra", "Hihya", "Port Said",
                                         "Al Qahirah al Jadidah", "Damanhur",
                                         "Minya", "Az Zamalik", "Dikirnis", "Miami", "Al Fayyum", "Al Fashn",
                                         "Shibîn el-Qanâṭir", "Gharbia",
                                         "El Alamein", "Mit Birah wa Kafr ash Shahid", "Sharqia", "Zagazig",
                                         "Bi'r al `Abd", "Aga",
                                         "Damietta", "Luxor", "Suez", "Ibshaway", "Cairo", "Ismailia", "Alexandria",
                                         "Munuf", "Samannud",
                                         "Hawsh `Isa", "Tanta", "Tima", "Al Marj", "Kafr Shukr", "Tala", "Badr",
                                         "Bani Suwayf", "Dakahlia",
                                         "Bilbeis", "Bulaq Abu al `Ila"],
                                  "MA": ["Salé", "Bejaad", "Berkane", "Imintanout", "Fes", "El Jadida", "Kenitra",
                                         "Taounate", "Azrou",
                                         "Laayoune", "Douar Laayoune", "Sidi Ifni", "Bouskoura", "Berrechid",
                                         "Khemisset", "Beni Mellal",
                                         "Nador", "Tangier", "Meknes", "Settat", "Agadir", "Temara", "Tétouan",
                                         "Ben Guerir", "Ain Taoujdat",
                                         "Casablanca", "Errachidia", "Ait Slimane", "Guercif", "Oujda", "Ain Harrouda",
                                         "Asni", "Sefrou",
                                         "Marrakesh", "Rabat", "Khouribga", "Oulad Teima", "Oued Zem"],
                                  "HK": ["Central", "Tsuen Wan"],
                                  "VI": ["Frederickstadt"],
                                  "CA": ["Montreal", "Burnaby", "Nanaimo", "Hamilton", "Langdon", "Stoney Creek",
                                         "Brantford", "Scarborough",
                                         "Windsor", "Canmore", "Vaughan", "Richmond Hill", "Victoria", "Gatineau",
                                         "St. George", "Dorval",
                                         "Vancouver", "Calgary", "Whitby", "Medicine Hat", "Fort St. John", "Trenton",
                                         "Coquitlam",
                                         "Stittsville", "Halifax", "Niagara Falls", "Strathroy", "Cold Lake",
                                         "Sherbrooke", "Duncan",
                                         "Toronto", "Oshawa", "Saint-Constant", "Saint-Jerome", "Barrie", "Markham",
                                         "North York",
                                         "Amhertsburg", "Etobicoke", "Greater Sudbury", "Langley", "Ottawa",
                                         "Beauharnois", "Mississauga",
                                         "Burlington", "Marieville", "Joliette", "Brampton", "Edmonton", "Surrey",
                                         "North Vancouver",
                                         "Laval"],
                                  "NL": ["Zutphen", "Hengelo", "Terneuzen", "Ede", "Doetinchem", "Dordrecht",
                                         "Lekkerkerk", "Zwolle",
                                         "Vlaardingen", "Delfzijl", "Papendrecht", "Capelle aan den IJssel", "Ulft",
                                         "Naaldwijk", "Delft",
                                         "Drempt", "Assen", "Sleeuwijk", "Leiden", "Schiedam", "Budel", "Almelo",
                                         "Winsum", "Amstelveen",
                                         "Bovenkarspel", "Leusden", "Son en Breugel", "Leeuwarden",
                                         "Hardinxveld-Giessendam", "Kerkrade",
                                         "The Hague", "Sliedrecht", "Hellevoetsluis", "Voorhout", "Zoetermeer",
                                         "Oegstgeest", "Lelystad",
                                         "Zaandam", "Schelluinen", "Soest", "Meppel", "Arnhem", "Helmond", "Sittard",
                                         "Dronten", "Utrecht",
                                         "Borculo", "Hoofddorp", "Groningen", "Duiven", "Oss", "Veldhoven",
                                         "Barendrecht", "Rotterdam",
                                         "Kapelle", "Amsterdam", "Heemskerk", "Stadskanaal", "Bergen op Zoom",
                                         "Almere Stad", "Enschede",
                                         "Oisterwijk", "Maastricht", "Maassluis", "Benschop", "Harlingen"],
                                  "CY": ["Nicosia", "Limassol"],
                                  "SK": ["Košice", "Humenné", "Nitra"],
                                  "CH": ["Lausanne", "Zurich", "Liebefeld", "Zweidlen-Dorf", "Gumligen", "Hochwald",
                                         "Lucerne", "Geneva",
                                         "Kriens", "Buchs"],
                                  "CN": ["Huizhou", "Baoding", "Weifang", "Nantong", "Chengdu", "Dalian", "Hangzhou",
                                         "Jining", "Nanning",
                                         "Beijing", "Dongguan", "Yangzhou", "Wuxi", "Changchun", "Chifeng", "Wuhan",
                                         "Guangzhou", "Shanghai",
                                         "Nanjing", "Zhenjiang", "Shenzhen", "Dongying", "Changzhou"],
                                  "KZ": ["Aktobe", "Almaty", "Aktau", "Astana", "Pavlodar", "Kokshetau", "Atyrau"],
                                  "CM": ["Yaoundé"],
                                  "AZ": ["Baku", "Nakhchivan", "Sumqayit"], "TC": ["Providenciales"],
                                  "HU": ["Oroshaza", "Nagykata", "Baja", "Sarvar", "Gyal", "Budapest", "Urkut",
                                         "Nyiregyhaza", "Mako",
                                         "Mohács", "Lucfalva"],
                                  "NP": ["Kathmandu", "Janakpur Dham", "Birtamod", "Taulihawa", "Pokhara", "Biratnagar",
                                         "Damak", "Jhapa"],
                                  "TH": ["Pattaya", "Nakhon Ratchasima", "Nonthaburi", "Lampang", "Surin",
                                         "Mueang Samut Prakan",
                                         "Chiang Mai", "Nakhon Pathom", "Sakon Nakhon", "Bangkok", "Chanthaburi",
                                         "Chon Buri", "Bang Phli",
                                         "Si Sa Ket", "Trang", "Chachoengsao", "Pak Kret", "Ko Samui",
                                         "Changwat Sara Buri"],
                                  "RO": ["Ineu", "Sibiu", "Bucharest", "Piatra Neamţ", "Mangalia", "Lugoj", "Galati",
                                         "Piteşti", "Ploieşti",
                                         "Cernavodă", "Brad", "Bistriţa", "Urziceni", "Constanța", "Alba Iulia",
                                         "Vaslui", "Iasi", "Ilfov",
                                         "Cluj-Napoca", "Pascani", "Timișoara", "Voluntari", "Mediaş",
                                         "Odorheiu Secuiesc", "Baia Mare",
                                         "Slobozia", "Otopeni", "Caracal", "Bacau"],
                                  "BG": ["Sofia", "Varna", "Slivnitsa", "Sandanski", "Belitsa", "Sveshtari", "Dupnitsa",
                                         "Kozloduy", "Rousse",
                                         "Sevlievo", "Dryanovo", "Plovdiv", "Petrich", "Ravda", "Sredets",
                                         "Blagoevgrad", "Haskovo", "Burgas",
                                         "Peshtera", "Lom", "Dobrich", "Byala Slatina", "Sliven", "Ribnik"],
                                  "RS": ["Čačak", "Starcevo", "Rusko Selo", "Stara Pazova", "Odzaci", "Niš",
                                         "Kragujevac", "Belgrade",
                                         "Senta", "Subotica", "Lazarevac", "Zrenjanin", "Novi Sad", "Smederevo",
                                         "Prokuplje", "Sombor",
                                         "Basaid", "Jagodina", "Ivanjica", "Novi Pazar"],
                                  "EC": ["Quito", "Gualaquiza", "Rosa Zarate", "Cotacachi", "Portoviejo", "Cuenca",
                                         "Milagro",
                                         "Santo Domingo de los Colorados", "Babahoyo", "Zamora", "Guayaquil",
                                         "La Concordia Numero Uno",
                                         "Azogues", "Ambato"], "BN": ["Bandar Seri Begawan"], "SO": ["Merca"],
                                  "YT": ["Mtsangadoua"],
                                  "US": ["Fayetteville", "Oneida", "Washington", "Concord", "Bay Shore", "San Gabriel",
                                         "Louisville", "Alma",
                                         "Lincoln Park", "El Paso", "Elk Grove", "Schenectady", "Beacon",
                                         "Tappahannock", "Oceanside",
                                         "Philadelphia", "Cornwall-on-Hudson", "Collegeville", "Middleton", "Houston",
                                         "Odessa", "Charleston",
                                         "New Smyrna Beach", "Sycamore", "Perry", "Lewisville", "Tempe", "Stockton",
                                         "Staten Island",
                                         "Las Vegas", "Clarksville", "San Diego", "Porter Ranch", "Toledo",
                                         "New Philadelphia", "Manteca",
                                         "Salt Lake City", "Newport Beach", "Bear", "Pittsburgh", "Harrisonburg",
                                         "Wise", "Lawrenceville",
                                         "Greenville", "Tyler", "Elk Grove Village", "Lynwood", "Rancho Cucamonga",
                                         "Mission", "Honolulu",
                                         "Des Plaines", "Billings", "Denver", "New York", "Eupora", "Wallingford",
                                         "Troy", "Franklin Park",
                                         "Frederick", "Richardson", "Ventura", "Cleveland", "York", "Yulee", "Reno",
                                         "Baytown", "Whittier",
                                         "Indianapolis", "Wichita", "Hollywood", "Lorain", "West Des Moines", "Seattle",
                                         "Arlington",
                                         "Glen Burnie", "Montgomery", "Summerland Key", "Paterson", "Tulsa", "St Louis",
                                         "Council Bluffs",
                                         "Cedar Knolls", "Wayne", "Encino", "Petaluma", "Henderson", "Brooklyn Park",
                                         "Rockford",
                                         "Orange Park", "Santa Rosa", "Auburn", "Orlando", "Bristol", "Hawthorne",
                                         "Westland",
                                         "Fort Lauderdale", "Kenosha", "Oxnard", "Fort Worth", "Lake Placid", "Justin",
                                         "Somerset", "Austin",
                                         "Scappoose", "Kissimmee", "Redmond", "Midland", "Upland", "Westminster",
                                         "Fort Lee", "Iola",
                                         "Meriden", "Bradenton", "Sarasota", "Rochester", "Burlingame", "Dandridge",
                                         "Pocatello", "Baker",
                                         "Spring Valley", "Marion", "Cheyenne", "Clifton", "Hamilton", "Acmetonia",
                                         "West Palm Beach",
                                         "Hillsboro", "Lenexa", "Steubenville", "Allentown", "Stone Mountain",
                                         "Brandon", "San Francisco",
                                         "Barnegat", "Lee's Summit", "Montross", "Irvine", "Benton Harbor", "Palmdale",
                                         "Wilmington",
                                         "Livermore", "Freeport", "Frisco", "Monroe", "Avenel", "Coeur d'Alene",
                                         "Mantua", "Phoenix",
                                         "Fremont", "Burlington", "Westerly", "Potsdam", "Costa Mesa", "Rex", "Ashburn",
                                         "Los Angeles",
                                         "Dobbs Ferry", "Lauderhill", "Tallahassee", "Glendale", "Malden", "Benton",
                                         "Milwaukee", "Spring",
                                         "Durham", "Carbondale", "Harriman", "Huntington Beach", "O'Fallon", "Miami",
                                         "Latrobe", "Boydton",
                                         "Victorville", "Springfield", "Shepherdsville", "North Hollywood", "La Mirada",
                                         "Conyers",
                                         "Valparaiso", "San Bruno", "Eustis", "Jersey City", "Sacramento", "Memphis",
                                         "Keswick", "Raeford",
                                         "Newport", "Santa Ana", "Fredericksburg", "Apple Valley", "Saint Joseph",
                                         "Columbia", "Fresno",
                                         "Renton", "Inglewood", "Crestline", "Lindenhurst", "Riverside", "Cranston",
                                         "Worthington", "Gilbert",
                                         "Smithtown", "Six Lakes", "Mountain View", "Omaha", "Jensen Beach",
                                         "Greenbrier", "Canyon Lake",
                                         "North Kansas City", "Okeechobee", "Kansas City", "Centerville", "Kent",
                                         "Piscataway", "Portland",
                                         "Canyon Country", "Katy", "Tampa", "Detroit", "Asheville", "Bowling Green",
                                         "Dulles", "Ruthven",
                                         "Saint Clair", "Brooklyn", "Greeley", "St. George", "Edison", "Hixson",
                                         "Phoenixville", "Sterling",
                                         "Spokane", "Round Rock", "Panama City", "DeKalb", "Lebanon",
                                         "Glenwood Springs", "La Habra",
                                         "Cincinnati", "Doylestown", "Nashville", "Irving", "Ocala", "Mobile",
                                         "Madisonville", "Pittsfield",
                                         "Redding", "Coral Springs", "Columbus", "Charlotte", "Hesperia", "Dumfries",
                                         "Thousand Oaks",
                                         "Atlantic City", "Morehead", "Hacienda Heights", "New Castle", "Hamtramck",
                                         "Union City", "Garwood",
                                         "Mount Pleasant", "Fairport", "Delray Beach", "Worcester", "Mountain Top",
                                         "San Jose", "Lakeland",
                                         "Flushing", "Zanesville", "Clermont", "White Cottage", "Dayton", "Chicago",
                                         "Santa Clara",
                                         "Beachwood", "Derby", "El Dorado Hills", "Gardnerville", "Independence",
                                         "Greenwood", "Manassas",
                                         "Atlanta", "San Antonio", "Asbury Park", "Long Branch", "Southfield",
                                         "Clinton", "Novi",
                                         "Harrodsburg", "Ellicott City", "Federal Way", "Rye", "Reston", "Kenilworth",
                                         "Valrico", "Secaucus",
                                         "Overland Park", "Sterling Heights", "Gainesville", "Woodinville", "Anderson",
                                         "West Covina",
                                         "Pflugerville", "Haslet", "North Bergen", "Mooresville", "Lakewood",
                                         "Long Beach", "Covina",
                                         "Seaside Heights", "Hyattsville", "Milford", "Dallas", "Bakersfield",
                                         "Maryville", "Johnston",
                                         "San Ramon", "Norwood", "Oak Harbor", "East Orange", "Hialeah",
                                         "Fernandina Beach", "Downingtown",
                                         "Sedro-Woolley", "Guyton", "Los Banos", "Colorado Springs", "Minneapolis",
                                         "Kennewick", "The Bronx",
                                         "The Dalles", "Kanab", "Garden Grove", "Vancouver", "Lubbock", "Chapel Hill",
                                         "Miamisburg",
                                         "Northville", "Newark", "Parrish", "Scottsdale", "Tucson", "Jupiter",
                                         "Johns Island", "Edmonds",
                                         "Plymouth", "Keller", "Boardman", "Lapeer", "Elmsford", "Saint Paul", "Denton",
                                         "Brookline",
                                         "Rancho Palos Verdes", "Jacksonville", "Naples", "Castro Valley", "Plantation",
                                         "Quincy",
                                         "North Charleston", "Little River", "Birmingham", "Fontana", "Albany",
                                         "Milton", "Keansburg"],
                                  "JP": ["Tajiri", "Hashido", "Shimoigusa", "Kugayama", "Moegino", "Higashiasahimachi",
                                         "Iwata", "Asahikawa",
                                         "Onuma", "Takasago", "Habikino", "Yachiyo", "Ichibacho", "Chiyoda-ku",
                                         "Otemachi", "Aioicho",
                                         "Honcho", "Ibaraki", "Sapporo", "Otemae", "Minoh", "Sagata", "Shimotsuruma",
                                         "Soga", "Kanuma",
                                         "Gifu", "Yamamotodori", "Tenjin", "Ekimaedori", "Hoshigaoka", "Ikegami",
                                         "Maebashi", "Saiwaicho",
                                         "Niizo", "Akasaka", "Toyonaka", "Oshiocho", "Akiyama", "Ōtsu", "Tsudanuma",
                                         "Katayamazu", "Yokohama",
                                         "Asagayakita", "Machida", "Higashiomiya", "Kurashiki", "Nishikicho",
                                         "Utsunomiya", "Kamakura",
                                         "Kokuba", "Toyoshiki", "Numazu", "Nagoya", "Gojo", "Suita", "Matsuyama",
                                         "Himeji", "Kurume",
                                         "Kasumicho", "Kochi", "Sakai", "Minamiuebaru", "Kanazawa", "Fukuyama",
                                         "Minamishimmachi",
                                         "Katsushika", "Toyama", "Ebetsu", "Oka", "Aobadai", "Kasuga", "Fujioka",
                                         "Yokkaichi", "Sakurai",
                                         "Fukushima", "Inzai", "Uonuma", "Nishihama", "Tanashicho", "Edogawa",
                                         "Shikishimacho", "Tsukamoto",
                                         "Hanakoganei", "Chuo", "Netabi", "Osaka", "Sendai", "Saganaka", "Chigasaki",
                                         "Niigata", "Hirakata",
                                         "Ueki", "Otaru", "Hamamatsu", "Nakamura", "Kobe", "Shimizu", "Motomiya",
                                         "Hiroshima", "Kitakyushu",
                                         "Takasaki", "Iruma", "Yutakacho", "Sanda Shi", "Sechigo", "Minatomirai",
                                         "Ikebukuro-honcho",
                                         "Yokosuka", "Matsudo", "Shiroi", "Shizuoka", "Hitoichimachi", "Ichikawa",
                                         "Kiyokane", "Sannomaru",
                                         "Momochihama", "Chiba", "Sakaecho", "Torishima", "Ida", "Kawasaki", "Jōyō",
                                         "Izumi-honcho", "Mito",
                                         "Edagawa", "Shinchiba", "Kuwae", "Nakano", "Takaokanishi", "Omizo", "Ōita",
                                         "Miyazaki", "Joetsu",
                                         "Sugaya", "Nagano", "Kumamoto", "Marugame", "Nishiogikita", "Meieki",
                                         "Chuodai", "Minamiedo",
                                         "Adachi", "Yamagata", "Okinawa", "Handa", "Yao", "Tokyo", "Higashinakajima",
                                         "Obihiro",
                                         "Shakujiimachi", "Hakatacho", "Kamimizo", "Suge-notoro", "Kofu", "Hikone",
                                         "Toyota", "Shinjo",
                                         "Hamanocho", "Nagasaki", "Mori", "Ogawa", "Iikura", "Hirono", "Aisai",
                                         "Okazaki", "Imanosho",
                                         "Okayama", "Kawagoe", "Koshigaya", "Natorigaoka", "Umeda", "Kashiwa",
                                         "Takamatsu", "Hakusancho-sada",
                                         "Minamimorimachi", "Higashine", "Ichinomiya", "Fukuoka", "Kyoto", "Neyagawa",
                                         "Tahara", "Heiwajima",
                                         "Uruma", "Karasawa", "Hiyoshi", "Hachiōji", "Takatsuki", "Meinohama",
                                         "Nakakura"],
                                  "AF": ["Kabul", "Jalalabad"], "LA": ["Vientiane", "Thakhek"], "VC": ["Kingstown"],
                                  "GH": ["Accra"],
                                  "GY": ["Georgetown"],
                                  "AR": ["Pilar", "Alta Gracia", "Santo Tome", "Venado Tuerto", "Ramallo",
                                         "Resistencia",
                                         "Adolfo Gonzales Chaves", "San Miguel de Tucumán", "Elisa", "Gualeguaychú",
                                         "San Miguel",
                                         "San Rafael", "Tres de Febrero", "Villa General Ramírez", "Córdoba", "Bovril",
                                         "San Fernando",
                                         "San Vicente", "San Pedro de Jujuy", "Saladillo", "City Bell", "Balcarce",
                                         "Pinamar",
                                         "Vicente Lopez", "Guernica", "Las Brenas", "Rio Grande", "Cutral-Co",
                                         "Tres Arroyos", "Chilecito",
                                         "Mar del Plata", "La Plata", "Leones", "Tortuguitas", "Puerto Eldorado",
                                         "Perico",
                                         "Santa Clara del Mar", "Ayacucho", "Ciudadela", "Palpala", "Wilde",
                                         "Libertador General San Martin",
                                         "Campo Largo", "Rufino", "Zapala", "Leandro N. Alem", "Dolores", "Del Viso",
                                         "Moreno",
                                         "San Salvador", "Orán", "La Calera", "Empalme San Vicente", "San Justo",
                                         "Villa Mercedes",
                                         "Chivilcoy", "Clorinda", "Neuquén", "Zárate", "Santa Fe", "Pampa del Infierno",
                                         "Rio Primero",
                                         "Trelew", "Villa Carlos Paz", "Villa Ballester", "Rosario del Tala",
                                         "Concepción del Uruguay",
                                         "Longchamps", "Crespo", "Ituzaingo", "Presidencia de la Plaza",
                                         "Veinticinco de Mayo", "Berazategui",
                                         "Gaiman", "Chimbas", "Federal", "Puerto Madryn", "Colon", "Necochea",
                                         "Fontana", "Tandil", "Glew",
                                         "Libertad", "Pehuajó", "Villa Adelina", "Rosario", "Ingeniero Maschwitz",
                                         "Paraná", "Villa Alsina",
                                         "Mercedes", "Santa Rosa", "Belen de Escobar", "Mar del Tuyu", "Beccar",
                                         "Merlo", "Oro Verde",
                                         "Pergamino", "Adrogue", "Isidro Casanova", "Gobernador Crespo", "Posadas",
                                         "El Talar", "Albardon",
                                         "Salsipuedes", "Barranqueras", "Cruz del Eje", "Río Gallegos", "San Juan",
                                         "San Martin", "Luján",
                                         "Guatimozin", "Bahía Blanca", "Concordia", "Esther", "San Pedro",
                                         "Bella Vista", "La Rioja",
                                         "Rio Segundo", "San Luis", "Lanus", "Campana", "Jose C. Paz",
                                         "Florencio Varela",
                                         "San Francisco Solano", "Pico Truncado", "Junín", "28 de Noviembre",
                                         "Trenque Lauquen", "Berisso",
                                         "Salta", "San Salvador de Jujuy", "Obera", "Ushuaia", "General Pinedo",
                                         "Castelar", "Curuzu Cuatia",
                                         "Mendoza", "La Banda", "San Isidro", "Avellaneda", "Pilciao", "Caviahue",
                                         "Burzaco", "Laprida",
                                         "Presidencia Roque Sáenz Peña", "Quilmes", "Monte Grande", "Catamarca",
                                         "Cinco Saltos", "Florida",
                                         "Buenos Aires", "Río Cuarto", "Carmen de Areco", "Tunuyan", "Corrientes",
                                         "Santiago del Estero",
                                         "Tigre", "Formosa", "General Roca", "Nueve de Julio", "Yerba Buena",
                                         "Hurlingham",
                                         "San Francisco del Monte de Oro", "Concepcion", "Ranchos", "Olavarría",
                                         "Aguilares", "Maipu",
                                         "Rodeo del Medio", "Boulogne", "Nogoya", "La Paz", "Arrecifes", "Castelli",
                                         "Montecarlo",
                                         "Gonzalez Catan", "Llavallol", "Moron", "General San Martin", "Santa Teresita",
                                         "Lomas del Mirador",
                                         "Caseros", "Lomas de Zamora", "La Leonesa", "Villa María", "Laferrere",
                                         "Ciudad Evita",
                                         "Jesus Maria", "El Colorado", "San Jose de la Esquina", "Puerto Vilelas",
                                         "Luis Guillon", "Ensenada",
                                         "Villa Madero", "Munro"], "GA": ["Libreville"],
                                  "NA": ["Walvis Bay", "Windhoek", "Swakopmund"],
                                  "KH": ["Siem Reap", "Phnom Penh", "Sihanoukville", "Pursat", "Bavet", "Battambang"],
                                  "MX": ["Venustiano Carranza", "Querétaro City", "Toluca", "Solidaridad",
                                         "Puerto Vallarta", "Parral",
                                         "Ciudad Obregón", "Nogales", "Culiacán", "San Vicente", "Huauchinango",
                                         "Cabo San Lucas",
                                         "Huixquilucan de Degollado", "Mexico City", "Guadalupe Trujillo",
                                         "Puente de Ixtla",
                                         "San Luis Potosí City", "Zapotlanejo", "Juarez", "Tula de Allende", "Irapuato",
                                         "Atitalaquia",
                                         "Ciudad Nezahualcoyotl", "Iztapalapa", "Oaxaca City", "Puebla City",
                                         "Chilpancingo", "Zapopan",
                                         "Altamira", "Ensenada", "Zamora", "Naucalpan", "Lázaro Cárdenas",
                                         "Gustavo Adolfo Madero",
                                         "Tlalnepantla", "Monclova", "Ciudad Juárez", "Campeche", "Cuernavaca",
                                         "Tampico", "Coyoacán", "León",
                                         "Tecoman", "Torreón", "Monterrey", "Poza Rica de Hidalgo", "Tlalpan",
                                         "Macuspana", "Pachuca",
                                         "Tlapa de Comonfort", "Chalco", "Puerto Peñasco", "Heroica Matamoros",
                                         "Mérida", "Chihuahua City",
                                         "Centro", "Tijuana", "Ecatepec", "Xochimilco", "Coatzacoalcos", "Mazatlán",
                                         "Guaymas", "Minatitlán",
                                         "Reynosa", "Jalpa de Mendez", "Hermosillo", "Guadalajara", "Mexicali",
                                         "Guadalupe"],
                                  "BD": ["Shailkupa", "Habiganj", "Netrakona", "Noagaon", "Mirpur", "Nilphamari",
                                         "Chuadanga", "Gazipur",
                                         "Mymensingh", "Ulipur", "Feni", "Saidpur", "Ullapara", "Chittagong", "Barguna",
                                         "Rajshahi",
                                         "Kishorganj", "Dhaka", "Comilla", "Bogra", "Barishal", "Raipur", "Narsingdi",
                                         "Pabna", "Noakhali",
                                         "Meherpur", "Narayanganj", "Sylhet", "Jessore", "Tongi", "Manikganj",
                                         "Cox's Bazar", "Sirajganj",
                                         "Sunamganj", "Gaibandha", "Bholuka"],
                                  "PK": ["Faisalabad", "Gujrat", "Jhelum", "Bahawalpur", "Little Attock", "Multan",
                                         "Hafizabad", "Lakki",
                                         "Mandi Burewala", "Islamabad", "Karachi", "Quetta", "Rawalpindi", "Hyderabad",
                                         "Mianwali", "Sialkot",
                                         "Sargodha", "Rahim Yar Khan", "Kasur", "Shahkot", "Shabqadar", "Lahore",
                                         "Gujranwala", "Pakpattan",
                                         "Goth Hāla", "Rawlakot", "Mardan", "Chak Forty-two SP", "Manga Mandi",
                                         "Peshawar"],
                                  "GE": ["Oni", "Zugdidi", "Kutaisi", "Akhalk'alak'i", "Tbilisi", "Batumi"],
                                  "KY": ["George Town"],
                                  "GL": ["Aasiaat"], "MM": ["Tachilek", "Yangon", "Mandalay"], "VU": ["Norsup"],
                                  "FI": ["Salo", "Helsinki", "Lappeenranta"],
                                  "PH": ["Caloocan City", "Caba", "Malabon", "Santa Rita", "Bulacan", "Siaton",
                                         "Cainta", "Iloilo City",
                                         "Davao City", "San Pablo City", "Marilao", "Angeles City", "Carmen",
                                         "Malaybalay", "Tarlac City",
                                         "Panabo", "Lingayen", "Lapu-Lapu City", "Bacoor", "Calamba", "Alcala",
                                         "Quezon City",
                                         "Antipolo City", "Taguig", "Masbate", "Ozamiz", "Tagudin", "Kasilawan",
                                         "Pasay", "Talavera",
                                         "Carmona", "Pasig-bo", "Magugpo Poblacion", "Tuguegarao City", "Canaman",
                                         "Cadiz", "Marikina City",
                                         "Cotabato City", "Saravia", "Tanjay", "Cebu City", "Lahug", "Cabanatuan City",
                                         "Malolos", "Goa",
                                         "Norzagaray", "Malate", "Ramon Magsaysay", "Makati City", "La Trinidad",
                                         "San Pedro",
                                         "Mandaluyong City", "Roxas City", "Laoag", "Santo Tomas", "Tabogon",
                                         "Bacolod City", "Butuan",
                                         "Mandaue City", "Pototan", "Maddela", "Iligan", "General Santos",
                                         "Santa Maria", "Las Pinas", "Naga",
                                         "Sorsogon", "Bislig", "Calauag", "Cabuyao", "Lipa City", "Zamboanga City",
                                         "Paranaque City",
                                         "Manila", "Murcia", "San Jose", "Santa Rosa", "Rodriguez", "Umingan", "Isulan",
                                         "Pagsanjan",
                                         "Cavite City", "Lagindingan", "Legazpi", "Nasugbu", "San Jose del Monte",
                                         "Urdaneta", "Batangas",
                                         "Los Banos", "Calauan", "Cagayan de Oro", "Lucena City", "Binangonan", "Pasig",
                                         "San Juan",
                                         "Koronadal", "Agoo", "Tabaco", "Calbayog City", "San Miguel", "Tanauan",
                                         "Kawit", "San Marcelino",
                                         "Solano", "Baguio City", "Puerto Princesa City", "Tanza", "Balingasag",
                                         "Dasmarinas", "Barobo",
                                         "Green Park", "Dagupan", "Pagadian", "San Carlos City", "Tagbilaran",
                                         "General Trias", "Imus",
                                         "Tandag", "San Carlos", "Concepcion Dos", "Malanday", "Kidapawan", "Santiago",
                                         "Valenzuela",
                                         "Bocaue", "San Fernando City", "Caruhatan", "Mabalacat"], "ER": ["Asmara"],
                                  "MP": ["Saipan"],
                                  "RU": ["Vyborg", "Nakhodka", "Izhevsk", "Yekaterinburg", "Shchelkovo", "Cheboksary",
                                         "Stupino",
                                         "Kostomuksha", "Tver", "St Petersburg", "Sayanogorsk", "Petrozavodsk",
                                         "Bratsk", "Tomsk", "Magadan",
                                         "Novokuznetsk", "Vladivostok", "Tikhvin", "Blagoveshchensk", "Kopeysk",
                                         "Kirov", "Yaroslavl",
                                         "Rostov-on-Don", "Tuapse", "Minusinsk", "Naro-Fominsk", "Belovo",
                                         "Dolgoprudnyy", "Kaliningrad",
                                         "Petropavlovsk-Kamchatsky", "Klimovsk", "Ust'-Kut", "Neftekamsk", "Kirzhach",
                                         "Pechora",
                                         "Cherepovets", "Yablonitsy", "Voronezh", "Komsomolsk-on-Amur", "Penza",
                                         "Svetogorsk", "Berezniki",
                                         "Zhukovskiy", "Ufa", "Orenburg", "Miass", "Smolensk", "Barnaul", "Volgograd",
                                         "Morshansk", "Abakan",
                                         "Murmansk", "Bologoye-4", "Surgut", "Derbent", "Mytishchi", "Armavir",
                                         "Taganrog", "Seversk",
                                         "Vyksa", "Yakutsk", "Ivanovo", "Donetsk", "Apatity", "Otradnoye",
                                         "Novorossiysk", "Ulyanovsk",
                                         "Syktyvkar", "Sarov", "Krasnoyarsk", "Chelyabinsk", "Makhachkala", "Ussuriysk",
                                         "Cheremkhovo",
                                         "Okha", "Saransk", "Leninogorsk", "Tolyatti", "Sochi", "Tambov",
                                         "Zagoryanskiy", "Chaykovskiy",
                                         "Kanevskaya", "Mezhdurechensk", "Ust'-Ilimsk", "Omsk", "Astrakhan",
                                         "Naberezhnyye Chelny",
                                         "Korolyov", "Nizhniy Novgorod", "Kostroma", "Engel's", "Chita", "Nevel",
                                         "Marfino", "Bryansk",
                                         "Nal'chik", "Balashikha", "Vitimskiy", "Klin", "Kudymkar", "Kirovsk",
                                         "Vladikavkaz", "Belaya Glina",
                                         "Nizhnekamsk", "Irkutsk", "Ulan-Ude", "Tula", "Korsakov", "Frolovo",
                                         "Ramenskoye", "Korkino",
                                         "Novocherkassk", "Belgorod", "Monchegorsk", "Kolomna", "Kemerovo", "Poronaysk",
                                         "Krasnopol'ye",
                                         "Taysara", "Kursk", "Salekhard", "Krasnodar", "Kazan'", "Arkhangelsk",
                                         "Kraskovo", "Biysk",
                                         "Arsen'yev", "Dalnegorsk", "Pervouralsk", "Vsevolozhsk", "Murino", "Kolpino",
                                         "Ukhta",
                                         "Zheleznogorsk", "Khabarovsk", "Angarsk", "Reutov", "Kholmsk", "Saratov",
                                         "Ishnya", "Tosno",
                                         "Lipetsk", "Vologda", "Kol'chugino", "Veliky Novgorod", "Chekhov", "Oryol",
                                         "Olya", "Moscow",
                                         "Tyumen", "Yuzhno-Sakhalinsk", "Novosibirsk", "Sterlitamak", "Kaluga",
                                         "Nogliki", "Yoshkar-Ola",
                                         "Sergiyev Posad", "Kurgan", "Samara", "Iksha", "Koryazhma", "Nazarovo",
                                         "Obninsk", "Uzlovaya",
                                         "Stavropol", "Perm", "Vladimir", "Karpinsk"],
                                  "CU": ["Santa Clara", "Camagüey", "San German", "La Playa", "Havana", "Bayamo"],
                                  "TN": ["Rades", "El Fahs", "Kelibia", "Beni Khalled", "Manouba", "Sukrah", "Mateur",
                                         "El Kef", "Gafsa",
                                         "Ferryville", "Sahline", "Siliana", "Hammam Sousse", "Tajerouine", "Hammamet",
                                         "Bizerte", "Akouda",
                                         "Borj Cedria", "La Marsa", "Houmt Souk", "Tebourba", "Sfax", "Medjez el Bab",
                                         "Tozeur", "Zahrouni",
                                         "Sidi Bouzid", "Aryanah", "Ben Arous", "Teboulba", "Nabeul", "Zaghouan",
                                         "Megrine", "Sousse",
                                         "Monastir", "Menzel Jemil", "Cité El Khadhra", "Kairouan", "Soliman",
                                         "Ksar Hellal", "Chebba",
                                         "Korba", "Tunis", "Mahdia"], "LT": ["Vilnius", "Kaunas", "Klaipėda"],
                                  "BE": ["Zoersel", "Nieuwpoort", "Lanaken", "Overmere", "Ghent", "Mouscron",
                                         "Zuienkerke", "Couvin",
                                         "Torhout", "Brussels", "Antwerp", "Zingem", "Aywaille", "Roeselare",
                                         "Roosdaal", "Messelbroek",
                                         "Snaaskerke", "Namur", "Edegem", "Gavere", "Charleroi", "Battice", "Quaregnon",
                                         "Marche-en-Famenne",
                                         "Riemst", "Oudenaarde", "Dilbeek"], "EE": ["Tallinn", "Jõhvi"],
                                  "MW": ["Lilongwe"],
                                  "LU": ["Luxembourg"],
                                  "DZ": ["Seddouk", "Naciria", "Bou Haroun", "Bordj Zemoura", "Telerghma",
                                         "Hassi Messaoud", "Ain Fakroun",
                                         "M'Chedallah", "Maghnia", "Sougueur", "Ras el Oued", "Tissemsilt", "Béjaïa",
                                         "Collo", "Guelma",
                                         "Larbaâ", "Oued el Alleug", "Heliopolis", "Ouargla", "Blida", "El Hammam",
                                         "El Aouinet", "Birtouta",
                                         "Arris", "Hassi Bahbah", "Chebli", "Bir el Djir", "Draria", "Bougaa",
                                         "Mecheria", "Tidjelabine",
                                         "Bir el Ater", "Azib Aboudaou", "Bou Saada", "Algiers", "Lakhdaria", "Baraki",
                                         "Ghardaïa", "Rouiba",
                                         "Ain Taya", "Sétif", "Theniet el Had", "Kouba", "Zgoum", "Souk Ahras",
                                         "Mascara", "Ain Beida",
                                         "Kolea", "Lardjem", "Taghit", "M'Sila", "Mostaganem", "Boumerdes", "Kouinine",
                                         "Souma", "Ghazaouet",
                                         "Aflou", "Hennaya", "'Ain el Hammam", "El Eulma", "Ain Oulmene", "Constantine",
                                         "Sidi Aissa",
                                         "Tébessa", "El Hadjira", "Barika", "Sidi Aich", "Berriane", "El Bayadh",
                                         "Ain Temouchent", "Jijelli",
                                         "Djelfa", "Tlemcen", "Sebdou", "Boudjima", "Tolga", "El Tarf", "El Affroun",
                                         "Tiaret", "Skikda",
                                         "Relizane", "Beni Amrane", "Tipasa", "Hassi Maameche", "Sidi Aoun", "Rahouia",
                                         "Didouche Mourad",
                                         "Arzew", "Bordj Bou Arreridj", "Boghni", "L'Agha", "El Achour", "Feraoun",
                                         "Adrar", "Sedrata",
                                         "Batna City", "Biskra", "Sidi Akkacha", "El Abadia", "Ighram", "Sidi Okba",
                                         "Bouïra", "Ain Nouissy",
                                         "Laghouat", "Meskiana", "Hadjout", "Cherchell", "Amalou", "Zarzaitine", "Oran",
                                         "Abadla",
                                         "ash-Shalif", "Zeralda", "Mila", "Ramdane Djamal", "El Omaria", "Taher",
                                         "Mazouna", "'Ain el Melh",
                                         "Sidi Bel Abbes", "El Madania", "El Milia", "Bou Arfa", "El Oued", "Amizour",
                                         "Béchar", "Annaba",
                                         "Draa Ben Khedda", "Khenchela", "Tizi Ouzou", "Saida", "Djendel",
                                         "Bab Ezzouar", "Reghaia", "Sig",
                                         "Debila", "Messaad", "Tamanghasset", "Bordj el Bahri", "Medea", "Dar el Beida",
                                         "Akbou", "Nedroma",
                                         "Oum el Bouaghi", "Rouina", "Boufarik", "Hammam Dalaa", "Ourlal", "Arbatache",
                                         "Berrahal",
                                         "Ain Defla", "Reguiba", "Ain Touta"],
                                  "VN": ["Cao Lanh", "Kon Tum", "Bac Ninh", "Tam Binh", "Hanoi", "Da Nang", "Nam Định",
                                         "Tan Tuc", "Tra Vinh",
                                         "Bac Giang", "Tan Phu", "Bến Tre", "Cao Bang", "Can Tho", "Thai Nguyen",
                                         "Haiphong", "Hung Yen",
                                         "An Giang", "Ca Mau", "Ha Giang", "Binh Duong", "Ho Chi Minh City",
                                         "Hai Duong", "Lao Cai", "Vinh",
                                         "Soc Trang", "Bien Hoa", "Viet Tri", "Tinh Binh Duong", "Sơn La", "Thai Binh",
                                         "Ninh Binh",
                                         "Tay Ninh", "Lai Chau", "My Tho", "Vĩnh Long", "Vinh Yen", "Pleiku",
                                         "Vũng Tàu", "Rach Gia",
                                         "Nha Trang", "Thuan An", "Tan Tien", "Thanh Hóa", "Binh Tan", "Thanh Son"],
                                  "LV": ["Riga", "Liepāja"], "MD": ["Chisinau", "Cahul", "Soltanesti"],
                                  "MU": ["Beau Bassin-Rose Hill", "Port Louis"], "SB": ["Honiara"],
                                  "SV": ["Zacatecoluca", "San Salvador", "Santo Tomas", "La Libertad", "Sonsonate",
                                         "Ahuachapan", "Lourdes",
                                         "San Miguel", "Soyapango", "Quezaltepeque", "Santa Ana", "La Union",
                                         "San Miguel Ingenio",
                                         "Usulutan", "San Martin", "Nahuizalco", "Santa Tecla"],
                                  "HR": ["Koprivnica", "Zagreb", "Osijek", "Rijeka", "Donja Voca", "Split"],
                                  "IL": ["Rishon LeTsiyyon", "Jerusalem", "Tel Aviv", "Haifa", "Holon", "Ashquelon",
                                         "Qiryat Ata"],
                                  "NC": ["Noumea"], "KW": ["Kuwait City"], "FM": ["State of Pohnpei"],
                                  "MY": ["Cyberjaya", "Shah Alam", "George Town", "Kuala Lumpur", "Petaling Jaya",
                                         "Kota Kinabalu",
                                         "Puchong Batu Dua Belas", "Batu Pahat", "Kuala Terengganu", "Johor Bahru",
                                         "Ipoh"],
                                  "GF": ["Cayenne"], "PY": ["Caacupe", "Luque", "Asunción", "Estancia Nueva Esperanza"],
                                  "MG": ["Mahajanga", "Toamasina", "Antananarivo"], "KE": ["Nairobi"],
                                  "LC": ["Castries"],
                                  "PA": ["Panama City", "David"], "BW": ["Gaborone", "Francistown"],
                                  "CL": ["Santiago", "Antofagasta", "Concepción", "Futrono", "La Union", "Castro",
                                         "Iquique", "Talca",
                                         "Osorno", "Quillota"], "SC": ["Victoria"], "KG": ["Bishkek"],
                                  "PF": ["Papeete"],
                                  "ES": ["Las Torres de Cotillas", "Puerto de la Cruz", "A Pobra do Caraminal",
                                         "Tomelloso", "Igualada",
                                         "Málaga", "Elche", "Armilla", "Ripoll", "Murcia", "Madrid", "Albacete",
                                         "Boadilla del Monte",
                                         "Barcelona", "Castelló de la Plana", "Ferrol", "Santa Coloma de Gramenet",
                                         "Casariche", "Torrent",
                                         "Tarragona", "Jerez de la Frontera", "Espartinas", "Valencia", "Vigo"],
                                  "UA": ["Cherkasy", "Pobuzke", "Odesa", "Uman", "Sevastopol", "Yavoriv", "Kremenchug",
                                         "Mala Vyska",
                                         "Teplodar", "Donetsk", "Mohyliv-Podilskyy", "Okhtyrka", "Kherson", "Selidovo",
                                         "Mykolayiv", "Kalush",
                                         "Lviv", "Simferopol", "Horishni Plavni", "Irpin", "Hadyach", "Kyiv",
                                         "Chernihiv", "Horodok",
                                         "Kamianske", "Chornomorsk", "Perechyn", "Nova Vodolaha",
                                         "Korsun-Shevchenkivskyy", "Kharkiv",
                                         "Arbuzynka", "Khmelnytskyi", "Kropyvnytskyi", "Chernivtsi", "Kakhovka",
                                         "Dnipro", "Zaporizhzhya",
                                         "Bila Tserkva", "Crimea", "Sambir", "Terebovlia", "Kamianets-Podilskyi",
                                         "Vinnytsia", "Polonne"],
                                  "GN": ["Conakry"], "GM": ["Serrekunda"],
                                  "IT": ["Parabiago", "Ardenno", "San Pietro a Maida", "Misano Adriatico",
                                         "Pozzuolo del Friuli",
                                         "Rignano Flaminio", "Arezzo", "Milan", "Teramo", "Castelfranco Emilia", "Rome",
                                         "Aversa", "Naples",
                                         "Teverola", "Arona", "Salerno", "Turin", "Città Sant'Angelo", "Baricella",
                                         "Campana",
                                         "Pomigliano d'Arco", "Valdagno di Trento", "Montevarchi", "Siena", "Pescara",
                                         "Bari", "Florence",
                                         "Assisi", "Siziano", "Macerata", "San Giuseppe Vesuviano", "Bologna",
                                         "Bitritto", "Vicenza",
                                         "Perugia"],
                                  "PT": ["Matosinhos Municipality", "Lisbon", "Caldas da Rainha", "Oia",
                                         "Ponta Delgada", "Coimbra",
                                         "Barreiro", "Covilha", "Retorta", "Vila Nova de Gaia", "Golega", "Leiria",
                                         "Vila Nova de Famalicao",
                                         "Guimarães", "Oeiras", "Arcozelo", "Odivelas", "Amadora", "Evora", "Estoril",
                                         "Oliveira do Bairro"],
                                  "BO": ["Sucre", "Cochabamba", "Oruro", "Yacuiba", "La Paz", "Santa Cruz"],
                                  "FJ": ["Lautoka", "Suva"],
                                  "NZ": ["Auckland", "Tauranga", "Christchurch"],
                                  "NO": ["Gressvik", "Trondheim", "Oslo", "Strauman", "Tromsø", "Mandal"],
                                  "SR": ["Paramaribo"],
                                  "GB": ["Havant", "Barnet", "Hayes", "Waltham Abbey", "Southsea", "Islington",
                                         "Burnley", "Cardiff",
                                         "Hartlepool", "Lambeth", "Walsall", "Watford", "Colchester", "Oldbury",
                                         "Glasgow", "Belfast",
                                         "Wimborne Minster", "Rothwell", "South Shields", "Brent", "Motherwell",
                                         "Bristol", "Bognor Regis",
                                         "Manchester", "Darlington", "Thurso", "Brierley Hill", "Kettering",
                                         "Northampton", "Epsom", "Harrow",
                                         "Porth", "Edinburgh", "Blackburn", "St Helens", "Dagenham", "Southport",
                                         "Sheffield", "New Milton",
                                         "Cheltenham", "Huntingdon", "Maidstone", "Dunstable", "Thornton Heath",
                                         "Portsmouth", "Birmingham",
                                         "Banbury", "Margate", "London", "Bromley", "Wakefield", "Dartford", "Corby",
                                         "Hemel Hempstead",
                                         "High Wycombe", "Chelmsford", "Greenford", "Wembley", "Cambridge",
                                         "Great Malvern", "Leyton",
                                         "Maidenhead", "Bedford", "Aylesbury", "Liverpool", "Brighton", "Leeds",
                                         "Ormskirk", "Coventry"],
                                  "PL": ["Suchy Las", "Pisz", "Skarzysko-Kamienna", "Siedlisko", "Pruszków", "Wyszków",
                                         "Lublin", "Pajeczno",
                                         "Wroclaw", "Ruda Śląska", "Radomsko", "Piaseczno", "Warsaw", "Lodz", "Gdansk",
                                         "Zglobice",
                                         "Częstochowa", "Glogowek", "Stalowa Wola", "Krakow", "Gdynia"],
                                  "MK": ["Tetovo", "Gevgelija", "Skopje"],
                                  "BA": ["Mostar", "Brcko", "Sekovici", "Visoko", "Sarajevo", "Banja Luka", "Tuzla",
                                         "Gracanica"],
                                  "GP": ["Pointe-à-Pitre", "Petit-Bourg", "Les Abymes", "Morne-a-l'Eau",
                                         "Capesterre-Belle-Eau"],
                                  "MT": ["Sliema", "Qormi", "Zejtun", "Ghajnsielem", "Swieqi"],
                                  "IQ": ["Al Hillah", "Basrah", "Kirkuk", "Tikrit", "Sulaymaniyah", "Karbala", "Erbil",
                                         "Kut", "Al Anbar",
                                         "Najaf", "Mosul", "Fallujah", "Ramadi", "Hayy al Muthanna", "Baghdad", "Duhok",
                                         "Baqubah", "Samarra",
                                         "Ar Rumaythah", "Raniye"],
                                  "AU": ["Melbourne", "Bungarribee", "Canberra", "Sydney", "Perth", "Adelaide"]}

us_countries = {'US'}
uk_gb_countries = {'GB'}
canada_countries = {'CA'}
english_speaking_countries = {"AU", "IE", "NZ"}
other_1st_world_countries = {"AT", "BE", "DK", "FI", "FR", "DE", "IT", "JP", "LU", "NL", "NO", "KR", "ES", "SE",
                             "CH"}


# define a function that returns a country based on the given weights
def get_country():
    us_weight = 0.68
    uk_gb_weight = 0.08
    canada_weight = 0.08
    english_speaking_weight = 0.07
    other_1st_world_weight = 0.05


    # add all the remaining countries to a set named other_countries
    all_countries = \
        {"GD", "DM", "LK", "MN", "PE", "XK", "MO", "AM", "TW", "LY", "SA", "NG", "GQ", "BR", "ID", "DO",
         "PG", "FR", "CZ", "BY", "DK", "KR", "CI", "LB", "BZ", "CW", "CO", "ET", "AD", "QA", "UZ", "TR", "PR",
         "HT", "ZW",
         "BB", "SE", "AT", "AO", "AE", "ME", "IR", "NI", "DE", "UY", "JO", "SI", "BF", "CD", "YE", "ZA", "GT",
         "SZ", "BM",
         "PW", "HN", "MQ", "IN", "JM", "MR", "VE", "GR", "AL", "IE", "SN", "PS", "TT", "CR", "TZ", "RW",
         "RE", "EG",
         "MA", "HK", "VI", "CA", "NL", "CY", "SK", "CH", "CN", "KZ", "CM", "AZ", "TC", "HU", "NP", "TH",
         "RO", "BG",
         "RS", "EC", "BN", "SO", "YT", "US", "JP", "AF", "LA", "VC", "GH", "GY", "AR", "GA", "NA",
         "KH", "MX",
         "BD", "PK", "GE", "KY", "GL", "MM", "VU", "FI", "PH", "ER", "MP", "RU", "CU", "TN", "LT", "BE",
         "EE", "MW",
         "LU", "DZ", "VN", "LV", "MD", "MU", "SB", "SV", "HR", "IL", "NC", "KW", "FM", "MY", "GF", "PY", "MG",
         "KE", "LC",
         "PA", "BW", "CL", "SC", "KG", "PF", "ES", "UA", "GN", "GM", "IT", "PT",
         "BO", "FJ",
         "NZ", "NO", "SR", "GB", "PL", "MK", "BA", "GP", "MT", "IQ", "AU"}
    other_countries = all_countries - us_countries - uk_gb_countries - canada_countries - english_speaking_countries - other_1st_world_countries

    r = random.random()
    if r < us_weight:
        return random.choice(list(us_countries))
    elif r < us_weight + uk_gb_weight:
        return random.choice(list(uk_gb_countries))
    elif r < us_weight + uk_gb_weight + canada_weight:
        return random.choice(list(canada_countries))
    elif r < us_weight + uk_gb_weight + canada_weight + english_speaking_weight:
        return random.choice(list(english_speaking_countries))
    elif r < us_weight + uk_gb_weight + canada_weight + english_speaking_weight + other_1st_world_weight:
        return random.choice(list(other_1st_world_countries))
    else:
        return random.choice(list(other_countries))


def fetch_percentage_value(number, percent):
    """
    A Simple Function To Calculate And Return The Value Of A Percentage On a Number
    :param number: The Number To Calculate On
    :param percent: The Percentage Of Number Needed
    :return: The Value Of The Percentage
    """
    value = number * percent / 100
    return value


def retrieve_list_data_from_file(file_path):
    loaded_list = []
    with open(file_path, "r") as l_file:
        for l in l_file:
            loaded_list.append(l.splitlines()[0])
    return loaded_list


def generate_persona_language(country_code):
    en_languages = {'01': ['en-001', 'en'], '50': ['en-150', 'en'], 'AG': ['en-AG', 'en'], 'AI': ['en-AI', 'en'],
                    'AS': ['en-AS', 'en'], 'AT': ['en-AT', 'en'], 'AU': ['en-AU', 'en'], 'BB': ['en-BB', 'en'],
                    'BE': ['en-BE', 'en'], 'BI': ['en-BI', 'en'], 'BM': ['en-BM', 'en'], 'BS': ['en-BS', 'en'],
                    'BW': ['en-BW', 'en'], 'BZ': ['en-BZ', 'en'], 'CA': ['en-CA', 'en'], 'CC': ['en-CC', 'en'],
                    'CH': ['en-CH', 'en'], 'CK': ['en-CK', 'en'], 'CM': ['en-CM', 'en'], 'CX': ['en-CX', 'en'],
                    'CY': ['en-CY', 'en'], 'DE': ['en-DE', 'en'], 'DG': ['en-DG', 'en'], 'DK': ['en-DK', 'en'],
                    'DM': ['en-DM', 'en'], 'ER': ['en-ER', 'en'], 'FI': ['en-FI', 'en'], 'FJ': ['en-FJ', 'en'],
                    'FK': ['en-FK', 'en'], 'FM': ['en-FM', 'en'], 'GB': ['en-GB', 'en'], 'GD': ['en-GD', 'en'],
                    'GG': ['en-GG', 'en'], 'GH': ['en-GH', 'en'], 'GI': ['en-GI', 'en'], 'GM': ['en-GM', 'en'],
                    'GU': ['en-GU', 'en'], 'GY': ['en-GY', 'en'], 'HK': ['en-HK', 'en'], 'IE': ['en-IE', 'en'],
                    'IL': ['en-IL', 'en'], 'IM': ['en-IM', 'en'], 'IN': ['en-IN', 'en'], 'IO': ['en-IO', 'en'],
                    'JE': ['en-JE', 'en'], 'JM': ['en-JM', 'en'], 'KE': ['en-KE', 'en'], 'KI': ['en-KI', 'en'],
                    'KN': ['en-KN', 'en'], 'KY': ['en-KY', 'en'], 'LC': ['en-LC', 'en'], 'LR': ['en-LR', 'en'],
                    'LS': ['en-LS', 'en'], 'MG': ['en-MG', 'en'], 'MH': ['en-MH', 'en'], 'MO': ['en-MO', 'en'],
                    'MP': ['en-MP', 'en'], 'MS': ['en-MS', 'en'], 'MT': ['en-MT', 'en'], 'MU': ['en-MU', 'en'],
                    'NA': ['en-NA', 'en'], 'NF': ['en-NF', 'en'], 'NG': ['en-NG', 'en'], 'NL': ['en-NL', 'en'],
                    'NR': ['en-NR', 'en'], 'NU': ['en-NU', 'en'], 'NZ': ['en-NZ', 'en'], 'PG': ['en-PG', 'en'],
                    'PH': ['en-PH', 'en'], 'PK': ['en-PK', 'en'], 'PN': ['en-PN', 'en'], 'PR': ['en-PR', 'en'],
                    'PW': ['en-PW', 'en'], 'RW': ['en-RW', 'en'], 'SB': ['en-SB', 'en'], 'SC': ['en-SC', 'en'],
                    'SD': ['en-SD', 'en'], 'SE': ['en-SE', 'en'], 'SG': ['en-SG', 'en'], 'SH': ['en-SH', 'en'],
                    'SI': ['en-SI', 'en'], 'SL': ['en-SL', 'en'], 'SS': ['en-SS', 'en'], 'SX': ['en-SX', 'en'],
                    'SZ': ['en-SZ', 'en'], 'TC': ['en-TC', 'en'], 'TK': ['en-TK', 'en'], 'TO': ['en-TO', 'en'],
                    'TT': ['en-TT', 'en'], 'TV': ['en-TV', 'en'], 'TZ': ['en-TZ', 'en'], 'UG': ['en-UG', 'en'],
                    'UM': ['en-UM', 'en'], 'US': ['en-US', 'en'], 'VC': ['en-VC', 'en'], 'VG': ['en-VG', 'en'],
                    'VI': ['en-VI', 'en'], 'VU': ['en-VU', 'en'], 'WS': ['en-WS', 'en'], 'ZA': ['en-ZA', 'en'],
                    'ZM': ['en-ZM', 'en'], 'ZW': ['en-ZW', 'en']}
    default = ['en-US', 'en']
    default_2 = ['en-GB', 'en']
    if country_code == 'US':
        return en_languages.get(country_code, default)
    elif country_code == 'CA':
        if random.random() < 0.69:
            return en_languages.get(country_code, default)
        else:
            return default
    elif country_code == 'GB':
        if random.random() < 0.92:
            return en_languages.get(country_code, default)
        else:
            return default
    elif country_code in english_speaking_countries:
        if random.random() < 0.55:
            if random.random() < 0.58:
                return default
            else:
                return default_2
        else:
            return en_languages.get(country_code, default)
    else:
        if random.random() < 0.82:
            if random.random() < 0.72:
                return default
            else:
                return default_2
        else:
            return en_languages.get(country_code, default)
    return default

def generate_persona(
        no_of_persona_to_generate=120114, percentage_of_smartphone=57.34, percentage_of_pc=42.66,
        percentage_of_windows=[96.5346, {'chrome': 100, 'firefox': 0, 'edge': 0}],
        percentage_of_mac=[2.0019, {'chrome': 100, 'firefox': 0, 'edge': 0}],
        percentage_of_linux=[1.4635, {'chrome': 100, 'firefox': 0, 'edge': 0}],
        percentage_of_android=76.44, percentage_of_ios=23.56,
        has_mouse_percentage=69.12):
    user_id = 0
    # Laptop To Desktop Is In Ratio 2:1
    hardware = "Desktop"
    # Device type, pc or smartphone
    device_type = "is_pc"
    # CPU Cores
    hardware_concurrency = 8
    # RAM Memory In GB
    memory = 8
    has_mouse = False
    has_battery = False
    operating_system = "Android"
    has_touch = True
    browser = "Chrome"
    browser_version = 103
    screen_resolution = [1024, 720]
    gpu_vendor = "Qualcomm"
    gpu_renderer = "Mali"
    # mobile referrals: https://lm.facebook.com/ https://m.facebook.com/ https://lm.instagram.com/
    # https://m.instagram.com https://mobile.twitter.com/
    # desktop referrals: https://l.facebook.com https://www.facebook.com/ https://l.instagram.com/
    # https://www.intagram.com
    # general referrals: https://www.google.com/ https://t.co/ https://www.pinterest.com/ https://www.linkedin.com/
    # https://www.reddit.com/
    origins_referrals = ["https://www.google.com/", "https://l.instagram.com/", "facebook.com", "twitter.com"]
    continent = "Americas"
    country = "usa"
    timezone_offset = "8"
    vpn_client = "nordvpn"
    ovpn_file_name = None
    proxy_client = "proxyrack.com"
    proxy_geo = None
    canvas_spoof = ()
    audio_context_spoof = 0.0
    font_spoof = []
    webgl_spoof = []

    pc = fetch_percentage_value(no_of_persona_to_generate, percentage_of_pc)
    smartphone = fetch_percentage_value(no_of_persona_to_generate, percentage_of_smartphone)

    windows, mac, linux, android, ios = [], [], [], 0, 0
    memories = [[16, 47.08], [8, 26.81], [4, 10.35], [6, 4.24], [7, 3.46], [12, 2.39], [15, 1.94], [3, 1.28], [2, 0.71],
                [10, 0.33], [5, 0.22], [11, 0.17], [1, 0.17], [14, 0.8], [13, 0.03], [9, 0.02]]
    hardware_concurrencies = [[4, 38.79], [6, 31.61], [2, 13.53], [8, 13.39], [12, 0.92], [3, 0.63], [10, 0.61],
                              [16, 0.24], [18, 0.02], [1, 0.22], [5, 0.01], [14, 0.01], [24, 0.01], [32, 0.01],
                              ]
    # for memory in memories:
    #         memory[1] = fetch_percentage_value(pc, memory[1])
    #     for hardware_concurrency in hardware_concurrencies:
    #         hardware_concurrency[1] = fetch_percentage_value(pc, hardware_concurrency[1])

    windows.append(round(fetch_percentage_value(pc, percentage_of_windows[0])))
    windows.append({'chrome': round(fetch_percentage_value(windows[0], percentage_of_windows[1].get("chrome"))),
                    'firefox': round(fetch_percentage_value(windows[0], percentage_of_windows[1].get("firefox"))),
                    'edge': round(fetch_percentage_value(windows[0], percentage_of_windows[1].get("edge")))})

    mac.append(round(fetch_percentage_value(pc, percentage_of_mac[0])))
    mac.append({'chrome': round(fetch_percentage_value(mac[0], percentage_of_mac[1].get("chrome"))),
                'firefox': round(fetch_percentage_value(mac[0], percentage_of_mac[1].get("firefox"))),
                'edge': round(fetch_percentage_value(mac[0], percentage_of_mac[1].get("edge")))})

    linux.append(round(fetch_percentage_value(pc, percentage_of_linux[0])))
    linux.append({'chrome': round(fetch_percentage_value(linux[0], percentage_of_linux[1].get("chrome"))),
                  'firefox': round(fetch_percentage_value(linux[0], percentage_of_linux[1].get("firefox"))),
                  'edge': round(fetch_percentage_value(linux[0], percentage_of_linux[1].get("edge")))})

    android = round(fetch_percentage_value(smartphone, percentage_of_android))
    ios = round(fetch_percentage_value(smartphone, percentage_of_ios))

    to_use_devices = json.load(open("/home/kali/to-use-devices.txt", "r"))
    os_version_refractors = retrieve_list_data_from_file("/home/kali/os_info_refractors")
    chrome_version_refractors = json.load(open("/home/kali/chrome_user_agents_versio_refractors", "r"))
    firefox_version_refractors = json.load(open("/home/kali/firefox_ua_version_refractors", "r"))
    edge_version_refractors = json.load(open("/home/kali/edge_ua_version_refractors", "r"))
    pc_screen_resolutions = json.load(open("/home/kali/pc_screen_resolutions"))
    webgl_renderers = json.load(open("/home/kali/unmasked_webgl_renderers", "r"))
    mobile_referrers = ["https://lm.facebook.com/", "https://lm.instagram.com/"]
    desktop_referrers = ["https://l.facebook.com", "https://l.instagram.com/"]
    general_referrers = ["https://www.google.com/", "https://t.co/", "https://www.pinterest.com/",
                         "https://www.linkedin.com/", "https://www.reddit.com/"]
    ovpns_file_names = retrieve_list_data_from_file("/home/kali/vpn_file_names")

    # for i in range(len(pc_screen_resolutions)):
    #     pc_screen_resolutions[i][2] = round(fetch_percentage_value(pc, pc_screen_resolutions[i][2]))

    pc_personas = []
    botsdb = mysql.connector.connect(host="ec2-34-226-239-19.compute-1.amazonaws.com",
                                     user="root",
                                     password="suck my 1000 N&ughts",
                                     database="pr_bots_identities", connect_timeout=10000)

    sql = "INSERT INTO us_based_identities(\
          DEVICE_TYPE, HARDWARE, UA_OS, PLATFORM, CANVAS_FP_OFFSET, AUDIO_CONTEXT_FP_OFFSET, FONT_FP_OFFSET,\
          WEBGL_FP_OFFSET, HARDWARE_CONCURRENCY, MEMORY, HAS_MOUSE, HAS_BATTERY, HAS_TOUCH, BROWSER, BROWSER_VERSION,\
          SCREEN_RESOLUTION, GPU_VENDOR, GPU_RENDERER, PROXY_CLIENT, PROXY_GEO, REFERRALS, READING_SPEED, LANGUAGE,\
          MOUSE_DELTA_Y) VALUES (%s, \
          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    botsdb_cursor = botsdb.cursor()
    for i in range(round(pc)):
        pc_persona = []

        pc_persona.append(i)
        pc_persona.append("is_pc")

        # Laptop Or Desktop
        if random.random() > 0.42:
            hardware = "Laptop"
        else:
            hardware = "Desktop"

        # Has Mouse Or Not
        if hardware == "Desktop":
            has_mouse = "has_mouse"
        else:
            if random.random() < 0.20:
                has_mouse = "has_mouse"
            else:
                has_mouse = "no_mouse"

        # Has Battery Or Not
        if hardware == "Laptop":
            has_battery = "has_battery"
        else:
            if random.random() < 0.01:
                has_battery = "has_battery"
            else:
                has_battery = "no_battery"

        pc_persona.append(hardware)
        # Operating System
        if i <= windows[0]:
            rand = random.random()
            if rand <= 0.7:
                pc_persona.append(os_version_refractors[11])
            elif 0.7 < rand <= 0.95:
                pc_persona.append(os_version_refractors[7])
            else:
                pc_persona.append(os_version_refractors[random.randint(0, 11)])

            if i <= windows[1].get("chrome"):
                browser = "chrome"
                if random.random() < 0.7:
                    browser_version = chrome_version_refractors[random.randint(51, 69)]
                else:
                    browser_version = chrome_version_refractors[random.randint(0, 50)]
            elif i <= windows[1].get("chrome") + windows[1].get("firefox"):
                browser = "firefox"
                if random.random() < 0.7:
                    browser_version = firefox_version_refractors[random.randint(14, 19)]
                else:
                    browser_version = firefox_version_refractors[random.randint(0, 13)]
            elif i <= windows[1].get("chrome") + windows[1].get("firefox") + windows[1].get("edge"):
                browser = "edge"
                browser_version = edge_version_refractors[random.randint(0, len(edge_version_refractors) - 1)]

        elif i <= windows[0] + mac[0]:
            rand = random.random()
            if rand < 0.35:
                pc_persona.append(os_version_refractors[26])
            elif 0.35 < rand < 0.7:
                pc_persona.append(os_version_refractors[25])
            else:
                pc_persona.append(os_version_refractors[random.randint(18, 24)])

            if i <= windows[0] + mac[1].get("chrome"):
                browser = "chrome"
                if random.random() < 0.7:
                    browser_version = chrome_version_refractors[random.randint(51, 69)]
                else:
                    browser_version = chrome_version_refractors[random.randint(0, 50)]
            elif i <= windows[0] + mac[1].get("chrome") + mac[1].get("firefox"):
                browser = "firefox"
                if random.random() < 0.7:
                    browser_version = firefox_version_refractors[random.randint(14, 19)]
                else:
                    browser_version = firefox_version_refractors[random.randint(0, 13)]
            elif i <= windows[0] + mac[1].get("chrome") + mac[1].get("firefox") + mac[1].get("edge"):
                browser = "edge"
                browser_version = edge_version_refractors[random.randint(0, len(edge_version_refractors) - 1)]

        elif i <= windows[0] + mac[0] + linux[0]:
            if random.random() < 0.85:
                pc_persona.append(os_version_refractors[13])
            else:
                pc_persona.append(os_version_refractors[random.randint(12, 17)])

            if i <= windows[0] + mac[0] + linux[1].get("chrome"):
                browser = "chrome"
                if random.random() < 0.7:
                    browser_version = chrome_version_refractors[random.randint(51, 69)]
                else:
                    browser_version = chrome_version_refractors[random.randint(0, 50)]
            elif i <= windows[0] + mac[0] + linux[1].get("chrome") + linux[1].get("firefox"):
                browser = "firefox"
                if random.random() < 0.7:
                    browser_version = firefox_version_refractors[random.randint(14, 19)]
                else:
                    browser_version = firefox_version_refractors[random.randint(0, 13)]
            elif i <= windows[0] + mac[0] + linux[1].get("chrome") + linux[1].get("firefox") + linux[1].get("edge"):
                browser = "edge"
                browser_version = edge_version_refractors[random.randint(0, len(edge_version_refractors) - 1)]

        # PC Screen Resolutions
        probability_of_screen = random.uniform(0, 100)
        preceding_prob_sum = 0
        for j in range(len(pc_screen_resolutions)):
            preceding_prob_sum += pc_screen_resolutions[j][2]
            if probability_of_screen <= preceding_prob_sum:
                screen_resolution = [pc_screen_resolutions[j][0], pc_screen_resolutions[j][1],
                                     pc_screen_resolutions[j][0], pc_screen_resolutions[j][1], 1]
                break

        # Webgl Renderer And Vendor
        while True:
            gpu_renderer = webgl_renderers[random.randint(0, len(webgl_renderers) - 1)]
            if gpu_renderer[1] == "desktop":
                if "ANGLE (AMD" in gpu_renderer[0]:
                    gpu_vendor = "AMD"
                    gpu_renderer = gpu_renderer[0]
                    break
                elif "ANGLE (Radeon" in gpu_renderer[0]:
                    gpu_vendor = "AMD"
                    gpu_renderer = gpu_renderer[0]
                    break
                elif "ANGLE (ATI" in gpu_renderer[0]:
                    gpu_vendor = "ATI"
                    gpu_renderer = gpu_renderer[0]
                    break
                elif "ANGLE (Intel" in gpu_renderer[0]:
                    gpu_vendor = "Intel"
                    gpu_renderer = gpu_renderer[0]
                    break
                elif "ANGLE (NVIDIA" in gpu_renderer[0]:
                    gpu_vendor = "NVIDIA"
                    gpu_renderer = gpu_renderer[0]
                    break

        # Referrals
        origins_referrals = []
        no_of_referrers = random.randint(1, round((len(desktop_referrers) + len(general_referrers)) / 2))
        for j in range(no_of_referrers):
            referrer_index = random.randint(0, len(desktop_referrers) + len(general_referrers) - 1)
            if referrer_index <= 1:
                referrer = desktop_referrers[referrer_index]
            else:
                referrer = general_referrers[referrer_index - 2]
            if referrer in origins_referrals:
                continue
            origins_referrals.append(referrer)
        if False:
            # VPN
            ovpn_index = i
            if (i + 1) % len(ovpns_file_names) == 0:
                ovpns_file_names.extend(ovpns_file_names)
            ovpn_file_name = ovpns_file_names[ovpn_index]
            if "nordvpn" in ovpn_file_name:
                vpn_client = "nordvpn"
            elif "ipvanish" in ovpn_file_name:
                vpn_client = "ipvanish"
            else:
                vpn_client = "no_attrib"
        else:
            country = get_country()
            proxy_geo = f"country-{country}-city-{random.choice(proxy_rack_country_cities_list[country])}"
        # Hardware Concurrency And Memory
        probability_of_hc = random.uniform(0, 100)
        preceding_prob_sum = 0
        for hc in hardware_concurrencies:
            preceding_prob_sum += hc[1]
            if probability_of_hc <= preceding_prob_sum:
                hardware_concurrency = hc[0]
                break

        probability_of_mem = random.uniform(0, 100)
        preceding_prob_sum = 0
        for mem in memories:
            preceding_prob_sum += mem[1]
            if probability_of_mem <= preceding_prob_sum:
                memory = mem[0]
                break

        # Navigator Platform
        if "Windows" in pc_persona[3]:
            pc_persona.append("Win32")
        elif "Mac OS" in pc_persona[3]:
            pc_persona.append("MacIntel")
        elif "Linux x86_64" in pc_persona[3]:
            pc_persona.append("Linux x86_64")
        elif "Linux i686" in pc_persona[3]:
            pc_persona.append("Linux i686")
        else:
            pc_persona.append("void")

        # Canvas Spoof
        canvas_spoof = [random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 2), random.randint(-1, 2)]
        # Audio Context Spoof
        audio_context_spoof = random.randint(1, 9) / 10
        # Font Spoof
        font_spoof = [random.randint(-1, 2), random.randint(-1, 2)]
        # Webgl Spoof
        webgl_spoof = [random.random(), random.random()]
        # Reading Speed
        reading_speed = random.randint(730, 1130)
        # Mouse Delta Y
        mouse_delta_y = 50
        if random.random() < 0.5:
            mouse_delta_y = random.randint(12, 110)

        pc_persona.append(canvas_spoof)
        pc_persona.append(audio_context_spoof)
        pc_persona.append(font_spoof)
        pc_persona.append(webgl_spoof)
        pc_persona.append(hardware_concurrency)
        pc_persona.append(memory)
        pc_persona.append(has_mouse)
        pc_persona.append(has_battery)
        pc_persona.append("no_touch")
        pc_persona.append(browser)
        pc_persona.append(browser_version)
        pc_persona.append(screen_resolution)
        pc_persona.append(gpu_vendor)
        pc_persona.append(gpu_renderer)
        pc_persona.append(proxy_client)
        pc_persona.append(proxy_geo)
        pc_persona.append(origins_referrals)
        pc_persona.append(reading_speed)
        pc_persona.append(generate_persona_language(country))
        pc_persona.append(mouse_delta_y)
        print(pc_persona)
        db_entry_val = (str(pc_persona[1]), str(pc_persona[2]), str(pc_persona[3]),
                        str(pc_persona[4]), str(pc_persona[5]), float(pc_persona[6]), str(pc_persona[7]),
                        str(pc_persona[8]), int(pc_persona[9]), int(pc_persona[10]), str(pc_persona[11]),
                        str(pc_persona[12]), str(pc_persona[13]), str(pc_persona[14]), str(pc_persona[15]),
                        str(pc_persona[16]), str(pc_persona[17]), str(pc_persona[18]), str(pc_persona[19]),
                        str(pc_persona[20]), str(pc_persona[21]), str(pc_persona[22]), json.dumps(str(pc_persona[23])),
                        str(pc_persona[24]))
        botsdb_cursor.execute(sql, db_entry_val)
        pc_end = i + 1

    for i in range(round(smartphone)):
        i += pc_end
        sp_persona = []

        sp_persona.append(i)
        sp_persona.append("is_smartphone")

        # Laptop Or Desktop
        hardware = "smartphone"
        # Has Mouse Or Not
        has_mouse = "no_mouse"

        # Has Battery Or Not
        has_battery = "has_battery"

        rand = random.random()
        if rand <= 0.4:
            hardware_index = random.randint(21, 44)
        elif 0.4 < rand <= 0.55:
            hardware_index = random.randint(0, 20)
        else:
            hardware_index = random.randint(45, len(to_use_devices) - 1)
        hardware = to_use_devices[hardware_index][0]

        sp_persona.append(hardware)
        # Operating System
        if to_use_devices[hardware_index][2] == "Android":
            operating_system = "Linux; Android "
            if isinstance(to_use_devices[hardware_index][3], list):
                if random.random() <= 0.8:
                    operating_system += str(
                        to_use_devices[hardware_index][3][len(to_use_devices[hardware_index][3]) - 1])
                else:
                    operating_system += str(to_use_devices[hardware_index][3][
                                                random.randint(0, len(to_use_devices[hardware_index][3]) - 1)])
            else:
                operating_system += str(to_use_devices[hardware_index][3])
            operating_system += "; "
            if isinstance(to_use_devices[hardware_index][1], list):
                operating_system += to_use_devices[hardware_index][1][
                    random.randint(0, len(to_use_devices[hardware_index][1]) - 1)]
            else:
                operating_system += hardware
        elif to_use_devices[hardware_index][2] == "iOS":
            operating_system = "iPhone; CPU iPhone OS "
            if isinstance(to_use_devices[hardware_index][3], list):
                if random.random() <= 0.7:
                    os_version = str(to_use_devices[hardware_index][3][len(to_use_devices[hardware_index][3]) - 1])
                else:
                    os_version = str(to_use_devices[hardware_index][3][
                                         random.randint(0, len(to_use_devices[hardware_index][3]) - 1)])

            else:
                os_version = str(to_use_devices[hardware_index][3])
            os_version = os_version.replace(".", "_")
            operating_system += os_version + " like Mac OS X"

        sp_persona.append(operating_system)
        browser = "chrome"
        if random.random() < 0.7:
            browser_version = chrome_version_refractors[random.randint(51, 69)]
        else:
            browser_version = chrome_version_refractors[random.randint(0, 50)]
        # Screen Resolutions
        screen_resolution = [to_use_devices[hardware_index][5], to_use_devices[hardware_index][6],
                             to_use_devices[hardware_index][7], to_use_devices[hardware_index][8],
                             to_use_devices[hardware_index][9]]
        # Webgl Renderer And Vendor
        if isinstance(to_use_devices[hardware_index][12], list):
            sp_gpu_index = random.randint(0, len(to_use_devices[hardware_index][12]) - 1)
            gpu_vendor = to_use_devices[hardware_index][12][sp_gpu_index]
            gpu_renderer = to_use_devices[hardware_index][13][sp_gpu_index]
        else:
            gpu_vendor = to_use_devices[hardware_index][12]
            gpu_renderer = to_use_devices[hardware_index][13]
        # Referrals
        origins_referrals = []
        no_of_referrers = random.randint(1, round((len(desktop_referrers) + len(general_referrers)) / 2))
        for j in range(no_of_referrers):
            referrer_index = random.randint(0, len(desktop_referrers) + len(general_referrers) - 1)
            if referrer_index <= 1:
                referrer = desktop_referrers[referrer_index]
            else:
                referrer = general_referrers[referrer_index - 2]
            if referrer in origins_referrals:
                continue
            origins_referrals.append(referrer)

        # VPN
        if False:
            ovpn_index = i
            if (i + 1) % len(ovpns_file_names) == 0:
                ovpns_file_names.extend(ovpns_file_names)
            ovpn_file_name = ovpns_file_names[ovpn_index]
            if "nordvpn" in ovpn_file_name:
                vpn_client = "nordvpn"
            elif "ipvanish" in ovpn_file_name:
                vpn_client = "ipvanish"
            else:
                vpn_client = "void"
        else:
            country = get_country()
            proxy_geo = f"country-{country}-city-{random.choice(proxy_rack_country_cities_list[country])}"
        # Hardware Concurrency And Memory
        hardware_concurrency = to_use_devices[hardware_index][10]
        if isinstance(to_use_devices[hardware_index][11], list):
            memory = to_use_devices[hardware_index][11][random.randint(0, len(to_use_devices[hardware_index][11]) - 1)]
        else:
            memory = to_use_devices[hardware_index][11]
        # Navigator Platform
        if isinstance(to_use_devices[hardware_index][4], list):
            sp_persona.append(random.randint(0, len(to_use_devices[hardware_index][4]) - 1))
        elif to_use_devices[hardware_index][4]:
            sp_persona.append(to_use_devices[hardware_index][4])
        else:
            sp_persona.append("void")

        # Canvas Spoof
        canvas_spoof = [random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 2), random.randint(-1, 2)]
        # Audio Context Spoof
        audio_context_spoof = random.randint(1, 9) / 10
        # Font Spoof
        font_spoof = [random.randint(-1, 2), random.randint(-1, 2)]
        # Webgl Spoof
        webgl_spoof = [random.random(), random.random()]
        # Reading Speed
        reading_speed = random.randint(580, 930)
        # Mouse Delta Y
        mouse_delta_y = 50

        sp_persona.append(canvas_spoof)
        sp_persona.append(audio_context_spoof)
        sp_persona.append(font_spoof)
        sp_persona.append(webgl_spoof)
        sp_persona.append(hardware_concurrency)
        sp_persona.append(memory)
        sp_persona.append(has_mouse)
        sp_persona.append(has_battery)
        sp_persona.append("has_touch")
        sp_persona.append(browser)
        sp_persona.append(browser_version)
        sp_persona.append(screen_resolution)
        sp_persona.append(gpu_vendor)
        sp_persona.append(gpu_renderer)
        sp_persona.append(proxy_client)
        sp_persona.append(proxy_geo)
        sp_persona.append(origins_referrals)
        sp_persona.append(reading_speed)
        sp_persona.append(generate_persona_language(country))
        sp_persona.append(mouse_delta_y)
        print(sp_persona)
        db_entry_val = (str(sp_persona[1]), str(sp_persona[2]), str(sp_persona[3]),
                        str(sp_persona[4]), str(sp_persona[5]), float(sp_persona[6]), str(sp_persona[7]),
                        str(sp_persona[8]), int(sp_persona[9]), int(sp_persona[10]), str(sp_persona[11]),
                        str(sp_persona[12]), str(sp_persona[13]), str(sp_persona[14]), str(sp_persona[15]),
                        str(sp_persona[16]), str(sp_persona[17]), str(sp_persona[18]), str(sp_persona[19]),
                        str(sp_persona[20]), str(sp_persona[21]), str(sp_persona[22]), json.dumps(str(sp_persona[23])),
                        str(sp_persona[24]))
        botsdb_cursor.execute(sql, db_entry_val)
    botsdb.commit()


generate_persona()
