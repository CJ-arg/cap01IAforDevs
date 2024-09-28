# CHALLENGE: Copilotos

Este challenge tiene como objetivo comprender y afianzar las mejores prácticas en el uso de copilotos para código impulsados por IA y entender cómo pueden mejorar la eficiencia y productividad en el desarrollo de software.

Este homework está diseñado no solo para aquellos familiarizados con el desarrollo de software y el uso de APIs, sino también para quienes pueden ser nuevos en la programación o en el uso específico de Python y FastAPI. Una de las metas principales es demostrar cómo, incluso sin un profundo conocimiento previo del lenguaje o del framework, una persona puede crear una API simple y funcional con la ayuda de un copiloto de código impulsado por IA.

Antes de comenzar, es esencial familiarizarte con algunas herramientas y librerías que se utilizarán:
- **FastAPI**: Un moderno framework web para construir APIs con Python 3.7+ que es rápido (de alta performance), fácil de aprender, y viene con soporte automático para documentación.
- **Pydantic**: Utilizado para la validación de datos y la configuración del esquema de tu API utilizando Python type annotations.
- **Passlib**: Para el cifrado de contraseñas.
- **PyJWT**: Para generar y verificar tokens JWT en el proceso de autenticación.

## Configuración del ambiente
Es recomendable crear un ambiente virtual para manejar las dependencias de manera aislada. Una vez localizado dentro de la carpeta `CAP01_CHALLENGE` Puedes hacerlo ejecutando:
```
python3 -m venv venv
```
Para activar el ambiente virtual, usa el siguiente comando:

En Windows:
```
.\venv\Scripts\activate
```

En Unix o MacOS:
```
source venv/bin/activate
```

## Instalacion de dependencias
Una vez activado el ambiente virtual, instala las dependencias necesarias ejecutando:
```
pip install -r requirements.txt
```

## Ejecutar tu aplicación
Para iniciar tu API FastAPI, ejecuta:
```
uvicorn main:app --reload
```

## Endpoints básicos de la API
Recuerda trabajar sobre el archivo `main.py`
1. ### Bubble Sort
- Ruta: `/bubble-sort`
- Método: `POST`
- Descripción: Recibe una lista de números y devuelve la lista ordenada utilizando el algoritmo de Bubble Sort.
- Entrada: `{"numbers": [lista de números]}`
- Salida: `{"numbers": [lista de números ordenada]}`
2. ### Filtro de Pares
- Ruta: `/filter-even`
- Método: `POST`
- Descripción: Recibe una lista de números y devuelve únicamente aquellos que son pares.
- Entrada: `{"numbers": [lista de números]}`
- Salida: `{"even_numbers": [lista de números pares]}`
3. ### Suma de Elementos
- Ruta: `/sum-elements`
- Método: `POST`
- Descripción: Recibe una lista de números y devuelve la suma de sus elementos.
- Entrada: `{"numbers": [lista de números]}`
- Salida: `{"sum": suma de los números}`
4. ### Máximo Valor
- Ruta: `/max-value`
- Método: `POST`
- Descripción: Recibe una lista de números y devuelve el valor máximo.
- Entrada: `{"numbers": [lista de números]}`
- Salida:  `{"max": número máximo}`
5. ### Búsqueda Binaria
- Ruta: `/binary-search`
- Método: `POST`
- Descripción: Recibe un número y una lista de números ordenados. Devuelve true y el índice si el número está en la lista, de lo contrario false y -1 como index.
- Entrada: `{"numbers": [lista de números], "target": int}`
- Salida:  `{"found": booleano, "index": int}`


El payload debe estar definido por:


```python 
class BinarySearchPayload(BaseModel):
    numbers: List[int]
    target: int
```

### 1. Implementación de Autenticación
- **Objetivo**: Añadir un sistema de autenticación básico utilizando tokens.
- **Descripción**: Implementa un endpoint para la creación de usuarios y otro para el inicio de sesión. Los usuarios deben autenticarse para poder acceder a los endpoints existentes.
- **Ruta Registro**: `/register`
  - **Método**: `POST`
  - **Entrada (Body)**: `{"username": "user1", "password": "pass1"}`
  - **Salida**: `{"message": "User registered successfully"}`
  - **Status Code**:
    - 200: Registro exitoso
    - 400: El usuario ya existe
- **Ruta Login**: `/login`
  - **Método**: `POST`
  - **Entrada (Body)**: `{"username": "user1", "password": "pass1"}`
  - **Salida**: `{"access_token": <token_de_acceso>}`
  - **Status Code**:
    - 200: Login Exitoso
    - 401: Credenciales Inválidas

### 2. Cifrado de Contraseñas
- **Objetivo**: Mejorar la seguridad almacenando las contraseñas de manera segura.
- **Descripción**: Utiliza `CryptContext` de `passlib` para cifrar las contraseñas antes de guardarlas en tu base de datos simulada (`fake_db`).

### Nota Sobre Autenticación con Tokens JWT

Recuerda que, una vez registrado e iniciado sesión, se debe generar un token JWT con algoritmo HS256. Este token debe incluirse como un parámetro de consulta (`query parameter`) llamado `token` en cada solicitud a los endpoints protegidos. El token sirve como tu credencial de autenticación, permitiendo que el sistema verifique tu identidad y autorice tu acceso a los recursos solicitados.



