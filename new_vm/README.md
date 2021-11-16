# Workflow for Calling Intersight Virtual Machine build

## Update
* Updated with latest vCenter MOID using this code:
`https://intersight.com/apidocs/apirefs/api/v1/virtualization/VmwareVcenters/get/`

## Information
* Gather workflow definition from this info
Workflow Definition Moid:5e6ae227696f6e2d30d32303 from:  
>   "ObjectType": "workflow.WorkflowDefinitionList"  
>   "link": "https://www.intersight.com/api/v1/workflow/WorkflowDefinition". 
  
* Start workflow called with /api/v1/workflow/WorkflowInfos.  
POST using WorkflowInfos.json file as payload. 
WorkflowInfo.json overwritten by command line args, below.  
  
## Useage:  
python3 app.py -h.  
   
usage: app.py [-h] [-i IMAGE] [-c CPUS] [-m MEMORY] VmName. 
  
Create new VM via Intersight.  
  
positional arguments:  
>  VmName      Virtual Machine Name. 
  
optional arguments:    
> -h, --help  show this help message and exit.   
> -i IMAGE    Image URL for VM - OVF or OVA format.   
> -c CPUS     Number of virtual CPUs.   
> -m MEMORY   Amount of Memory in MB where 1024 is 1 GiB.   

### Example:
python3 newvm-app.py -i http://172.24.1.70/install/ubuntu-18.04-server-cloudimg-amd64.ova -c 1 -m 1024 my_vm_01