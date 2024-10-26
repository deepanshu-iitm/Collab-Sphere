from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.decorators import role_required
from app.models import Campaign, AdRequest, User, db
from datetime import datetime

bp = Blueprint('sponsor_routes', __name__, url_prefix='/sponsor')

def convert_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

@bp.route('/campaigns', methods=['POST'])
@jwt_required()
@role_required('sponsor')
def create_campaign():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    budget = data.get('budget')
    visibility = data.get('visibility')
    goals = data.get('goals')
    sponsor_id = get_jwt_identity()['id']

    if not all([name, description, start_date, end_date, budget, visibility]):
        return jsonify({'msg': 'Missing required fields'}), 400
    
    try:
        start_date = convert_date(start_date)
        end_date = convert_date(end_date)
        if start_date >= end_date:
            return jsonify({'msg': 'Start date must be before end date'}), 400
    except ValueError as e:
        return jsonify({'msg': str(e)}), 400

    campaign = Campaign(
        name=name,
        description=description,
        start_date=start_date,
        end_date=end_date,
        budget=budget,
        visibility=visibility,
        goals=goals,
        sponsor_id=sponsor_id
    )

    db.session.add(campaign)
    db.session.commit()

    return jsonify({'msg': 'Campaign created successfully'}), 201

@bp.route('/campaigns', methods=['GET'])
@jwt_required()
@role_required('sponsor')
def get_campaigns():
    sponsor_id = get_jwt_identity()['id']
    campaigns = Campaign.query.filter_by(sponsor_id=sponsor_id).all()
    serialized_campaigns = [{
        'id': campaign.id,
        'name': campaign.name,
        'description': campaign.description,
        'start_date': campaign.start_date.strftime('%Y-%m-%d') if campaign.start_date else None,
        'end_date': campaign.end_date.strftime('%Y-%m-%d') if campaign.end_date else None,
        'budget': campaign.budget,
        'visibility': campaign.visibility,
        'goals': campaign.goals,
        'sponsor_id': campaign.sponsor_id
    } for campaign in campaigns]
    
    return jsonify(serialized_campaigns)

@bp.route('/campaigns/<int:campaign_id>', methods=['GET'])
@jwt_required()
@role_required('sponsor')
def get_campaign(campaign_id):
    sponsor_id = get_jwt_identity()['id']
    campaign = Campaign.query.filter_by(id=campaign_id, sponsor_id=sponsor_id).first_or_404()
    serialized_campaign = {
        'id': campaign.id,
        'name': campaign.name,
        'description': campaign.description,
        'start_date': campaign.start_date.strftime('%Y-%m-%d') if campaign.start_date else None,
        'end_date': campaign.end_date.strftime('%Y-%m-%d') if campaign.end_date else None,
        'budget': campaign.budget,
        'visibility': campaign.visibility,
        'goals': campaign.goals,
        'sponsor_id': campaign.sponsor_id
    }
    return jsonify(serialized_campaign)

@bp.route('/campaigns/<int:campaign_id>', methods=['PUT'])
@jwt_required()
@role_required('sponsor')
def update_campaign(campaign_id):
    sponsor_id = get_jwt_identity()['id']
    campaign = Campaign.query.filter_by(id=campaign_id, sponsor_id=sponsor_id).first_or_404()
    data = request.get_json()

    if 'name' in data:
        campaign.name = data['name']
    if 'description' in data:
        campaign.description = data['description']
    if 'start_date' in data:
        try:
            campaign.start_date = convert_date(data['start_date'])
        except ValueError as e:
            return jsonify({'msg': str(e)}), 400
    if 'end_date' in data:
        try:
            campaign.end_date = convert_date(data['end_date'])
            if campaign.start_date >= campaign.end_date:
                return jsonify({'msg': 'Start date must be before end date'}), 400
        except ValueError as e:
            return jsonify({'msg': str(e)}), 400
    if 'budget' in data:
        campaign.budget = data['budget']
    if 'visibility' in data:
        campaign.visibility = data['visibility']
    if 'goals' in data:
        campaign.goals = data['goals']

    db.session.commit()

    return jsonify({'msg': 'Campaign updated successfully'}), 200

@bp.route('/campaigns/<int:campaign_id>', methods=['DELETE'])
@jwt_required()
@role_required('sponsor')
def delete_campaign(campaign_id):
    sponsor_id = get_jwt_identity()['id']
    campaign = Campaign.query.filter_by(id=campaign_id, sponsor_id=sponsor_id).first_or_404()
    db.session.delete(campaign)
    db.session.commit()

    return jsonify({'msg': 'Campaign deleted successfully'}), 200

