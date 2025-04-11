version: "3.0"
pipeline:
  - name: "SpacyNLP"
    model: "en_core_web_sm"  # A smaller spaCy model
  - name: "SpacyTokenizer"
  - name: "IntentClassifier"
policies:
  - name: "MemoizationPolicy"
  - name: "RulePolicy"
