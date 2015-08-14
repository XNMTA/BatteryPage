from bottle import route, run, template,request,response
import json

@route('/battery') #receive from IOS
def receive():
    try:
        data=request.query.data.lower()
        json_data=json.loads(data)
        file_object = open(json_data['udid'], 'a')
        file_object.write(json.dumps(json_data)+'\n')
        return "succeed"
    except Exception , e:
        return "failed"
    finally:
        file_object.close()

@route('/api/:udid') #api for web page
def getdata(udid):
    file_object = open(udid,'r')
    line=file_object.readline()
    result=[]
    while line<>'':
        result.append(json.loads(line))
        line=file_object.readline()
    return json.dumps(result)

@route('/index/:udid') #web page
def render(udid):
    file_object = open('index.html','r')
    all_the_text=file_object.read()
    return all_the_text

run(host='10.32.36.45', port=8080)
#run(host='localhost', port=8080)
