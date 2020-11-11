# Contacts App with Django-Backend
A backend developed to mimic a contacts application. It supports addition of multiple email fields, address fields, and phone numbers. 

# A screenshot of the view at http://localhost:8000/api/contacts/
![Optional Text](../main/img1.png)

# A sample post request to the api at http://localhost:8000/api/contacts/add
              {
                  "first_name":"John",
                  "last_name":"Smith",
                  "company": null,
                  "notes":"Some notes that are needed to be written",
                  "email":[
                      {
                          "email":"john@gmail.com"
                      },{
                          "email":"john@work.com"
                      }
                  ],
                  "phone":[{
                      "number":"123456789"},
                      {"number":"987655421"}
                      ],
                  "social_media":[{"url":"https://www.instagram.com"}],
                  "address":[
                      {
                          "street":"1 Avenue",
                          "street_detal":"Floor1",
                          "city":"New York City",
                          "country":"United States"
                      }
                  ]
              }
              
 ![Optional Text](../main/img2.png)
 
 
 # To retrieve the details of any contact visit: http://localhost:8000/api/contacts/ID
  
  ![Optional Text](../main/img3.png)
  
              
