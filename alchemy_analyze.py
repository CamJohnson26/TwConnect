#!/usr/bin/env python
from alchemyapi import AlchemyAPI
import json

class types:
	combinedTypes = ["Company", "Facility", "GeographicFeature", "NaturalDisaster", "Organization", "Person", "PrintMedia", "Region", "Sport", "StateOrCounty"];
	entertainmentTypes = ["EntertainmentAward", "Movie", "MusicGroup", "Celebrity", "FilmActor", "FilmArtDirector", "FilmCastingDirector", "FilmCharacter", "FilmCinematographer", "FilmCritic", "FilmDirector", "FilmEditor", "OperaSinger", "OperaDirector"];
	sportsTypes = ["SoccerClub", "SportsAssociation", "CricketAdministrativeBody", "BasketballCoach", "BasketballPlayer", "Boxer", "CricketBowler", "CricketCoach", "CricketPlayer", "CricketUmpire", "Cyclist", "FootballCoach", "FootballPlayer", "FootballReferee", "FootballTeamManager", "HockeyCoach", "HockeyPlayer", "OlympicAthlete", "SportsOfficial", "MartialArt", "Golfer"];
	politicsTypes = ["U.S.Congressperson", "USPresident", "USVicePresident"];
	technologyTypes = ["ComputerScientist", "ProgrammingLanguageDesigner", "RecordingEngineer", "ProgrammingLanguageDeveloper", "VideoGameActor", "VideoGameDesigner", "VisualArtist"];
	
def get_category(text):
	"""
	find the category that input text belongs to

	INPUT:
	test -> input text that need to be analyze

	OUTPUT:
	category string that input belongs to. "null" means alchemyapi fails somehow
	"""
	
	alchemyapi = AlchemyAPI()
	decoder = json.JSONDecoder()

	response = alchemyapi.category('text',text)

	if response['status'] == 'OK':
		analysizedData = decoder.decode(json.dumps(response))
		category = analysizedData.get("category")
		return category
	else:
		return "null"

def get_grouped_category(texts):
	"""
	get category and corresponding statistic for multiplt texts

	INPUT:
	text -> text array to be analyzed

	OUTPUT:
	statistic -> dict that has the frequence of each category, like{"soccer": 12, "football": 24}
	category -> array that each text belongs to in sequence
	"""
	alchemyapi = AlchemyAPI()
	decoder = json.JSONDecoder()

	statistic = {"null": 0}
	category = []

	for text in texts:
		response = alchemyapi.category('text',text)

		if response['status'] == 'OK':
			analysizedData = decoder.decode(json.dumps(response))
			category.append(analysizedData.get("category"))
			if (statistic.get(category[-1]) != None):
				statistic[category[-1]] = statistic.get(category[-1]) + 1
			else:
				statistic[category[-1]] = 1
		else:
			print(response['status']);
			statistic["null"] = statistic.get("null") + 1
			category.append("null")
			
	return statistic, category

def extract_entities(text):
	"""
	find the category that input text belongs to

	INPUT:
	test -> input text that need to be analyze

	OUTPUT:
	category string that input belongs to. "null" means alchemyapi fails somehow
	"""
	
	alchemyapi = AlchemyAPI()
	decoder = json.JSONDecoder()
	entities = []
	type = ""

	response = alchemyapi.entities('text',text, {'sentiment': 0})

	if response['status'] == 'OK':
		analysizedData = decoder.decode(json.dumps(response))
		results = analysizedData.get("entities")
		for result in results:
			if result.get("type") in types.combinedTypes:
				type = get_category(text);
				if type == 'arts_entertainment' or type == 'gaming' or type == 'recreation':
					type = "entertainment";
				elif type == 'sports':
					type = "sports";
				elif type == 'computers_internet' or type == 'health' or type == 'science_technology':
					type = "technology";
				elif type == 'culture_politics':
					type = "politics";
				else:
					continue;
			else:
				type = result.get("type");
				if type in types.entertainmentTypes:
					type = "entertainment";
				elif type in types.sportsTypes:
					type = "sports";
				elif type in types.politicsTypes:
					type = "politics";
				elif type in types.technologyTypes:
					type = "technology";
				else:
					continue;
			entity = {
				"text": result["text"],
				"relevance": result["relevance"],
				"type": type,
				"count": int(result["count"])
			}
			entities.append(entity);
		return entities
	else:
		print(response['status']);
		return []
