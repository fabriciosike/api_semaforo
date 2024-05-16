#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_tempo_proximo_semaforo(distancia, velocidade, aceleracao):
    tempo_aceleracao = velocidade / aceleracao
    distancia_aceleracao = 0.5 * aceleracao * (tempo_aceleracao ** 2)
    distancia_restante = distancia - distancia_aceleracao
    tempo_constante = distancia_restante / velocidade
    tempo_total = tempo_aceleracao + tempo_constante
    tempo_proximo_semaforo = tempo_total - 3
    tempo_proximo_semaforo = math.floor(tempo_proximo_semaforo)
    
    return tempo_proximo_semaforo

@app.route('/calcular_tempo_proximo_semaforo', methods=['POST'])
def api_calcular_tempo_proximo_semaforo():
    dados = request.get_json()
    distancia = dados['distancia']
    velocidade = dados['velocidade']
    aceleracao = dados['aceleracao']
    tempo_proximo_semaforo = calcular_tempo_proximo_semaforo(distancia, velocidade, aceleracao)
    return jsonify({'tempo_proximo_semaforo': tempo_proximo_semaforo})

if __name__ == '__main__':
    app.run(debug=False)




