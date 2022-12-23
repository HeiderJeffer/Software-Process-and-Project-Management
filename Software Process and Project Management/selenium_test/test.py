print ("test")
print("ayyylmao")
import mechanize
br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.addheaders = [('User-agent', 'Firefox')]

response = br.open("http://127.0.0.1:8000")
print br.title()
print response.geturl()
print response.info()  # headers
print response.read()  # body
#title test
test = br.title() == "MovieMe!"
print test
assert test == 1, 'title is wrong'
#HTTP response test
print response.code
assert response.code == 200, 'HTTP response not OK'


response = br.open("http://127.0.0.1:8000/admin")
print response.code

for form in br.forms():
    #print "Form name:", form.name
    print form
br.select_form(nr=0)


# for control in br.form.controls:
#     print control
#     print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

