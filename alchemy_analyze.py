#!/usr/bin/env python
from alchemyapi import AlchemyAPI
import json

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
 
        response = alchemyapi.entities('text',text, {'sentiment': 0})

        if response['status'] == 'OK':
            analysizedData = decoder.decode(json.dumps(response))
            results = analysizedData.get("entities")
            for result in results:
                    entity = {
                            "text": result["text"],
                            "relevance": result["relevance"],
                            "type": result["type"],
                            "count": result["count"]
                            }
                    entities.append(entity);
            return entities
        else:
        	return None
