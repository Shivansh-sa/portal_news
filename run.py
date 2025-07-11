# run.py

from app import create_app

# Create the Flask app using factory method
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
