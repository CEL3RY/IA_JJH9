# Identificación de Color en Imágenes Digitales

El primer paso fue identificar los objetos de color rojo en la imagen. El rojo puede ser un color particularmente difícil de aislar debido a sus numerosas tonalidades y variaciones bajo diferentes condiciones de luz. Para abordar esto, convertí la imagen del espacio de color RGB (Red-Green-Blue) al espacio de color HSV (Hue-Saturation-Value). El HSV es preferible para la segmentación de color ya que separa la 'tonalidad' del color de su 'saturación' y 'valor', lo que facilita la identificación de colores en una amplia gama de luminosidades.

Una vez en el espacio de color HSV, creé un rango de valores que representan el color rojo, teniendo en cuenta sus diversas tonalidades desde el rojo claro hasta el rojo oscuro. Este rango se definió ajustando los valores de 'tonalidad' para el rojo y estableciendo umbrales para 'saturación' y 'valor' que permitieran capturar la mayoría de las variantes del rojo sin incluir colores no deseados.

El siguiente paso fue aplicar una máscara a la imagen original utilizando este rango definido. La máscara permite extraer solo aquellos píxeles que se encuentran dentro del rango especificado, aislando así los objetos rojos del resto de la imagen. Este proceso se conoce como segmentación de color, y es crucial para aplicaciones como el seguimiento de objetos, la clasificación de imágenes y la visión por computadora en general.

Para mejorar la precisión de la segmentación, implementé filtros adicionales para reducir el ruido y mejorar la claridad de los objetos segmentados. Estos filtros incluyeron operaciones morfológicas como la erosión y dilatación, que ayudan a eliminar pequeños artefactos y unificar áreas segmentadas, respectivamente. Además, utilicé técnicas de suavizado como el filtro Gaussiano para reducir la aspereza de los bordes de los objetos segmentados.

Finalmente, realicé pruebas con diversas imágenes para validar la eficacia del algoritmo de segmentación. Estas pruebas incluyeron imágenes con diferentes condiciones de iluminación y fondos variados para asegurar que el algoritmo sea robusto y fiable en distintos escenarios. Los resultados demostraron una alta tasa de precisión en la identificación de objetos rojos, con mínima interferencia de otros colores. Este éxito abre la puerta a aplicaciones más avanzadas, como el reconocimiento de patrones y la detección de objetos específicos en entornos complejos.

# Segmentación de Color mediante Espacio de Color HSV

Utilicé OpenCV para la conversión y segmentación de color. Definí rangos de tonalidad para el color rojo dentro del espacio de color HSV y apliqué una máscara que aísla los píxeles rojos de la imagen. Las imágenes reales son a menudo imperfectas; pueden tener ruido y variaciones de color que hacen que la segmentación no sea perfecta.

Para mejorar la máscara de color rojo, apliqué operaciones morfológicas para eliminar el ruido y cerrar pequeños huecos dentro de los objetos. Estas operaciones incluyeron técnicas como la erosión y dilatación, que son efectivas para reducir el ruido y mejorar la continuidad visual de los objetos segmentados. Además, utilicé filtros de suavizado como el filtro Gaussiano para reducir la aspereza en los bordes y mejorar la calidad visual de los objetos segmentados.

Otro aspecto crucial fue la implementación de técnicas de ajuste dinámico de los rangos de segmentación. Desarrollé un método para ajustar automáticamente los rangos de tonalidad, saturación y valor en función de las características específicas de cada imagen. Esto aseguró que el algoritmo se mantuviera robusto y efectivo bajo diferentes condiciones de iluminación y en diversos entornos.

Finalmente, realicé una serie de pruebas con un conjunto diverso de imágenes para validar y afinar el proceso de segmentación. Esto incluyó imágenes con diferentes niveles de iluminación, fondos variados y presencia de colores similares al rojo. Estas pruebas permitieron identificar y corregir deficiencias en el algoritmo, asegurando una alta tasa de precisión en la identificación y segmentación de objetos rojos en una amplia gama de situaciones.

# Etiquetado de Componentes Conectados

El segundo gran desafío fue contar los objetos rojos individualmente. Para esto, la biblioteca SciPy, con su función `label` dentro del módulo `ndimage`, se volvió invaluable. Esta función identifica regiones conectadas de píxeles en la máscara roja, 'etiquetando' cada objeto rojo encontrado.

Cada grupo de píxeles conectados que representaba un objeto rojo fue asignado con un identificador único. Esto permitió calcular características individuales como el área, el perímetro, o el centroide de cada objeto.

Enfrenté el desafío de diferenciar entre objetos cercanos, ajustando los parámetros de la función `label` para mejorar la sensibilidad en la detección de bordes entre objetos adyacentes. Esto fue crucial en escenas con múltiples objetos rojos agrupados.

Implementé un paso de post-procesamiento para mejorar la precisión del etiquetado. Utilicé técnicas de análisis morfológico para refinar las etiquetas, eliminando etiquetas de áreas muy pequeñas y combinando etiquetas de regiones separadas por pequeños huecos pero pertenecientes al mismo objeto.

Para validar la efectividad de este enfoque, realicé pruebas en diferentes conjuntos de imágenes, incluyendo aquellas con variadas densidades y disposiciones de objetos rojos, así como diferentes condiciones de iluminación. Los resultados mostraron una alta precisión en el conteo y la identificación de objetos individuales, demostrando la eficacia de combinar la segmentación de color en el espacio HSV con el etiquetado de componentes conectados en SciPy. Este enfoque abre nuevas posibilidades para aplicaciones en visión por computadora y análisis de imágenes.
