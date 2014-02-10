Deployment
==========

Here is how to deploy the health engine to Heroku.

Prerequisites
-------------

- Get [Heroku Toolbelt](https://toolbelt.heroku.com/)
    
Commands
--------

    cd /path/to/health-engine
    heroku login
    git remote add heroku git@heroku.com:health-engine.git
    git push heroku master
    heroku config:set ENVIRONMENT=production
    
    