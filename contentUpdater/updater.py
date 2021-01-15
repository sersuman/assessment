from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from contentUpdater import scrappingApi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrappingApi.update_content, 'interval', minutes=10)
    scheduler.start()