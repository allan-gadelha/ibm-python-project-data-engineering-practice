import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime
import os

log_file = "log_file.txt"
target_file = "transformed_data.csv"
output_folder = "ETL Process Practice/output"
log_folder = "ETL Process Practice/log"

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    dataframe = dataframe.rename(columns={"car_model": "Model", "year_of_manufacture": "Year", "price": "Price", "fuel": "Fuel"})
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    dataframe = dataframe.rename(columns={"car_model": "Model", "year_of_manufacture": "Year", "price": "Price", "fuel": "Fuel"})
    return dataframe

def extract_from_xml(file_to_process): 
    dataframe = pd.DataFrame(columns=["Model", "Year", "Price","Fuel"]) 
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for car in root: 
        model = car.find("car_model").text 
        year = float(car.find("year_of_manufacture").text) 
        price = float(car.find("price").text)
        fuel = car.find("fuel").text 
        dataframe = pd.concat([dataframe, pd.DataFrame([{"Model":model, "Year":year, "Price":price, "Fuel":fuel}])], ignore_index=True) 
    return dataframe

def extract():
    # create an empty data frame to hold extracted data 
    extracted_data = pd.DataFrame(columns=["Model", "Year", "Price","Fuel"]) 
     
    # process all csv files 
    for csvfile in glob.glob("ETL Process Practice/data/*.csv"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("ETL Process Practice/data/*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("ETL Process Practice/data/*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data

def transform(data): 
    '''Rouding to 2 decimal places '''
    data['Price'] = round(data['Price'], 2)  

    return data

def load_data(target_file, transformed_data):
    target_file = os.path.join(output_folder, target_file)
    transformed_data.to_csv(target_file)

def log_progress(message): 
    log_file_path = os.path.join(log_folder, log_file)
    
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    
    with open(log_file_path,"a") as f: 
        f.write(timestamp + ',' + message + '\n')

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 