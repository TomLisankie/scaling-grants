from dotenv import load_dotenv
import os
import mwclient
import pandas

load_dotenv()

def mediawiki_formatted_competition_name(competition_name):
    # The reason this function exists is because MediaWiki has some weird thing with entities not starting with numbers
    if competition_name[0].isdigit():
        return "LFC" + competition_name
    return competition_name

def get_proposals_for_competition(competition_name):
    site = mwclient.Site('torque.leverforchange.org/', competition_name + '/', scheme="https")
    site.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
    proposals = site.api('torquedataconnect', format='json', path='/' + mediawiki_formatted_competition_name(competition_name))
    return proposals

competition_name = "100Change2020"
mw_formatted_name = mediawiki_formatted_competition_name(competition_name)
proposal_data = get_proposals_for_competition(competition_name)
# 455
# print(len(proposal_data[mw_formatted_name]))
# print()
# # Empower 25 million people with safe water and sanitation
# print(next(filter(lambda p: p["Review Number"] == "6988", proposal_data[mw_formatted_name]))['Project Title'])
# print()
# # count of all available columns
# print(len(proposal_data[mw_formatted_name][365].keys()))


def aggregate_submissions_into_dataframe(proposal_data):
    aggregate_dict = {}
    for key in proposal_data[0]:
        aggregate_dict[key] = []
        for proposal in proposal_data:
            # go through each proposal, find the value for the key, put it in the list for the key in the dict
            aggregate_dict[key].append(proposal[key])
    print(proposal_data[454])
    return pandas.DataFrame.from_dict(aggregate_dict)

proposals_dataframe = aggregate_submissions_into_dataframe(proposal_data[mw_formatted_name])
proposals_dataframe.to_csv("data.csv")
