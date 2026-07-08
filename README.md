# Sistema de Pedidos de Comida

## Integrantes del Grupo B25

- Pertile, Valentina Giuliana
- Gómez, Luciana Magali 
  

## Comisión

Comisión: K 1.2. (Comisión 2)


## Descripción general

Link al github: https://github.com/gomezlucianamagali05-cmd/Grupo-B25-Trabajo-Final---Integrador-PYTHON-.git

Este proyecto consiste en un sistema de gestión de pedidos para un local gastronómico desarrollado en Python y ejecutado por consola.

El sistema permite administrar pedidos de clientes mediante un menú interactivo. Entre sus principales funcionalidades se encuentran:

- Visualización del menú de productos.
- Selección de productos y cantidades.
- Cálculo automático del importe total.
- Aplicación de promociones y descuentos.
- Selección del medio de pago.
- Registro de pedidos realizados.
- Generación de estadísticas básicas de ventas.

Durante el desarrollo se implementaron estructuras condicionales, ciclos, funciones, validaciones de datos, acumuladores, contadores y manejo básico de errores, cumpliendo con los requisitos establecidos en la consigna.

## Manual de Ejecución del Sistema
Video explicativo: https://drive.google.com/drive/folders/1Z4bsZEAPeBCFwExRil5s3jcOxeAUL957?usp=drive_link

Al iniciar el programa, se visualizará el **Menú Principal** en la consola con tres opciones numéricas. Para ejecutar cualquiera de ellas, se debe ingresar el número correspondiente y presionar **Enter**.

---

### Opción 1: Crear Pedido

Esta opción gestiona toda la compra de un cliente en tiempo real a través de los siguientes pasos:

1. **Selección de Categoría:** El sistema mostrará el listado de categorías disponibles (1. Entradas, 2. Principales, 3. Bebidas, 4. Postres) y una opción extra para finalizar. Ingrese el número de la categoría deseada y presione **Enter**.
2. **Selección del Producto:** Se desplegarán los productos de la categoría elegida con sus precios. Ingrese el número del producto que el cliente quiere llevar y presione **Enter**.
3. **Ingreso de Cantidad:** El sistema solicitará la cantidad de unidades. Ingrese un número entero entre 1 y 50, y presione **Enter**.
4. **Continuidad del Pedido:** En la pantalla aparecerá la pregunta `¿Desea agregar otro producto? (SI/NO):`.
* **Para seguir cargando:** Escriba `SI` y presione **Enter**. El sistema lo regresará al listado de categorías para repetir el proceso.
* **Para cerrar la orden:** Escriba `NO` y presione **Enter**.


5. **Procesar el Pago:** El programa mostrará el resumen de lo consumido, el subtotal y el menú de medios de pago. Ingrese el número del método de pago elegido (1. Efectivo, 2. Débito, 3. Crédito, 4. Transferencia) y presione **Enter**.
6. **Finalización:** El sistema calculará el descuento correspondiente, mostrará el **TOTAL A PAGAR**, actualizará los datos internos de la caja y lo devolverá automáticamente al Menú Principal.

---

### Opción 2: Ver Estadísticas del Día

Esta opción se utiliza para monitorear el estado de las ventas del comercio en el turno actual sin alterar los datos.

1. En el Menú Principal, ingrese el número `2` y presione **Enter**.
2. El sistema imprimirá en pantalla un bloque de información con:
* **Clientes atendidos:** Cantidad de pedidos completados con éxito.
* **Caja total:** El dinero neto acumulado (con los descuentos ya restados).
* **Ticket promedio:** El gasto estimado por cliente (este dato solo aparece si ya se registró al menos un pedido).


3. Tras mostrar los datos, el programa lo dejará nuevamente en el Menú Principal listo para otra acción.

---

### Opción 3: Salir

Esta opción finaliza la jornada laboral y cierra la ejecución del programa.

1. En el Menú Principal, ingrese el número `3` y presione **Enter**.
2. El sistema ejecutará automáticamente una última lectura de las estadísticas, mostrando en pantalla el balance y cierre final de la caja del día.
3. Se mostrará el mensaje de despedida `¡Hasta la próxima!` y el programa finalizará de forma segura, liberando la consola de comandos.

---

## Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizaron herramientas de Inteligencia Artificial como apoyo al aprendizaje, la resolución de problemas y la organización del trabajo en equipo.

* **Claude** fue utilizado como herramienta de asistencia durante el desarrollo del código mediante preguntas sobre errores encontrados y posibles soluciones, la estructura del programa y el funcionamiento de diferentes características y herramientas del lenguaje Python. Las respuestas obtenidas fueron analizadas y utilizadas como guía para corregir y mejorar el código.

* **ChatGPT (OpenAI)** fue utilizado como apoyo en la organización y división de tareas entre los integrantes del grupo, en la redacción de descripciones para los commits realizados y en consultas relacionadas con el uso de GitHub y Visual Studio Code (VS Code).

En todos los casos, las respuestas y sugerencias generadas por estas herramientas fueron revisadas, analizadas y adaptadas por los integrantes del grupo antes de ser aplicadas al proyecto. La utilización de IA se realizó como herramienta de apoyo, manteniendo la comprensión y validación de las decisiones tomadas durante el desarrollo del sistema.
