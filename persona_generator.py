import json
import random


# device name, ua model, device os, os version, device platform, logical width, logical height, original width, original height, device pixel ratio, hardware concurrency, memory, gpu vendor name, webgl renderer, [language, color depth]


def load_json_file(filename) -> dict:
    """
    Load the contents of a JSON file into a dictionary.

    :param filename: The name of the JSON file to load
    :return: A dictionary with the contents of the JSON file
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


english_speaking_countries = {"US", "CA", "GB", "AU", "IE", "NZ"}
proxy_cities = load_json_file("./docs/proxy_cities/smartproxy.json")
country_distribution = load_json_file("./config/identities_country_distribution.json")
other_countries = list(proxy_cities.keys() - country_distribution.keys())


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
    en_languages = {
        "01": ["en-001", "en"],
        "50": ["en-150", "en"],
        "AG": ["en-AG", "en"],
        "AI": ["en-AI", "en"],
        "AS": ["en-AS", "en"],
        "AT": ["en-AT", "en"],
        "AU": ["en-AU", "en"],
        "BB": ["en-BB", "en"],
        "BE": ["en-BE", "en"],
        "BI": ["en-BI", "en"],
        "BM": ["en-BM", "en"],
        "BS": ["en-BS", "en"],
        "BW": ["en-BW", "en"],
        "BZ": ["en-BZ", "en"],
        "CA": ["en-CA", "en"],
        "CC": ["en-CC", "en"],
        "CH": ["en-CH", "en"],
        "CK": ["en-CK", "en"],
        "CM": ["en-CM", "en"],
        "CX": ["en-CX", "en"],
        "CY": ["en-CY", "en"],
        "DE": ["en-DE", "en"],
        "DG": ["en-DG", "en"],
        "DK": ["en-DK", "en"],
        "DM": ["en-DM", "en"],
        "ER": ["en-ER", "en"],
        "FI": ["en-FI", "en"],
        "FJ": ["en-FJ", "en"],
        "FK": ["en-FK", "en"],
        "FM": ["en-FM", "en"],
        "GB": ["en-GB", "en"],
        "GD": ["en-GD", "en"],
        "GG": ["en-GG", "en"],
        "GH": ["en-GH", "en"],
        "GI": ["en-GI", "en"],
        "GM": ["en-GM", "en"],
        "GU": ["en-GU", "en"],
        "GY": ["en-GY", "en"],
        "HK": ["en-HK", "en"],
        "IE": ["en-IE", "en"],
        "IL": ["en-IL", "en"],
        "IM": ["en-IM", "en"],
        "IN": ["en-IN", "en"],
        "IO": ["en-IO", "en"],
        "JE": ["en-JE", "en"],
        "JM": ["en-JM", "en"],
        "KE": ["en-KE", "en"],
        "KI": ["en-KI", "en"],
        "KN": ["en-KN", "en"],
        "KY": ["en-KY", "en"],
        "LC": ["en-LC", "en"],
        "LR": ["en-LR", "en"],
        "LS": ["en-LS", "en"],
        "MG": ["en-MG", "en"],
        "MH": ["en-MH", "en"],
        "MO": ["en-MO", "en"],
        "MP": ["en-MP", "en"],
        "MS": ["en-MS", "en"],
        "MT": ["en-MT", "en"],
        "MU": ["en-MU", "en"],
        "NA": ["en-NA", "en"],
        "NF": ["en-NF", "en"],
        "NG": ["en-NG", "en"],
        "NL": ["en-NL", "en"],
        "NR": ["en-NR", "en"],
        "NU": ["en-NU", "en"],
        "NZ": ["en-NZ", "en"],
        "PG": ["en-PG", "en"],
        "PH": ["en-PH", "en"],
        "PK": ["en-PK", "en"],
        "PN": ["en-PN", "en"],
        "PR": ["en-PR", "en"],
        "PW": ["en-PW", "en"],
        "RW": ["en-RW", "en"],
        "SB": ["en-SB", "en"],
        "SC": ["en-SC", "en"],
        "SD": ["en-SD", "en"],
        "SE": ["en-SE", "en"],
        "SG": ["en-SG", "en"],
        "SH": ["en-SH", "en"],
        "SI": ["en-SI", "en"],
        "SL": ["en-SL", "en"],
        "SS": ["en-SS", "en"],
        "SX": ["en-SX", "en"],
        "SZ": ["en-SZ", "en"],
        "TC": ["en-TC", "en"],
        "TK": ["en-TK", "en"],
        "TO": ["en-TO", "en"],
        "TT": ["en-TT", "en"],
        "TV": ["en-TV", "en"],
        "TZ": ["en-TZ", "en"],
        "UG": ["en-UG", "en"],
        "UM": ["en-UM", "en"],
        "US": ["en-US", "en"],
        "VC": ["en-VC", "en"],
        "VG": ["en-VG", "en"],
        "VI": ["en-VI", "en"],
        "VU": ["en-VU", "en"],
        "WS": ["en-WS", "en"],
        "ZA": ["en-ZA", "en"],
        "ZM": ["en-ZM", "en"],
        "ZW": ["en-ZW", "en"],
    }
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
    return default


def default_persona_callback(persona):
    print(persona)


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
    origins_referrals = [
        "https://www.google.com/",
        "https://l.instagram.com/",
        "facebook.com",
        "twitter.com",
    ]
    continent = "Americas"
    country = "usa"
    timezone_offset = "8"
    vpn_client = "nordvpn"
    ovpn_file_name = None
    proxy_client = "gate.smartproxy.com"
    proxy_geo = None
    canvas_spoof = ()
    audio_context_spoof = 0.0
    font_spoof = []
    webgl_spoof = []

    pc = fetch_percentage_value(no_of_persona_to_generate, percentage_of_pc)
    smartphone = fetch_percentage_value(
        no_of_persona_to_generate, percentage_of_smartphone
    )

    windows, mac, linux, android, ios = [], [], [], 0, 0
    memories = [
        [16, 47.08],
        [8, 26.81],
        [4, 10.35],
        [6, 4.24],
        [7, 3.46],
        [12, 2.39],
        [15, 1.94],
        [3, 1.28],
        [2, 0.71],
        [10, 0.33],
        [5, 0.22],
        [11, 0.17],
        [1, 0.17],
        [14, 0.8],
        [13, 0.03],
        [9, 0.02],
    ]
    hardware_concurrencies = [
        [4, 38.79],
        [6, 31.61],
        [2, 13.53],
        [8, 13.39],
        [12, 0.92],
        [3, 0.63],
        [10, 0.61],
        [16, 0.24],
        [18, 0.02],
        [1, 0.22],
        [5, 0.01],
        [14, 0.01],
        [24, 0.01],
        [32, 0.01],
    ]
    # for memory in memories:
    #         memory[1] = fetch_percentage_value(pc, memory[1])
    #     for hardware_concurrency in hardware_concurrencies:
    #         hardware_concurrency[1] = fetch_percentage_value(pc, hardware_concurrency[1])

    windows.append(round(fetch_percentage_value(pc, percentage_of_windows[0])))
    windows.append(
        {
            "chrome": round(
                fetch_percentage_value(
                    windows[0], percentage_of_windows[1].get("chrome")
                )
            ),
            "firefox": round(
                fetch_percentage_value(
                    windows[0], percentage_of_windows[1].get("firefox")
                )
            ),
            "edge": round(
                fetch_percentage_value(windows[0], percentage_of_windows[1].get("edge"))
            ),
        }
    )

    mac.append(round(fetch_percentage_value(pc, percentage_of_mac[0])))
    mac.append(
        {
            "chrome": round(
                fetch_percentage_value(mac[0], percentage_of_mac[1].get("chrome"))
            ),
            "firefox": round(
                fetch_percentage_value(mac[0], percentage_of_mac[1].get("firefox"))
            ),
            "edge": round(
                fetch_percentage_value(mac[0], percentage_of_mac[1].get("edge"))
            ),
        }
    )

    linux.append(round(fetch_percentage_value(pc, percentage_of_linux[0])))
    linux.append(
        {
            "chrome": round(
                fetch_percentage_value(linux[0], percentage_of_linux[1].get("chrome"))
            ),
            "firefox": round(
                fetch_percentage_value(linux[0], percentage_of_linux[1].get("firefox"))
            ),
            "edge": round(
                fetch_percentage_value(linux[0], percentage_of_linux[1].get("edge"))
            ),
        }
    )

    android = round(fetch_percentage_value(smartphone, percentage_of_android))
    ios = round(fetch_percentage_value(smartphone, percentage_of_ios))

    to_use_devices = json.load(open("./docs/to_use_devices.txt", "r"))
    os_versions = retrieve_list_data_from_file("./docs/os_info_refractors.txt")
    chrome_versions = json.load(open("./docs/chrome_versions.txt", "r"))
    firefox_versions = json.load(open("./docs/firefox_versions.txt", "r"))
    edge_versions = json.load(open("./docs/edge_versions.txt", "r"))
    pc_screen_resolutions = json.load(open("./docs/pc_screen_resolutions.txt"))
    webgl_renderers = json.load(open("./docs/unmasked_webgl_renderers.txt", "r"))
    mobile_referrers = ["https://lm.facebook.com/", "https://lm.instagram.com/"]
    desktop_referrers = ["https://l.facebook.com", "https://l.instagram.com/"]
    general_referrers = [
        "https://www.google.com/",
        "https://t.co/",
        "https://www.pinterest.com/",
        "https://www.linkedin.com/",
        "https://www.reddit.com/",
    ]
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
                pc_persona.append(os_versions[11])
            elif 0.7 < rand <= 0.95:
                pc_persona.append(os_versions[7])
            else:
                pc_persona.append(os_versions[random.randint(0, 11)])

            if i <= windows[1].get("chrome"):
                browser = "chrome"
                if random.random() < 0.7:
                    browser_version = chrome_versions[random.randint(51, 69)]
                else:
                    browser_version = chrome_versions[random.randint(0, 50)]
            elif i <= windows[1].get("chrome") + windows[1].get("firefox"):
                browser = "firefox"
                if random.random() < 0.7:
                    browser_version = firefox_versions[random.randint(14, 19)]
                else:
                    browser_version = firefox_versions[random.randint(0, 13)]
            elif i <= windows[1].get("chrome") + windows[1].get("firefox") + windows[
                1
            ].get("edge"):
                browser = "edge"
                browser_version = edge_versions[
                    random.randint(0, len(edge_versions) - 1)
                ]

        elif i <= windows[0] + mac[0]:
            rand = random.random()
            if rand < 0.35:
                pc_persona.append(os_versions[26])
            elif 0.35 < rand < 0.7:
                pc_persona.append(os_versions[25])
            else:
                pc_persona.append(os_versions[random.randint(18, 24)])

            if i <= windows[0] + mac[1].get("chrome"):
                browser = "chrome"
                if random.random() < 0.7:
                    browser_version = chrome_versions[random.randint(51, 69)]
                else:
                    browser_version = chrome_versions[random.randint(0, 50)]
            elif i <= windows[0] + mac[1].get("chrome") + mac[1].get("firefox"):
                browser = "firefox"
                if random.random() < 0.7:
                    browser_version = firefox_versions[random.randint(14, 19)]
                else:
                    browser_version = firefox_versions[random.randint(0, 13)]
            elif i <= windows[0] + mac[1].get("chrome") + mac[1].get("firefox") + mac[
                1
            ].get("edge"):
                browser = "edge"
                browser_version = edge_versions[
                    random.randint(0, len(edge_versions) - 1)
                ]

        elif i <= windows[0] + mac[0] + linux[0]:
            if random.random() < 0.85:
                pc_persona.append(os_versions[13])
            else:
                pc_persona.append(os_versions[random.randint(12, 17)])

            if i <= windows[0] + mac[0] + linux[1].get("chrome"):
                browser = "chrome"
                if random.random() < 0.7:
                    browser_version = chrome_versions[random.randint(51, 69)]
                else:
                    browser_version = chrome_versions[random.randint(0, 50)]
            elif i <= windows[0] + mac[0] + linux[1].get("chrome") + linux[1].get(
                "firefox"
            ):
                browser = "firefox"
                if random.random() < 0.7:
                    browser_version = firefox_versions[random.randint(14, 19)]
                else:
                    browser_version = firefox_versions[random.randint(0, 13)]
            elif i <= windows[0] + mac[0] + linux[1].get("chrome") + linux[1].get(
                "firefox"
            ) + linux[1].get("edge"):
                browser = "edge"
                browser_version = edge_versions[
                    random.randint(0, len(edge_versions) - 1)
                ]

        # PC Screen Resolutions
        probability_of_screen = random.uniform(0, 100)
        preceding_prob_sum = 0
        for j in range(len(pc_screen_resolutions)):
            preceding_prob_sum += pc_screen_resolutions[j][2]
            if probability_of_screen <= preceding_prob_sum:
                screen_resolution = [
                    pc_screen_resolutions[j][0],
                    pc_screen_resolutions[j][1],
                    pc_screen_resolutions[j][0],
                    pc_screen_resolutions[j][1],
                    1,
                ]
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
            proxy_geo = f"country-{country.lower()}-city-{random.choice(proxy_cities[country])[0]}"
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
        persona_callback(pc_persona)
        db_entry_val = (
            str(pc_persona[1]),
            str(pc_persona[2]),
            str(pc_persona[3]),
            str(pc_persona[4]),
            str(pc_persona[5]),
            float(pc_persona[6]),
            str(pc_persona[7]),
            str(pc_persona[8]),
            int(pc_persona[9]),
            int(pc_persona[10]),
            str(pc_persona[11]),
            str(pc_persona[12]),
            str(pc_persona[13]),
            str(pc_persona[14]),
            str(pc_persona[15]),
            str(pc_persona[16]),
            str(pc_persona[17]),
            str(pc_persona[18]),
            str(pc_persona[19]),
            str(pc_persona[20]),
            str(pc_persona[21]),
            str(pc_persona[22]),
            json.dumps(str(pc_persona[23])),
            str(pc_persona[24]),
        )
        # botsdb_cursor.execute(sql, db_entry_val)
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
            proxy_geo = f"country-{country.lower()}-city-{random.choice(proxy_cities[country])[0]}"
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
        # db_entry_val = (
        #     str(sp_persona[1]),
        #     str(sp_persona[2]),
        #     str(sp_persona[3]),
        #     str(sp_persona[4]),
        #     str(sp_persona[5]),
        #     float(sp_persona[6]),
        #     str(sp_persona[7]),
        #     str(sp_persona[8]),
        #     int(sp_persona[9]),
        #     int(sp_persona[10]),
        #     str(sp_persona[11]),
        #     str(sp_persona[12]),
        #     str(sp_persona[13]),
        #     str(sp_persona[14]),
        #     str(sp_persona[15]),
        #     str(sp_persona[16]),
        #     str(sp_persona[17]),
        #     str(sp_persona[18]),
        #     str(sp_persona[19]),
        #     str(sp_persona[20]),
        #     str(sp_persona[21]),
        #     str(sp_persona[22]),
        #     json.dumps(str(sp_persona[23])),
        #     str(sp_persona[24]),
        # )
    #     botsdb_cursor.execute(sql, db_entry_val)
    # botsdb.commit()


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
