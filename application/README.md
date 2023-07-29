# Installation

At this moment the application can only be installed on localhost. To set this up, please follow the following guidelines:

In this installation example, we demonstrate using the conda 

```
git clone https://github.com/MadelineMulder/FRESH.git
cd application
conda env create -f freshenv.yml
conda activate freshenv
```

Once you have activated the environment, go to the <b>main.py</b> file and set the correct path to the <i>Grand_Bahama.shp</i> and <i>hurricanepolygon.shp</i> which are in the data folder. Do the same for the <i>index.html</i> in the templates folder

When done run the script python main.py in your console and a url will be provided where you can visualize the application in your local machine.

You should have something like this:
<p align="center">
  <img width="452" alt="fresh" src="https://github.com/MadelineMulder/FRESH/assets/72496335/35e904a6-cbc7-4dbe-b6cb-00d9d1d0f152"width="1000">
</p>
