from flask import Flask


app = Flask(__name__)

# criando rota (rota é como vamos nos comunicar com outros clientes), recebendo informaçoes e devolve informacoes para o soliciantante 

@app.route("/")
def hello_word():
    return "Hello word!" 

# criando outra rota(outra pagina)
@app.route("/about")
def about():
    return "Página sobre"


if __name__ == "__main__": # metodo para desenvolvimento local 
    app.run(debug=True) # propriedade debug vai permitir que a entender oq esta acontecendo no servidor web

# 