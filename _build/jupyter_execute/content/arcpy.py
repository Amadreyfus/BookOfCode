(arcpy)=
# Arcpy 

```{important} Folder Setup
It is important for a blank project to be setup in ArcGIS Pro before using arcpy as it creates the necessary project folders and objects
to successfully use the package. Furthermore, it is a good idea to setup an "intermediate data" subfolder in your main folder to handle
all outputs from arcpy and python as they can get quite messy.
```

```ipython
# Here is an example of an intermediate folder address within the main folder `Connecticut`

r'C:\Users\SeanJ\JupyterFolder\CrashometryV2Data\Connecticut\IntermediateData'
```

(arcpybasics)=
## Basic Steps to Arcpy Scripting


### Step 1: Set up your arcpy workspace and allow for overwriting

Doing this grants the neccessary functionality to any files/interactions between arcpy and this folder.  

It essentially establishes your working directory for any arcpy calls.  

Overwriting allows you to overwrite previous files so you never have problems reexecuting commands.  

```ipython
#Setting up my arcpy workspace, basically my working directory for basic arcpy functions
arcpy.env.workspace = r'C:\Users\SeanJ\JupyterFolder\CrashometryV2Data\Connecticut\IntermediateData'

#Making sure that I can overwrite previous files if I need to.
arcpy.env.overwriteOutput = True
```

### Step2: Establishes path to the ArcGIS project I want to interact with

```ipython
#Establishes the path to the arcGIS project I want, which will contain my layers, features, tables, maps..
project = arcpy.mp.ArcGISProject(r'C:\Users\SeanJ\JupyterFolder\CrashometryV2Data\Connecticut\ArcGISProject\ArcGISProject.aprx')
```

### Step3: Dealing with Maps in the Project

```python
#Create a results object that is a list of maps
result_maps = project.listMaps()

#Simple loop to create a list with names of map objects in current project.
list_maps = []
for m in result_maps:
    list_maps.append(m.name)
    
#Check the result of this list population, should be 1 map by default
list_maps  

#Assigning a reference to the first (and only in this case) map in my list which will point to the map object
my_map = result_maps[0]

#Check the name of map, using `.name` attribute, is "Map" by default 
my_map.name
```

### Step4: Adding Data to Map as a Feature

```ipython
#Adding a standalone table (as a feauture) to my project that contains stripped down crash data for CT for 2019-May2020
my_map.addDataFromPath(r'C:\Users\SeanJ\JupyterFolder\CrashometryV2Data\Connecticut\CT_Jan_2019_May_2020_Sparse.csv')


#Checking to make sure that my table has be uploaded
for i in my_map.listTables():
    print(i)
    
#Assigning a reference variable to my table result object
table = my_map.listTables()[0]

#Converting my table into a format that will allow it to integrate as a geospatial map layer, simple point shape file. This
#is an intermediate step and the result must be uploaded to the map explicitly.
arcpy.management.XYTableToPoint(table, 'CT_TableToPoint', "Longitude", "Latitude")

#Adding the shapefile we just output to map as a layer
my_map.addDataFromPath(r'C:\Users\SeanJ\JupyterFolder\CrashometryV2Data\Connecticut\IntermediateData\CT_TableToPoint.shp')

#This is a shapefile that contains polygons of all counties in the United States
my_map.addDataFromPath(r'C:\Users\SeanJ\JupyterFolder\CrashometryV2Data\CountyShapeFile\tl_2017_us_county.shp')

#Quick Check to make sure we have our necessary layers and see where they are indexed.
for index, member in enumerate(my_map.listLayers()):
    print(index, member.name)
```

<br \>

So, now we have a map with a bunch of feature layers inside of our project. Opening up ArcGIS desktop will display all this data for us
visually.

<br />


(spatial)=
## Spatial Joins

We now have some distinct layers and can do a spatial join on them combining them into a single dataset based off some geospatial attribute

```ipython
#Assigning references in order to pass them as arguments to future function
target_feature = my_map.listLayers()[1]
join_feature = my_map.listLayers()[0]

#Performing the Spatial join, "CT_County_Spatial" is our desired filename.
arcpy.analysis.SpatialJoin(target_feature, join_feature, "CT_County_Spatial", join_operation='JOIN_ONE_TO_ONE',
                           join_type='KEEP_ALL', match_option='INTERSECT')


#Converting the spatially joined shapefile into a csv so we can upload it as a DataFrame
arcpy.TableToTable_conversion("CT_County_Spatial.shp", r"C:\Users\SeanJ\JupyterFolder\CrashometryV2Data\Connecticut\IntermediateData",
                              "CT_County_SpatialJoin.csv" )
```