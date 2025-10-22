"""
Sample code to iterate over an iterator and split into multiple files

"""
import os
def generate_records(query:dict)->iter:
    if query is None:
        raise ValueError("query was not specified")
    return range(1000)

def generate_file_name(folder: str, batch_index: int)->str:
    name=f"batch_{batch_index}.txt"
    return os.path.join(folder, name)

def split_results(results:iter, batch_size:int, folder: str)->None:
    if not os.path.exists(folder):
        raise ValueError(f"The specified path does not exist: {folder}")
    batch_count=0
    records_in_current_batch=0
    current_file_name = generate_file_name(folder=folder, batch_index=batch_count)
    for record_index in results:
        print(f"{record_index=}, {batch_count=}, {records_in_current_batch=}, {current_file_name=}")
        records_in_current_batch+=1
        with open(current_file_name, mode="a", encoding="utf8") as f:
            f.write(f"{record_index}\n")
        if records_in_current_batch >= batch_size:
            records_in_current_batch=0
            batch_count+=1
            current_file_name=generate_file_name(folder=folder, batch_index=batch_count)
    pass

if __name__=="__main__":
    results=generate_records(query={})
    split_results(results=results,batch_size=30,folder='c:/truetemp/mongo_iter/')
    print("Hello world")