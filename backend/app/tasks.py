from app import create_celery_app, db, mail
from flask_mail import Message
from datetime import datetime, timedelta
from app.models import User, AdRequest, Campaign

celery = create_celery_app()

@celery.task
def daily_reminder():
    with celery.app.app_context():
        today = datetime.utcnow()
        pending_requests = AdRequest.query.filter_by(status='pending').all()
        for request in pending_requests:
            influencer = User.query.get(request.influencer_id)
            if (today - influencer.last_login).days > 1:
                send_reminder_email(influencer.email)

def send_reminder_email(email):
    msg = Message('Daily Reminder', recipients=[email])
    msg.body = 'You have pending ad requests. Please log in to review them.'
    mail.send(msg)

@celery.task
def monthly_activity_report():
    with celery.app.app_context():
        sponsors = User.query.filter_by(role='sponsor').all()
        for sponsor in sponsors:
            campaigns = Campaign.query.filter_by(sponsor_id=sponsor.id).all()
            report = generate_report(campaigns)
            send_report_email(sponsor.email, report)

def generate_report(campaigns):
    report = 'Monthly Activity Report\n\n'
    for campaign in campaigns:
        report += f'Campaign: {campaign.name}\n'
        report += f'Start Date: {campaign.start_date}\n'
        report += f'End Date: {campaign.end_date}\n'
        report += f'Budget: {campaign.budget}\n'
        report += f'Goals: {campaign.goals}\n'
        report += '\n'
    return report

def send_report_email(email, report):
    msg = Message('Monthly Activity Report', recipients=[email])
    msg.body = report
    mail.send(msg)
