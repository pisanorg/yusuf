# GET Partners RESTful API for the Partner Integration Platform

## Rithik Bansal

The main aim of the project was to create an Application Programming Interface (API) which followed the Representational State Tranfer (REST) architecture as its groundwork. The endpoint being used was the HTTP “GET” endpoint. The GET Partners API provides the ability to get information for a collection of partner resources using the ISO country code of the market where they work and a combination of query parameters. There was a total of 15 query parameters which the consumer could use in any possible combination. The result included the information of all the employees who fulfilled all the criteria passed in the request by the consumer. The request URL used by the users looked like as follows:

  https://serviceEndpoint/partners?<params>
  where <params> are passed in the following format: /partners?lastName={value}&partnerId={value}....

The first step was to validate the consumer through the JWT (JSON Web Token) which came as part of the request to ensure that the consumer is an authorized user. The step was critical to prevent personal identifiable information falling into the hands of a malicious user. Second step was to validate each passed in query parameter and its respective values for data consistency and sanity. Lastly, the query built was used to retrieve the information from the NoSQL database hosted via Cosmos DB offering of Azure Cloud.

The cases where the consumer calls the API with “illegal” data and values, the API would then return a meaningful message to the user which would guide them to rectify the error in their request. The message would be returned in conjunction with its respective Http status code where 200 being for successful requests and 400 status codes being for client-side error.

Testing was performed using the Junit testing library for unit testing and integration testing. As a developer, we aim for our unit testing to have 95% code coverage. We also incorporated the use of logging libraries to help pinpoint the error if it occurs and be used to monitor application health. The API was successfully built over the internship duration with above par performance and efficiency.
