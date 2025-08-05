from workflows_cdk import Response, Request
from flask import request as flask_request
from main import router

@router.route("/execute", methods=["GET", "POST"])
def execute():
    """
    This is the function that is executed when you click on "Run" on a workflow that uses this action.
    """
    request = Request(flask_request)

    # The data object of request.data will contain all of the fields filled in the form and defined in the schema.json file.
    data = request.data

    # Your logic here
    # Here you can add your logic to execute the action which may consist of, for example:
    # - calling an API
    # - doing some calculations
    # - doing some data transformations
    # - validating data
    

    output = []

    return Response(data=output, metadata={"affected_rows": len(output)})


@router.route("/schema", methods=["POST"])
def schema():
      
    base_schema = {
        "metadata": {},
        "fields": [
        {
            "id": "api_key",
            "type": "string",
            "label": "API Key",
            "description": "The API key for the Twilio Sendgrid account.",
            "required": True,

        }
        ]
    }
    return Response(data={"schema": base_schema})

