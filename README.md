# The Realtor Saved Homes Scraper

## Problem

- The Realtor website doesn't have an easy way to export all of your saved homes links to share with a realtor.

## Solution

- A web scraper that targets your saved homes and outputs their links into one file. It also sorts them by city for convenience.

### Requirements to use
- Need the proper selenium webdirver installed
- Need your realtor login (EMAIL, PASSWORD) provided in a .env file at the same level of the scraper.py

### Example Output

```
Buckeye
https://www.realtor.com/realestateandhomes-detail/26065-W-Yukon-Dr_Buckeye_AZ_85396_M15159-56243
https://www.realtor.com/realestateandhomes-detail/26234-W-Behrend-Dr_Buckeye_AZ_85396_M22107-85091

Goodyear
https://www.realtor.com/realestateandhomes-detail/17152-W-Watkins-St_Goodyear_AZ_85338_M18472-29653
https://www.realtor.com/realestateandhomes-detail/16987-W-Hammond-St_Goodyear_AZ_85338_M20855-40281
https://www.realtor.com/realestateandhomes-detail/15857-W-Yavapai-St_Goodyear_AZ_85338_M14770-13364
https://www.realtor.com/realestateandhomes-detail/17699-W-Tonto-St_Goodyear_AZ_85338_M15444-27423

Surprise
https://www.realtor.com/realestateandhomes-detail/16079-W-Acapulco-Ln_Surprise_AZ_85379_M17797-78297
https://www.realtor.com/realestateandhomes-detail/16508-N-114th-Dr_Surprise_AZ_85378_M25725-96702
https://www.realtor.com/realestateandhomes-detail/15390-W-Teal-Ln_Surprise_AZ_85374_M11568-33985

```
