from dotenv import load_dotenv
import os
import mwclient

load_dotenv()

def mediawiki_formatted_competition_name(competition_name):
    if competition_name[0].isdigit():
        return "LFC" + competition_name
    return competition_name

def get_proposals_for_competition(competition_name):
    site = mwclient.Site('torque.leverforchange.org/', competition_name + '/', scheme="https")
    site.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
    proposals = site.api('torquedataconnect', format='json', path='/' + mediawiki_formatted_competition_name(competition_name))
    return proposals

proposal_data = get_proposals_for_competition("100Change2020")
# 455
print(len(proposal_data["LFC100Change2020"]))
print()
# Empower 25 million people with safe water and sanitation
print(next(filter(lambda p: p["Review Number"] == "6988", proposal_data["LFC100Change2020"]))['Project Title'])
print()
# All available columns
print(proposal_data["LFC100Change2020"][0].keys())
