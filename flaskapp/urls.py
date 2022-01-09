import views
import app

app.api.add_resource(views.ApiIndex, '/')
app.api.add_resource(views.ApiPut, '/<string:id_key>')
