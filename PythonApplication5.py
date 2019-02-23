# Import system modules
import arcpy
import os

# Set local variables
workspace = r"D:\GIS 610 _ Assignment 3\Exercise 3.gdb\Exercise 3.gdb"
outWorkspace = r"D:\GIS 610 _ Assignment 3"
 
# Want to join USA cities to states and calculate the mean city population
# for each state
targetFeatures = os.path.join(workspace, "census tracts")
joinFeatures = os.path.join(workspace, "general offense")

outfc = os.path.join(outWorkspace, "Tracts_Offense")