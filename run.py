from src import create_app

app = create_app()

if __name__ == '__main__':
    # debug=True permite que o servidor reinicie sozinho quando mudamos o código
    app.run(host='0.0.0.0', port=5000, debug=True)

