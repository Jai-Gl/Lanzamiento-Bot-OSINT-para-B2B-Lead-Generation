import csv
from playwright.sync_api import sync_playwright

def extraer_leads_buscador():
    print("[*] Iniciando motor de búsqueda OSINT para prospectos B2B...")
    datos_recolectados = []

    with sync_playwright() as p:
        # Modo visible para que se vea genial en el video
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()
        
        # Usamos DuckDuckGo en su versión HTML pura (cero bloqueos, cero Captchas)
        # Buscamos empresas de tecnología o soporte en Bogotá
        url_objetivo = "https://html.duckduckgo.com/html/?q=empresas+de+tecnologia+bogota+colombia"
        print(f"[*] Escaneando resultados en: {url_objetivo}")
        
        pagina.goto(url_objetivo)
        
        # Pausa de 2 segundos para que la página cargue visualmente en tu grabación
        pagina.wait_for_timeout(2000)
        
        print("[*] Interceptando resultados de búsqueda...")
        # DuckDuckGo usa la clase .result para cada enlace
        resultados = pagina.query_selector_all(".result")
        
        for resultado in resultados[:15]: # Extraemos los 15 mejores
            try:
                # 1. Nombre de la empresa / Título de la página
                titulo_elem = resultado.query_selector(".result__title")
                titulo = titulo_elem.inner_text().strip() if titulo_elem else "Sin título"
                
                # 2. Descripción (El fragmento de texto bajo el enlace)
                desc_elem = resultado.query_selector(".result__snippet")
                descripcion = desc_elem.inner_text().strip().replace('\n', ' ') if desc_elem else "Sin descripción"
                
                # 3. Enlace web de la empresa
                link_elem = resultado.query_selector(".result__url")
                enlace = link_elem.inner_text().strip() if link_elem else "Sin enlace"
                
                print(f"[+] Lead capturado: {titulo[:30]}...")
                datos_recolectados.append([titulo, descripcion, enlace])
                
            except Exception as e:
                continue
            
        navegador.close()
        return datos_recolectados

def guardar_en_excel(datos):
    nombre_archivo = "Leads_OSINT_Tecnologia_Bogota.csv"
    print(f"\n[*] Generando base de datos limpia en {nombre_archivo}...")
    
    # Delimitador punto y coma garantizado para el Excel
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo, delimiter=';')
        escritor.writerow(["Empresa / Título", "Descripción del Servicio", "Sitio Web"])
        escritor.writerows(datos)
        
    print("[+] ¡Extracción OSINT finalizada con éxito!")

if __name__ == "__main__":
    registros = extraer_leads_buscador()
    if registros:
        guardar_en_excel(registros)