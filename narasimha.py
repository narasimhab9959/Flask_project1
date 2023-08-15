from flask import Flask,render_template

FAI=Flask(__name__)# this __name__ is for takes the Current Module name means foldername..


@FAI.route('/Hope') # by using decorators we can intaract with both the functions..
def Hope():
    return 'Hi emchestunnav unnava asalu....?'

# Route is  like (URLMapping ) in django we use Url mapping , In Flask We use Route...

@FAI.route('/Last')
def Last():
    return render_template('Last.html',name='narasimha' ,age=21)


if __name__=='__main__':
    FAI.run(debug=True,host='192.168.1.74',port=5001)
# This Host Number is Ip Address of the System,By Using these we can fetch Data by IP adress of number..



