from dotenv import load_dotenv
import os
import mwclient

load_dotenv()

site = mwclient.Site('torque.leverforchange.org/', '100Change2020/', scheme="https")
site.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
proposalData = site.api('torquedataconnect', format='json', path='/LFC100Change2020')
# 100
print(len(proposalData["LFC100Change2020"]))
print()
# Empower 25 million people with safe water and sanitation
print(next(filter(lambda p: p["Review Number"] == "6988", proposalData["LFC100Change2020"]))['Project Title'])
print()
# All available columns
print(proposalData["LFC100Change2020"][0].keys())
