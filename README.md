# vk-tools
Checks the availability of the ID in VK.

Two modes of operation: checking the availability of an ID by the list (words.json) and turbing a specific ID.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ваш-репозиторий/vk_id_checker.git
   cd vk_id_checker
2. Install dependencies:
   ```bash
   pip install aiohttp win10toast asyncio

3. Create a words.json file with a list of IDs to check or add to an existing one.

## Usage
1. Run the script and select the mode.
```bash
python main.py
```

## Operating modes:
1. ID Checking
Checks all IDs from words.json and saves free ones in results_date_time.txt.

2. ID Turbing
Monitors one ID and displays a notification when it becomes free.
