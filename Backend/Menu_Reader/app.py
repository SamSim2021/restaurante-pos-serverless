# Contenido de backend/menu_reader/app.py
import json
import boto3

# Inicializa el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb')
# Asegúrate de que el nombre de la tabla coincida exactamente
table = dynamodb.Table('RestauranteMenu')

def lambda_handler(event, context):
    """
    Función que lee todos los ítems de la tabla RestauranteMenu.
    """
    try:
        response = table.scan()
        
        return {
            'statusCode': 200,
            'headers': {
                # Esta cabecera es CRUCIAL para que el frontend pueda acceder a la API.
                'Access-Control-Allow-Origin': '*' 
            },
            'body': json.dumps(response['Items'])
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }