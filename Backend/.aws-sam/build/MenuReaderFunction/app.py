import json
import boto3
from decimal import Decimal # Necesitas importar Decimal

# Inicializa el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('RestauranteMenu')

# ----------------------------------------------------
# Función auxiliar para manejar tipos Decimal
# ----------------------------------------------------
def decimal_default_proc(obj):
    # Si el objeto es de tipo Decimal, conviértelo a float (para precios)
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError # Si no es Decimal, lanza un error normal

def lambda_handler(event, context):
    try:
        response = table.scan()
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            # APLICA LA FUNCIÓN AUXILIAR AQUÍ:
            'body': json.dumps(
                response['Items'], 
                default=decimal_default_proc # Usa la función para manejar Decimal
            )
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }