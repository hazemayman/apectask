from django import forms

Faculty_choices = ['Engineering' , 'Medicine' , 'Commerce' ,'Arts' , 'MassCommunication' , 'ComputerScience']
Univesity_choices= [
    ('Cairo', 'Cairo'),
    ('Ain Shams', 'Ain Shams'),
    ('Helwan', 'Helwan'),
]
faculty_choices= [
    ('Engineering', 'Engineering'),
    ('Medicine', 'Medicine'),
    ('Commerce', 'Commerce'),
    ('Arts', 'Arts'),
    ('MassCommunication', 'MassCommunication'),
    ('ComputerScience', 'ComputerScience'),
]
academic_year = [
    ('Freshman', 'Freshman'),
    ('First year', 'First year'),
    ('Second year', 'Second year'),
    ('Third year', 'Third year'),
    ('Fourth year', 'Fourth year'),
]
preferences = [
    ('PR', 'PR'),
    ('HT', 'HT'),
    ('IT', 'IT'),
    ('mm', 'mm'),
]

TeamChoices = [
    ('Alone' , 'Alone'),
    ('Team' , 'Team'),
]
LeaderChoices = [
    ('yes' , 'yes'),
    ('no' , 'no'),
]


class FirstPage(forms.Form):
 
    Name = forms.CharField(label='Your name ', max_length=100)
    MobileNumber = forms.CharField(label='Mobile Number ', max_length=20)
    Univesity = forms.CharField(label='what is your university ? ', widget=forms.Select(choices=Univesity_choices))
    Faculty = forms.CharField(label='what is your faculty ? ', widget=forms.Select(choices=faculty_choices))
    Academic_year = forms.CharField(label='what is your Academic Year ? ', widget=forms.Select(choices=academic_year))
    First_preference = forms.CharField(label='what is your first preference ? ', widget=forms.Select(choices=preferences))
    Second_preference = forms.CharField(label='what is your second preference ? ', widget=forms.Select(choices=preferences))
    Previous_experience = forms.CharField(label = "what is your previous experience ? " ,widget=forms.Textarea)


class SecondPage(forms.Form):

    Whyapec = forms.CharField(label = "Why Choosing APEC ? " , widget=forms.Textarea)
    Hear = forms.CharField(label = "Why Choosing APEC ? "  , max_length = 100)
    First_second_pref = forms.CharField(label = "Why did you choose your first and second prefernces ? " , widget=forms.Textarea)
    Percentage = forms.CharField(label = "what pecentage do you prefer your first to second prefernces ? "  , max_length = 100)
    Expect = forms.CharField(label = "if you are accepted, what are your expectations from the year ? " , widget=forms.Textarea)
    PersonalSkills =  forms.CharField(label = "what personal skills would you like to improve by the end of the year ? " , widget=forms.Textarea)



class ThirdPage(forms.Form):

    ALone_team = forms.ChoiceField(label = "do you work in team or work alone ? " ,widget = forms.RadioSelect , choices = TeamChoices )
    Schedule =  forms.CharField(label = "how do you schedule your day ? " ,widget=forms.Textarea )
    Learn = forms.CharField(label = "state a time in which you learned something by yoursel. (I.e not necessarily Academic ) " ,widget=forms.Textarea)
    LeaderRadio = forms.ChoiceField(label = "do you prefer being a leader ? Explain " ,widget=forms.RadioSelect, choices = LeaderChoices )
    LeaderChar =  forms.CharField(label = '' , widget=forms.Textarea)



