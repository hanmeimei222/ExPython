import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

'''
# one parameter
class Index(object):
    def GET(self):
        form = web.input(name = "Nobody")
        greeting = "Hello %s" % form.name

        return render.index(greeting = greeting)
'''
'''
# two parameters
class Index(object):
    def GET(self):
        form = web.input(name = "Nobody", greet = "Hello")
        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
            return render.index(greeting = greeting)
        else:
            return "ERROR: greet is required."

'''


# with html forms
class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        # default value used when hello_form has no element called greet or name
        form = web.input(name="Nobody", greet="Hello")
        if form.name:
            greeting = "%s, %s" % (form.greet, form.name)
            return render.index(greeting=greeting)
        else:
            return "ERROR:name is required."

if __name__ == "__main__":
    app.run()
