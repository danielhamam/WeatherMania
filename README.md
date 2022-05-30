# WeatherMania

## Setup

Tools you will need:
* python3  

### Development

The `Makefile` encapsulates helpful commands...make sure to install `make` to use it.

```

# --------------------------------------------------------------------------------
#                       STEP-BY-STEP DEVELOPMENT SET-UP
# --------------------------------------------------------------------------------

# (1) - Install Python Virtual Environment / Application dependencies
make setup

# (2) Run development server
make dev

# (3) Initialize SQLite Database w/ Schema via Alembic (updates to latest db schema)
make init

# Access the server at http://127.0.0.1:5000. 
```
```
# --------------------------------------------------------------------------------
#                       HOW TO MAKE DATABASE CHANGES
# --------------------------------------------------------------------------------

-> When you run 'make init', it's using alembic to apply database migrations
-> Pull latest code and 'make init' to update to latest schema the code requires
-> Steps to make changes:
    1. Update models.py with your desired change (like a new attribute to a table)
    2. Run alembic revision --autogenerate -m "enter description of new change"
    -- Migration is now ready, now we need to apply the migration to the database --
    3. Execute 'make init'
    4. Locate the newly generated file in alembic/versions/*.py
```