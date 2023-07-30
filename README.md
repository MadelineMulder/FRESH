<p align="center">
    <img src="logo_banner.jpg" alt="FRESH Logo Banner">
</p>

# Welcome to the FRESH Project
*This is a repository for the final PLUS Practice for Software Development class (summer semester 2023).*  

FRESH stands for **F**lood **R**outing for **E**mergency **S**ervices for **H**urricanes. 

The FRESH project focuses on network analysis and visualization on Grand Bahama Island during hurricane Dorian (2019). The project was meant to continue the work begun during the [Foresight DRM: Disaster Mapping Hackathon 2023](https://storymaps.arcgis.com/stories/f819f3563aef4cad8cfae7072eed0d07). The impetus for this project was to translate the web application that was created during the Hackathon from javascript to python using OSMnx and Folium. 

The end result of this project is a web application created through Flask which hosts two apps:
- A routing app which allows users to input starting and end coordinates on the Grand Bahama Island and recieve routing results for the best path between the two points
- A hurricane visualization app which displays the dynamic path of hurricane Dorian as it approaches the Grand Bahama island over a series of days.  

In addition to the web application with the routing and hurricane apps a website was also developed to provide background and documentation for the project using Github pages. The website can be found here: [FRESH Project Website](https://madelinemulder.github.io/FRESH/index.html)

*Team Members: Lisah Ligono, Madeline Mulder, Parinda Pannoon*



## How to Deploy the FRESH Web Application Using Flask

At this moment the application can only be installed on localhost. To set this up, please follow the following guidelines:

In this installation example, we demonstrate how to deploy the app using conda 

```
git clone https://github.com/MadelineMulder/FRESH.git
cd application
conda env create -f freshenv.yml
conda activate freshenv
```

Once you have activated the environment, go to the <b>main.py</b> file and set the correct path to the <i>Grand_Bahama.shp</i> and <i>hurricanepolygon.shp</i> which are in the data folder. Do the same for the <b>index.html</> in the templates folder

When done, run the script <b>main.py</b> in your console and a url will be provided where you can visualize the application in your local machine.

You should have something like this:
<p align="center">
  <img width="452" alt="fresh" src="https://github.com/MadelineMulder/FRESH/assets/72496335/35e904a6-cbc7-4dbe-b6cb-00d9d1d0f152"width="1000">
</p>




## Contents of This Repository
*In alphabetical order (images are not included in the following list)*

* **Application Directory:** Contains the code for the Flask web application which hosts the routing and hurricane visualization apps
    * **Template Directory:** Contains HTML code for Flask project homepage and sample coordinate for testing the routing app 
    * **color.py:** Contains code for styling hurricane visualization app
    * **freshenv.yml:** Contains environment for Flask projects
    * **main.py:** Contains code for Flask project and both routing and hurricane visualization app
* **CSS Directory:** contains style sheet for the FRESH project website
* **Data Directory:** Contains data related to the FRESH Project including study area boundary files.
* **Routing Directory:** Contains reference material for the routing portion of the project including an early draft of the routing app code and reference code on how to incorporate user input
* **About.HTML:** Contains HTML code and content for the about page of FRESH Project website
* **Documentation.HTML:** Contains HTML code and content for the documentation page of FRESH Project website
* **Index.HTML:** Contains HTML code and content for the homepage of FRESH Project website




