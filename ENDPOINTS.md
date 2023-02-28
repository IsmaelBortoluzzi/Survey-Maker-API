## Table Of Endpoints

- [Authentication](#authentication)
- [City](#city)
- [Contact](#contact)
- [Survey](#survey)
- [Survey To Respond](#survey-to-respond)
- [Survey Question](#survey-question)
- [Survey Question Choice](#survey-question-choice)


## Authentication

<br>

#### get token

URL:
    
    api/v1/token/

JSON:

    {
        "username": "YOUR USERNAME",
        "password": "YOUR PASSWORD"
    }

METHOD:
    
    POST

<br>

#### refresh

URL:
    
    api/v1/token/refresh/

JSON:

    {
        "refresh": "YOUR REFRESH TOKEN"
    }

METHOD:
    
    POST
<br>

## City
<br>

#### get cities

URL:
    
    api/v1/city/?city=QUERY FOR CITY'S NAME

METHOD:
    
    GET
<br>

#### get one city

URL:
    
    api/v1/city/ID OF THE CITY (IT'S AN INTEGER NUMBER)

METHOD:
    
    GET
<br>

## Contact
<br>

#### get one contact

URL:
    
    api/v1/contact/ID OF THE CONTACT (IT'S AN INTEGER NUMBER)

METHOD:
    
    GET
<br>

#### get all contacts (only superusers)

URL:
    
    api/v1/contact/

METHOD:
    
    GET
<br>

#### create contact

URL:
    
    api/v1/contact/

JSON:

    {
        "first_name": "FIRST NAME",
        "last_name": "LAST NAME",
        "password": "PASSWORD",
        "username": "A CHOSEN USERNAME (MUST BE UNIQUE)",
        "email": "EMAIL",
        "city_id": ID OF THE CITY,
        "gender": "masculine/feminine",
        "birthday": "YYYY-MM-DD"
    }

METHOD:
    
    POST
<br>

## Survey

<br>

#### get all surveys

URL:
    
    api/v1/survey/

METHOD:
    
    GET
<br>

#### get one survey

URL:
    
    api/v1/survey/SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/

METHOD:
    
    GET
<br>

#### get one survey

URL:
    
    api/v1/survey/

JSON:

    {
        "valid_until": "YYYY-MM-DD HH:mm:ss",
        "survey_model": {
            "date_responded": "YYYY-MM-DD HH:mm:ss",
            "respondent": ID OF THE CONTACT WHO RESPONDED (IN THIS CASE, THE AUTHOR),
            "questions": [
                {
                    "name": "QUESTION NAME",
                    "question_type": "descriptive",
                    "written_answer": "",
                    "answer_choices": []
                },
                {
                    "name": "QUESTION NAME",
                    "question_type": "mutually_exclusive",
                    "written_answer": "",
                    "answer_choices": [
                        {
                            "text": "CHOICE ONE",
                            "chosen": false
                        },
                        {
                            "text": "CHOICE TWO",
                            "chosen": false
                        },
                        {
                            "text": "CHOICE THREE",
                            "chosen": false
                        }
                    ]
                },
                {
                    "name": "QUESTION NAME",
                    "question_type": "multiple_choice",
                    "written_answer": "",
                    "answer_choices": [
                        {
                            "text": "CHOICE ONE",
                            "chosen": false
                        },
                        {
                            "text": "CHOICE TWO",
                            "chosen": false
                        },
                        {
                            "text": "CHOICE THREE",
                            "chosen": false
                        },
                        {
                            "text": "CHOICE FOUR",
                            "chosen": false
                        },
                        {
                            "text": "CHOICE FIVE",
                            "chosen": false
                        }
                    ]
                }
            ]
        },
        "title": "SURVEY TITLE"
    }

METHOD:
    
    POST
<br>

#### delete one survey

URL:
    
    api/v1/survey/SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/

METHOD:
    
    DELETE
<br>

#### update title

URL:
    
    api/v1/survey/SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/

JSON:

    {
        "title": "NEW TITLE"
    }

METHOD:
    
    PATCH
<br>


## Survey To Respond

<br>

#### get surveys to respond

URL:
    
    api/v1/survey-to-respond/?survey=SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)

METHOD:
    
    GET
<br>

#### get one surveys to respond

URL:
    
    api/v1/survey-to-respond/RESPONDED SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/

METHOD:
    
    GET
<br>

#### post survey to respond

URL:
    
    api/v1/survey-to-respond/

JSON:

    {
        "date_responded": "YYYY-MM-DD HH:mm:ss",
        "survey": "SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)",
        "respondent": ID OF THE PERSON WHO RESPONDED,
        "questions": [
            {
                "name": "QUESTION NAME",
                "question_type": "descriptive",
                "written_answer": "ANSWER",
                "answer_choices": []
            },
            {
                "name": "QUESTION NAME",
                "question_type": "mutually_exclusive",
                "written_answer": "",
                "answer_choices": [
                    {
                        "text": "CHOICE ONE",
                        "chosen": T/F
                    },
                    {
                        "text": "CHOICE TWO",
                        "chosen": T/F
                    },
                    {
                        "text": "CHOICE THREE",
                        "chosen": T/F
                    }
                ]
            },
            {
                "name": "QUESTION NAME",
                "question_type": "multiple_choice",
                "written_answer": "",
                "answer_choices": [
                    {
                        "text": "CHOICE ONE",
                        "chosen": T/F
                    },
                    {
                        "text": "CHOICE TWO",
                        "chosen": T/F
                    },
                    {
                        "text": "CHOICE THREE",
                        "chosen": T/F
                    },
                    {
                        "text": "CHOICE FOUR",
                        "chosen": T/F
                    },
                    {
                        "text": "CHOICE FIVE",
                        "chosen": T/F
                    }
                ]
            }
        ]
    }

METHOD:
    
    POST
<br>

#### delete one survey

URL:
    
    api/v1/survey-to-respond/RESPONDED SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/

METHOD:
    
    DELETE
<br>


## Survey Question

<br>

##### add question

URL:
    
    api/v1/survey-to-respond/add-del-question/SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/

JSON:

    {
        "name": "NEW QUESTION NAME",
        "question_type": "ONE OF THE 3 CHOICES ('descriptive', 'multiple_choice', 'mutually_exclusive')",
        "written_answer": "",
        "answer_choices": [
            {
                "text": "CHOICE ONE",
                "chosen": T/F
            },
            {
                "text": "CHOICE TWO",
                "chosen": T/F
            },
            {
                "text": "CHOICE THREE",
                "chosen": T/F
            }
        ]
    }

METHOD:
    
    POST
<br>

#### update question name

URL:
    
    api/v1/survey-to-respond/add-del-question/SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/?current_name=EXACT QUESTION NAME/

JSON:

    {
        "name": "NEW NAME"
    }

METHOD:
    
    PATCH
<br>

#### update question name

URL:
    
    api/v1/survey-to-respond/add-del-question/SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/?name=EXACT QUESTION NAME/

METHOD:
    
    DELETE
<br>


## Survey Question Choice

<br>

#### add question choice

URL:
    
    api/v1/survey-to-respond/add-del-question-choice/SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/

JSON:

    {
        "question_name": "QUESTION NAME",
        "text": "NEW TEXT CHOICE OF THE NEW CHOICE"
    }

METHOD:
    
    POST
<br>

#### update question choice

URL:
    
    api/v1/survey-to-respond/add-del-question-choice/SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/

JSON:

    {
        "question_name": "QUESTION NAME",
        "text": "NEW TEXT CHOICE OF THE CHOICE",
        "old_text": "CURRENT TEXT OF THE CHOICE"
    }

METHOD:
    
    PATCH
<br>


#### delete question choice

URL:
    
    api/v1/survey-to-respond/add-del-question-choice/SURVEY ID (STRING REPRESENTING THE OBJECT ID IN MONGODB)/

JSON:

    {
        "question_name": "QUESTION NAME",
        "text": "EXACT TEXT OF CHOICE TO BE DELETED"
    }

METHOD:
    
    DELETE
<br>
