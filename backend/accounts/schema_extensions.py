from drf_spectacular.extensions import OpenApiAuthenticationExtension

from accounts.authentication import CustomJWTAuthentication

print("DEBUG: === accounts/schema.py is being processed ===")
print(f"DEBUG: CustomJWTAuthentication class imported: {CustomJWTAuthentication}")
# Add this debug print statement
print(f"DEBUG: ID of CustomJWTAuthentication in accounts/schema.py (target_class): {id(CustomJWTAuthentication)}")


class CustomJWTAuthenticationExtension(OpenApiAuthenticationExtension):
    target_class = 'backend.accounts.authentication.CustomJWTAuthentication'
    name = 'CustomeJWTAuth'

    def get_security_definition(self, auto_schema):
        return {
            'type': 'apiKey',
            'in': 'cookie',
            'name': 'access',
            'description': 'JWT token stored in an HTTP-only cookie named "access"',
        }