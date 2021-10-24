from services.obfuscation_facade_service import ObfuscationService

class ObfuscationProxy:
    def validate(self, request) -> bool:
        pass

    def pre_process(self, request):
        areas = image = None
        return (areas, image)

    def post_process(self, res):
        pass

    def forward(self, request):
        obfuscation_service = ObfuscationService()
        if self.validate(request):
            areas, images = self.pre_process(request)
            to_ret = obfuscation_service.obfuscate(areas, images)
            self.post_process(to_ret)
            return to_ret
            
