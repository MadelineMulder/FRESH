import geopandas as gpd

    
def pink(feature):
        return {
            'fillColor': '#ffc0cb',  
            'color': '#000000',      
            'weight': 1,            
            'fillOpacity': 0.6      
        }

def yellow(feature):
        return {
            'fillColor': '#ffff00',  
            'color': '#000000',      
            'weight': 1,             
            'fillOpacity': 0.6      
        }
def green(feature):
        return {
            'fillColor': '#90ee90',  
            'color': '#000000',      
            'weight': 1,             
            'fillOpacity': 0.6      
        }
def purple(feature):
        return {
            'fillColor': '#800080',  
            'color': '#000000',      
            'weight': 1,             
            'fillOpacity': 0.6      
        }
def red(feature):
        return {
            'fillColor': '#ff0000',  
            'color': '#000000',      
            'weight': 1,             
            'fillOpacity': 0.6      
        }

   
colorlist = {
        '2-Agricultural Areas': '#ffff00',
        '3-Forests and Semi-natural Areas': '#90ee90',
        '998-Others': '#ff0000'
       
    }
   

def cat(feature):
        category_value = feature['properties']['obj_type']  # Replace 'category' with the actual column name in your shapefile

        # Get the color based on the category value from the category_colors dictionary
        color = colorlist.get(category_value, '#808080')  # Default color: Gray

        return {
            'fillColor': color,
            'color': '#000000',
            'weight': 1,
            'fillOpacity': 1.0
        }