# 🕵️‍♂️ OSINT B2B Lead Scraper

Herramienta de Inteligencia de Fuentes Abiertas (OSINT) desarrollada en Python para la generación automatizada de prospectos corporativos (B2B Lead Generation).

Este script utiliza **Playwright** para extraer información pública de empresas locales directamente desde motores de búsqueda, evadiendo bloqueos de IP y sistemas reCAPTCHA comunes en los directorios comerciales tradicionales.

## 📺 Demostración de la Herramienta


https://github.com/user-attachments/assets/196d344b-94c8-43d7-94f4-2d08d99a1cb5


## 🚀 Características
* **Extracción OSINT:** Busca y recopila datos directamente desde resultados orgánicos de búsqueda (DuckDuckGo HTML puro).
* **Bypass Anti-Bot:** Al consultar motores de búsqueda ligeros, evita bloqueos de seguridad pesados como Cloudflare o barreras de "Verificación Humana".
* **Exportación Estructurada:** Genera un archivo `.csv` delimitado por punto y coma (`;`), optimizado para abrirse nativamente en Excel (configuración regional LATAM) en 3 columnas perfectas: Empresa, Descripción del Servicio y Sitio Web.
* **Demostración Visual:** Ejecuta Chromium en modo visible (`headless=False`) para auditar el funcionamiento y flujo del bot en tiempo real.

## 🛠️ Tecnologías Utilizadas
* Python 3
* Playwright (API Síncrona)
* Módulo `csv` nativo

## 📦 Uso y Despliegue
1. Descarga los archivos del repositorio.
2. Instala la librería de automatización:
   ```bash
   pip install playwright
   playwright install chromium
