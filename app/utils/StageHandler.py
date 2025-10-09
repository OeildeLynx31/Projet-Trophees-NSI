import os, importlib

def getStageByID(id):
  try:
    stageClass = importlib.import_module(f"app.stages.stage_{id}.stage")
    return stageClass.Stage
  except ModuleNotFoundError:
    print(f"Stage with ID {id} not found.")
    return None
  
  
"""
Pls use this syntax to create new stages:
stage_{the id of your stage}/stage.py
"""