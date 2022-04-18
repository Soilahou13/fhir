import json,random
from app import app
from flask import Flask, render_template,request,jsonify
from os import listdir
from os.path import isfile, join


@app.route('/', methods = ['GET'])
def Patient():
    identifiant = request.args.get("id")
    Organisation =  'app/fhir/Organization/0.json'
    info_organisation = json.load(open(Organisation))
    open(Organisation).close()
    Patient = 'app/fhir/Patient/'+str(identifiant)+'.json'
    info_patient = json.load(open(Patient))
    open(Patient).close()
    Vaccins = 'app/fhir/Vaccins/'+str(identifiant)+'.json'
    info_vaccins = json.load(open(Vaccins))
    open(Vaccins).close()
    MedicationRequest = 'app/fhir/MedicationRequest/'+str(identifiant)+'.json'
    Medication = json.load(open(MedicationRequest))
    open(Vaccins).close()
    return render_template ('index.html',Patient=info_patient,Organisation=info_organisation,Vaccins = info_vaccins,Medication=Medication)

@app.route("/Nouveau")
def nouveau_patient():
    return render_template('Nouveau.html')

@app.route("/confirmation",methods=['POST'])
def informations_patient():    
    identifiant = request.form.get('identifier')
    nom = request.form.get('name')
    genre = request.form.get('gender')
    date = request.form.get('birthDate')
    adresse = request.form.get('address')
    covid = request.form.get('covid')
    dtp = request.form.get('dtp')
    coqueluche = request.form.get('Coqueluche')
    rubeole=request.form.get('Rubeole')
    hepatite=request.form.get('Hepatite')
    rougeole=request.form.get('Rougeole')
    oreillons=request.form.get('Oreillons')

    patient = {
              "resourceType" : "Patient",
              "identifier" : identifiant,
              "active" : "<boolean>",
              "name" : nom,
              "telecom" : "[{ ContactPoint }]",
              "gender" : genre,
              "birthDate" : date,
              "deceasedBoolean" : "<boolean>",
              "deceasedDateTime" : "<dateTime>",
              "address" : adresse,
              "maritalStatus" : "{ CodeableConcept }",
              "multipleBirthBoolean" : "<boolean>",
              "multipleBirthInteger" : "<integer>",
              "photo" : "[{ Attachment }]",
              "contact" : [{
                "relationship" : "[{ CodeableConcept }]",
                "name" : "{ HumanName }",
                "telecom" : "[{ ContactPoint }]",
                "address" : "{ Address }",
                "gender" : "<code>",
                "organization" : "{ Reference(Organization) }",
                "period" : "{ Period }"
              }],
              "communication" : [{
                "language" : "{ CodeableConcept }",
                "preferred" : "<boolean>"
              }],
              "generalPractitioner" : "[{ Reference(Organization|Practitioner|PractitionerRole) }]",
              "managingOrganization" : "{ Reference(Organization) }",
              "link" : [{ 
                "other" : "{ Reference(Patient|RelatedPerson) }",
                "type" : "<code>"
              }]
            }
    with open("app/fhir/Patient/"+str(identifiant)+".json", "w") as f_write:
        json.dump(patient, f_write, indent=2)
        
    Vaccins = {
        "Covid" : covid,
        'DTP' : dtp,
        'Coqueluche': coqueluche,
        'Rubeole' : rubeole,
        'Hepatite': hepatite,
        'Rougeole' : rougeole,
        'Oreillons' : oreillons
        }
        
    with open("app/fhir/Vaccins/"+str(identifiant)+".json", "w") as f_write:
        json.dump(Vaccins, f_write, indent=2)
    
    return ("<a href='/'>Page principale</a>")

@app.route("/Modifier", methods = ['GET'])
def modifier_patient():
    identifiant = request.args.get("id")
    Medication = 'app/fhir/MedicationRequest/'+str(identifiant)+'.json'
    infomed = json.load(open(Medication))
    open(Medication).close()
    return render_template ('modification.html',infomed=infomed)

# def immunization():
#     fichiers = [f for f in listdir("fhir/Vaccins") if isfile(join("fhir/Vaccins", f))]
    
#     for i in range (0,len(fichiers)):
#         a = open ('fhir/Vaccins/'+fichiers[i])
#         b = json.load(a)
#         if b["Covid"]== "realised":
#             donnée1 = {
#                 "patient":"1"
#                 }
#             with open("fhir/Immunization/"+str(i)+".json", "w") as f_write:
# c                json.dump(donnée1, f_write , indent=2)
#             print ("modifié")
#         immunization()
#     print (fichiers)
    