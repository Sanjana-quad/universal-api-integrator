from src.parsers.json_parser import load_json
from src.parsers.csv_parser import load_csv
from src.parsers.yaml_parser import load_yaml
from src.logger.logger import get_logger
from src.nlp.text_cleaner import clean_text


log = get_logger("etl")

def run_pipeline():
    config = load_yaml("src/parsers/input/pipeline.yaml")
    json_data = load_json("src/parsers/input/sample.json")
    csv_data = load_csv("src/parsers/input/users.csv")

    if json_data and "name" in json_data:
        json_data["name_clean"] = clean_text(json_data["name"])

    log.info("ETL pipeline executed with text cleaning")
    return {
        "config": config,
        "json": json_data,
        "csv": csv_data,
    }

    # log.info("ETL pipeline executed successfully")

    # return {
    #     "config": config,
    #     "json": json_data,
    #     "csv": csv_data
    # }