@bp.route('/campaigns/<int:campaign_id>/adrequests', methods=['POST'])
@jwt_required()
@role_required('sponsor')
def create_ad_request(campaign_id):
    data = request.get_json()
    sponsor_id = get_jwt_identity()['id']
    
    campaign = Campaign.query.filter_by(id=campaign_id, sponsor_id=sponsor_id).first()
    if not campaign:
        return jsonify({'msg': 'Campaign not found or not owned by you'}), 404

    influencer_id = data.get('influencer_id')
    messages = data.get('messages')
    requirements = data.get('requirements')
    payment_amount = data.get('payment_amount')
    status = data.get('status')

    if not all([campaign_id, influencer_id, messages, requirements, payment_amount, status]):
        return jsonify({'msg': 'Missing required fields'}), 400

    ad_request = AdRequest(
        campaign_id=campaign_id,
        influencer_id=influencer_id,
        messages=messages,
        requirements=requirements,
        payment_amount=payment_amount,
        status=status
    )

    db.session.add(ad_request)
    db.session.commit()

    return jsonify({'msg': 'Ad request created successfully'}), 201

@bp.route('/campaigns/<int:campaign_id>/adrequests', methods=['GET'])
@jwt_required()
@role_required('sponsor')
def get_ad_requests(campaign_id):
    sponsor_id = get_jwt_identity()['id']
    campaign = Campaign.query.filter_by(id=campaign_id, sponsor_id=sponsor_id).first_or_404()
    ad_requests = AdRequest.query.filter_by(campaign_id=campaign_id).all()
    serialized_ad_requests = [{
        'id': ad_request.id,
        'campaign_id': ad_request.campaign_id,
        'influencer_id': ad_request.influencer_id,
        'messages': ad_request.messages,
        'requirements': ad_request.requirements,
        'payment_amount': ad_request.payment_amount,
        'status': ad_request.status
    } for ad_request in ad_requests]
    
    return jsonify(serialized_ad_requests)

@bp.route('/campaigns/<int:campaign_id>/adrequests/<int:ad_request_id>', methods=['GET'])
@jwt_required()
@role_required('sponsor')
def get_ad_request(campaign_id, ad_request_id):
    sponsor_id = get_jwt_identity()['id']
    campaign = Campaign.query.filter_by(id=campaign_id, sponsor_id=sponsor_id).first_or_404()
    ad_request = AdRequest.query.filter_by(id=ad_request_id, campaign_id=campaign_id).first_or_404()
    serialized_ad_request = {
        'id': ad_request.id,
        'campaign_id': ad_request.campaign_id,
        'influencer_id': ad_request.influencer_id,
        'messages': ad_request.messages,
        'requirements': ad_request.requirements,
        'payment_amount': ad_request.payment_amount,
        'status': ad_request.status
    }
    return jsonify(serialized_ad_request)


@bp.route('/campaigns/<int:campaign_id>/adrequests/<int:ad_request_id>', methods=['PUT'])
@jwt_required()
@role_required('sponsor')
def update_ad_request(campaign_id, ad_request_id):
    ad_request = AdRequest.query.filter_by(id=ad_request_id, campaign_id=campaign_id).first_or_404()
    data = request.get_json()

    if 'influencer_id' in data:
        ad_request.influencer_id = data['influencer_id']
    if 'messages' in data:
        ad_request.messages = data['messages']
    if 'requirements' in data:
        ad_request.requirements = data['requirements']
    if 'payment_amount' in data:
        ad_request.payment_amount = data['payment_amount']
    if 'status' in data:
        ad_request.status = data['status']
    
    db.session.commit()

    return jsonify({'msg': 'Ad request updated successfully'}), 200

@bp.route('/campaigns/<int:campaign_id>/adrequests/<int:ad_request_id>', methods=['DELETE'])
@jwt_required()
@role_required('sponsor')
def delete_ad_request(campaign_id, ad_request_id):
    ad_request = AdRequest.query.filter_by(id=ad_request_id, campaign_id=campaign_id).first()
    if not ad_request:
        return jsonify({'msg': 'Ad request not found'}), 404

    db.session.delete(ad_request)
    db.session.commit()

    return jsonify({'msg': 'Ad request deleted successfully'}), 200

@bp.route('/search/influencers', methods=['GET'])
@jwt_required()
@role_required('sponsor')
def search_influencers():
    niche = request.args.get('niche')
    min_reach = request.args.get('min_reach', type=int)
    max_reach = request.args.get('max_reach', type=int)
    min_followers = request.args.get('min_followers', type=int)
    max_followers = request.args.get('max_followers', type=int)

    query = User.query

    if niche:
        query = query.filter(User.niche.ilike(f'%{niche}%'))
    if min_reach is not None:
        query = query.filter(User.reach >= min_reach)
    if max_reach is not None:
        query = query.filter(User.reach <= max_reach)
    if min_followers is not None:
        query = query.filter(User.followers >= min_followers)
    if max_followers is not None:
        query = query.filter(User.followers <= max_followers)

    influencers = query.all()

    return jsonify([{
        'id': influencer.id,
        'name': influencer.name,
        'niche': influencer.niche,
        'reach': influencer.reach,
        'followers': influencer.followers
    } for influencer in influencers]), 200
