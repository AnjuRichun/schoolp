from django import forms
from detailapp.models import Student, Course
class StudentForm(forms.ModelForm):
    class Meta:
        model =Student
        fields = '__all__'
    name=forms.CharField()
    DOB =forms.DateField()
    age= forms.IntegerField()
    gender= forms.CharField()
    phone_number= forms.CharField()
    email_id= forms.EmailField()
    address =forms.CharField(widget=forms.Textarea)
    department= forms.Select()
    course=forms.Select()
    purpose= forms.Select()
    materials_provide=forms.MultipleChoiceField(choices=[('debit','debit note books'),('pen','pen'),('exam papers','exam papers')],widget=forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()
        if 'department' in self.data:
            try:
                department_id=int(self.data.get('department'))
                self.fields['course'].queryset=Course.objects.filter(department_id=department_id).order_by('name')
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset=self.instance.department.course_set.order_by('name')

