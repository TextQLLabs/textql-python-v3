# TextqlRPCPublicRbacCreateAPIKeyResult

CreateApiKeyResponse minus its deprecated api_key_hash alias.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `api_key`                                                                            | [Optional[models.TextqlRPCPublicRbacAPIKey]](../models/textqlrpcpublicrbacapikey.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `api_key_secret`                                                                     | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | Only ever returned here; the server stores a hash and cannot reissue it.             |