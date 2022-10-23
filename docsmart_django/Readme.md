

## API Reference

#### Onboarding

```http
  POST /api/auth/register
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `first_name` | `string` | **Required**. |
| `last_name` | `string` | **Required**.  |
| `email` | `string` | **Required**.  |
| `password` | `string` | **Required**. |
| `company_number` | `string` | **Required**. |
| `company_name` | `string` | **Required**. |

## Usage/Examples

```javascript
var axios = require('axios');
var data = JSON.stringify({
  "first_name": "Gbemi",
  "last_name": "David",
  "email": "gbemilanre@gmail.com",
  "password": "Olubukola123_",
  "company_number": "76987123445624",
  "company_name": "Kaminario"
});

var config = {
  method: 'post',
  url: 'https://docsmart.herokuapp.com/api/auth/register',
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
```
#### Responses

```json
{
    "user_object": {
        "first_name": "string",
        "last_name": "string",
        "email": "string"
    },
    "company_object": {
        "company_number": "string",
        "company_name": "string"
    }
}
```


#### Login

```http
  POST /api/auth/login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. |
| `password` | `string` | **Required**.  |


## Usage/Examples

```javascript
var axios = require('axios');
var FormData = require('form-data');
var data = new FormData();
data.append('email', 'gbemilanre@gmail.com');
data.append('password', 'Olubukola123_');

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
```
#### Responses

```json
{
    "user": {
        "first_name": "Gbemi",
        "last_name": "David",
        "email": "gbemilanre@gmail.com"
    },
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImdiZW1pbGFucmVAZ21haWwuY29tIn0.kNWvIwVbZQsEISj3hMcgKF11COdyhXO4niZJZDE_JG4"
}
```

#### Invite

```http
  POST /api/auth/invite
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. |
| `company_id` | `string` | **Required**. Company Id|
| `user_id` | `int` | **Required**. Users Id|


## Usage/Examples

```javascript
var axios = require('axios');
var data = JSON.stringify({
  "email": "gbemi@gmail.com",
  "company_id": 2,
  "user_id": 2
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

```
#### Responses

```json
{ 
  "email" : "string" 
}
```

#### Complete Invite

```http
  POST /api/auth/complete-invite
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `first_name` | `string` | **Required**. |
| `last_name` | `string` | **Required**.  |
| `email` | `string` | **Required**.  |
| `password` | `string` | **Required**. |
| `phone` | `string` | **Required**. |

## Usage/Examples

```javascript
var axios = require('axios');
var data = JSON.stringify({
  "first_name": "David",
  "last_name": "Lanre",
  "phone": "8120897603",
  "email": "gbemi@gmail.com",
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
```
#### Responses

```json
{
  "first_name": "string",
  "last_name": "string",
  "phone": "string",
  "email": "string"
}
```

#### Create Documents

```http
  POST api/documents/create-document
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `first_name` | `string` | **Required**. |
| `last_name` | `string` | **Required**.  |
| `email` | `string` | **Required**.  |
| `password` | `string` | **Required**. |
| `phone` | `string` | **Required**. |

## Usage/Examples

```javascript
var axios = require('axios');
var data = JSON.stringify({
  "first_name": "David",
  "last_name": "Lanre",
  "phone": "8120897603",
  "email": "gbemi@gmail.com",
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
```
#### Responses

```json
{
  "first_name": "string",
  "last_name": "string",
  "phone": "string",
  "email": "string"
}
```

#### Fetch User Documents

```http
  GET /api/documents/fetch-user-documents
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `string` | **Required**. Bearer Auth In header|


## Usage/Examples

```javascript
var axios = require('axios');

var config = {
  method: 'get',
  url: 'http://127.0.0.1:8000/api/documents/fetch-user-documents',
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
```
#### Responses

```json
{
  [
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
    ]
}
```

#### Fetch Documents Documents

```http
  GET /api/documents/fetch-company-folder-structure-with-perm
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `string` | **Required**. Bearer Auth In header|


## Usage/Examples

```javascript
var axios = require('axios');

var config = {
  method: 'get',
  url: 'http://127.0.0.1:8000/api/documents/fetch-company-folder-structure-with-perm',
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
```
#### Responses

```json
{
  [
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
    ]
}
```

#### Delete User Document

```http
  GET /api/documents/delete-document
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `string` | **Required**. Bearer Auth In header|
| `document_id` | `int` | **Required**. Document ID|


## Usage/Examples

```javascript
var axios = require('axios');
var FormData = require('form-data');
var data = new FormData();
data.append('document_id', '11');

var config = {
  method: 'post',
  url: 'http://127.0.0.1:8000/api/documents/delete-document',
  headers: { 
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImxhbnJlQGdtYWlsLmNvbSJ9.bk6UAItDwJIFqsWT6MCaOrocKrNKbMVs9b6a4Xwgqj8', 
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
```
#### Responses

```json
{
  "message": "We're unable to delete this document"
}
```

#### Delete Company Document

```http
  GET /api/documents/delete-company-document
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `string` | **Required**. Bearer Auth In header|
| `document_id` | `int` | **Required**. Document ID|


## Usage/Examples

```javascript
var axios = require('axios');
var FormData = require('form-data');
var data = new FormData();
data.append('document_id', '8');

var config = {
  method: 'post',
  url: 'http://127.0.0.1:8000/api/documents/delete-company-document',
  headers: { 
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImxhbnJlQGdtYWlsLmNvbSJ9.bk6UAItDwJIFqsWT6MCaOrocKrNKbMVs9b6a4Xwgqj8', 
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
```
#### Responses

```json
{
  "message": "Document deleted successfully"
}
```

#### Create User Folder

```http
  POST api/documents/create-single-user-folder
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `string` | **Required**. Bearer Auth In header|
| `folder_name` | `string` | **Required**. Name of folder|
| `current_path` | `string` | **Required**. Current path user is in|


## Usage/Examples

```javascript
var axios = require('axios');
var FormData = require('form-data');
var data = new FormData();
data.append('folder_name', 'bills');
data.append('current_path', 'legal/');

var config = {
  method: 'post',
  url: 'http://127.0.0.1:8000/api/documents/create-single-user-folder',
  headers: { 
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImxhbnJlQGdtYWlsLmNvbSJ9.bk6UAItDwJIFqsWT6MCaOrocKrNKbMVs9b6a4Xwgqj8', 
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

```
#### Responses

```json
{
  [folder Object]
}
```

#### Create User Folder

```http
  GET /api/documents/fetch-user-folder-structure-with-perm
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `string` | **Required**. Bearer Auth In header|

## Usage/Examples

```javascript
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

```
#### Responses

```json
{
  [folder Object]
}
```

#### Create User Folder

```http
  GET /api/documents/fetch-user-folder-structure-with-perm
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Bearer Token` | `string` | **Required**. Bearer Auth In header|

## Usage/Examples

```javascript
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

```
#### Responses

```json
{
  [folder Object]
}
```


  




















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
