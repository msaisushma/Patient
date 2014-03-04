from bottle import route, error ,run ,request,post,get,delete,put
mbr_dict = {}

@error(404)
@error(500)
def error404(error):
    return 'Page not found'
def error500(error):
	return 'Internal server error'

@route('/member')

def member_list():
    return "No records found"

@post('/member')
def member_post():
	mbr_id  = request.POST['mbr_id']
	name = request.POST['name']
	gender = request.POST['gender']
	age = request.POST['age']
	address = request.POST['address']
	phone = request.POST['phone']
	details =[name,gender,age,address,phone]
	mbr_dict.update({mbr_id:details})
	return '<b>Member Created with ID {0}'.format(mbr_id)


@get('/member/<mbr_id>')
def show_details(mbr_id):
    return mbr_dict[mbr_id]
	

@delete('/member/<mbr_id>')
def deleteInfo(mbr_id):
    del(mbr__dict[mbr_id])
		#return "Deleted Sucessfully {0}".format(mbr_id)

@put('/member/<mbr_id>')
def updateInfo(mbr_id):
	name = request.POST['name']
	gender = request.POST['gender']
	age = request.POST['age']
	address = request.POST['address']
	phone = request.POST['phone'] 
	details =[name,gender,age,address,phone]
	mbr_dict.update({mbr_id:details})
	return mbr_dict
	

run(host='localhost', port=8080)
