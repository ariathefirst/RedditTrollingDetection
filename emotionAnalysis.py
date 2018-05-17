personality_insights = PersonalityInsightsV3(
  version='2017-10-13',
  username='{username}',
  password='{password}')

with open(join(dirname(__file__), './profile.json')) as profile_json:
  profile = personality_insights.profile(
    profile_json.read(), content_type='application/json',
    raw_scores=True, consumption_preferences=True)

print(json.dumps(profile, indent=2))
