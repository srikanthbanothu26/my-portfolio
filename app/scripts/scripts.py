from flask import Blueprint,render_template

script_bp = Blueprint('scripts', __name__)
@script_bp.route('/',methods=['GET','POST'])
def home():
    return render_template("main.html")

@script_bp.route('/about',methods=['GET','POST'])
def about():
    return render_template("about.html")

@script_bp.route('/contact',methods=['GET','POST'])
def contact():
    return render_template("contact.html")

@script_bp.route('/projects',methods=['GET','POST'])
def projects():
    return render_template("projects.html")


@script_bp.route('/education',methods=['GET','POST'])
def education():
    return render_template("education.html")

@script_bp.route('/skills',methods=['GET','POST'])
def skills():
    return render_template("skills.html")

@script_bp.route('/certifications',methods=['GET','POST'])
def certifications():
    return render_template("certifications.html")