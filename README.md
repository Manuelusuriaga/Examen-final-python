# Examen-final-python

Aplicación de Seguimiento de Gastos
Contexto: Crea una aplicación de terminal para el seguimiento de gastos personales. Los usuarios deben poder registrar sus ingresos y gastos, listar los gastos ordenados por fecha y generar un balance que contenga el total de los gastos, el total de ingresos, la capacidad de ahorro (diferencia entre ingresos totales y gastos totales)

Las funciones a implementar son:

1. Agregar Transacción: Esta función recibe los datos de una transacción (monto, fecha, descripción y tipo) y la agrega a la lista de transacciones.

2. Listar Transacciones: Muestra una lista de transacciones ordenadas por fecha en la consola.

3. Balance: Calcula el balance financiero actual: ingresos, gastos y capacidad de ahorro (ingresos - egresos).

4. Guardar Datos: Guarda la lista de transacciones en un archivo llamado 'datos_financieros.pkl' utilizando el módulo pickle.

5. Cargar Datos: Intenta cargar los datos previos de transacciones desde el archivo 'datos_financieros.pkl' utilizando pickle. Si el archivo no existe, inicializa en un estado vacío.
