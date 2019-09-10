import sling

commons = sling.Store()
commons.load("data/nlp/schemas/meta-schema.sling")
commons.load("data/nlp/schemas/document-schema.sling")
commons.load("data/nlp/schemas/recipe-schema.sling")
commons.freeze()