package(default_visibility = ["//visibility:public"])

cc_library(
  name = "pyapi",
  srcs = [
    "pyapi.cc",
    "pyarray.cc",
    "pybase.cc",
    "pydate.cc",
    "pyframe.cc",
    "pymisc.cc",
    "pymyelin.cc",
    "pyparser.cc",
    "pyphrase.cc",
    "pyrecordio.cc",
    "pystore.cc",
    "pytask.cc",
    "pywiki.cc",
  ],
  hdrs = [
    "pyarray.h",
    "pybase.h",
    "pydate.h",
    "pyframe.h",
    "pymisc.h",
    "pymyelin.h",
    "pyparser.h",
    "pyphrase.h",
    "pyrecordio.h",
    "pystore.h",
    "pytask.h",
    "pywiki.h",
  ],
  deps = [
    ":tasks",
    "//sling/base",
    "//sling/file",
    "//sling/file:recordio",
    "//sling/frame",
    "//sling/frame:json",
    "//sling/frame:turtle",
    "//sling/frame:xml",
    "//sling/http:http-server",
    "//sling/myelin:flow",
    "//sling/myelin:compiler",
    "//sling/myelin:compute",
    "//sling/myelin:gradient",
    "//sling/nlp/document",
    "//sling/nlp/document:document-tokenizer",
    "//sling/nlp/document:lex",
    "//sling/nlp/document:phrase-tokenizer",
    "//sling/nlp/embedding:plausibility-model",
    "//sling/nlp/kb:calendar",
    "//sling/nlp/kb:facts",
    "//sling/nlp/kb:phrase-table",
    "//sling/nlp/parser",
    "//sling/nlp/parser/trainer:frame-evaluation",
    "//sling/nlp/wiki:wikidata-converter",
    "//sling/task:dashboard",
    "//sling/task:job",
    "//sling/task:process",
    "//sling/stream:file",
    "//sling/stream:memory",
    "//sling/string:text",
  ],
  copts = [
    "-Wno-write-strings",
    "-Wno-invalid-offsetof",
    "-DPYVER=35"
  ],
)

cc_library(
  name = "tasks",
  deps = [
    "//sling/nlp/wiki:aliases",
    "//sling/nlp/wiki:wikidata-importer",
    "//sling/nlp/wiki:wikipedia-importer",
    "//sling/nlp/wiki:wikipedia-documents",
    "//sling/nlp/wiki:wikipedia-links",

    "//sling/nlp/document:vocabulary-builder",

    "//sling/nlp/kb:fact-lexicon",
    "//sling/nlp/kb:name-table-builder",
    "//sling/nlp/kb:phrase-table-builder",

    "//sling/nlp/embedding:fact-embeddings",
    "//sling/nlp/embedding:word-embeddings",
    "//sling/nlp/embedding:fact-plausibility",

    "//sling/nlp/ner:idf",
    "//sling/nlp/ner:labeler",

    "//sling/task:frame-store-reader",
    "//sling/task:frame-store-writer",
    "//sling/task:sharder",
    "//sling/task:sorter",
    "//sling/task:record-file-reader",
    "//sling/task:record-file-writer",
    "//sling/task:text-file-reader",
    "//sling/task:text-file-writer",
    "//sling/task:text-map-reader",
    "//sling/task:text-map-writer",
    "//sling/task:workers",
  ],
)

cc_binary(
  name = "pysling.so",
  deps = [
    ":pyapi",
    "//sling/base",
    "//sling/file:posix",
  ],
  linkshared = 1,
  linkstatic = 1,
)

