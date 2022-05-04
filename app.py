from flask import Flask, jsonify, render_template, request, redirect, url_for
from models import db, datitos
from logging import exception

app = Flask(__name__)


#COFIGURAMOS EL ACCESO A LA BASE DE DATOS
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/datitos.db" #Direccion abs en linux
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#CONFIGURAMOS LA RUTA PARA INDEX

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/entrada_espanol')
def entrada_espanol():
    return render_template('intro_esp.html')

@app.route('/entrada_guarani')
def entrada_guarani():
    return render_template('intro_grn.html')

#AGARRAMOS LOS DATOS QUE NECESITAMOS DE LA BASE DE DATOS Y LO CONVERTIMOS A JSON
@app.route("/api/datitos", methods=["GET"]) #get porque solo queremos hacer lectura de datos
def getDatitos():
    try:

        datitoz = datitos.query.all()
        toReturn = [datox.serialize() for datox in datitoz]
        return jsonify(toReturn), 200

    except Exception:
        exception("[SERVER]: Error->")
        return jsonify({"msg": "Ha ocurrido un error"}),500

    return '<h1>Success</h1>'

@app.route("/api/agregardatos", methods=["POST"])
def addPersona():
    try:
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        fecha_nac = request.form["fecha_nac"]
        numero = "numero"
        edad = "edad"
        num_tel = request.form["num_tel"]
        email = request.form["email"]
        sobre_mi = request.form["sobre_mi"]
        departamento = request.form["departamento"]
        localidad = request.form["localidad"]
        virtud1 = request.form["virtud1"]
        virtud2 = request.form["virtud2"]
        virtud3 = request.form["virtud3"]
        hab1 = request.form["hab1"]
        hab2 = request.form["hab2"]
        hab3 = request.form["hab3"]
        soft1 = request.form["soft1"]
        soft2 = request.form["soft2"]
        soft3 = request.form["soft3"]
        año1form = "2015" #request.form["año1form"]
        año2form = "2018" #request.form["año2form"]
        año3form = "2020" #request.form["año3form"]
        enteduc1 = request.form["enteduc1"]
        enteduc2 = request.form["enteduc2"]
        enteduc3 = request.form["enteduc3"]
        ciuform1 = "Educacion Escolar Basica" #request.form["ciuform1"]
        ciuform2 = "Bachiller Tecnico en Informatica" # request.form["ciuform2"]
        ciuform3 = "Contador Publico" #request.form["ciuform3"]
        añoinicio1 = request.form["añoinicio1"]
        añoinicio2 = "2019 " # request.form["añoinicio2"]
        añoinicio3 = "2018" # request.form["añoinicio3"]
        añoinicio4 = "2017" # request.form["añoinicio4"]
        añofin1 = request.form["añofin1"]
        añofin2 = "2019"#request.form["añofin2"]
        añofin3 = "2018" #request.form["añofin3"]
        añofin4 = "2018" # request.form["añofin4"]
        nomempresa1 = request.form["nomempresa1"]
        nomempresa2 = "Spraytec Paraguay S.A." # request.form["nomempresa2"]
        nomempresa3 = "Stardust" # request.form["nomempresa3"]
        nomempresa4 = "Lar Paraguay" # request.form["nomempresa4"]
        puesto1 = request.form["puesto1"]
        puesto2 = " Auxiliar Administrativo/Comercial" # request.form["puesto2"]
        puesto3 = "Ejecutivo de Cuentas" # request.form["puesto3"]
        puesto4 = "Auxiliar Contable" # request.form["puesto4"]
        actrealiz1 = request.form["actrealiz1"]
        actrealiz2 = "Elaboracion de planillas para el control de comisiones de vendedores, tareas administrativas en general, control de stock, conciliacion de estado de cuenta de clientes, entre otros." # request.form["actrealiz2"]
        actrealiz3 = "Contacto con los diversos clientes de la agencia, manejo de redes sociales, búsqueda de clientes potenciales" # request.form["actrealiz3"]
        actrealiz4 = "Tareas administrativas/contables en general, control de retenciones, archivo de documentos fiscales, entre otros." # request.form["actrealiz4"]
        contactoref1 = request.form["contactoref1"]
        contactoref2 = "0985128232"#request.form["contactoref2"]
        contactoref3 = "0985123231" #request.form["contactoref3"]
        nombreref1 = request.form["nombreref1"]
        nombreref2 = request.form["nombreref2"]
        nombreref3 = request.form["nombreref3"]
        empresaref1 = request.form["empresaref1"]
        empresaref2 = request.form["empresaref2"]
        empresaref3 = request.form["empresaref3"]
        idioma1 = request.form["idioma1"]
        idioma2 = request.form["idioma2"]
        idioma3 = request.form["idioma3"]
        idiomanivel1 = request.form["idiomanivel1"]
        idiomanivel2 = request.form["idiomanivel2"]
        idiomanivel3 = request.form["idiomanivel3"]

        persona = datitos(id, nombre,apellido,numero,edad,fecha_nac,email,num_tel,sobre_mi,departamento, localidad, virtud1,virtud2,virtud3,hab1,hab2,hab3,soft1,soft2,soft3,año1form,año2form,año3form,enteduc1,enteduc2,enteduc3,ciuform1,ciuform2,ciuform3,añoinicio1,añoinicio2,añoinicio3,añoinicio4,añofin1,añofin2,añofin3,añofin4,nomempresa1,nomempresa2,nomempresa3,nomempresa4,puesto1,puesto2,puesto3,puesto4,actrealiz1,actrealiz2,actrealiz3,actrealiz4,contactoref1,contactoref2,contactoref3,nombreref1,nombreref2,nombreref3,empresaref1,empresaref2,empresaref3,idioma1,idioma2,idioma3,idiomanivel1,idiomanivel2,idiomanivel3)
        db.session.add(persona)
        db.session.commit()

        return redirect('/cv?nombre='+nombre)
    except Exception as k:
        print(k)
        exception("[SERVER]: Error in route  /api/addPersona, Log: \n")
        return jsonify({"msg": "Algo ha salido mal"}),500

@app.route("/cv", methods=["GET"])
def llenarcv():
        namePersona = request.args["nombre"]
        datos = {}
        datos["perfil"] = datitos.query.filter_by(nombre=namePersona).first()
        print(datos)
        return render_template("modelo_1_cv.html", data=datos)

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/formulario_guarani')
def formulario_guarani():
    return render_template('formulario_guarani.html')

if __name__ == "__main__":
    app.run(debug=True,port=4000)

