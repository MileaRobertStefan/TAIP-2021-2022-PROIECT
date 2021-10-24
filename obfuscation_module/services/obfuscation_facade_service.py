
class ObfuscationService:
    def __init__(self, key_builder, obfuscation_context):
        self.key_builder = key_builder
        self.obfuscation_context = obfuscation_context

    def obfuscate(self, areas_container, image):
        self.key_builder.set_initial_step(image)
        for obfuscation_area in areas_container:
            image = self.obfuscation_context.obfuscate(obfuscation_area, image, self.key_builder)
        return image, self.key_builder.build()

