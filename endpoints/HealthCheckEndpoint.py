from flask_restful import Resource


class HealthCheckEndpoint(Resource):
    def get(self):
        return {'health': 'decent'}
