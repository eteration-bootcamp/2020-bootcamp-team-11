# Python Backend API

README will be updated shortly. Meanwhile, please find API endpoints below with available request types.
Apologies for no explanation and no formatting on README.

GET:
http://eteration.germanywestcentral.cloudapp.azure.com/api/job/<id>
http://eteration.germanywestcentral.cloudapp.azure.com/api/job/<id>/<param>
http://eteration.germanywestcentral.cloudapp.azure.com/api/jobs

POST:
http://eteration.germanywestcentral.cloudapp.azure.com/api/job
JSON Example: '{"name": "Senior Python Engineer", "company": "Eteration International", "description": "Good Job!", "location": "London, UK", "contract": "Full Time", "tags": "python", "new": true, "featured": true}'

PUT:
http://eteration.germanywestcentral.cloudapp.azure.com/api/job/<id>

DELETE:
http://eteration.germanywestcentral.cloudapp.azure.com/api/job/<id>
