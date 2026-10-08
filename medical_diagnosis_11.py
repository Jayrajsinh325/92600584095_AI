print('=====Expert System=====')
print('Answer the following questions with yes or no.')
q1=input('Do you have fever? : Yes / No\n').lower()
q2=input('DO you have cough? : Yes / NO\n').lower()
q3=input('DO you have headache? : Yes / NO\n').lower()

if q1=='no' and q2=='no' and q3=='no':
    print('You seem to be Healthy.')
elif q1=='yes' and q2=='no' and q3=='no':
    print('You may have a Mild Infaction.')
elif q1=='no' and q2=='yes' and q3=='no':
    print('You may have a Throuat Infection or Mild Infection.')
elif q1=='no' and q2=='no' and q3=='yes':
    print('You may have Strees, Magraine, or Fatigue.')
elif q1=='yes' and q2=='yes' and q3=='no':
    print('You may have Flu.')
elif q1=='yes' and q2=='no' and q3=='yes':
    print('You may have a Viral Fever.')
elif q1=='no' and q2=='yes' and q3=='yes':
    print('You may have Common Cold.')
elif q1=='yes' and q2=='yes' and q3=='yes':
    print('You may have Flu or a Viral Infection.')
else :
    print('Please, Give proper answer about your health.')