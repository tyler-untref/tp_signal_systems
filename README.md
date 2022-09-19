![UNTREF Logo](logo.png)
# Trabajo práctico - Desarrollo de software para el cálculo de parámetros acústicos ISO 3382

## Objetivo general
El siguiente trabajo propone realizar un software modular que permita el cálculo de parámetros acústicos propuestos en la normativa ISO 3382 (UNE-EN ISO 3382, 2010). Un sistema íntegro que contemple todos los elementos necesarios para una medición in-situ.

## Objetivos particulares
Los alumnos adquirirán las siguientes habilidades:

* Desarrollo de funciones para:
    * Generación y reproducción de ruido rosa.
    * Generación y reproducción de sine sweep.
    * Adquisición de la RI.
    * Procesamiento de las RI.
* Adquirir las capacidades de interpretar los lineamientos de una normativa.
* Autonomía en la lectura del material dispuesto por los docentes.
* Autoevaluación de todo el material desarrollado.
* Presentación de avances.
* Los resultados optenidos no deben diferir en más de ±0.5 s de los arrojados por algún software comercial.
* Documentar (en [LaTeX](https://www.latex-project.org/)) el procedimiento de medición y diseño de scripts.

## Consigna
La siguiente [presentación](https://docs.google.com/presentation/d/1XJAI0wFRRS6IaVops3jCAcfdRxvMJyQs_mIetzehh1c/edit?usp=sharing) tiene el detalle de la consigna del TP.

## Entregas

<table>
	<tr>
		<th>N° de entrega</th>
		<th>Función</th>
		<th>Uso</th>
        <th>Test</th>
 	</tr>
 	<tr>
  		<td rowspan="3"><a href="">1° entrega</a></td>
   		<td>Función de sintetización de ruido rosa</td>
		<td>Se utiliza para ajustar el nivel de la fuente al menos a 45 dB por encima del nivel de ruido de fondo en la banda de frecuencia correspondiente</td>
   		<td rowspan="3" style="text-align:left"><ul><li>Corroborar que ambas funciones (Ruido rosa - Sine sweep logarítmico + Filtro
            inverso) se comportan adecuadamente utilizando, por ejemplo el software Audacity, para ver sus respectivos espectros.
        </li><li>Convolucionar un sine sweep logarítmico generado y su respectivo filtro inverso y estudiar resultados.</li><li>Reproducir y grabar de manera simultánea.</li></ul>
        </td>
 	</tr>
	<tr>
  		<td>Función de generación de sine sweep logarítmico + filtro inverso</td>
   		<td>Se utiliza para obtener la respuesta al impulso a partir del sine sweep logarítmico</td>
 	</tr>
	<tr>
  		<td>Adquisición y reproducción</td>
   		<td>Se utiliza para adquirir y reproducir las señales durante una medición in-situ.</td>
 	</tr>
    <tr>
  		<td rowspan="5"><a href="">2° entrega</a></td>
   		<td>Función de carga de archivos de audio (dataset)</td>
		<td>Se utiliza para administrar información al software y evaluar los parámetros acústicos ISO 3382 de dichos audio</td>
   		<td rowspan="5" style="text-align:left"><ul><li>Verificar el espectro de los filtros generados, utilizando scipy.</li><li>Obtener respuesta al impulso a partir de los 
            sine sweep y el filtro inverso descargados (dataset).</li>
            <li>Evaluar las respuestas al impulso sintetizadas, las respuesta al impulso generadas y sine sweep, con algún programa comercial</li></ul>
        </td>	
 	</tr>
	<tr>
  		<td>Función de sintetización de respuesta al impulso</td>
   		<td>Se utiliza evaluar el algoritmo con una señal conocida</td>
 	</tr>
    <tr>
  		<td>Función obtener respuesta al impulso</td>
   		<td>Se utiliza para obtener la respuesta al impulso a partir del sine sweep logarítmico</td>
 	</tr>
	<tr>
  		<td>Función filtros norma IEC 61260</td>
   		<td>La función filtros norma IEC 61260 es útil para filtrar la respuesta al impulso y calcular los parámetros acústicos por frecuencia</td>
 	</tr>
    <tr>
        <td>Función conversión a escala logarítmica normalizada</td>
		<td>Se utiliza para visualizar la señal en una escala más acorde al fenómeno que se estudia</td>
    </tr>
    <tr>
  		<td rowspan="5"><a href="">3° entrega</a></td>
   		<td>Función suavizado de señal</td>
   		<td>Se utiliza para las fluctuaciones producto del ruido intrínseco en la respuesta al impulso.</td>
   		<td rowspan="5" style="text-align:left">
            <ul>
                <li>Graficar en escala logarítmica la señales de interés.</li>
                <li>Probar con las respuestas al impulso sintetizadas y las muestras descargadas. En caso de utilizar más de una toma por recinto, calcular el valor medio y la desviación estándar.</li>
                <li>Graficar los resultados.</li>
                <li>Establecer la integración de todas las funciones usando un archivo de programa “main”.</li>
                <li>Compara los resultados con software específico para el análisis de señales o plugins del mercado.</li>
            </ul>
        </td>	
 	</tr>	
	<tr>
  		<td>Función integral de Schroeder</td>
   		<td>La función integral de Schroeder representa la curva de decaimiento de la energía acústica.</td>
 	</tr>
    <tr>
  		<td>Función regresión lineal por mínimos cuadrados </td>
   		<td>La función regresión lineal por mínimos cuadrados permite evaluar el tiempo de reverberación.</td>
 	</tr>
    <tr>
  		<td>Función cálculo de parámetros acústicos </td>
   		<td>Se utiliza para determinar las características acústicas de recintos cerrados</td>
 	</tr>
    <tr>
  		<td>Informe final</td>
   		<td>Realizar informe final usando LaTex y respetando el formato dado</td>
 	</tr>
    <tr>
  		<td rowspan="1">Extra</td>
   		<td>Función Lundeby</td>
		<td>Se utiliza para encontrar los extremos de integración más precisos.</td>
   		<td rowspan="1" style="text-align:left"><ul><li>Probar con las respuestas muestras descargadas nuevamente y cuantificar la diferencia respecto a no utilizar 
            Lundeby.</li></ul>
        </td>	
 	</tr>
</table>
