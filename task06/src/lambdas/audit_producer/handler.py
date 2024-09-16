import os

import boto3
from commons.abstract_lambda import AbstractLambda
from commons.log_helper import get_logger

_LOG = get_logger('AuditProducer-handler')

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')


class AuditProducer(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        config_table = dynamodb.Table(os.environ.get("trigger_table"))
        audit_table = dynamodb.Table(os.environ.get("target_table_name"))

        _LOG("===============>>>>>", event)
        return 200


HANDLER = AuditProducer()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
