import arcpy

current_workspace = r'D:\GIS 610 _ Assignment 3\Exercise 3.gdb\Exercise 3.gdb'

geometry_type = "POLYGON"

spatial_reference = arcpy.SpatialReference(102100)

featureClassNamesList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']


arcpy.env.workspace = current_workspace

arcpy.env.overwriteOutput = True


# functions


def createFeatureClass(in_fc_name):

    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)

    print('Feature Class ' + in_fc_name + ' was sucessfully created.')

createFC = [createFeatureClass(fc) for fc in featureClassNamesList]

for fc in featureClassNamesList:
     createFeatureClass(fc)


print('All Done')
