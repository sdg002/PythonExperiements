import sys

def hardcoded_secrets():
    secret="Pass@!*(34"
    invoke_rest_endpoint(apikey=secret)


def invoke_rest_endpoint(apikey: str)->None:
    return None



dev_output_folder="\\dev.server.com\out"
prod_output_folder="\\prod.server.com\out"

def hardcoded_parameters():
    generate_data_files(output=dev_output_folder)

def generate_data_files(output:str):
    pass


def genreate_some_reports():
    if (sys.argv[1] == "dev"):
        generate_data_files(output=dev_output_folder)
    else:
        generate_data_files(output=prod_output_folder)
