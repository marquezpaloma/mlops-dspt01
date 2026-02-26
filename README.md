# mlops-dspt01
Proyecto M5 – Sistema de Monitoreo y Gestión del Ciclo de Vida de un Modelo ML

🎯 Objetivo del Proyecto

El objetivo de este proyecto fue desarrollar un pipeline completo de Machine Learning bajo un enfoque MLOps, cubriendo todas las etapas del ciclo de vida del modelo:
	•	📂 Organización estructurada del proyecto
	•	🧹 Limpieza y preparación de datos
	•	⚙️ Ingeniería de features
	•	🤖 Entrenamiento y evaluación de modelos
	•	🚀 Simulación de despliegue
	•	📈 Monitoreo y detección de drift
	•	📊 Generación de reportes y métricas comparativas

Se trabajó bajo un flujo profesional utilizando control de versiones (Git), trabajo por branches y buenas prácticas de estructura modular.

⸻

🔹 Avance 1 – Estructura y Organización del Proyecto

📌 Objetivo

Crear una base sólida y escalable para el desarrollo del pipeline ML.

🛠️ Implementación

Se estructuró el repositorio en carpetas organizadas:
	•	data/ → datasets originales y procesados
	•	notebooks/ → exploración y experimentación
	•	src/ → scripts productivos (feature engineering, deploy, monitoring)
	•	models/ → modelo entrenado (model.pkl)
	•	reports/ → métricas y visualizaciones
	•	README.md y requirements.txt

🎯 Conclusión del avance

Se estableció una arquitectura clara y modular, permitiendo separar código experimental del código productivo.

💡 Insight

Una buena estructura inicial reduce deuda técnica futura y facilita escalabilidad.

⸻

🔹 Avance 2 – Limpieza de Datos e Ingeniería de Features

📌 Objetivo

Preparar los datos para el entrenamiento del modelo.

🛠️ Implementación
	•	Limpieza de valores nulos
	•	Conversión de variables categóricas
	•	Normalización / transformación de variables
	•	Creación de nuevas features relevantes

Se documentó el proceso en notebooks y luego se trasladó a scripts reutilizables dentro de src/.

🔎 Hallazgos
	•	Algunas variables tenían alta dispersión.
	•	Se detectaron columnas con poca relevancia predictiva.
	•	La calidad del dataset impactaba directamente en estabilidad del modelo.

🎯 Conclusión

La ingeniería de features fue determinante en la mejora del rendimiento del modelo.

💡 Insight

El rendimiento del modelo depende más de la calidad del feature engineering que del algoritmo elegido.

⸻

🔹 Avance 3 – Entrenamiento y Evaluación del Modelo

📌 Objetivo

Entrenar un modelo supervisado y evaluar su desempeño.

🛠️ Implementación
	•	División en train/test
	•	Entrenamiento del modelo
	•	Generación de métricas:
	•	Accuracy
	•	Precision
	•	Recall
	•	F1-score
	•	Curva ROC
	•	Comparación entre modelos

El modelo final se guardó como model.pkl en la carpeta models/.

🔎 Hallazgos
	•	Se observó balance entre precision y recall.
	•	La curva ROC permitió visualizar claramente la capacidad discriminatoria.
	•	Algunos modelos mostraban overfitting inicial.

🎯 Conclusión

Se seleccionó el modelo con mejor equilibrio entre métricas y estabilidad.

💡 Insight

La métrica óptima depende del contexto del problema, no siempre la accuracy es suficiente.

⸻

🔹 Avance 4 – Simulación de Deploy y Monitoreo

📌 Objetivo

Simular el comportamiento del modelo en producción y detectar posibles problemas post-despliegue.

🛠️ Implementación
	•	Simulación de datos nuevos
	•	Evaluación con datos fuera del entrenamiento
	•	Detección de drift
	•	Comparación de métricas pre y post deploy
	•	Generación de reportes automáticos

Scripts productivos:
	•	model_deploy.py
	•	model_monitoring.py

🔎 Hallazgos
	•	Se detectaron cambios en la distribución de algunas variables.
	•	El rendimiento del modelo puede degradarse si cambia el contexto de los datos.
	•	El monitoreo continuo es fundamental en entornos reales.

🎯 Conclusión

El modelo no debe considerarse estático: requiere supervisión constante para mantener su rendimiento.

💡 Insight

El verdadero valor de MLOps no está solo en entrenar modelos, sino en mantenerlos estables y confiables en producción.

🚀 Tecnologías Utilizadas
	•	Python
	•	Pandas
	•	Scikit-learn
	•	Matplotlib
	•	Git & GitHub
	•	Control de versiones con branches
	•	Estructuración modular de proyecto

⸻

📌 Conclusión General del Proyecto

Este proyecto permitió implementar un flujo completo de Machine Learning bajo un enfoque MLOps, integrando:
	•	Organización profesional del código
	•	Separación entre experimentación y producción
	•	Versionado con Git
	•	Evaluación técnica del modelo
	•	Monitoreo post-despliegue

Se logró comprender que el ciclo de vida del modelo no termina en el entrenamiento, sino que requiere monitoreo continuo y capacidad de adaptación frente a cambios en los datos.

⸻

🎓 Aprendizajes Clave
	•	La estructura del proyecto impacta en su mantenibilidad.
	•	La ingeniería de features es crítica para el desempeño.
	•	Las métricas deben interpretarse en contexto.
	•	El monitoreo es indispensable en producción.
	•	El flujo Git con branches y PRs refleja prácticas reales de trabajo en equipo.