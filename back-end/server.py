from flask import Flask, render_template, request, jsonify
import socket
from datetime import datetime

app = Flask(__name__, 
                static_folder='../front_end',    # Pasta para arquivos estáticos (CSS/JS)
            template_folder='../front_end')  # Pasta para templates HTML
# Lista para armazenar os nomes e IPs
nomes_ips = []

@app.route('/main.js')  # Rota de teste - adicione temporariamente
def serve_js():
    return app.send_static_file('main.js')

@app.route('/')
def home():
    client_ip = request.remote_addr
    return render_template('index.html', client_ip=client_ip)

@app.route('/salvar_nome', methods=['POST'])
def salvar_nome():
    nome = request.form['nome']
    client_ip = request.remote_addr
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    nomes_ips.append({
        'nome': nome,
        'ip': client_ip,
        'data': data_hora
    })

    return render_template('index.html',
                         nome=nome,
                         nomes_ips=nomes_ips,
                         client_ip=client_ip)

@app.route('/remover_ip/<ip>', methods=['DELETE'])
def remover_ip(ip):
    global nomes_ips
    nomes_ips = [item for item in nomes_ips if item['ip'] != ip]
    return jsonify({'status': 'success', 'message': f'IP {ip} removido'})

@app.route('/get_nomes', methods=['GET'])
def get_nomes():
    return jsonify(nomes_ips)

if __name__ == '__main__':
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Servidor rodando em: http://{local_ip}:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)