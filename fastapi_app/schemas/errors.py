from collections.abc import Mapping
from typing import List, Optional, Union, Dict

from pydantic import BaseModel, Field


class Error(BaseModel):
    code: int
    type: str
    message: str = Field()
    errors: Optional[Union[List, Dict]] = Field(..., example=[])


class ErrorResponses(Mapping):
    _error_responses = {
        404: {
            'description': 'Not Found',
            'model': Error,
            'content': {
                'application/json': {
                    'example': {
                        'error': {
                            'code': 404,
                            'type': 'not_found',
                            'message': 'The server cannot find the requested resource.',
                            'errors': {
                                'Accept-Language': "language 'en' is not available."
                            }
                        }
                    }
                }
            }
        },
        406: {
            'description': 'Not Acceptable',
            'model': Error,
            'content': {
                'application/json': {
                    'example': {
                        'error': {
                            'code': 406,
                            'type': 'not_acceptable',
                            'message': 'The server cannot produce a response matching the list of acceptable values '
                                       'defined in the headers of the request.',
                            'errors': {
                                'Accept-Language': "unacceptable value 'en'"
                            }
                        }
                    }
                }
            }
        },
        422: {
            'description': 'Unprocessable Entity',
            'model': Error,
            'content': {
                'application/json': {
                    'example': {
                        'error': {
                            'code': 422,
                            'type': 'unprocessable_entity',
                            'message': 'The request was well-formed but was unable to be followed due to semantic '
                                       'errors.',
                            'errors': {
                                'Accept-Language': "unallowed value 'en'"
                            }
                        }
                    }
                }
            }
        },
        503: {
            'description': 'External Resource Exception',
            'model': Error,
            'content': {
                'application/json': {
                    'example': {
                        'error': {
                            'code': 503,
                            'type': 'service_unavailable',
                            'message': 'The request was well-formed but there was an error while calling an external '
                                       'resource',
                            'errors': {}
                        }
                    }
                }
            }
        }
    }

    def __init__(self, codes=None):
        self._storage = {key: value for key, value in self._error_responses.items() if codes is None or key in codes}

    def __getitem__(self, key):
        return self._storage[key]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)