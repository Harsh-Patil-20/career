from django.shortcuts import render
import numpy as np
import pandas as pd
from django.urls import path
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
import os
import pandas as pd
import pickle
#def index(request):
#   return render(request,'index.html')

def homepage_view(request):
    """Renders the new homepage."""
    return render(request, 'home.html')

def questionnaire_view(request):
    return render(request,'index.html') # Renders the form template

my_dir = os.path.dirname(__file__)
pickle_file_path = os.path.join(my_dir, 'lr_clf.pkl')
with open(pickle_file_path, 'rb') as pickle_file:
    model = pickle.load(pickle_file)
def predict(request):
     if request.method=='POST':       
        temp={}
        p={} #personality dict
        d={"Strongly Disagree": 1,"Disagree":2,"Slightly Disagree":3,"Neutral":4,"Slightly Agree":5,"Agree":6,"Strongly Agree":7}
        temp['Database Fundamentals'] = int(request.POST.get('db_rating'))
        temp['Computer Architecture'] = int(request.POST.get('comp_arch_rating'))
        temp['Distributed Computing Systems'] = int(request.POST.get('dist_comp_rating'))
        temp['Cyber Security'] = int(request.POST.get('cybersecurity'))
        temp['Networking'] = int(request.POST.get('networking'))
        temp['Software Development'] = int(request.POST.get('development'))
        temp['Programming Skills'] = int(request.POST.get('programmingskills'))
        temp['Project Management'] = int(request.POST.get('project_management_rating'))
        temp['Computer Forensics Fundamentals'] = int(request.POST.get('computer_forensics_fundamental_rating'))
        temp['Technical Communication'] = int(request.POST.get('technical_communication_rating'))
        temp['AI ML'] = int(request.POST.get('ai_ml_rating'))
        temp['Software Engineering'] = int(request.POST.get('software_eng_rating'))
        temp['Business Analysis'] = int(request.POST.get('business_analysis_rating'))
        temp['Communication skills'] = int(request.POST.get('communication_skills_rating'))
        temp['Data Science'] = int(request.POST.get('data_science_rating'))
        temp['Troubleshooting skills'] = int(request.POST.get('troubleshooting-rating'))
        temp['Graphics Designing'] = int(request.POST.get('graphics-designing-rating'))
        p['ext1']=int(d[request.POST.get('ext1')])
        p['ext2']=int(d[request.POST.get('ext2')])
        p['ext3']=int(d[request.POST.get('ext3')])
        p['ext4']=int(d[request.POST.get('ext4')])
        p['est1']=int(d[request.POST.get('est1')])
        p['est2']=int(d[request.POST.get('est2')])
        p['est3']=int(d[request.POST.get('est3')])
        p['est4']=int(d[request.POST.get('est4')])
        p['agr1']=int(d[request.POST.get('agr1')])
        p['agr2']=int(d[request.POST.get('agr2')])
        p['agr3']=int(d[request.POST.get('agr3')])
        p['agr4']=int(d[request.POST.get('agr4')])
        p['csn1']=int(d[request.POST.get('csn1')])
        p['csn2']=int(d[request.POST.get('csn2')])
        p['csn3']=int(d[request.POST.get('csn3')])
        p['csn4']=int(d[request.POST.get('csn4')])
        p['opn1']=int(d[request.POST.get('opn1')])
        p['opn2']=int(d[request.POST.get('opn2')])
        p['opn3']=int(d[request.POST.get('opn3')])
        p['opn4']=int(d[request.POST.get('opn4')])
        p['otc']=int(d[request.POST.get('otc')])
        p['hed']=int(d[request.POST.get('hed')])
        p['ste1']=int(d[request.POST.get('ste1')])
        p['ste2']=int(d[request.POST.get('ste2')])
        p['ste3']=int(d[request.POST.get('ste3')])
        p['ste4']=int(d[request.POST.get('ste4')])
        p['con']=int(d[request.POST.get('con')])
        p['emo']=int(d[request.POST.get('emo')])
        p['set1']=int(d[request.POST.get('set1')])
        p['set2']=int(d[request.POST.get('set2')])
        p['set3']=int(d[request.POST.get('set3')])
        p['set4']=int(d[request.POST.get('set4')])   
        temp['Extraversion'] = (p['ext1'] + p['ext2'] + p['ext3'] + p['ext4'])/28
        temp['Agreeableness'] = (p['agr1'] + p['agr2'] + p['agr3'] + p['agr4'])/28
        temp['Conscientousness'] = (p['csn1'] + p['csn2'] + p['csn3'] + p['csn4'])/28
        temp['Openness'] = (p['opn1'] + p['opn2'] + p['opn3'] + p['opn4'])/28
        temp['Emotional_Range'] = p['emo']/7
        temp['Openness to Change'] = p['otc']/7
        temp['Hedonism'] = p['hed']/7
        temp['Self-enhancement'] = (p['ste1'] + p['ste2'] + p['ste3'] + p['ste4'])/28
        temp['Self-transcendence'] = (p['set1'] + p['set2'] + p['set3'] + p['set4'])/28
        temp['Conversation'] = p['con']/7
        testdata = pd.DataFrame([temp], columns=model.feature_names_in_)
        scoreval=model.predict(testdata)[0]
        pred=''
        if scoreval == 0:
               pred = 'AI ML Specialist'
        elif scoreval==1:
            pred = 'API Specialist'
        elif scoreval ==2:
            pred = 'Application Support Engineer'
        elif scoreval ==3:
            pred = 'Business Analyst'
        elif scoreval ==4:
            pred = 'Customer Service Executive'
        elif scoreval ==5:
            pred = 'Cyber Security Specialist'
        elif scoreval ==6:
            pred = 'Database Administrator'
        elif scoreval ==7:
            pred = 'Graphics Designer'
        elif scoreval ==8:
            pred = 'Hardware Engineer'
        elif scoreval ==9:
            pred = 'Helpdesk Engineer'
        elif scoreval ==10:
            pred = 'Information Security Specialist'
        elif scoreval ==11:
            pred = 'Networking Engineer'
        elif scoreval ==12:
            pred = 'Project Manager'
        elif scoreval ==13:
            pred = 'Software Developer'
        elif scoreval ==14:
            pred = 'Software tester'
        elif scoreval ==15:
            pred ='Technical Writer'
        probs_1= model.predict_proba(testdata) 
        probs=probs_1[0]
        m=len(probs)

        roles = {
            0: 'AI ML Specialist', 1: 'API Specialist', 2: 'Application Support Engineer',
            3: 'Business Analyst', 4: 'Customer Service Executive', 5: 'Cyber Security Specialist',
            6: 'Database Administrator', 7: 'Graphics Designer', 8: 'Hardware Engineer',
            9: 'Helpdesk Engineer', 10: 'Information Security Specialist', 11: 'Networking Engineer',
            12: 'Project Manager', 13: 'Software Developer', 14: 'Software Tester', 15: 'Technical Writer'
        }

        # Sorting the probabilities and selecting top 3 roles
        top_indices = np.argsort(probs)[-3:][::-1]  # Get indices of top 3 roles
        top_roles = [(roles[i], int(probs[i] * 100)) for i in top_indices]  # Get role names and percentages

        return render(request, 'result.html', {
            'result': pred,
            'x': top_roles[0][0],  # Most likely role
            'y': top_roles[1][0],  # Second most likely
            'z': top_roles[2][0]   # Third most likely
        })
