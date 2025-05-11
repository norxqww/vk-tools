# vk configuration
api = "https://api.vk.com/method/users.get"
api_ver = "5.207"
client = "6146827"  # android id

# get settings
timeout = 20
concurrency = 5  # Для режима 2 (турбо-чек)
user_agents = [
    'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',  
    'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0'
]

# file settings
file_prefix = "results_"
words_file = "words.json"