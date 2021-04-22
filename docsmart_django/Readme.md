**DocSmart API**
----
  <_Additional information about your API call. Try to use verbs that match both request type (fetching vs modifying) and plurality (one vs multiple)._>
* **Base Url: https://docsmart.herokuapp.com/**
* **Swagger Url: https://docsmart.herokuapp.com/swagger**
* **Admin Url: https://docsmart.herokuapp.com/admin**

* Admin Email: admin@docsmart.com
* Admin Password: Admin123_

# Register:
* **URL**

  **/api/auth/register**


* **Method:**

    `POST`
  

*  **URL Params**

    **Required:**



* **Data Params**
    
           `{
          "first_name": "String",
          "last_name": "String",
          "email": "String",
          "password": "String_",
          "company_number": "String",
          "company_name": "String"
          }`
  


* **Success Response:**
  
  `Returns user email and sends an email for user to complete their registration`

  * **Code:** 201 <br />
    **Content:** 
    
              `{
              "user_object": {
                  "first_name": "string",
                  "last_name": "string",
                  "email": "string"
              },
              "company_object": {
                  "company_number": "string",
                  "company_name": "string"
              }
          }`
 

* **Error Response:**

  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 400 BAD REQUEST <br />
    **Content:** 
    
        `{
        "email": [
            "This field is required."
        ]
        }`
    
        `{
        "user_error": {
        "fieldname": [
                "error message"
            ]},
        "company_error": {
            "fieldname": [
                "error message"
            ]
        }
    }`

  OR

  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:** 
    
            `{ message : "Error message", 'status': Failed }`


* **Sample Call:**

      var axios = require('axios');
      var data = JSON.stringify({
        "first_name": "David",
        "last_name": "Lanre",
        "phone": "2348120816502",
        "email": "gbemilanre@gmail.com",
        "password": "Kaminari123_",
        "company_name": "Kaminaronn",
        "company_email": "kaminarin@gmail.com"
      });

      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/auth/complete-signup',
        headers: { 
          'Content-Type': 'application/json'
        },
        data : data
      };

      axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });


* **Notes:**

  <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> 


# Login:
* **URL**

  **api/auth/login**


* **Method:**

    `POST`
  

*  **URL Params**

    **Required:**


* **Data Params**
    
          `{
            'email':	'string'
            'password': 'string'
          }`

* **Success Response:**
  
  `Returns the user obkect along with a jwt token tombe passed in the headers for authenticated requests`

  * **Code:** 200 <br />
    **Content:** 
    
        `{
            "user": {
                "first_name": "string",
                "last_name": "string",
                "phone": "string",
                "email": "string"
            },
            "token": "Token"
        }`
    

* **Error Response:**

  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 401 Unauthorized <br />
    **Content:**
            
            `{
                "message": "Invalid credentials",
                "status": "failed"
            }`

  OR

  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:** 
    
        `{ message : "Error message" }`


* **Sample Call:**

        var axios = require('axios');
        var FormData = require('form-data');
        var data = new FormData();
        data.append('email', 'gbemilanre@gmail.com');
        
        var config = {
          method: 'post',
          url: 'http://127.0.0.1:8000/api/auth/login',
          headers: { 
            ...data.getHeaders()
          },
          data : data
        };
        
        axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data));
        })
        .catch(function (error) {
          console.log(error);
        });

* **Notes:**


# Invite User:
* **URL**

  **/api/auth/invite**


* **Method:**

    `POST`
  

*  **URL Params**

    **Required:**



* **Data Params**
  
        `{
        "email": string,
        "company_id": int
        }`


* **Success Response:**
  
  `Returns user email and sends an email for user to complete their registration`

  * **Code:** 200 <br />
    **Content:** 
    
        `{ email : string }`
 

* **Error Response:**

  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 400 BAD REQUEST <br />
    **Content:**
    
        `{
        "message": "user_id field is required and must not be empty"
        }`
    
        `{
        "field_name": [
            "This field is required."
        ]
    }`

  OR

  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:** `{ message : "Error message" , status: "failed"}`


* **Sample Call:**

      var axios = require('axios');
      var data = JSON.stringify({
        "email": "me@gmail.com",
        "user_id": 1,
        "company_id": 1
      });

      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/auth/invite',
        headers: { 
          'Content-Type': 'application/json'
        },
        data : data
      };

      axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });


* **Notes:**

  <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._>
  
# Complete User Invite:
* **URL**

  **/api/auth/complete-invite**


* **Method:**

    `POST`
  

*  **URL Params**

    **Required:**



