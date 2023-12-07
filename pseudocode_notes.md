# RANDOM NOTES + PSEUDOCODE

## schemas
- need to make for each set of schemas
    - base model type
    - create
    - update


## controllers
- handle the business logic of your application
    - use a controller to handle crud operations
    - make a controller for every 'action' / 'table'?


## Wednesday 12/6
### TODO: BACKEND
- order of operations to follow...
    - [ ] base schema
    - [ ] create schema
    - [ ] update schema
    - [ ] endpoint
    - [ ] add to schema init file
    - [ ] add router to api file


## Thursday 12/7
### TODO: BACKEND
#### PRIORITY USER STORY - USER, BUSINESS, DRINK,
- [x] change in all models from str to DateTime
- [ ] run alembic to update models in db
- [x] create schemas for the rest of models
    - [x] badge
    - [x] business
    - [x] collection_tracker
    - [x] drink
    - [x] msg
    - [x] review
        - in the review schema there are foreign keys?
            - do these need to be written in differently?
            - also foreign key - user id in collection
            - also foreign key - business  id in drink
    - [x] tag
    - [x] token
    - [x] user

- [ ] update alembic
- [ ] adjust relationships
- [ ] create rest of crud in controllers
- [ ] check/create endpoints

#### TO CHECK:
- [ ] check on foreign keys in schemas
- [ ] check on foreign key in controllers
    - drink controller
- [ ] check relationships between related models - (PRIORITY - mapped lists etc)
    - ex - business and tag
- [ ] check relationships within related schemas
    - ex - business
- [ ] check in collection model
    - is it many drinks to a collection? OR many drinks to many collections?

#### CRUD SO FAR (within controllers):
##### PRIORITY USER STORY - USER, BUSINESS, DRINK
##### SECOND PRIORITY - COLLECTION
##### (crud checklist listed in order of priority)
- [ ] user
    - [x] create - post
    - [x] read - get
    - [x] update - put
    - [ ] delete - delete
- [ ] business
    - [x] create - post
    - [x] read - get
    - [ ] update - put
    - [ ] delete - delete
- [ ] drink
    - [x] create - post
    - [x] read - get
    - [ ] update - put
    - [ ] delete - delete
- [ ] collection_tracker
    - [ ] create - post
    - [ ] read - get
    - [ ] update - put
    - [ ] delete - delete
- [ ] tag
    - [ ] create - post
    - [ ] read - get
    - [ ] update - put
    - [ ] delete - delete
- [ ] badge
    - [ ] create - post
    - [ ] read - get
    - [ ] update - put
    - [ ] delete - delete
- [ ] review
    - [ ] create - post
    - [ ] read - get
    - [ ] update - put
    - [ ] delete - delete

#### Business Model
- parent - Business
    - relationships:
        - [x] (tags - business) : many tags to a business
            - [x] check in Tag model
                - (businesses - tag) : many businesses to a tag

        - [x] (reviews - business) : many reviews to a business
            - [ ] check in Review model

        - [x] (drinks - business) : many drinks to a business
            - [ ] check in Drink model

- child - BusinessTag
    - relationships:
        - [x] (business - tags) : a business has many tags
        - [x] (tag - businesses) : a tag has many businesses

#### Drink Model
- parent - Drink
    - relationships:
        - [x] (collection_trackers - drink) : many collections have the same specific drink
            - [x] check in Collection model
                - (drink - collection_trackers) : a specific drink is in many collections

        - [x] (business - drinks) : a business has many drinks
            - [x] check in Business model (parent)
                - (drinks - business) : many drinks to a business

#### Collection_tracker Model
- parent - Collection
    - relationships:
        - [x] (drinks - collection_tracker) : many drinks to a collection
            - [ ] check in Drink model
                - () :

        - [ ] (badges - collection_tracker) : many badges to a collection
            - [ ] check in Badge model (parent)
                - () :

        - [ ] (user - collection_tracker) : a user has many collections
            - [ ] check in User model (parent)
                - () :

- child - CollectionTrackerDrink
    - relationships:
        - [ ] () :
        - [ ] () :


- child - CollectionTrackerBadge
    - relationships:
        - [ ] () :
        - [ ] () :

##### example relationships written in models
- use list when there are "starts many" relationships
    - with list:
        reviews = relationship(list("Review"), back_populates="business")
            drinks = relationship(list("Drink"), back_populates="business")

    - no list:
        business = relationship("Business", back_populates="tags")
        tag = relationship("Tag", back_populates="businesses")
