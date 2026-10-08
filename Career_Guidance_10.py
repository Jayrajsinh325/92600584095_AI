print("===================================")
print("   CAREER GUIDANCE SYSTEM   ")
print("===================================")
coding=input("Do you like Coding ? Yes or No :").lower()
mathematics=input("Do you like Mathematics ? Yes or No :").lower()
biology=input("Do you like Biology ? Yes or No :").lower()
drawing =input("Do you like Drawing ? Yes or No :").lower()

print("========= Career Suggestion ========")

if(coding=='no' and mathematics=='no' and biology=='no' and drawing=='no'):
    print("Suggested Career: Explore your interest and career option furthur.")
    
elif(coding=='no' and mathematics=='no' and biology=='no' and drawing=='yes'):
    print("Suggested Career: Graphic Designer/ Animator")
    
elif(coding=='no' and mathematics=='no' and biology=='yes' and drawing=='no'):
    print("Suggested Career: Pharmacist / Nurse")
    
elif(coding=='no' and mathematics=='no' and biology=='yes' and drawing=='yes'):
    print("Suggested Career: Medical illusrator / Heathcare Educator")
    
elif(coding=='no' and mathematics=='yes' and biology=='no' and drawing=='no'):
    print("Suggested Career: Engineer / Data Analyst")
    
elif(coding=='no' and mathematics=='yes' and biology=='no' and drawing=='yes'):
    print("Suggested Career: Architach")
    
elif(coding=='no' and mathematics=='yes' and biology=='yes' and drawing=='no'):
    print("Suggested Career: Doctor")
    
elif(coding=='no' and mathematics=='yes' and biology=='yes' and drawing=='yes'):
    print("Suggested Career: Medical illusrator / Biomedical Designer")
    
elif(coding=='yes' and mathematics=='no' and biology=='no' and drawing=='no'):
    print("Suggested Career: Programmer / Web Devloper")
    
elif(coding=='yes' and mathematics=='no' and biology=='no' and drawing=='yes'):
    print("Suggested Career: Web Designer / UI-UX Desiner")
    
elif(coding=='yes' and mathematics=='no' and biology=='yes' and drawing=='no'):
    print("Suggested Career: Heath App Devloper")
    
elif(coding=='yes' and mathematics=='no' and biology=='yes' and drawing=='yes'):
    print("Suggested Career: Medical illusrator")
    
elif(coding=='yes' and mathematics=='yes' and biology=='no' and drawing=='no'):
    print("Suggested Career: Software Engineer / Computer Scientist")
    
elif(coding=='yes' and mathematics=='yes' and biology=='no' and drawing=='yes'):
    print("Suggested Career: Game Developer / UI Engineer")

elif(coding=='yes' and mathematics=='yes' and biology=='yes' and drawing=='no'):
    print("Suggested Career: Bioinformatics Scientist")
    
elif(coding=='yes' and mathematics=='yes' and biology=='yes' and drawing=='yes'):
    print("Suggested Career: Biomedical Software Engineer / Medical Technology Specialist")

else:
    print("Choose Data Properly")
    
print("Thank you for Using the Career Guidance Expert System!")