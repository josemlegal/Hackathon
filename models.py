from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class datitos(db.Model):
    rowid       = db.Column(db.Integer, primary_key=True)
    nombre      = db.Column(db.String(200))
    apellido    = db.Column(db.String(200))
    edad        = db.Column(db.Integer)
    fecha_nac   = db.Column(db.String(200))
    email       = db.Column(db.String(200))
    num_tel     = db.Column(db.Integer)
    sobre_mi    = db.Column(db.String(200))
    departamento    = db.Column(db.String(200))
    localidad    = db.Column(db.String(200))
    virtud1     = db.Column(db.String(200))
    virtud2     = db.Column(db.String(200))
    virtud3     = db.Column(db.String(200))
    hab1        = db.Column(db.String(200))
    hab2        = db.Column(db.String(200))
    hab3        = db.Column(db.String(200))
    soft1        = db.Column(db.String(200))
    soft2        = db.Column(db.String(200))
    soft3        = db.Column(db.String(200))
    enteduc1        = db.Column(db.String(200))
    enteduc2        = db.Column(db.String(200))
    enteduc3        = db.Column(db.String(200))
    ciuform1        = db.Column(db.String(200))
    ciuform2        = db.Column(db.String(200))
    ciuform3        = db.Column(db.String(200))
    añoinicio1        = db.Column(db.String(200))
    añoinicio2        = db.Column(db.String(200))
    añoinicio3        = db.Column(db.String(200))
    añoinicio4        = db.Column(db.String(200))
    añofin1        = db.Column(db.String(200))
    añofin2        = db.Column(db.String(200))
    añofin3        = db.Column(db.String(200))
    añofin4        = db.Column(db.String(200))
    nomempresa1        = db.Column(db.String(200))
    nomempresa2        = db.Column(db.String(200))
    nomempresa3        = db.Column(db.String(200))
    nomempresa4        = db.Column(db.String(200))
    puesto1        = db.Column(db.String(200))
    puesto2        = db.Column(db.String(200))
    puesto3        = db.Column(db.String(200))
    puesto4        = db.Column(db.String(200))
    actrealiz1        = db.Column(db.String(200))
    actrealiz2        = db.Column(db.String(200))
    actrealiz3        = db.Column(db.String(200))
    actrealiz4        = db.Column(db.String(200))
    contactoref1        = db.Column(db.Integer)
    contactoref2        = db.Column(db.Integer)
    contactoref3        = db.Column(db.Integer)
    nombreref1        = db.Column(db.String(200))
    nombreref2        = db.Column(db.String(200))
    nombreref3        = db.Column(db.String(200))
    idioma1        = db.Column(db.String(200))
    idioma2        = db.Column(db.String(200))
    idioma3        = db.Column(db.String(200))
    idiomanivel1        = db.Column(db.String(200))
    idiomanivel2        = db.Column(db.String(200))
    idiomanivel3        = db.Column(db.String(200))

    def __init__(self, id, nombre,apellido,numero,edad,fecha_nac,email,num_tel,sobre_mi, departamento, localidad, virtud1,virtud2,virtud3,hab1,hab2,hab3,soft1,soft2,soft3,año1form,año2form,año3form,enteduc1,enteduc2,enteduc3,ciuform1,ciuform2,ciuform3,añoinicio1,añoinicio2,añoinicio3,añoinicio4,añofin1,añofin2,añofin3,añofin4,nomempresa1,nomempresa2,nomempresa3,nomempresa4,puesto1,puesto2,puesto3,puesto4,actrealiz1,actrealiz2,actrealiz3,actrealiz4,contactoref1,contactoref2,contactoref3,nombreref1,nombreref2,nombreref3,empresaref1,empresaref2,empresaref3,idioma1,idioma2,idioma3,idiomanivel1,idiomanivel2,idiomanivel3):
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.edad  =  edad
        self.fecha_nac  =  fecha_nac
        self.email  =  email
        self.num_tel  =  num_tel
        self.departamento  =  departamento
        self.localidad  =  localidad
        self.sobre_mi  =  sobre_mi
        self.virtud1  =  virtud1
        self.virtud2  =  virtud2
        self.virtud3  =  virtud3
        self.hab1  =  hab1
        self.hab2  =  hab2
        self.hab3  =  hab3
        self.soft1  =  soft1
        self.soft2  =  soft2
        self.soft3  =  soft3
        self.año1form  =  año1form
        self.año2form  =  año2form
        self.año3form  =  año3form
        self.enteduc1  =  enteduc1
        self.enteduc2  =  enteduc2
        self.enteduc3  =  enteduc3
        self.ciuform1  =  ciuform1
        self.ciuform2  =  ciuform2
        self.ciuform3  =  ciuform3
        self.añoinicio1  =  añoinicio1
        self.añoinicio2  =  añoinicio2
        self.añoinicio3  =  añoinicio3
        self.añoinicio4  =  añoinicio4
        self.añofin1  =  añofin1
        self.añofin2  =  añofin2
        self.añofin3  =  añofin3
        self.añofin4  =  añofin4
        self.nomempresa1  =  nomempresa1
        self.nomempresa2  =  nomempresa2
        self.nomempresa3  =  nomempresa3
        self.nomempresa4  =  nomempresa4
        self.puesto1  =  puesto1
        self.puesto2  =  puesto2
        self.puesto3  =  puesto3
        self.puesto4  =  puesto4
        self.actrealiz1  =  actrealiz1
        self.actrealiz2  =  actrealiz2
        self.actrealiz3  =  actrealiz3
        self.actrealiz4  =  actrealiz4
        self.contactoref1  =  contactoref1
        self.contactoref2  =  contactoref2
        self.contactoref3  =  contactoref3
        self.nombreref1  =  nombreref1
        self.nombreref2  =  nombreref2
        self.nombreref3  =  nombreref3
        self.empresaref1  =  empresaref1
        self.empresaref2  =  empresaref2
        self.empresaref3  =  empresaref3
        self.idioma1  =  idioma1
        self.idioma2  =  idioma2
        self.idioma3  =  idioma3
        self.idiomanivel1  =  idiomanivel1
        self.idiomanivel2  =  idiomanivel2
        self.idiomanivel3  =  idiomanivel3


    def __str__(self):
        return "id:  {}. nombre: {}.apellido: {}.edad: {}.fecha_nac: {}.email: {}.num_tel: {}.sobre_mi: {}.departamento: {}.localidad: {}.virtud1: {}.virtud2: {}.virtud3: {}.hab1: {}.hab2: {}.hab3: {}.soft1: {}.soft2: {}.soft3: {}.año1form: {}.año2form: {}.año3form: {}.enteduc1: {}.enteduc2: {}.enteduc3: {}.ciuform1: {}.ciuform2: {}.ciuform3: {}.añoinicio1: {}.añoinicio2: {}.añoinicio3: {}.añoinicio4: {}.añofin1: {}.añofin2: {}.añofin3: {}.añofin4: {}.nomempresa1: {}.nomempresa2: {}.nomempresa3: {}.nomempresa4: {}.puesto1: {}.puesto2: {}.pues.o3: {}.puesto4: {}.actrealiz1: {}.actrealiz2: {}.actrealiz3: {}.actrealiz4: {}.contactoref1: {}.cont.ctoref2: {}.contactoref3: {}.nombreref1: {}.nombreref2: {}.nombreref3: {}.empresaref1: {}.empr.saref2: {}.empresaref3: {}.idioma1: {}.idioma2: {}.idioma3: {}.idiomanivel1: {}.idiomanivel2: {}.idiomanivel3: {}".format(
        self.id,
        self.nombre ,
        self.apellido ,
        self.edad ,
        self.fecha_nac ,
        self.email ,
        self.num_tel ,
        self.sobre_mi ,
        self.departamento,
        self.localidad,
        self.virtud1 ,
        self.virtud2 ,
        self.virtud3 ,
        self.hab1 ,
        self.hab2 ,
        self.hab3 ,
        self.soft1 ,
        self.soft2 ,
        self.soft3 ,
        self.año1form ,
        self.año2form ,
        self.año3form ,
        self.enteduc1 ,
        self.enteduc2 ,
        self.enteduc3 ,
        self.ciuform1 ,
        self.ciuform2 ,
        self.ciuform3 ,
        self.añoinicio1,
        self.añoinicio2 ,
        self.añoinicio3 ,
        self.añoinicio4 ,
        self.añofin1 ,
        self.añofin2 ,
        self.añofin3 ,
        self.añofin4 ,
        self.nomempresa1 ,
        self.nomempresa2 ,
        self.nomempresa3 ,
        self.nomempresa4 ,
        self.puesto1 ,
        self.puesto2 ,
        self.puesto3 ,
        self.puesto4 ,
        self.actrealiz1 ,
        self.actrealiz2 ,
        self.actrealiz3 ,
        self.actrealiz4 ,
        self.contactoref1 ,
        self.contactoref2 ,
        self.contactoref3 ,
        self.nombreref1 ,
        self.nombreref2 ,
        self.nombreref3 ,
        self.empresaref1 ,
        self.empresaref2 ,
        self.empresaref3 ,
        self.idioma1 ,
        self.idioma2 ,
        self.idioma3 ,
        self.idiomanivel1 ,
        self.idiomanivel2 ,
        self.idiomanivel3
        )
    
    def serialize(self):
        return{
            "rowid": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "numero": self.numero
        }