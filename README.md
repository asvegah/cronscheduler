## Instructions to run this code:
#### From zip file:
* Unzip file
* `cd` into `cronscheduler`  
* run `chmod +x scheduler.py`
* run the code using an input like: `./application.py HH:MM < config`
    * Eg: `​./scheduler.py 16:10 < config`
    * HH:MM is the simulated 'current time'
    * `< config` is the standard input file

#### Cloning from Github:

* Clone or dowload the repo
* `cd` into `get-next-cron-schedule`  
* run `chmod +x application.py`
* run the code using an input like: `./application.py HH:MM < config`
    * Eg: `​./application.py 16:10 < config`
    * HH:MM is the simulated 'current time'
    * `< config` is the standard input file


## Potential Improvements:

* Make the code work for a full cron schedule.
* Create automated tests
* Refactor main logic in `calculate_difference()`    