Por ejemplo, si deseas acceder a un endpoint protegido después de haber iniciado sesión, tu solicitud podría verse así:

```
POST /some-protected-endpoint?token=<tu_token_jwt_aquí>
```

Asegúrate de reemplazar `<tu_token_jwt_aquí>` con el token JWT real que recibiste como respuesta del endpoint de login. La ausencia de este token o el uso de un token inválido resultará en una respuesta de error, indicando que no estás autorizado para acceder al recurso solicitado.

Este mecanismo de autenticación es crucial para la seguridad de la aplicación, asegurando que solo los usuarios autenticados puedan acceder a ciertos endpoints y realizar acciones específicas.


- **Status Code**:
  - 200: Operacion Exitosa
  - 401: Credenciales Inválidas / Autorización fállida.

##### Nota: ```Por simplicidad, este proyecto utiliza parámetros de consulta para pasar el token JWT. En aplicaciones de producción, se recomienda usar headers de autorización para tokens y el cuerpo de la solicitud para credenciales de usuario, adheriéndose a las mejores prácticas de seguridad para proteger la información sensible.```

Recuerda hacer uso del comando `/doc` en el copiloto para documentar tus funciones.

## Ejemplo de Uso
```
Entrada: {"numbers": [5, 3, 8, 6, 1, 9]}
```
- Salida Bubble Sort:  `{"numbers": [1, 3, 5, 6, 8, 9]}`
- Salida Filtro de Pares: `{"even_numbers": [8, 6]}`
- Salida Suma de Elementos: `{"sum": 32}`
- Salida Máximo Valor: `{"max": 9}`

#### Registro de Usuario
```bash
curl -X 'POST' \
  'http://localhost:8000/register' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "user1",
  "password": "pass1"
}'
```

#### Inicio de Sesión
```bash
curl -X 'POST' \
  'http://localhost:8000/login' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "user1",
  "password": "pass1"
}'
```
Este comando devolverá un token que deberás usar en las siguientes solicitudes como parte del parámetro \`token\`.

#### Bubble Sort (Autorizado)
Asegúrate de reemplazar `<TOKEN>` con el token obtenido durante el inicio de sesión.
```bash
curl -X 'POST' \
  'http://localhost:8000/bubble-sort?token=<TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "numbers": [3, 2, 1]
}'
```

#### Filtro de Pares (Autorizado)
```bash
curl -X 'POST' \
  'http://localhost:8000/filter-even?token=<TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "numbers": [5, 3, 8, 6, 1, 9]
}'
```

#### Suma de Elementos (Autorizado)
```bash
curl -X 'POST' \
  'http://localhost:8000/sum-elements?token=<TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "numbers": [5, 3, 8, 6, 1, 9]
}'
```

#### Máximo Valor (Autorizado)
```bash
curl -X 'POST' \
  'http://localhost:8000/max-value?token=<TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "numbers": [5, 3, 8, 6, 1, 9]
}'
```

#### Búsqueda Binaria (Autorizado)
```bash
curl -X 'POST' \
  'http://localhost:8000/binary-search?token=<TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "numbers": [1, 2, 3, 4, 5],
  "target": 3
}'
```



### Este archivo main.py implementa una API web utilizando FastAPI que ofrece varios servicios relacionados con operaciones matemáticas y búsqueda, con un sistema de autenticación básico.

El propósito principal de este código es proporcionar una serie de endpoints que realizan diferentes operaciones con números, como ordenación, filtrado, suma, búsqueda del valor máximo y búsqueda binaria. Además, incluye funcionalidades de registro e inicio de sesión de usuarios.

La API toma como entrada listas de números y, en algunos casos, un número objetivo. También acepta información de usuario para el registro y el inicio de sesión. Las entradas se envían en formato JSON a través de solicitudes HTTP POST.

Como salida, la API devuelve los resultados de las operaciones realizadas, también en formato JSON. Por ejemplo, para la ordenación de burbuja, devuelve la lista ordenada; para el filtrado de números pares, devuelve la lista de números pares; para la suma, devuelve el total, y así sucesivamente.

El código logra su propósito implementando cada operación como una función separada. Utiliza algoritmos comunes como la ordenación de burbuja y la búsqueda binaria. Para la autenticación, utiliza tokens JWT (JSON Web Tokens) para mantener las sesiones de usuario.

En cuanto a los flujos de lógica importantes, el código verifica la autenticación del usuario antes de realizar cualquier operación. Si el token no es válido, se devuelve un error. Además, para el registro de usuarios, se verifica si el usuario ya existe antes de crear uno nuevo, y para el inicio de sesión, se comprueba si las credenciales son correctas antes de generar un token.

En resumen, este código crea una API web que ofrece servicios matemáticos básicos y de búsqueda, con un sistema de autenticación simple, proporcionando una plataforma segura para realizar estas operaciones a través de internet.


## Correr Pruebas
Para validar la funcionalidad de tu API, utiliza pytest para ejecutar el módulo de pruebas automatizadas. Asegúrate de estar en el directorio raíz del proyecto y ejecuta:
```
pytest tests.py
```
Esto correrá todas las pruebas definidas en tests.py y te mostrará los resultados.
