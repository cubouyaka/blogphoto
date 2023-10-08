from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError('Password must contain a letter', code='password_no_letters')
                
    def get_help_text(self):
        return 'Your password must contain at least a letter.'
    
class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not  any(character.isdigit() for character in password):
            raise ValidationError('Password must contain a digit number', code='password_no_digit')
        
    def get_help_text(self):
        return 'Your password must contain at least a digit number.'