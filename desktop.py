import logging
import sys
import requests
import multiprocessing
from time import sleep
from webview import Viewer

def start_flask():
    try:
        from app import app
        app.run(threaded=True,
                debug=False,
                port=8081,
                host="127.0.0.1",
                use_reloader=False)
    except:
        logging.fatal("Could not start flask")


def wait_server_ready():
    attempts = 50
    while attempts > 0:
        try:
            resp = requests.get('http://127.0.0.1:8081')
            if resp.status_code == 200:
                return
            else:
                logging.info("Status code %s", resp.status_code)
        except:
            logging.info("Server not ready: request errored")
        attempts = attempts-1
        sleep(.2)
    raise Exception("No server could be loaded")

def dumb_method():
    logging.warning("I'm just a dumb method")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    try:
        server = multiprocessing.Process(
                target=start_flask, args=())
        logging.info("Starting server")
        server.start()
        logging.info("Waiting for server ready")
        wait_server_ready()
        logging.info("Server ready")
        viewer = Viewer("http://127.0.0.1:8081/hedy")
        viewer.run_viewer()
    except Exception as e: 
        logging.exception("Oh no")
        viewer.show_error(str(e))
        viewer.exec_app()
    finally:
        logging.info("Shutting down flask")
        server.terminate()
        server.join()    
        sys.exit(0)
