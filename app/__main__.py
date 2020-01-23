from .app import app

port = 4022
if __name__ == '__main__':
    app.run('0.0.0.0', port)

    