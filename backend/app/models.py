from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), nullable=False)
    company_name = db.Column(db.String(128), nullable=True)  # For sponsors
    industry = db.Column(db.String(128), nullable=True)  # For sponsors
    budget = db.Column(db.Float, nullable=True)  # For sponsors
    name = db.Column(db.String(128), nullable=True)  # For influencers
    category = db.Column(db.String(128), nullable=True)  # For influencers
    niche = db.Column(db.String(128), nullable=True)  # For influencers
    reach = db.Column(db.Integer, nullable=True)  # For influencers
    approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    visibility = db.Column(db.String(64), nullable=False)
    goals = db.Column(db.Text, nullable=False)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sponsor = db.relationship('User', backref=db.backref('campaigns', lazy=True))

class AdRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    messages = db.Column(db.Text, nullable=True)
    requirements = db.Column(db.Text, nullable=False)
    payment_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(64), nullable=False)
    campaign = db.relationship('Campaign', backref=db.backref('ad_requests', lazy=True))
    influencer = db.relationship('User', backref=db.backref('ad_requests', lazy=True))

class Flag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flagged_id = db.Column(db.Integer, nullable=False)
    flagged_type = db.Column(db.String(50), nullable=False)  # 'user' or 'campaign'
    reason = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Flag {self.flagged_type}: {self.flagged_id}>'
