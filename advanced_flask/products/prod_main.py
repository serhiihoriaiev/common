import os
import re

from flask import Blueprint, render_template, redirect, current_app, request, session
from werkzeug.utils import secure_filename
from advanced_flask.products.initialize import product_list
from advanced_flask.products.form import AddForm

prod = Blueprint('products', __name__, template_folder='templates', static_folder='static_pr')


@prod.route('/products')
def get_prod_list():
    if request.query_string:
        #  get the name of parameter from query string
        key = re.match('^(.+)=', request.query_string.decode('utf-8')).group(1)
        value = request.args.get(key)
        data = [pr for pr in product_list if pr[key] == value]
        return render_template('all_products.html', data=data, sess=session)
    return render_template('all_products.html', data=product_list, sess=session)


@prod.route('/product/<prod_id>')
def get_product(prod_id):
    product = [pr for pr in product_list if pr['id'] == prod_id][0]
    session[product['name']] = True
    return render_template('product.html', product=product)


@prod.route('/add_product', methods=['GET', 'POST'])
def add_prod_form():
    add_form = AddForm()
    #  check if form submitted
    if add_form.validate_on_submit():
        img = add_form.image_input.data
        #  save image if it's submitted
        if img:
            img.save(os.path.join(current_app.root_path, 'products/static_pr/', secure_filename(img.filename)))
        data = {
            'id': str(max([int(d['id']) for d in product_list]) + 1),
            'name': add_form.name_input.data,
            'description': add_form.desc_input.data,
            'img_name': secure_filename(img.filename) if img else '',
            'price': str(add_form.price_input.data)
        }
        product_list.append(data)
        return redirect('/products')
    return render_template("add_product.html", form=add_form)
