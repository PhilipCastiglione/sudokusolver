import web

urls = (
 '/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('sudokusolver/')

class index:
	def GET(self):
		return render.ss_frontend()
		
if __name__ == "__main__":
	app.run()