* **Data Params**
  
        `{
        "first_name": "string",
        "last_name": "string",
        "phone": "string",
        "email": "string",
        "password": "string"
        }`


* **Success Response:**
  
  `Returns user email and sends an email for user to complete their registration`

  * **Code:** 200 <br />
    **Content:** 
    
            `{
            "first_name": "string",
            "last_name": "string",
            "phone": "string",
            "email": "string"
            }`
 

* **Error Response:**

  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 400 BAD REQUEST <br />
    **Content:**
    
        `{
        "message": "user_id field is required and must not be empty"
        }`
    
        `{
        "field_name": [
            "This field is required."
        ]
        }`

  OR

  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:** 
    
        `{ message : "Error message" , status: "failed"}`


* **Sample Call:**

      var axios = require('axios');
      var data = JSON.stringify({
        "first_name": "David",
        "last_name": "Lanre",
        "phone": "2348120816502",
        "email": "me@gmail.com",
        "password": "Kaminari123_"
      });

      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/auth/complete-invite',
        headers: { 
          'Content-Type': 'application/json'
        },
        data : data
      };

      axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });



* **Notes:**

  <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._>
 
 
# Create Document:
* **URL**

  **/api/documents/create-document**


* **Method:**

    `POST`
  

*  **Header Params**

    **Required: [Bearer Token]**



* **Data Params**
  
    `{
    "name": "string| Name of document",
    "path": "string| Path to document folder",
    "company_id": "Int|Document ID",
    "created_by": "Int | User ID",
    "last_edited_by": "Int | User ID"
    }`


* **Success Response:**
  
  `Returns user email and sends an email for user to complete their registration`

  * **Code:** 200 <br />
    **Content:**
    
    `{
    "message": "Document created successfully"
    }`
 

* **Error Response:**

  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 400 BAD REQUEST <br />
    **Content:**
    
          `{
          "message": "user_id field is required and must not be empty"
          }`
    
          `{
          "field_name": [
              "This field is required."
          ]
          }`

  OR

  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:** `{ message : "Error message" , status: "failed"}`


* **Sample Call:**

      var axios = require('axios');
      var data = JSON.stringify({
        "name": "Document",
        "path": "/home/user/path",
        "company_id": 1,
        "created_by": 1,
        "last_edited_by": 1
      });

      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/documents/create-document',
        headers: { 
          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImxhbnJlQGdtYWlsLmNvbSJ9.bk6UAItDwJIFqsWT6MCaOrocKrNKbMVs9b6a4Xwgqj8', 
          'Content-Type': 'application/json'
        },
        data : data
      };

      axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });




* **Notes:**

  <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> 


# Fetch User Document:
* **URL**

  **/api/documents/fetch-user-documents**


* **Method:**

    `POST`
  

*  **Header Params**

    **Required: [Bearer Token]**



* **Data Params**



* **Success Response:**


  * **Code:** 200 <br />
    **Content:**
    
        `[
        {
            "id": 15,
            "name": "docsmart1.1.pdf",
            "path": "/home/user/path",
            "date_last_edited": "2021-04-02T17:14:12.783777Z",
            "created_at": "2021-04-02T17:14:12.783777Z",
            "updated_at": "2021-04-02T17:14:12.783777Z",
            "permissions": [
                {
                    "id": 8,
                    "can_view": true,
                    "can_edit": false,
                    "can_delete": false,
                    "document_id": 15,
                    "user_id": 1
                }
            ]
        },
        {
            "id": 19,
            "name": "document",
            "path": "/home/user/path",
            "date_last_edited": "2021-04-11T21:24:01.949112Z",
            "created_at": "2021-04-11T21:24:01.949112Z",
            "updated_at": "2021-04-11T21:24:01.949112Z",
            "permissions": [
                {
                    "id": 12,
                    "can_view": true,
                    "can_edit": false,
                    "can_delete": false,
                    "document_id": 19,
                    "user_id": 1
                }
            ]
        }
    ]`
 

* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:**
    
        `{
        "message": "user_id field is required and must not be empty"
        }`
    
        `{
        "field_name": [
            "This field is required."
        ]
        }`

  OR

  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:**
    
          `{ message : "Error message" , status: "failed"}`
    


* **Sample Call:**

      var axios = require('axios');
      var data = JSON.stringify({
        "name": "Document",
        "path": "/home/user/path",
        "company_id": 1,
        "created_by": 1,
        "last_edited_by": 1
      });

      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/documents/create-document',
        headers: { 
          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImxhbnJlQGdtYWlsLmNvbSJ9.bk6UAItDwJIFqsWT6MCaOrocKrNKbMVs9b6a4Xwgqj8', 
          'Content-Type': 'application/json'
        },
        data : data
      };

      axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });


