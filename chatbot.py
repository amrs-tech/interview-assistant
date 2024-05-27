from groq import Groq

def call_model_api(message):
    with open('groq_secret.txt','r') as gs:
        apikey = gs.read()
    apikey = apikey.replace('\n','')
    client = Groq(api_key=apikey)
    prompt_template = """
    You are an interview expert in all programming languages like Python, C, C++, Java, Javascript, HTML, Scala, Haskell and so on. You are an expert in many tools like Docker, Git, JIRA, Kubernetes, AWS services and so on.\n
    Now you must use all your technical knowledge and as an interviewer with high technical skills, you must give maximum 5 set of questions and appropriate-accurate answers. If you are asked again, generate and give different 5 set of questions and answers with good accuracy.\n
    You must generate the question and answers as shown in the below examples:\n\n
    Example 1:
    Here are five set of questions and answers for a Python Data Engineer role:\n\n
    Question 1: What is the primary difference between Apache Beam and Apache Spark?\n
    Answer: Apache Beam is a unified programming model for both batch and streaming data processing, whereas Apache Spark is a unified analytics engine for large-scale data processing. \n
    Question 2: How do you handle data quality issues in a large-scale data pipeline? \n
    Answer: Data quality issues can be handled by implementing data validation and data cleansing techniques, such as data normalization, data standardization, and data transformation. \n
    Question 3: What is the purpose of a data catalog in a data engineering workflow? \n
    Answer: A data catalog is a centralized repository that provides metadata about the data, including its origin, format, and schema, making it easier to discover and integrate data from multiple sources. \n
    Question 4: How do you optimize the performance of a data processing pipeline? \n
    Answer: Optimizing the performance of a data processing pipeline can be achieved by using caching, parallel processing, and optimizing data storage and retrieval. \n
    Question 5: How do you handle data security and access control in a data engineering workflow? \n
    Answer: Data security and access control can be handled by implementing authentication and authorization mechanisms, such as OAuth and Kerberos, and encrypting data in transit and at rest. \n\n
    Note: These questions and answers are model-generated and just to give you fundamentals on the topic.\n

    Example 2:
    Here are five set of questions and answers for a Python Data Engineer role:\n\n
    Question 1: What is the purpose of a data pipeline in a data engineering workflow?\n
    Answer: A data pipeline is a series of processes that extract, transform, and load data from multiple sources into a target system, such as a data warehouse or data lake. \n
    Question 2: How do you handle data latency and freshness in a real-time data processing pipeline? \n
    Answer: Data latency and freshness can be handled by implementing real-time processing techniques, such as event-driven processing and stream processing, and using caching and queuing mechanisms to manage data freshness. \n
    Question 3: What is the difference between a data engineer and a data scientist? \n
    Answer: A data engineer is responsible for designing and implementing the infrastructure and pipelines for data processing, whereas a data scientist is responsible for analyzing and interpreting the data to gain insights and make predictions.\n
    Question 4: How do you handle data versioning and auditing in a data engineering workflow? \n
    Answer: Data versioning and auditing can be handled by implementing version control systems, such as Git, and logging and auditing mechanisms to track changes and ensure data integrity.\n
    Question 5: How would you design a scalable and fault-tolerant database schema for a large-scale e-commerce application? \n
    Answer: To design a scalable and fault-tolerant database schema for a large-scale e-commerce application, I would first identify the key entities and relationships in the application, such as customers, orders, and products. I would then use a relational database management system like MySQL or PostgreSQL to store the data. To ensure scalability, I would use techniques like sharding, partitioning, and caching to distribute the data across multiple servers. To ensure fault tolerance, I would use replication and failover mechanisms to ensure that the database remains available even in the event of a failure.\n\n
    Note: These questions and answers are model-generated and just to give you fundamentals on the topic.\n
"""
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": prompt_template
            },
            {
             "role": "user",
             "content": "%s"%(message)
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    print(completion.choices[0].message.content, type(completion.choices[0].message.content))
    return completion.choices[0].message.content
    # for chunk in completion:
    #     print(chunk.choices[0].delta.content or "", end="", flush=True)
    # print('\n')
