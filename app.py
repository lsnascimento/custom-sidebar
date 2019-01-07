from flask import Flask, render_template


app = Flask(__name__)


_items = [
    { 
        'name': 'Project', 
        'class': '', 
        'url': '/' ,
        'submenu': [
            { 'name': 'Details', 'url': '/', 'class': '' },
            { 'name': 'Activity', 'url': '/project/activity', 'class': '' },
            { 'name': 'Security Dashboard', 'url': '/project/security_dashboard', 'class': '' },
            { 'name': 'Cycle Analytics', 'url': '/project/cycle_analytics', 'class': '' }
        ]
    },
    { 'name': 'Repository', 'class': '', 'url': '/repository' },
    { 
        'name': 'Issues', 
        'class': '', 
        'subclass': '', 
        'url': '/issues',
        'submenu': [
            { 'name': 'List', 'url': '/issues', 'class': '' },
            { 'name': 'Boards', 'url': '/issues/boards', 'class': '' },
            { 'name': 'Labels', 'url': '/issues/labels', 'class': '' },
            { 'name': 'Service Desk', 'url': '/issues/service_desk', 'class': '' },
            { 'name': 'Milestones', 'url': '/issues/milestones', 'class': '' }
        ]
    },
    { 'name': 'Merge Requests', 'class': '', 'url': '/merge_requests' },
    { 'name': 'CI / CD', 'class': '', 'url': '/ci_cd' }
]

def setActiveClass(item_name, submenu_name=''):
    for item in _items:
        if (item['name'].lower() == item_name):
            item['class'] = 'active'
            item['subclass'] = 'visible'
            if 'submenu' in item:
                for submenu_item in item['submenu']:
                    if submenu_item['name'].lower() == submenu_name:
                        submenu_item['class'] = 'active-submenu'
                    else:
                        submenu_item['class'] = 'inactive-submenu'
        else:
            item['class'] = ''
            item['subclass'] = 'invisible'

@app.route('/')
def index():
    setActiveClass('project', 'details')
    return render_template('project.html', items=_items)

@app.route('/project/activity')
def project_activity():
    setActiveClass('project', 'activity')
    return render_template('project/activity.html', items=_items)

@app.route('/project/security_dashboard')
def project_security_dashboard():
    setActiveClass('project', 'security_dashboard')
    return render_template('project/security_dashboard.html', items=_items)

@app.route('/project/cycle_analytics')
def project_cycle_analytics():
    setActiveClass('project', 'cycle_analytics')
    return render_template('project/cycle_analytics.html', items=_items)

@app.route('/repository')
def repository():
    setActiveClass('repository')
    return render_template('repository.html', items=_items)

@app.route('/issues')
def issues():
    setActiveClass('issues', 'list')
    return render_template('issues.html', items=_items)

@app.route('/issues/boards')
def issues_boards():
    setActiveClass('issues', 'boards')
    return render_template('issues/boards.html', items=_items)

@app.route('/issues/labels')
def issues_labels():
    setActiveClass('issues', 'labels')
    return render_template('issues/labels.html', items=_items)

@app.route('/issues/service_desk')
def issues_service_desk():
    setActiveClass('issues', 'service desk')
    return render_template('issues/service_desk.html', items=_items)

@app.route('/issues/milestones')
def issues_milestones():
    setActiveClass('issues', 'milestones')
    return render_template('issues/milestones.html', items=_items)

@app.route('/merge_requests')
def merge_requests():
    setActiveClass('merge requests')
    return render_template('merge-requests.html', items=_items)

@app.route('/ci_cd')
def ci_cd():
    setActiveClass('ci / cd')
    return render_template('ci-cd.html', items=_items)

if __name__ == '__main__':
    app.run(debug=True)
