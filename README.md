# Schema Generator 
This is a simple script to generate a Draft 4 JSON Schema using the GenSON JSON Schema generator. Utilizing GenSON's ability to extract a single schema from multiple json objects, this script intakes a directory containing json files and creates a single schema using all the json files contained within that directory. 

## Running
To run the script: 
1. Clone the repository 
2. Drag in all the json files you would like to include in your schema into the `/jsons` folder
3. run the import script `pip install -r req.txt`
4. run the generator script `python genSchema.py`
5. the output will be in the `schema.json` file 
