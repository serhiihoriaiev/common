import os
import re

from flask import Blueprint, render_template, redirect, current_app, request, session
from werkzeug.utils import secure_filename
from advanced_flask.supermarkets.initialize import supermarket_list
from advanced_flask.supermarkets.form import AddForm

sup = Blueprint('supermarkets', __name__, template_folder='templates', static_folder='static_sup')


@sup.route('/supermarkets')
def get_sup_list():
    if request.query_string:
        #  get the name of parameter from query string
        key = re.match('^(.+)=', request.query_string.decode('utf-8')).group(1)
        value = request.args.get(key)
        data = [sup for sup in supermarket_list if sup[key].lower() == value.lower()]
        return render_template('all_supermarkets.html', data=data, sess=session)
    return render_template('all_supermarkets.html', data=supermarket_list, sess=session)


@sup.route('/supermarket/<sup_id>')
def get_supermarket(sup_id):
    supermarket = [sup for sup in supermarket_list if sup['id'] == sup_id][0]
    session[supermarket['name']] = True
    return render_template('supermarket.html', supermarket=supermarket)


@sup.route('/add_supermarket', methods=['GET', 'POST'])
def add_sup_form():
    add_form = AddForm()
    #  check if form submitted
    if add_form.validate_on_submit():
        img = add_form.image_input.data
        #  save image if it's submitted
        if img:
            img.save(os.path.join(current_app.root_path, 'supermarkets/static_sup/', secure_filename(img.filename)))
        data = {
            'id': str(max([int(d['id']) for d in supermarket_list]) + 1),
            'name': add_form.name_input.data,
            'location': str(add_form.location_input.data),
            'img_name': secure_filename(img.filename) if img else ''
        }
        supermarket_list.append(data)
        return redirect('/supermarkets')
    return render_template("add_supermarket.html", form=add_form)
