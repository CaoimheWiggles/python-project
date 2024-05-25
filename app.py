""" from flask import Flask, url_for, render_template, redirect, request
from datetime import datetime, timedelta

app = Flask(__name__, template_folder='templates', static_folder='static')


def calculate_min_max_dates():
    current_date = datetime.now().date()
    next_year = current_date.year + 1

    min_date = datetime(next_year, 1, 1)
    max_date = datetime(next_year, 12, 31)

    return min_date, max_date

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    class Therapist:
        def __init__(self, name, specialization, description, image_url):
            self.name = name
            self.specialization = specialization
            self.description = description
            self.image_url = image_url

        def __str__(self):
            return f"{self.name} - {self.specialization}"

    therapist = Therapist(
        name="Dr. John McFadden",
        specialization="Therapist",
        description="Dr. John McFadden specializes in offering therapeutic support to men navigating the challenges of life",
        image_url="/static/images/portrait.jpg"
    )
    return render_template('about.html', therapist=therapist)


@app.route('/services', methods=['GET', 'POST'])
def services():
    min_date, max_date = calculate_min_max_dates()

    services = [
        {
            'name': 'Individual Therapy',
            'description': 'One-on-one counseling sessions tailored to your specific needs.'
        },
        {
            'name': 'Couples Therapy',
            'description': 'Therapeutic support for couples seeking to improve their relationships.'
        },
        {
            'name': 'Adolescence Therapy',
            'description': 'Guidance for teens having struggles.'
        }
    ]
    
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        name = request.form['name']
        email = request.form['email']
        contact_number = request.form['contact_number']  
        

        return render_template('thank_you.html', name=name, date=date, time=time, contact_number=contact_number)
    
    return render_template('services.html', services=services, min_date=min_date.strftime==('%Y-%m-%d'), max_date=max_date.strftime('%Y-%m-%d'))


testimonials_data = []

@app.route('/submit_testimonials', methods=['GET', 'POST'])
def submit_testimonials():
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']
        testimonials = request.form['testimonials']
        testimonials_data.append({'name': name, 'rating': rating, 'testimonials': testimonials})
        return redirect(url_for('thank_you'))
    return render_template('testimonials_form.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) """



from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__, template_folder='templates', static_folder='static')

def calculate_min_max_dates():
    current_date = datetime.now().date()
    next_year = current_date.year + 1
    min_date = datetime(next_year, 1, 1)
    max_date = datetime(next_year, 12, 31)
    return min_date, max_date

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    class Therapist:
        def __init__(self, name, specialization, description, image_url):
            self.name = name
            self.specialization = specialization
            self.description = description
            self.image_url = image_url

        def __str__(self):
            return f"{self.name} - {self.specialization}"

    therapist = Therapist(
        name="Dr. John McFadden",
        specialization="Therapist",
        description="Dr. John McFadden specializes in offering therapeutic support to men navigating the challenges of life",
        image_url="/static/images/portrait.jpg"
    )
    return render_template('about.html', therapist=therapist)

@app.route('/services', methods=['GET', 'POST'])
def services():
    min_date, max_date = calculate_min_max_dates()
    services = [
        {
            'name': 'Individual Therapy',
            'description': 'One-on-one counseling sessions tailored to your specific needs.'
        },
        {
            'name': 'Couples Therapy',
            'description': 'Therapeutic support for couples seeking to improve their relationships.'
        },
        {
            'name': 'Adolescence Therapy',
            'description': 'Guidance for teens having struggles.'
        }
    ]
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        name = request.form['name']
        email = request.form['email']
        contact_number = request.form['contact_number']
        return render_template('thank_you.html', name=name, date=date, time=time, contact_number=contact_number)
    return render_template('services.html', services=services, min_date=min_date.strftime('%Y-%m-%d'), max_date=max_date.strftime('%Y-%m-%d'))

testimonials_data = []

@app.route('/submit_testimonials', methods=['GET', 'POST'])
def submit_testimonials():
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']
        testimonials = request.form['testimonials']
        testimonials_data.append({'name': name, 'rating': rating, 'testimonials': testimonials})
        return redirect(url_for('thank_you'))
    return render_template('testimonials_form.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)