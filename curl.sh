url = "https://prod-51.eastus2.logic.azure.com:443/workflows/c02771baa06e4b2699496f9bb1bdb8f7/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=y-wDPDrNMmrgSpMnO41uYU1dHyCaA6RcNbTMdTlBO0M"


curl -X POST $url


curl -H "Content-Type: application/json" -X POST $url

curl -H "Content-Type: application/json" -X POST https://prod-51.eastus2.logic.azure.com:443/workflows/c02771baa06e4b2699496f9bb1bdb8f7/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=y-wDPDrNMmrgSpMnO41uYU1dHyCaA6RcNbTMdTlBO0M


curl -H "Content-Type: application/json" -X POST -d '{"username":"mkyong","password":"abc"}' $url
