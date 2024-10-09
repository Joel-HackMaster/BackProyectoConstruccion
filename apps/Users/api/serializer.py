from rest_framework import serializers
from django.core.mail import send_mail
from apps.Users.models import User
from email_validator import validate_email, EmailNotValidError
from fuzzywuzzy import process
from django.conf import settings
import Levenshtein

#Lista de dominios comunes
common_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('email',)

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError('Tienes que indicar un correo')
    
        try:
            validated_email = validate_email(value, check_deliverability=False)
            email = validated_email["email"]
        except EmailNotValidError as e:
            raise serializers.ValidationError(str(e))
        
        local_part, domain = email.split('@')
        best_match = max(common_domains, key=lambda x: Levenshtein.ratio(x, domain))
        similarity = Levenshtein.ratio(best_match, domain)
        print(similarity)
        if similarity < 0.8:
            corrected_email = f"{local_part}@{best_match}"
            raise serializers.ValidationError(f"¿Quisiste decir {corrected_email}?")
        
        return email
    
    def save(self, **kwargs):
        try:
            print(self.validated_data.get('email'))
            subject = "Bienvenido a nuetra plataform recibiras nuestras ofertas"
            message = 'Gracias por registrarte en nuestra plataforma.'
            recipient_list = [self.validated_data.get('email')]
            send_mail(subject, message, None, recipient_list)
            user = super().save(**kwargs)
            return user
        except Exception as e:
            raise serializers.ValidationError(str(e))

