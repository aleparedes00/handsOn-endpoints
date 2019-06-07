import os
import json

import connexion

app = connexion.App(
    '__name__', 
    specification_dir='swagger/',
    options={"swagger_ui": False}
)

app.add_api('contrat.yaml', strict_validation=True, validate_responses=False)

application = app.app

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    