## # **Instalar Django.**
1. Debemos crear la carpeta donde trabajaremos: mkdir django_premiosplatzi y nos dirigimos a la carpeta creada.

2. Crear el entorno virtual con venv en Windows py -m venv venv y en linux python3 -m venv venv.

3. Activar entorno virtual Windows: .\venv\Scripts\activite y en linux source venv/Scripts/Activate si por alguna razón no funciona utilice todo el link del donde se encuentra el activador Ej: C:\Users\monbre\OneDrive\Escritorio\programación\premiosPlatzi\venv\Scripts\activate

4. Instalar django: pip install django

5. Iniciar el repositorio de git: git init

6. Iniciar el proyecto de django: django-admin startproject premiosplatziapp

7. Para evitar llevar al repositorio remoto archivos innecesarios es importante crear el archivo: .gitignore (Donde se suele agregar la carpeta venv o archivos que no se desea subir al repositorio) para Windows se crea con fsutil file createnew .gitignore 0 y linux touch .gitignore