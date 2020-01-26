from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForm
import shelve, User

app = Flask(__name__)

@app.route('/product_search')
def productPage():
    usersDict = {}
    db = shelve.open('storage.db', 'r')
    usersDict = db['Users']
    db.close()

    usersList = []
    for key in usersDict:
        user = usersDict.get(key)
        usersList.append(user)

    return render_template('product_search.html', usersList=usersList, count=len(usersList))

@app.route('/text')
def FAQ():
    return render_template('text.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/createProduct', methods=['GET', 'POST'])
def createProduct():
    createUserForm = CreateUserForm(request.form)
    if request.method == 'POST' and createUserForm.validate():
        usersDict = {}
        db = shelve.open('storage.db', 'c')

        try:
            usersDict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")
    
        user = User.User(createUserForm.productName.data, createUserForm.category.data,
                         createUserForm.brand.data, createUserForm.quantity.data, createUserForm.price.data,
                         createUserForm.description.data)
        usersDict[user.get_userID()] = user
        db['Users'] = usersDict
        db.close()

        return redirect(url_for('retrieveProducts'))
    return render_template('createProduct.html', form=createUserForm)


@app.route('/retrieveProducts')
def retrieveProducts():
    usersDict = {}
    db = shelve.open('storage.db', 'r')
    usersDict = db['Users']
    db.close()

    usersList = []
    for key in usersDict:
        user = usersDict.get(key)
        usersList.append(user)

    return render_template('retrieveProducts.html', usersList=usersList, count=len(usersList))

@app.route('/updateProduct/<int:id>/', methods=['GET', 'POST'])
def updateProduct(id):
    updateUserForm = createProductForm(request.form)
    if request.method == 'POST' and updateUserForm.validate():
        userDict = {}
        db = shelve.open('storage.db', 'w')
        userDict = db['Users']

        user = userDict.get(id)
        user.set_productName(updateUserForm.productName.data)
        user.set_category(updateUserForm.category.data)
        user.set_brand(updateUserForm.brand.data)
        user.set_quantity(updateUserForm.quantity.data)
        user.set_price(updateUserForm.price.data)
        user.set_description(updateUserForm.description.data)

        db['Users'] = userDict
        db.close()

        return redirect(url_for('retrieveProducts'))
    else:
        userDict = {}
        db = shelve.open('storage.db', 'r')
        userDict = db['Users']
        db.close()

        user = userDict.get(id)
        updateUserForm.productName.data = user.get_productName()
        updateUserForm.category.data = user.get_category()
        updateUserForm.brand.data = user.get_brand()
        updateUserForm.quantity.data = user.get_quantity()
        updateUserForm.price.data = user.get_price()
        updateUserForm.description.data = user.get_description()

        return render_template('updateProduct.html', form=updateUserForm)


@app.route('/deleteUser/<int:id>', methods=['POST'])
def deleteUser(id):
    usersDict = {}
    db = shelve.open('storage.db', 'w')
    usersDict = db['Users']

    usersDict.pop(id)

    db['Users'] = usersDict
    db.close()

    return redirect(url_for('retrieveProducts'))


if __name__ == '__main__':
    app.run()
