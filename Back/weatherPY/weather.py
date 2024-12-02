
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from controllers.weather_controller import WeatherController

PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Rota para obter o clima
        if self.path.startswith("/weather"):
            self.handle_weather()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint nao encontrado.")

    def handle_weather(self):
        # Extrai parâmetros da URL
        query_components = parse_qs(urlparse(self.path).query)
        city = query_components.get("city", [None])[0]

        if not city:
            self.send_response(400)
            self.end_headers()
            self.wfile.write("O parâmetro 'city' é obrigatório.")
            return

        # Chama o controlador
        result = WeatherController.get_weather(city)
        self.send_response(result["status"])
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

# Inicializa o servidor
if __name__ == "__main__":
    with HTTPServer(("", PORT), RequestHandler) as httpd:
        print(f"Servidor iniciado na porta {PORT}")
        httpd.serve_forever()
