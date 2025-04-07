from flask import Flask, render_template, request, jsonify
from flask.helpers import make_response
import socket

app = Flask(__name__, 
                    template_folder='../front_end',
                    static_folder='../back-end',
                    static_host='')


# Lista para armazenas os nomes e ips
nomes_ips = []

@app.route('/')
def home():
    client_ip = request.remote_addr # Detecta o IP do visitante 
    return render_template('index.html', client_ip=client_ip) #  Renderiza a página HTML com o IP
@app.route('/salvar_nome', methods=['POST']) 
def salvar_nome():
    nome = request.form['nome'] # coletando o nome do formulario
    client_ip = request.remote_addr # pegando o ip local

    # adicionar a lista
    nomes_ips.append({'nome': nome,'ip': client_ip})

    # Retornar a lista atualizada
    return render_template('index.html',
                           nome=nome,
                           nomes_ips=nomes_ips,
                           client_ip=client_ip)

@app.route('/get_nomes', methods=['GET']) # Fornece os dados em formato JSON para integração com outros sistemas
def get_nome():
    return jsonify(nomes_ips)

if __name__ == '__main__':
    # Obter o IP da maquina local
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"servido rodando em: http://{local_ip}:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)