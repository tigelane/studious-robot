#!/usr/bin/env python3

# Import Intersight REST" Package
# Install with 'pip3 install intersight-rest'
import argparse
import intersight_rest as isREST
import json
from datetime import datetime

private_key_file = "./intersight_private_key.pem"
public_key_file = "./intersight_publickey.txt"
json_template_file = 'WorkflowNewVM.json'

def write_log(results):
    get_body = json.dumps(results.json(), indent=4)
    time_now = datetime.now()
    f_time_now = time_now.strftime("%m%d%Y%H%M%S")
    out_name = "deploy_newvm_log_" + f_time_now
    with open(out_name, 'w') as file_handle:
        file_handle.write(get_body)
        file_handle.close()
    return

def newvm(VmName, Image, CPUs, Memory):
    # Select Resource Path from https://www.intersight.com/apidocs 
    resource_path = '/workflow/WorkflowInfos'

    #-- Deployment file is JSON in local directory --#
    #-- Open File and read in default values --#
    #-- Overwrite default values with command line args --#
    with open(json_template_file) as json_file:
        workload_params = json.load(json_file)
        workload_params['Input']['VmName'] = VmName
        workload_params['Input']['Image'] = Image
        workload_params['Input']['CPUs'] = CPUs
        workload_params['Input']['Memory'] = Memory

    #-- Set Options --#
    options = {
        "http_method": "post",
        "resource_path": resource_path,
        "body": workload_params
    }

    #-- Send POST Request --#
    # Results in response code and body of response
    results = isREST.intersight_call(**options)
    print("Status Code: " + str(results.status_code))
    return results

def main(args):
    dict_vars = vars(args)

    # VmName required
    VmName = dict_vars['VmName']
    Image = dict_vars['Image']
    CPUs = dict_vars['CPUs']
    Memory = dict_vars['Memory']

    # Load Public/Private Keys
    isREST.set_private_key(open(private_key_file, "r") .read())
    isREST.set_public_key(open(public_key_file, "r") .read())

    # Create newvm() with variables VmName, Image, CPUs, Memory
    results = newvm(VmName, Image, CPUs, Memory)

    # Create a log file of our results
    write_log(results)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new VM via Intersight.')
    parser.add_argument('VmName', help='Virtual Machine Name')
    parser.add_argument('-i', dest='Image', help='Image URL for VM - OVF or OVA format', default='http://172.24.1.70/install/dsl.ova')
    parser.add_argument('-c', dest='CPUs', help='Number of CPUs', type=int, default= 1)
    parser.add_argument('-m', dest='Memory', help='Amount of Memory in MB where 1024 is 1 GiB', type=int, default= 1024)
    # parser.add_argument('-f', dest='credentials', help='Name of Credential file - without the ".py"')
    args, unknown = parser.parse_known_args()

    main(args)