#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://azure-openai-test9967.openai.azure.com/"
openai.api_version = "2023-09-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="gpt35-model",
  prompt="Provide a summary of the text below that captures its main idea.\n\nDeep learning vs. machine learningIf deep learning is a subset of machine learning, how do they differ? Deep learning distinguishes itself from classical machine learning by the type of data that it works with and the methods in which it learns.Machine learning algorithms leverage structured, labeled data to make predictions—meaning that specific features are defined from the input data for the model and organized into tables. This doesn’t necessarily mean that it doesn’t use unstructured data; it just means that if it does, it generally goes through some pre-processing to organize it into a structured format.Deep learning eliminates some of data pre-processing that is typically involved with machine learning. These algorithms can ingest and process unstructured data, like text and images, and it automates feature extraction, removing some of the dependency on human experts. For example, let’s say that we had a set of photos of different pets, and we wanted to categorize by “cat”, “dog”, “hamster”, et cetera. Deep learning algorithms can determine which features (e.g. ears) are most important to distinguish each animal from another. In machine learning, this hierarchy of features is established manually by a human expert. In deep learning, the algorithm learns these features automatically, which is why it is called “deep” learning.\n\nDeep learning is a subset of machine learning that distinguishes itself from classical machine learning by the type of data that it works with and the methods in which it learns. Deep learning algorithms can ingest and process unstructured data, like text and images, and it automates feature extraction, removing some of the dependency on human experts. In machine learning, the hierarchy of features is established manually by a human expert, whereas in deep learning, the algorithm learns these features automatically.\n\nDeep learning is a subset of machine learning that distinguishes itself from classical machine learning by the type of data that it works with and the methods in which it learns. Deep learning algorithms can ingest and process unstructured data, like text and images, and it automates feature extraction, removing some of the dependency on human experts. In machine learning, the hierarchy of features is established manually by a human expert, whereas in deep learning, the algorithm learns these features automatically. This is why it is called “deep” learning.\n\nDeep learning is a subset of machine learning that distinguishes itself from classical machine learning by the type of data that it works with and the methods in which it",
  temperature=0.3,
  max_tokens=250,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)