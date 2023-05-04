from api import create_app

application = create_app()
print(application)


def runApp():
    application.run(debug=True,port=7000)

if __name__ == "__main__":
    runApp()