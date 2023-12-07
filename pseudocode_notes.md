# schemas
- need to make for each set of schemas
    - base model type
    - create
    - update


# controllers
- handle the business logic of your application
    - use a controller to handle crud operations
    - make a controller for every 'action' / 'table'?


'''
TODO:
- base schema
- create schema
- update schema
- endpoint
- add to schema init file
- add router to api file
'''

# Thursday 12/7
# TODO:
- [x] change in all models from str to DateTime
- [ ] run alembic to update models in db
- [ ] create schemas for the rest of models
    - [x] badge
    - [x] business
    - [x] collection_tracker
    - [x] drink
    - [x] msg
    - [x] review
        - in the review schema there are foreign keys?
            - do these need to be written in differently?
    - [ ] tag
    - [x] token
    - [x] user

- [ ] update alembic
- [ ] adjust relationships
- [ ] create rest of crud in controllers
