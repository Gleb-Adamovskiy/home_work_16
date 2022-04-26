from app import create_app
# файл запуска приложения

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
