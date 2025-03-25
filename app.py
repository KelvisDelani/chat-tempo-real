from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Criando a instância do flask
app = Flask(__name__)

# Criando a instância do socketio
socketio = SocketIO(app)

# Definindo a rota para a página inicial (index.html)
@app.route('/')
def index():
    return render_template('index.html') # Renderizando o template HTML

# Definindo evento para capturar as mensagens e envia-las para todos os clientes
@socketio.on('message')
def handle_message(msg):
    print("Mensagem recebida:", msg) # Imprimindo a mensagem recebida no console
    emit('new_message', msg, broadcast=True) # Enviando a mensagem recebida para todos os clientes

# Rodando a aplicação
if __name__ == '__main__':
    socketio.run(app, debug=True) # Rodando o servidor com debug ativado    
