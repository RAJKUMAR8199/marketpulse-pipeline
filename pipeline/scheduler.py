from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', hours=6)
def run_pipeline():

    print("Running scraper...")

    subprocess.run(["python", "scraper/scraper.py"])

    print("Running cleaning pipeline...")

    subprocess.run(["python", "cleaning/clean.py"])

    print("Pipeline executed successfully")

print("Scheduler started...")

scheduler.start()