* **Notes:**

  <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> 


# Fetch FAQ:
* **URL**

  **api/auth/login**


* **Method:**

    `GET`
  

*  **URL Params**

    **Required:**


* **Data Params**

* **Success Response:**
  
  `Returns a collections of FAQs`

  * **Code:** 200 <br />
    **Content:** 
    
                [
                  {
                "subject": "Testing Faq",
                "category": "Payment",
                "content": "This is a test",
                "created_at": "2021-04-22T12:20:53.476824Z",
                "updated_at": "2021-04-22T12:20:53.476824Z"
                  }
                ]
    

* **Error Response:**

  * **Code:** 200 success <br />
    **Content:**
            
            `{
                "message": "No FAQs",
                "status": "success"
            }`

  OR

  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:** 
    
        `{ message : "Error message" }`


* **Sample Call:**

        var axios = require('axios');
        var FormData = require('form-data');
        var data = new FormData();
        data.append('email', 'gbemilanre@gmail.com');
        
        var config = {
          method: 'post',
          url: 'http://127.0.0.1:8000/api/auth/login',
          headers: { 
            ...data.getHeaders()
          },
          data : data
        };
        
        axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data));
        })
        .catch(function (error) {
          console.log(error);
        });

* **Notes:**

# Fetch User Document:
* **URL**

  **/api/documents/fetch-user-documents**


* **Method:**

    `POST`
  

*  **Header Params**

    **Required: [Bearer Token]**



* **Data Params**



* **Success Response:**


  * **Code:** 200 <br />
    **Content:**
    
        `[
        {
            "id": 15,
            "name": "docsmart1.1.pdf",
            "path": "/home/user/path",
            "date_last_edited": "2021-04-02T17:14:12.783777Z",
            "created_at": "2021-04-02T17:14:12.783777Z",
            "updated_at": "2021-04-02T17:14:12.783777Z",
            "permissions": [
                {
                    "id": 8,
                    "can_view": true,
                    "can_edit": false,
                    "can_delete": false,
                    "document_id": 15,
                    "user_id": 1
                }
            ]
        },
        {
            "id": 19,
            "name": "document",
            "path": "/home/user/path",
            "date_last_edited": "2021-04-11T21:24:01.949112Z",
            "created_at": "2021-04-11T21:24:01.949112Z",
            "updated_at": "2021-04-11T21:24:01.949112Z",
            "permissions": [
                {
                    "id": 12,
                    "can_view": true,
                    "can_edit": false,
                    "can_delete": false,
                    "document_id": 19,
                    "user_id": 1
                }
            ]
        }
    ]`
 

* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:**
    
        `{
        "message": "user_id field is required and must not be empty"
        }`
    
        `{
        "field_name": [
            "This field is required."
        ]
        }`

  OR

  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:**
    
          `{ message : "Error message" , status: "failed"}`
    


* **Sample Call:**

      var axios = require('axios');
      var data = JSON.stringify({
        "name": "Document",
        "path": "/home/user/path",
        "company_id": 1,
        "created_by": 1,
        "last_edited_by": 1
      });

      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/documents/create-document',
        headers: { 
          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImxhbnJlQGdtYWlsLmNvbSJ9.bk6UAItDwJIFqsWT6MCaOrocKrNKbMVs9b6a4Xwgqj8', 
          'Content-Type': 'application/json'
        },
        data : data
      };

      axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });




* **Notes:**

  <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> 


# Fetch User Folder:
* **URL**

  **/api/documents/fetch-user-folder-structure-with-perm**


* **Method:**

    `POST`
  

*  **Header Params**

    **Required: [Bearer Token]**



* **Data Params**



* **Success Response:**


  * **Code:** 200 <br />
    **Content:**
    
        `{
            "name": "user_1",
            "items": [],
            "type": "file"
        }`
 

* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:**
    
        `{
        "message": "user_id field is required and must not be empty"
        }`
    
        `{
        "field_name": [
            "This field is required."
        ]
        }`

  OR

  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:**
    
          `{ message : "Error message" , status: "failed"}`
    


* **Sample Call:**

      var axios = require('axios');

      var config = {
        method: 'get',
        url: 'http://127.0.0.1:8000/api/documents/fetch-user-folder-structure-with-perm',
        headers: { 
          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImxhbnJlQGdtYWlsLmNvbSJ9.bk6UAItDwJIFqsWT6MCaOrocKrNKbMVs9b6a4Xwgqj8'
        }
      };
      
      axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });


* **Notes:**
