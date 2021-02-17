import requests

url="https://prod-43.eastus2.logic.azure.com:443/workflows/5c6e0f773ffe402994f370caf512eb61/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=JM6hQoYPh4Winu1WTO0_1MYgCkrwbGt4g-9ebZVTkvs"

r = requests.post(f"{url}", json={"Pipeline_trigger_time": "202102"})
r.status_code


OK_@{formatDateTime(addhours(utcnow(),-3),'yyyy')}-@{formatDateTime(addhours(utcnow(),-3),'MM')}-@{formatDateTime(addhours(utcnow(), -3),'dd')}

OK_@{formatDateTime(adddays(utcnow(),-1), 'yyyy-MM-dd')}.txt

@formatDateTime(adddays(pipeline().TriggerTime, -1), 'yyyy-MM-dd HH:mm:ss')

servicotiposku,
unidadenegocio
compraentregastatus