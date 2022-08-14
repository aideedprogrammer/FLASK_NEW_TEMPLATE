from proj import intial_app

app = intial_app('development')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)

