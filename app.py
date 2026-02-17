import os
import logging
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import   decodeImage, encodeImageIntoBase64
from cnnClassifier.pipeline.prediction import PredictionPipeline

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)S"

)
logger = logging.getLogger(__name__)
app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp()

def _bad_request(message:str,status:int=400):
    """Return a uniform JSON error response"""
    return jsonify({"success":False, "error":message}), status
@app.route("/",methods=['GET'])
@cross_origin()
def home():
    """Serve the main UI page."""
    return render_template('index.html')



@app.route("/train",methods=["GET","POST"])
@cross_origin()
def trainRoute():
    """Trigger DVC pipeline and return status."""
    logger.info("Training pipeline triggered")
    exit_code = os.system("dvc repro")

    if exit_code != 0:
        logger.error("DVC pipeline exited with code %s",exit_code)
        return _bad_request("Training failed. Check server logs.",200)

    logger.info("Training completed successfully.")
    return jsonify({"success":True,"message":"Training completed successfully."})


@app.route("/predict",methods=['POST'])
@cross_origin()
def predict_route():
    """Accept a base64 image, run interface, return prediction."""
    payload = request.get_json(silent=True)
    if not payload:
        return _bad_request("Request body must be JSON."
                            )
    image_b64 = payload.get('image')
    if not image_b64:
        return _bad_request("Missing 'image' field in request body.")
    try:
        decodeImage(image_b64,clApp.filename)
        result = clApp.classifier.predict()
        logger.info("Prediction result: %s",result)
        return jsonify({"success":True,"result":result})
    except FileNotFoundError as exc:
        logger.exception("Model or image file not found.")
        return _bad_request(f"Resource not found: {exc}",404)
    except Exception as exc:
        logger.exception("Unhandled error during prediction.")
        return _bad_request(f"Prediction failed: {exc}",500)




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=False)