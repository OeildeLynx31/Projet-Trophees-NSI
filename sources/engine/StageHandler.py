import importlib

def getStageByID(id):
  try:
    stageClass = importlib.import_module(f"sources.stages.stage_{id}.stage")
    return stageClass.Stage
  except ModuleNotFoundError:
    return None
  
  
"""
Pls use this syntax to create new stages:
stage_{the id of your stage}/stage.py
"""