import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
	files = {
			"file": ("data.json", json_data)
	}
	# Infura's IPFS API endpoint
	ipfs_api_url = "https://ipfs.infura.io:5001/api/v0/add"
	response = requests.post(ipfs_api_url, files=files, auth=(project_id, project_secret))
	response.raise_for_status()
	
	result = response.json()
	cid = result.get("Hash")
	if not cid:
			raise ValueError("Failed to obtain CID from IPFS response")
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://ipfs.io/ipfs/{cid}"
	response = requests.get(url)
	response.raise_for_status()
	if content_type == "json":
			data = response.json()
	else:
			raise ValueError("Unsupported content_type. Only 'json' is supported in this implementation.")
    

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
