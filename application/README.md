# Installation

At this moment the application can only be installed on localhost. To set this up, please follow the following guidelines:

In this installation example, we demonstrate using the conda 

git clone https://github.com/MadelineMulder/FRESH.git

cd application

conda env create -f freshenv.yml

conda activate freshenv

Once you have activated the environment, go to the data folder and set the correct path to the <i>Grand_Bahama.shp</i> and <i>hurricanepolygon.shp</i> Do the same for the <i>index.html</i> in the templates folder

When done run the script python main.py in your console and a url will be provided where you can visualize the application in your local machine.
