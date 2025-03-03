import schedule
import time
import subprocess

def restart_cfpyapi():
    
    try:
        # Restart Command Function
        subprocess.run(['cf', 'restart', 'cfpyapi'], check=True)
        print("Success")
        return True
    except Exception as error:
        print(f"Restart failed: {error}")
        return False
    
    # Restart job is daily at 9:00 AM ET
    schedule.every().day.at("09:00").do(restart_cfpyapi)
    
    #Startup Message (For troubleshooting purposes)
    print("Schduler started")
    
    #Get time and run job (CF server is on us-east-1)
    while True:
        schedule.run_pending()
        current_hour = time.localtime().tm_hour
        
        #Check closer to designated restart time
        if current_hour == 8 or current_hour == 9:
            # Check every 5 mins around target time 
            time.sleep(5 * 60)
        else:
            # Check hourly
            time.sleep(60 * 60)