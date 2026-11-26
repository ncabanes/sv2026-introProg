# Crea una función escribir_centrado_subrayado, 
# que escriba centrado horizontalmente en pantalla
# (suponiendo una anchura de 80 columnas) y subrayado
# (con guiones) el texto que se indique como parámetro:
# 
# escribir_centrado_subrayado("Texto de ejemplo")
# 
#           Texto de ejemplo
#           ----------------

def escribir_centrado_subrayado(texto: str) -> None:
	espacios = 40 - len(texto) // 2
	print(" " * espacios + texto)
	print(" " * espacios + "-" * len(texto))

escribir_centrado_subrayado("Hola")
