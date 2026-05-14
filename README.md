Sistema de Tickets de Soporte TI
📌 Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de tickets de soporte técnico por consola para la empresa TechSoluciones S.A..

El sistema permite registrar incidencias, consultar tickets, listarlos y marcarlos como resueltos durante una sesión de trabajo.

Todos los tickets se almacenan temporalmente en una lista en memoria mientras el programa está en ejecución.

🧩 Caso de negocio

La empresa TechSoluciones S.A. recibe decenas de solicitudes de soporte diariamente y necesita una solución sencilla para administrar incidencias técnicas de manera organizada.

El objetivo del sistema es facilitar al equipo de TI:

Registrar tickets de soporte
Consultar información de tickets
Listar tickets registrados
Cambiar el estado de tickets
Generar reportes básicos

🗂️ Estructura de datos

Todos los tickets se almacenan en una lista llamada:

tickets = []

La lista se crea en main.py y se comparte con las diferentes funciones del sistema.

Cada ticket contiene información relacionada con:

Número de ticket
Descripción de la incidencia
Especialista asignado
Tipo de asunto
Fuente del ticket
Prioridad
Fecha y hora de apertura
Estado del ticket
⚙️ Funcionalidades del sistema
📥 Registro de tickets

Permite crear nuevos tickets de soporte ingresando la información correspondiente.

🔎 Consulta y listado

Permite visualizar tickets registrados y consultar información específica.

✅ Cierre y reporte

Permite actualizar el estado de los tickets y generar reportes básicos del sistema.

👥 Participantes del grupo
Angelica Herrera Gonzalez
Andrea LLorenta
Esteban Cordero
[Nombre integrante 4]
🛠️ Tecnologías utilizadas
Python
Git
GitHub
Consola / Terminal
▶️ Ejecución del proyecto

Clonar el repositorio:

git clone URL_DEL_REPOSITORIO

Ingresar a la carpeta del proyecto:

cd TIFC-PF-Sistema-Tickets

Ejecutar el programa:

python main.py
