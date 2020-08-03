# Java Spring Boot API

This micro-framework serves an API endpoint for Job Posting Application. It stores job postings in PostgreSQL database. It is based on Java Spring Boot for HTTP and postgresql for RDM ORM. Maven built is used for production development with NGINX Reverse Proxy.

## Active API Endpoint
###### Below HTTP API endpoint is active and working with load balanced with round robin with Python Application and Java Spring Application.
```http
http://eteration.germanywestcentral.cloudapp.azure.com/api
```

## Installation & Local Usage
###### JDK 8 and Maven is required. 
```python
# Build with Maven
mvn clean install 

# Start project (JAR build with Maven is already executable)
target/jobsapi.jar
```

## API Endpoints Documentation
###### POST request for new job posting.
```
Below key values in JSON must sent over body part of the JSON.
jobName, jobCompany, JobDescription, jobLocation, jobContract, jobTags, jobNew, jobFeatured
```
```python
POST /api/job
```

###### GET request for single Job by ID
```python
GET /api/job/<jobid> # Get All Parameters
GET /api/job/<jobid>/<param> # Get Single Paramater
```

###### GET request for all jobs
```python
GET /api/jobs
```

###### PUT request for updating single Job by ID
```python
PUT /api/job/<jobid> # All JSON keys inside of BODY request will be updated.
```

###### DELETE request for deleting single Job by ID
```python
DELETE /api/job/<jobid>
```

## Example Responses:
```javascript
"POST http://eteration.germanywestcentral.cloudapp.azure.com/api/job"
Body of Request:
{
   "jobName":"Senior Python Engineer",
   "jobCompany":"Eteration Turkey",
   "jobDescription":"Good Job!",
   "jobLocation":"Istanbul, Turkey",
   "jobContract":"Full Time",
   "jobTags":"python",
   "jobNew":true,
   "jobFeatured":true,
}
```

```javascript
"GET http://eteration.germanywestcentral.cloudapp.azure.com/api/job/1"
Response:
{
   "id":1,
   "jobName":"Junior Python Engineer",
   "jobCompany":"Eteration Turkey",
   "jobDescription":"Good Job!",
   "jobLocation":"Istanbul, Turkey",
   "jobContract":"Full Time",
   "jobTags":"python",
   "jobNew":true,
   "jobFeatured":true,
   "jobDate":"2020-08-02 12:33:13"
}
```

```javascript
"PUT http://eteration.germanywestcentral.cloudapp.azure.com/api/job/1"
Body of Request:
{
   "id":1,
   "jobName":"Senior Python Engineer",
}
```

```javascript
"DELETE http://eteration.germanywestcentral.cloudapp.azure.com/api/job/1"
Body of Request:
{
   "id":1,
   "jobName":"Senior Python Engineer",
}
```

### Status Codes
| Status Code | Description | JSON Value
| :--- | :--- | :--- |
| 200 | `OK` | {"status": 200}|
| 404 | `Not Found` | {"status": 404}|

