import json
import random


def load_json_file(filename) -> dict:
    """
    Load the contents of a JSON file into a dictionary.

    :param filename: The name of the JSON file to load
    :return: A dictionary with the contents of the JSON file
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


proxy_client = "gate.smartproxy.com"
proxy_cities = load_json_file("./docs/proxy_cities/smartproxy.json")
webgl_renderers = load_json_file("./docs/devices/devices.json")

memories = load_json_file("./docs/devices/memories.json")


english_speaking_countries = {"US", "CA", "GB", "AU", "IE", "NZ"}
country_distribution = load_json_file("./config/identities_country_distribution.json")
other_countries = list(proxy_cities.keys() - country_distribution.keys())

to_use_devices = json.load(open("./docs/to_use_devices.txt", "r"))
os_versions = load_json_file("./docs/devices/os.json")
chrome_versions = json.load(open("./docs/chrome_versions.txt", "r"))
firefox_versions = json.load(open("./docs/firefox_versions.txt", "r"))
edge_versions = json.load(open("./docs/edge_versions.txt", "r"))
pc_screen_resolutions = json.load(open("./docs/pc_screen_resolutions.txt"))
mobile_referrers = ["https://lm.facebook.com/", "https://lm.instagram.com/"]
desktop_referrers = ["https://l.facebook.com", "https://l.instagram.com/"]
general_referrers = [
    "https://www.google.com/",
    "https://t.co/",
    "https://www.pinterest.com/",
    "https://www.linkedin.com/",
    "https://www.reddit.com/",
]


def get_country():

    prob = random.random()

    cumm_prob = 0
    for key, value in country_distribution.items():
        cumm_prob += value
        if prob <= cumm_prob:
            return key
    return random.choice(other_countries)


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
    en_languages = load_json_file("./docs/browsers/languages.json")
    default = ["en-US", "en"]
    default_2 = ["en-GB", "en"]
    if country_code == "US":
        return en_languages.get(country_code, default)
    elif country_code == "CA":
        if random.random() < 0.69:
            return en_languages.get(country_code, default)
        else:
            return default
    elif country_code == "GB":
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


def default_persona_callback(persona):
    print(persona)


def get_gpu():
    gpu_renderer = random.choice(webgl_renderers)
    while True:
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
    return (gpu_vendor, gpu_renderer)


def get_browser(browser):
    if browser == "chrome":
        browser = "chrome"
        if random.random() < 0.7:
            browser_version = chrome_versions[random.randint(51, 69)]
        else:
            browser_version = chrome_versions[random.randint(0, 50)]
    elif browser == "firefox":
        browser = "firefox"
        if random.random() < 0.7:
            browser_version = firefox_versions[random.randint(14, 19)]
        else:
            browser_version = firefox_versions[random.randint(0, 13)]
    elif browser == "edge":
        browser = "edge"
        browser_version = edge_versions[random.randint(0, len(edge_versions) - 1)]
        return (browser, browser_version)


def generate_referrals():
    # Referrals
    origins_referrals = []
    no_of_referrers = random.randint(
        1, round((len(desktop_referrers) + len(general_referrers)) / 2)
    )
    for j in range(no_of_referrers):
        referrer_index = random.randint(
            0, len(desktop_referrers) + len(general_referrers) - 1
        )
        if referrer_index <= 1:
            referrer = desktop_referrers[referrer_index]
        else:
            referrer = general_referrers[referrer_index - 2]
        if referrer in origins_referrals:
            continue
        origins_referrals.append(referrer)
    return origins_referrals


def generate_persona(
    no_of_persona_to_generate=100,
    percentage_of_smartphone=57.34,
    percentage_of_pc=42.66,
    percentage_of_windows=[56.5346, {"chrome": 100, "firefox": 0, "edge": 0}],
    percentage_of_mac=[42.0019, {"chrome": 100, "firefox": 0, "edge": 0}],
    percentage_of_linux=[1.4635, {"chrome": 100, "firefox": 0, "edge": 0}],
    percentage_of_android=56.44,
    percentage_of_ios=43.56,
    persona_callback=default_persona_callback,
):
    id = 0
    # Laptop To Desktop Is In Ratio 2:1
    hardware = "Desktop"
    # CPU Cores
    hardware_concurrency = 8
    # RAM Memory In GB
    memory = 8
    has_mouse = False
    has_battery = False
    operating_system = "Android"
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
    origins_referrals = [
        "https://www.google.com/",
        "https://l.instagram.com/",
        "facebook.com",
        "twitter.com",
    ]
    country = "usa"
    proxy_client = "gate.smartproxy.com"
    proxy_geo = None
    canvas_spoof = ()
    audio_context_spoof = 0.0
    font_spoof = []
    webgl_spoof = []

    hardware_concurrencies = load_json_file(
        "./docs/devices/hardware_concurrencies.json"
    )
    # for memory in memories:
    #         memory[1] = fetch_percentage_value(pc, memory[1])
    #     for hardware_concurrency in hardware_concurrencies:
    #         hardware_concurrency[1] = fetch_percentage_value(pc, hardware_concurrency[1])

    # ovpns_file_names = retrieve_list_data_from_file("/home/kali/vpn_file_names")

    # for i in range(len(pc_screen_resolutions)):
    #     pc_screen_resolutions[i][2] = round(fetch_percentage_value(pc, pc_screen_resolutions[i][2]))

    pc_personas = []
    # botsdb = mysql.connector.connect(
    #     host="ec2-34-226-239-19.compute-1.amazonaws.com",
    #     user="root",
    #     password="suck my 1000 N&ughts",
    #     database="pr_bots_identities",
    #     connect_timeout=10000,
    # )

    # sql = "INSERT INTO us_based_identities(\
    #       DEVICE_TYPE, HARDWARE, UA_OS, PLATFORM, CANVAS_FP_OFFSET, AUDIO_CONTEXT_FP_OFFSET, FONT_FP_OFFSET,\
    #       WEBGL_FP_OFFSET, HARDWARE_CONCURRENCY, MEMORY, HAS_MOUSE, HAS_BATTERY, HAS_TOUCH, BROWSER, BROWSER_VERSION,\
    #       SCREEN_RESOLUTION, GPU_VENDOR, GPU_RENDERER, PROXY_CLIENT, PROXY_GEO, REFERRALS, READING_SPEED, LANGUAGE,\
    #       MOUSE_DELTA_Y) VALUES (%s, \
    #       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # botsdb_cursor = botsdb.cursor()

    def get_browser_with_prob(chrome_prob, firefox_prob, edge_prob):
        browser_pick_prob = random.uniform(0, 100)
        if browser_pick_prob <= chrome_prob:
            browser = get_browser("chrome")
        elif browser_pick_prob <= chrome_prob + firefox_prob:
            browser = get_browser("firefox")
        elif browser_pick_prob <= chrome_prob + firefox_prob + edge_prob:
            browser = get_browser("edge")
        return browser

    for i in range(round(pc)):
        pc_persona = {}

        pc_persona["ID"] = i
        pc_persona["DEVICE_TYPE"] = "is_pc"

        # Laptop Or Desktop
        if random.random() > 0.42:
            hardware = "Laptop"
        else:
            hardware = "Desktop"

        # Has Mouse Or Not
        if hardware == "Desktop":
            has_mouse = True
        else:
            if random.random() < 0.20:
                has_mouse = True
            else:
                has_mouse = False

        # Has Battery Or Not
        if hardware == "Laptop":
            has_battery = True
        else:
            if random.random() < 0.01:
                has_battery = True
            else:
                has_battery = False

        pc_persona["HARDWARE"] = hardware
        pc_persona["HAS_BATTERY"] = has_battery
        pc_persona["HAS_MOUSE"] = has_mouse

        pc_os_pick_prob = random.uniform(0, 100)
        if pc_os_pick_prob <= percentage_of_windows[0]:
            rand = random.random()
            if rand <= 0.7:
                os_version = os_versions["windows"][-11]
            elif 0.7 < rand <= 0.95:
                os_version = os_versions["windows"][7]
            else:
                os_version = random.choice(os_versions["windows"])

            browser, browser_version = get_browser_with_prob(
                percentage_of_windows[1]["chrome"],
                percentage_of_windows[1]["firefox"],
                percentage_of_windows[1]["edge"],
            )

        elif pc_os_pick_prob <= percentage_of_windows[0] + percentage_of_mac[0]:
            rand = random.random()
            if rand < 0.35:
                os_version = os_versions[26]
            elif 0.35 < rand < 0.7:
                os_version = os_versions[25]
            else:
                os_version = os_versions[random.randint(18, 24)]

            browser, browser_version = get_browser_with_prob(
                percentage_of_mac[1]["chrome"],
                percentage_of_mac[1]["firefox"],
                percentage_of_mac[1]["edge"],
            )

        elif (
            pc_os_pick_prob
            <= percentage_of_windows[0] + percentage_of_mac[0] + percentage_of_linux[0]
        ):
            if random.random() < 0.85:
                os_version = os_versions[13]
            else:
                os_version = os_versions[random.randint(12, 17)]

            browser, browser_version = get_browser_with_prob(
                percentage_of_linux[1]["chrome"],
                percentage_of_linux[1]["firefox"],
                percentage_of_linux[1]["edge"],
            )

        pc_persona["OS_VERSION"] = os_version
        pc_persona["BROWSER"] = browser
        pc_persona["BROWSER_VERSION"] = browser_version

        # PC Screen Resolutions
        probability_of_screen = random.uniform(0, 100)
        preceding_prob_sum = 0
        for j in range(len(pc_screen_resolutions)):
            preceding_prob_sum += pc_screen_resolutions[j][2]
            if probability_of_screen <= preceding_prob_sum:
                pc_persona["SCREEN_RESOLUTION"] = [
                    pc_screen_resolutions[j][0],
                    pc_screen_resolutions[j][1],
                    pc_screen_resolutions[j][0],
                    pc_screen_resolutions[j][1],
                    1,
                ]
                break

        pc_persona["GPU_VENDOR"], pc_persona["GPU_RENDERER"] = get_gpu()

        country = get_country()
        city = random.choice(proxy_cities[country])
        pc_persona["COUNTRY"] = country
        pc_persona["CITY"] = city
        proxy_geo = f"country-{country.lower()}-city-{city[0]}"

        pc_persona["PROXY_GEO"] = proxy_geo

        # Hardware Concurrency And Memory
        probability_of_hc = random.uniform(0, 100)
        preceding_prob_sum = 0
        for hc in hardware_concurrencies:
            preceding_prob_sum += hc[1]
            if probability_of_hc <= preceding_prob_sum:
                pc_persona["HARDWARE_CONCURRENCY"] = hc[0]
                break

        probability_of_mem = random.uniform(0, 100)
        preceding_prob_sum = 0
        for mem in memories:
            preceding_prob_sum += mem[1]
            if probability_of_mem <= preceding_prob_sum:
                pc_persona["MEMORY"] = mem[0]
                break

        # Navigator Platform
        if "Windows" in pc_persona[3]:
            platform = "Win32"
        elif "Mac OS" in pc_persona[3]:
            platform = "MacIntel"
        elif "Linux x86_64" in pc_persona[3]:
            platform = "Linux x86_64"
        elif "Linux i686" in pc_persona[3]:
            platform = "Linux i686"
        else:
            platform = "void"

        pc_persona["PLATFORM"] = platform

        pc_persona["FINGERPRINT"] = {
            "CANVAS_OFFSET": [
                random.randint(-1, 1),
                random.randint(-1, 1),
                random.randint(-1, 2),
                random.randint(-1, 2),
            ],
            "AUDIO_CONTEXT_OFFSET": random.randint(1, 9) / 10,
            "FONT_OFFSET": [random.randint(-1, 2), random.randint(-1, 2)],
            "WEBGL_OFFSET": [random.random(), random.random()],
        }
        pc_persona["READING_SPEED"] = random.randint(730, 1130)
        # Mouse Delta Y
        mouse_delta_y = 50
        if random.random() < 0.5:
            mouse_delta_y = random.randint(12, 110)

        pc_persona["MOUSE_DELTA_Y"] = mouse_delta_y
        pc_persona["HAS_TOUCH"] = False
        pc_persona["LANGUAGE"] = generate_persona_language(country)
        pc_persona["REFERRALS"] = generate_referrals()

        persona_callback(pc_persona)

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
                        to_use_devices[hardware_index][3][
                            len(to_use_devices[hardware_index][3]) - 1
                        ]
                    )
                else:
                    operating_system += str(
                        to_use_devices[hardware_index][3][
                            random.randint(
                                0, len(to_use_devices[hardware_index][3]) - 1
                            )
                        ]
                    )
            else:
                operating_system += str(to_use_devices[hardware_index][3])
            operating_system += "; "
            if isinstance(to_use_devices[hardware_index][1], list):
                operating_system += to_use_devices[hardware_index][1][
                    random.randint(0, len(to_use_devices[hardware_index][1]) - 1)
                ]
            else:
                operating_system += hardware
        elif to_use_devices[hardware_index][2] == "iOS":
            operating_system = "iPhone; CPU iPhone OS "
            if isinstance(to_use_devices[hardware_index][3], list):
                if random.random() <= 0.7:
                    os_version = str(
                        to_use_devices[hardware_index][3][
                            len(to_use_devices[hardware_index][3]) - 1
                        ]
                    )
                else:
                    os_version = str(
                        to_use_devices[hardware_index][3][
                            random.randint(
                                0, len(to_use_devices[hardware_index][3]) - 1
                            )
                        ]
                    )

            else:
                os_version = str(to_use_devices[hardware_index][3])
            os_version = os_version.replace(".", "_")
            operating_system += os_version + " like Mac OS X"

        sp_persona.append(operating_system)
        browser = "chrome"
        if random.random() < 0.7:
            browser_version = chrome_versions[random.randint(51, 69)]
        else:
            browser_version = chrome_versions[random.randint(0, 50)]
        # Screen Resolutions
        screen_resolution = [
            to_use_devices[hardware_index][5],
            to_use_devices[hardware_index][6],
            to_use_devices[hardware_index][7],
            to_use_devices[hardware_index][8],
            to_use_devices[hardware_index][9],
        ]
        # Webgl Renderer And Vendor
        if isinstance(to_use_devices[hardware_index][12], list):
            sp_gpu_index = random.randint(
                0, len(to_use_devices[hardware_index][12]) - 1
            )
            gpu_vendor = to_use_devices[hardware_index][12][sp_gpu_index]
            gpu_renderer = to_use_devices[hardware_index][13][sp_gpu_index]
        else:
            gpu_vendor = to_use_devices[hardware_index][12]
            gpu_renderer = to_use_devices[hardware_index][13]
        # Referrals
        origins_referrals = []
        no_of_referrers = random.randint(
            1, round((len(desktop_referrers) + len(general_referrers)) / 2)
        )
        for j in range(no_of_referrers):
            referrer_index = random.randint(
                0, len(desktop_referrers) + len(general_referrers) - 1
            )
            if referrer_index <= 1:
                referrer = desktop_referrers[referrer_index]
            else:
                referrer = general_referrers[referrer_index - 2]
            if referrer in origins_referrals:
                continue
            origins_referrals.append(referrer)

        country = get_country()
        proxy_geo = (
            f"country-{country.lower()}-city-{random.choice(proxy_cities[country])[0]}"
        )
        # Hardware Concurrency And Memory
        hardware_concurrency = to_use_devices[hardware_index][10]
        if isinstance(to_use_devices[hardware_index][11], list):
            memory = to_use_devices[hardware_index][11][
                random.randint(0, len(to_use_devices[hardware_index][11]) - 1)
            ]
        else:
            memory = to_use_devices[hardware_index][11]
        # Navigator Platform
        if isinstance(to_use_devices[hardware_index][4], list):
            sp_persona.append(
                random.randint(0, len(to_use_devices[hardware_index][4]) - 1)
            )
        elif to_use_devices[hardware_index][4]:
            sp_persona.append(to_use_devices[hardware_index][4])
        else:
            sp_persona.append("void")

        # Canvas Spoof
        canvas_spoof = [
            random.randint(-1, 1),
            random.randint(-1, 1),
            random.randint(-1, 2),
            random.randint(-1, 2),
        ]
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
        persona_callback(sp_persona)


from pymongo import MongoClient

# mongodb doesn't allow transactions unless you use a replicaset
mongo_client = MongoClient(
    "localhost", 27017, username="localhost", password="localhost"
)
identity_collection = mongo_client.bots.identities

curr_identity_id = 0


def add_new_identitiy(persona):
    global curr_identity_id
    print(persona)
    curr_identity_id += 1
    identity_collection.insert_one(
        {
            "ID": curr_identity_id,
            "DEVICE_TYPE": persona[1],
            "HARDWARE": persona[2],
            "UA_OS": persona[3],
            "PLATFORM": persona[4],
            "CANVAS_FP_OFFSET": persona[5],
            "AUDIO_CONTEXT_FP_OFFSET": persona[6],
            "FONT_FP_OFFSET": persona[7],
            "WEBGL_FP_OFFSET": persona[8],
            "HARDWARE_CONCURRENCY": persona[9],
            "MEMORY": persona[10],
            "HAS_MOUSE": persona[11],
            "HAS_BATTERY": persona[12],
            "HAS_TOUCH": persona[13],
            "BROWSER": persona[14],
            "BROWSER_VERSION": persona[15],
            "SREEN_RESOLUTION": persona[16],
            "GPU_VENDOR": persona[17],
            "GPU_RENDERER": persona[18],
            "PROXY_CLIENT": persona[19],
            "PROXY_GEO": persona[20],
            "REFERRALS": persona[21],
            "READING_SPEED": persona[22],
            "LANGUAGE": persona[23],
            "MOUSE_DELTA_Y": persona[24],
            "COOKIES": [],
        }
    )


generate_persona(persona_callback=add_new_identitiy)
