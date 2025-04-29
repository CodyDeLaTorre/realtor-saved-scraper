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
https://www.realtor.com/realestateandhomes-detail/17526-W-Coyote-Trail-Dr_Goodyear_AZ_85338_M16290-00294
https://www.realtor.com/realestateandhomes-detail/15962-W-Gibson-Ln_Goodyear_AZ_85338_M18873-79595
https://www.realtor.com/realestateandhomes-detail/18221-W-Pueblo-Ave_Goodyear_AZ_85338_M20474-48340
https://www.realtor.com/realestateandhomes-detail/16789-W-Taylor-St_Goodyear_AZ_85338_M20902-14971
https://www.realtor.com/realestateandhomes-detail/18473-W-Piedmont-Rd_Goodyear_AZ_85338_M18571-94181
https://www.realtor.com/realestateandhomes-detail/12690-S-184th-Ave_Goodyear_AZ_85338_M12096-16928
https://www.realtor.com/realestateandhomes-detail/18590-W-Vogel-Ave_Goodyear_AZ_85338_M13628-28313
https://www.realtor.com/realestateandhomes-detail/17447-W-Yavapai-St_Goodyear_AZ_85338_M18209-19898
https://www.realtor.com/realestateandhomes-detail/17163-W-Mohave-St_Goodyear_AZ_85338_M18386-21221
https://www.realtor.com/realestateandhomes-detail/1976-S-172nd-Ln_Goodyear_AZ_85338_M18448-81899
https://www.realtor.com/realestateandhomes-detail/15144-W-Washington-St_Goodyear_AZ_85338_M28635-83703
https://www.realtor.com/realestateandhomes-detail/16102-W-Miami-St_Goodyear_AZ_85338_M24577-63886
https://www.realtor.com/realestateandhomes-detail/10815-S-175th-Dr_Goodyear_AZ_85338_M23195-35057
https://www.realtor.com/realestateandhomes-detail/15547-W-Magnolia-St_Goodyear_AZ_85338_M22443-38686
https://www.realtor.com/realestateandhomes-detail/17555-W-Dalea-Dr_Goodyear_AZ_85338_M10472-67559

Surprise
https://www.realtor.com/realestateandhomes-detail/16079-W-Acapulco-Ln_Surprise_AZ_85379_M17797-78297
https://www.realtor.com/realestateandhomes-detail/16508-N-114th-Dr_Surprise_AZ_85378_M25725-96702
https://www.realtor.com/realestateandhomes-detail/15390-W-Teal-Ln_Surprise_AZ_85374_M11568-33985
https://www.realtor.com/realestateandhomes-detail/16543-W-Ironwood-St_Surprise_AZ_85388_M27565-93182
https://www.realtor.com/realestateandhomes-detail/16187-W-Port-Royale-Ln_Surprise_AZ_85379_M22342-50987
https://www.realtor.com/realestateandhomes-detail/14970-N-172nd-Dr_Surprise_AZ_85388_M20627-53120
https://www.realtor.com/realestateandhomes-detail/16034-W-Carmen-Dr_Surprise_AZ_85374_M20470-98275
https://www.realtor.com/realestateandhomes-detail/13257-W-Watson-Ln_Surprise_AZ_85379_M29571-81229
https://www.realtor.com/realestateandhomes-detail/26722-N-174th-Ln_Surprise_AZ_85387_M92066-78498
https://www.realtor.com/realestateandhomes-detail/14836-W-Desert-Hills-Dr_Surprise_AZ_85379_M22595-91828
```
