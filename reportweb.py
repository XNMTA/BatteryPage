from bottle import route, run, template,request,response
import json

@route('/battery')
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

@route('/index/:udid')
def render(udid):
    file_object = open('index.html','r')
    all_the_text=file_object.read()
    return all_the_text


run(host='localhost', port=8080)
