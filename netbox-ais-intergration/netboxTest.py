import schedule
import time
import requests
import json
import argparse
import yaml
from aos.client import AosClient


"""
ASN
"""
def aosAsnPoolDetails():
    # Get All Pool Details
    aosReturn = aos.resources.asn_pools.get_all()
    return aosReturn

def netboxAsnPoolDetails(apiEndpoint):
    netboxReturn = netboxRequestGet(apiEndpoint=apiEndpoint)
    netboxReturn = json.loads(netboxReturn)
    return netboxReturn

def asnCompare(aosReturn, netboxReturn, apiEndpoint):
    netboxList = []
    aosList=[]
    for item in netboxReturn['results']:
        netboxList.append(item['pool_id'])


    for pool in aosReturn:
        aosList.append(pool["id"])

    # compare AOS against Netbox
    compareList = list(set(netboxList)-set(aosList))

    for item in netboxReturn['results']:
        if item['pool_id'] in compareList:
            netboxRequestDelete(apiEndpoint=apiEndpoint, nbID=item['id'])

    for pool in aosReturn:
        displayName = pool["display_name"]
        startAsn = pool["ranges"][0]["first"]
        endAsn = pool["ranges"][0]["last"]
        tag = pool.get("tags"[0])
        pool_id = pool["id"]

        data = f'''{{
                "name": "{displayName}", 
                "first_asn": {startAsn}, 
                "last_asn": {endAsn}, 
                "tag": "{tag}", 
                "pool_id": "{pool_id}"
                
                }}'''

        netboxRequestPost(apiEndpoint=apiEndpoint, data=data)

def netboxAsn(apiEndpoint):

    netboxReturn=netboxAsnPoolDetails(apiEndpoint)
    aosReturn = aosAsnPoolDetails()
    asnCompare(aosReturn, netboxReturn, apiEndpoint)


"""
VNI
"""
def aosVniPoolDetails():
    # Get All Pool Details
    aosReturn = aos.resources.vni_pools.get_all()
    return aosReturn

def netboxVniPoolDetails(apiEndpoint):
    netboxReturn = netboxRequestGet(apiEndpoint=apiEndpoint)
    netboxReturn = json.loads(netboxReturn)
    return netboxReturn

def vniCompare(aosReturn, netboxReturn, apiEndpoint):
    netboxList = []
    aosList=[]
    for item in netboxReturn['results']:
        netboxList.append(item['pool_id'])


    for pool in aosReturn:
        aosList.append(pool["id"])

    # compare AOS against Netbox
    compareList = list(set(netboxList)-set(aosList))

    for item in netboxReturn['results']:
        if item['pool_id'] in compareList:
            netboxRequestDelete(apiEndpoint=apiEndpoint, nbID=item['id'])

    for pool in aosReturn:
        displayName = pool["display_name"]
        startAsn = pool["ranges"][0]["first"]
        endAsn = pool["ranges"][0]["last"]
        tag = pool.get("tags"[0])
        pool_id = pool["id"]

        data = f'''{{
                "name": "{displayName}", 
                "first_vni": {startAsn}, 
                "last_vni": {endAsn}, 
                "tag": "{tag}", 
                "pool_id": "{pool_id}"
                
                }}'''

        netboxRequestPost(apiEndpoint=apiEndpoint, data=data)

def netboxVni(apiEndpoint):

    netboxReturn=netboxVniPoolDetails(apiEndpoint)
    aosReturn = aosVniPoolDetails()
    vniCompare(aosReturn, netboxReturn, apiEndpoint)


"""
IP
"""
def aosIpPoolDetails():
    # Get All Pool Details
    aosReturn = aos.resources.ipv4_pools.get_all()
    return aosReturn


def netboxIpPoolDetails(apiEndpoint):
    netboxReturn = netboxRequestGet(apiEndpoint=apiEndpoint)
    netboxReturn = json.loads(netboxReturn)
    return netboxReturn


