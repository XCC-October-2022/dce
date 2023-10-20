from common.models.provider import Provider, ProviderProjectRequest, ProviderProjectResponse
import requests


class ProviderBackend():
    def __init__(self, provider: Provider):
        self.provider = provider

    def create_project(self, data: ProviderProjectRequest) -> ProviderProjectResponse:
        res = ProviderProjectResponse(**(requests.post(url=self.provider.create_url,
                            json=data.provider_request).json()))
        print(res)
        return res

    def delete_project(self, data: ProviderProjectRequest) -> ProviderProjectResponse:
        res = ProviderProjectResponse(**(requests.post(url=self.provider.delete_url,
                            json=data.provider_request).json()))
        return res
