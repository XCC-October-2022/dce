from common.models.provider import Provider, ProviderProjectRequest, ProviderProjectResponse
import requests


class ProviderBackend():
    def __init__(self, provider: Provider):
        self.provider = provider

    def create_project(self, data: ProviderProjectRequest) -> ProviderProjectResponse:
        res = requests.post(url=self.provider.create_url,
                            json=data.provider_request)
        state = res  # TODO: active or error
        project = res  # TODO: convert response into project if state is active
        return ProviderProjectResponse(project=project, state=state)

    def delete_project(self, data: ProviderProjectRequest) -> ProviderProjectResponse:
        res = requests.post(url=self.provider.delete_url,
                            json=data.provider_request)
        state = res  # TODO: deleted or error
        project = res  # TODO: convert response into project if state is active
        return ProviderProjectResponse(project=project, state=state)