def ipCompare(aosReturn, netboxReturn, apiEndpoint):
    netboxList = []
    aosList=[]
    for item in netboxReturn['results']:
        netboxList.append(item['pool_id'])

    for pool in aosReturn:
        aosList.append(pool["id"])

    # compare AOS against Netbox
    compareList = list(set(netboxList)-set(aosList))

    for item in netboxReturn['results']:
        if item['pool_id'] in compareList:
            netboxRequestDelete(apiEndpoint=apiEndpoint, nbID=item['id'])

    for pool in aosReturn:
        displayName = pool["display_name"]
        subnet = pool["subnets"][0]["network"]
        tag = pool.get("tags"[0])
        pool_id = pool["id"]

        data = f'''{{
                "name": "{displayName}", 
                "subnet": "{subnet}", 
                "tag": "{tag}", 
                "pool_id": "{pool_id}"
                
                }}'''
        
        netboxRequestPost(apiEndpoint=apiEndpoint, data=data)


def netboxIp(apiEndpoint):

    netboxReturn=netboxIpPoolDetails(apiEndpoint)
    aosReturn = aosIpPoolDetails()
    ipCompare(aosReturn, netboxReturn, apiEndpoint)


"""
Netbox Requests
"""
def netboxRequestPost(apiEndpoint, data):
    url = f"http://{NB_HOST}:{NB_PORT}{apiEndpoint}"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Token {}'.format(NB_TOKEN)}
    response = requests.post(url=url, headers=headers, data=data)

def netboxRequestGet(apiEndpoint):
    url = f"http://{NB_HOST}:{NB_PORT}{apiEndpoint}"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Token {}'.format(NB_TOKEN)}
    response = requests.get(url=url, headers=headers)
    return response.text

def netboxRequestDelete(apiEndpoint, nbID):
    url = f"http://{NB_HOST}:{NB_PORT}{apiEndpoint}{nbID}"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Token {}'.format(NB_TOKEN)}
    response = requests.delete(url=url, headers=headers)
    return response.text


"""
Generic
"""
def aosConnection():
    # AOS Connection
    aos = AosClient(protocol="https", host=AOS_IP, port=AOS_PORT)
    aos.auth.login(AOS_USER, AOS_PW)
    return aos

def yamlLoad(yamlFilename: str) -> dict:
    """Validates the user input YAML with template
    Args:
        inputDict (dict): User YAML Dict input
        yamlValidateFilename (str): YAML allowed values template
    """    
    with open(yamlFilename) as f:
        configDict = yaml.safe_load(f)

    netboxCreds=configDict['netbox']
    aosCreds=configDict['ais']
    print(netboxCreds)
    print(aosCreds)
    return aosCreds, netboxCreds

def args(argv=None):
    """Args Parse for user input
    Args:
        argv (str, required): Apstra YAML Config File. Defaults to None.
    Returns:
        dict: Dict of args
    """
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-f', '--filename',
                        required=True,
                        help='YAML Config File')

    args = parser.parse_args(argv)
    return args


"""
Runner
"""
def runner():
    # ASN Pools
    apiEndpoint = "/api/plugins/ais/asn_pools/"
    netboxAsn(apiEndpoint)
    # VNI Pools
    apiEndpoint = "/api/plugins/ais/vni_pools/"
    netboxVni(apiEndpoint)
    # IP Pools
    apiEndpoint = "/api/plugins/ais/ip_pools/"
    netboxIp(apiEndpoint)

def main():
    arg=args()
    aosCreds, netboxCreds=yamlLoad(arg.filename)

    global AOS_IP
    global AOS_PORT
    global AOS_USER
    global AOS_PW
    global NB_TOKEN
    global NB_HOST
    global NB_PORT

    AOS_IP = aosCreds['host']
    AOS_PORT = aosCreds['port']
    AOS_USER = aosCreds['username']
    AOS_PW = aosCreds['password']
    NB_TOKEN = netboxCreds['token']
    NB_HOST = netboxCreds['hostname']
    NB_PORT = netboxCreds['port']

    global aos
    aos=aosConnection()
    count=0
    """
    Schedule
    """
    schedule.every(2).seconds.do(runner)
    while 1:
        schedule.run_pending()
        time.sleep(1)
        count +=1 
        print(f"Run {count} Complete")   

if __name__ == "__main__":
    main()