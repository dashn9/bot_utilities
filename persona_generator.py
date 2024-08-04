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
webgl_renderers = load_json_file("./docs/devices/unmasked_webgl_renderers.json")

memories = load_json_file("./docs/devices/memories.json")


english_speaking_countries = {"US", "CA", "GB", "AU", "IE", "NZ"}
country_distribution = load_json_file("./config/identities_country_distribution.json")
other_countries = list(proxy_cities.keys() - country_distribution.keys())
hardware_concurrencies = load_json_file("./docs/devices/hardware_concurrencies.json")

smartphone_devices = load_json_file("./docs/devices/devices.json")
os_versions = load_json_file("./docs/devices/os.json")
chrome_versions = json.load(open("./docs/chrome_versions.txt", "r"))
firefox_versions = json.load(open("./docs/firefox_versions.txt", "r"))
edge_versions = json.load(open("./docs/edge_versions.txt", "r"))
pc_screen_resolutions = json.load(open("./docs/devices/pc_screen_resolutions.json"))
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
    while True:
        gpu_renderer = random.choice(webgl_renderers)
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
    elif browser == "safari":
        browser = "safari"
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
    percentage_of_windows=[57, {"chrome": 100, "safari": 0, "edge": 0}],
    percentage_of_mac=[43, {"chrome": 100, "safari": 0, "edge": 0}],
    percentage_of_linux=[0, {"chrome": 100, "safari": 0, "edge": 0}],
    percentage_of_android=56.44,
    percentage_of_ios=43.56,
    persona_callback=default_persona_callback,
):

    def get_browser_with_prob(chrome_prob, safari_prob, edge_prob):
        browser_pick_prob = random.uniform(0, 100)
        if browser_pick_prob <= chrome_prob:
            browser = get_browser("chrome")
        elif browser_pick_prob <= chrome_prob + safari_prob:
            browser = get_browser("safari")
        elif browser_pick_prob <= chrome_prob + safari_prob + edge_prob:
            browser = get_browser("edge")
        return browser

    def genenerate_pc_persona(id):
        pc_persona = {}

        pc_persona["ID"] = id
        pc_persona["DEVICE_TYPE"] = "computer"

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
        pc_persona["DEVICE_MODEL"] = None

        pc_os_pick_prob = random.uniform(0, 100)
        if pc_os_pick_prob <= percentage_of_windows[0]:
            os = "Windows"
            rand = random.random()
            if rand <= 0.7:
                os_version = os_versions["windows"][-11]
            elif 0.7 < rand <= 0.95:
                os_version = os_versions["windows"][7]
            else:
                os_version = random.choice(os_versions["windows"])

            browser, browser_version = get_browser_with_prob(
                percentage_of_windows[1]["chrome"],
                percentage_of_windows[1]["safari"],
                percentage_of_windows[1]["edge"],
            )

        elif pc_os_pick_prob <= percentage_of_windows[0] + percentage_of_mac[0]:
            os = "Mac"
            rand = random.random()
            if rand < 0.35:
                os_version = os_versions["macintosh"][-1]
            elif 0.35 < rand < 0.7:
                os_version = os_versions["macintosh"][-2]
            else:
                os_version = os_versions["macintosh"][
                    random.randint(0, len(os_versions["macintosh"]) - 3)
                ]

            browser, browser_version = get_browser_with_prob(
                percentage_of_mac[1]["chrome"],
                percentage_of_mac[1]["safari"],
                percentage_of_mac[1]["edge"],
            )

        elif (
            pc_os_pick_prob
            <= percentage_of_windows[0] + percentage_of_mac[0] + percentage_of_linux[0]
        ):
            os = "Linux"
            if random.random() < 0.85:
                os_version = os_versions["linux"][1]
            else:
                os_version = random.choice(os_versions["linux"])

            browser, browser_version = get_browser_with_prob(
                percentage_of_linux[1]["chrome"],
                percentage_of_linux[1]["safari"],
                percentage_of_linux[1]["edge"],
            )

        pc_persona["OS"] = os
        pc_persona["OS_VERSION"] = os_version
        pc_persona["BROWSER"] = browser
        pc_persona["BROWSER_VERSION"] = browser_version

        # PC Screen Resolutions
        probability_of_screen = random.uniform(0, 100)
        preceding_prob_sum = 0
        for j in range(len(pc_screen_resolutions)):
            preceding_prob_sum += pc_screen_resolutions[j][2]
            if probability_of_screen <= preceding_prob_sum:
                pc_persona["SCREEN_RESOLUTION"] = {
                    "logical_width": pc_screen_resolutions[j][0],
                    "logical_height": pc_screen_resolutions[j][1],
                    "original_width": pc_screen_resolutions[j][0],
                    "original_height": pc_screen_resolutions[j][1],
                    "density_pixel_ratio": 1,
                }
                break

        gpu = get_gpu()
        pc_persona["GPU"] = {"vendor": gpu[0], "webgl_renderer": gpu[1]}

        country = get_country()
        city = random.choice(proxy_cities[country])
        pc_persona["COUNTRY"] = country
        pc_persona["CITY"] = city[1]
        proxy_geo = f"country-{country.lower()}-city-{city[0]}"

        pc_persona["PROXY_CLIENT"] = proxy_client
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
        if "Windows" in os_version:
            platform = "Win32"
        elif "Mac OS" in os_version:
            platform = "MacIntel"
        elif "Linux x86_64" in os_version:
            platform = "Linux x86_64"
        elif "Linux i686" in os_version:
            platform = "Linux i686"
        else:
            platform = "void"

        pc_persona["PLATFORM"] = platform

        pc_persona["FINGERPRINT"] = {
            "canvas_offset": [
                random.randint(-1, 1),
                random.randint(-1, 1),
                random.randint(-1, 2),
                random.randint(-1, 2),
            ],
            "audio_context_offset": random.randint(1, 9) / 10,
            "font_offset": [random.randint(-1, 2), random.randint(-1, 2)],
            "webgl_offset": [random.random(), random.random()],
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

    def generate_sp_persona(id):

        sp_persona = {}

        sp_persona["ID"] = id
        sp_persona["DEVICE_TYPE"] = "smartphone"
        sp_persona["HAS_MOUSE"] = False

        sp_persona["HAS_BATTERY"] = True

        # There is a better way to write the code below such that you can filter out any specific device
        # based of set probabilities
        rand = random.random()
        if rand <= 0.4:
            hardware = random.choice(
                list(
                    filter(
                        lambda devices: devices["name"].startswith("Samsung"),
                        smartphone_devices,
                    )
                )
            )
        elif 0.4 < rand <= 0.55:
            hardware = random.choice(
                list(
                    filter(
                        lambda devices: devices["name"].startswith("iPhone"),
                        smartphone_devices,
                    )
                )
            )
        else:
            hardware = random.choice(
                list(
                    filter(
                        lambda devices: devices["os"] == "Android"
                        and not devices["name"].startswith("Samsung"),
                        smartphone_devices,
                    )
                )
            )

        sp_persona["HARDWARE"] = hardware["name"]
        # Operating System
        if hardware["os"] == "Android":
            if random.random() <= 0.8:
                os_version = hardware["os_versions"][-1]
            else:
                os_version = random.choice(hardware["os_versions"])

        elif hardware["os"] == "iOS":
            if random.random() <= 0.7:
                os_version = hardware["os_versions"][-1]
            else:
                os_version = random.choice(hardware["os_versions"])
        if hardware["models"]:
            device_model = random.choice(hardware["models"])
        else:
            device_model = hardware["name"]
        sp_persona["OS"] = hardware["os"]
        sp_persona["OS_VERSION"] = os_version
        sp_persona["DEVICE_MODEL"] = device_model

        browser = "chrome"
        if random.random() < 0.7:
            browser_version = chrome_versions[random.randint(51, 69)]
        else:
            browser_version = chrome_versions[random.randint(0, 50)]

        sp_persona["BROWSER"] = browser
        sp_persona["BROWSER_VERSION"] = browser_version
        # Screen Resolutions
        sp_persona["SCREEN_RESOLUTION"] = {
            "logical_width": hardware["logical_width"],
            "logical_height": hardware["logical_height"],
            "original_width": hardware["original_width"],
            "original_height": hardware["original_height"],
            "density_pixel_ratio": hardware["density_pixel_ratio"],
        }
        sp_persona["GPU"] = random.choice(hardware["gpu"])

        country = get_country()
        city = random.choice(proxy_cities[country])
        sp_persona["COUNTRY"] = country
        sp_persona["CITY"] = city[1]
        proxy_geo = f"country-{country.lower()}-city-{city[0]}"

        sp_persona["HAS_TOUCH"] = True
        sp_persona["LANGUAGE"] = generate_persona_language(country)
        sp_persona["REFERRALS"] = generate_referrals()

        sp_persona["PROXY_CLIENT"] = proxy_client
        sp_persona["PROXY_GEO"] = proxy_geo
        # Hardware Concurrency And Memory
        sp_persona["HARDWARE_CONCURRENCY"] = random.choice(
            hardware["hardware_concurrency"]
        )
        sp_persona["MEMORY"] = random.choice(hardware["memory"])

        sp_persona["PLATFORM"] = random.choice(hardware["platforms"])

        sp_persona["FINGERPRINT"] = {
            "canvas_offset": [
                random.randint(-1, 1),
                random.randint(-1, 1),
                random.randint(-1, 2),
                random.randint(-1, 2),
            ],
            "audio_context_offset": random.randint(1, 9) / 10,
            "font_offset": [random.randint(-1, 2), random.randint(-1, 2)],
            "webgl_offset": [random.random(), random.random()],
        }
        sp_persona["READING_SPEED"] = random.randint(580, 930)

        sp_persona["MOUSE_DELTA_Y"] = 50

        persona_callback(sp_persona)

    for i in range(no_of_persona_to_generate):
        if random.uniform(0, 100) <= percentage_of_smartphone:
            generate_sp_persona(i + 1)
        else:
            genenerate_pc_persona(i + 1)


from pymongo import MongoClient

# mongodb doesn't allow transactions unless you use a replicaset
mongo_client = MongoClient(
    "localhost", 27017, username="localhost", password="localhost"
)
identity_collection = mongo_client.bots.identities


def insert_persona_to_db(persona):
    persona["COOKIES"] = []
    persona["TIMEZONE"] = {}
    identity_collection.insert_one(persona)


generate_persona(persona_callback=insert_persona_to_db)
