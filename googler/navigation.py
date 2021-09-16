import os
import jinja2


import logging
#Jinja Loader

template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))


class NavigationHandler():
    def get(self):
        url = str(self.request.url)
        strRouter = url.split("/")
        strRouter = strRouter[len(strRouter) - 1]

        if strRouter == "header":
            template = template_env.get_template('templates/dynamic/navigation/header.html')
            context = {}
            self.response.write(template.render(context))
        elif strRouter == "sidebar":
            template = template_env.get_template('templates/dynamic/navigation/sidebar.html')
            context = {}
            self.response.write(template.render(context))
        elif strRouter == "footer":
            template = template_env.get_template('templates/dynamic/navigation/footer.html')
            context = {}
            self.response.write(template.render(context))
        else:
            pass


app = webapp2.WSGIApplication([
    ('/navigation/.*', NavigationHandler)
], debug=True)
