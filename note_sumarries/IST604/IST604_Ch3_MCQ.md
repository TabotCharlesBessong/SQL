# IST604 – Web Services & Distributed Computing
## Chapter 3: Developing Web Services Using SOAP — Practice MCQ

> **Instructions:** Select the best answer. Answers are provided at the end.

---

### Section A: SOAP Transmission & Standards

**1.** In SOAP message transmission, what is the role of a SOAP Intermediary?

- A) The final destination that processes the SOAP message
- B) The node that creates and initiates the SOAP message
- C) An optional node between sender and receiver that can perform filtering, logging, or caching
- D) A registry that stores service descriptions

---

**2.** What is the term for the final intended destination of a SOAP message?

- A) SOAP Broker
- B) SOAP Relay
- C) SOAP Router
- D) Ultimate SOAP Receiver

---

**3.** Which of the following best describes the role of WSDL in a SOAP-based web services ecosystem?

- A) It transports SOAP messages between service endpoints
- B) It acts as the metadata language describing what the service offers, where it is, and how to access it
- C) It registers service providers in a global directory
- D) It encrypts SOAP messages for secure transmission

---

**4.** UDDI registries store web service interface descriptions using which language/format?

- A) JSON
- B) OpenAPI/Swagger
- C) WSDL
- D) REST endpoints

---

### Section B: Implementation Structure

**5.** In JAX-WS best practice, what does SEI stand for and what is its role?

- A) Service Execution Instance — runs the web service operations
- B) Service Endpoint Interface — declares the methods that are the web service operations
- C) SOAP Encoding Interface — defines the XML encoding rules
- D) Service Exchange Interface — manages client-server communication

---

**6.** What does SIB stand for in the context of JAX-WS web service development?

- A) SOAP Implementation Bridge
- B) Service Integration Bean
- C) Service Implementation Bean
- D) SOAP Invocation Block

---

**7.** A Service Implementation Bean (SIB) can be implemented as which two Java component types?

- A) Abstract class or Singleton class
- B) POJO (Plain Old Java Object) or Stateless Session EJB
- C) Servlet or JSP
- D) Interface or Enum

---

**8.** Which of the following is the correct `Endpoint.publish()` syntax for publishing a web service at port 9873?

- A) `Endpoint.deploy("http://localhost:9873/ts", TimeServerImpl.class);`
- B) `Endpoint.start("http://localhost:9873/ts", "TimeServer");`
- C) `Endpoint.publish("http://127.0.0.1:9873/ts", new TimeServer2Implementation());`
- D) `Endpoint.register("9873/ts", new TimeServer2Implementation());`

---

### Section C: JAX-WS Annotations

**9.** Which annotation is used to mark a Java interface or class as a web service in JAX-WS?

- A) `@SOAPService`
- B) `@WebService`
- C) `@ServiceEndpoint`
- D) `@JAXWSService`

---

**10.** Which annotation exposes a specific method as an invokable web service operation?

- A) `@Expose`
- B) `@RemoteMethod`
- C) `@WebMethod`
- D) `@ServiceMethod`

---

**11.** What is the purpose of the `@SOAPBinding(style = SOAPBinding.Style.RPC)` annotation?

- A) Specifies that the service uses REST-style HTTP methods
- B) Marks the class as a stateless session bean
- C) Specifies that the SOAP messages use RPC (Remote Procedure Call) style binding
- D) Registers the service with the UDDI registry

---

**12.** In the `TimeServer2Implementation.java` code, what does `@WebService(endpointInterface = "JWS.TimeServer2Interface")` accomplish?

- A) Publishes the service at the JWS namespace URL
- B) Links the implementation class to its SEI, forming the complete web service contract
- C) Automatically generates the WSDL file for the service
- D) Imports all methods from the TimeServer2Interface class

---

### Section D: Client Programming

**13.** In a JAX-WS Java client, what is the purpose of the `QName` object?

- A) To specify the SOAP security credentials
- B) To identify the service by its namespace URI and service name as declared in the WSDL
- C) To define the XML encoding format for messages
- D) To set the maximum timeout for the web service call

---

**14.** What is the correct sequence for building a JAX-WS Java client without `wsimport`?

- A) Get Port → Create QName → Load WSDL URL → Call Method
- B) Load WSDL URL → Create QName → Create Service → Get Port → Call Method
- C) Create Service → Load WSDL → Get Port → Create QName → Call Method
- D) Import WSDL → Create Port → Bind to Service → Call Method

---

**15.** In the TimeServer client, the WSDL URL used is:

- A) `http://localhost:9873/ts`
- B) `http://localhost:9873/ts/service`
- C) `http://localhost:9873/ts?wsdl`
- D) `http://localhost:9873/wsdl/ts`

---

**16.** A Perl client uses which module to consume a SOAP web service?

- A) `use HTTP::SOAP`
- B) `use SOAP::Lite`
- C) `use WebService::Client`
- D) `use XML::SOAP`

---

### Section E: wsgen and wsimport

**17.** What is the primary purpose of the `wsimport` tool?

- A) To generate JAXB classes from an annotated Java implementation class
- B) To publish a web service endpoint on a specified port
- C) To generate client stubs (SEI, Service class) from an existing WSDL file
- D) To validate a WSDL document against the W3C specification

---

**18.** Which development approach does `wsgen` follow?

- A) Top-Down (Contract-First)
- B) Middle-Out
- C) Schema-First
- D) Bottom-Up (Code-First)

---

**19.** What does the `-keep` flag do in a `wsimport` command?

- A) Keeps the WSDL file locally after import
- B) Retains the generated Java source files instead of only the compiled `.class` files
- C) Prevents overwriting existing source files
- D) Keeps the web service endpoint running after generation

---

**20.** Which flag in `wsimport` specifies the target Java package for the generated classes?

- A) `-t`
- B) `-pkg`
- C) `-p`
- D) `-namespace`

---

**21.** A client developer receives only the WSDL URL of a deployed service. Which tool should they use to build a Java client?

- A) `wsgen`
- B) `javac`
- C) `wsimport`
- D) `wsdl2java` (non-standard)

---

**22.** After running `wsimport`, which three types of artifacts are generated?

- A) SOAP envelope, HTTP headers, XML schema
- B) Service Endpoint Interface (SEI), Service class, JAXB data beans
- C) WSDL file, deployment descriptor, WAR archive
- D) Annotation processor, binding file, endpoint publisher

---

### Section F: Document Style

**23.** What is the default SOAP binding style in JAX-WS if `@SOAPBinding` is omitted entirely?

- A) RPC style
- B) Wrapped style
- C) Document style
- D) Literal style

---

**24.** Which statement correctly distinguishes Document style from RPC style in JAX-WS?

- A) RPC style is the industry standard; Document style is only for legacy systems
- B) Document style sends full XML documents and supports complex data types; RPC style mimics a function call with simple types
- C) Document style is faster than RPC style because it uses JSON instead of XML
- D) RPC style supports both simple and complex types; Document style supports only simple types

---

**25.** In the Order Processing Service example, the `OrderClient2` uses `wsimport`-generated stubs. What is the first step in the 3-step client pattern when using generated stubs?

- A) Get the port by calling `service.getXxxPort()`
- B) Create a `QName` object with the service namespace
- C) Instantiate the generated Service class (e.g., `new OrderServiceImplService()`)
- D) Load the WSDL URL using `new URL("...")`

---

## Answer Key

| Q | Answer | Q | Answer | Q | Answer |
|---|---|---|---|---|---|
| 1 | C | 10 | C | 19 | B |
| 2 | D | 11 | C | 20 | C |
| 3 | B | 12 | B | 21 | C |
| 4 | C | 13 | B | 22 | B |
| 5 | B | 14 | B | 23 | C |
| 6 | C | 15 | C | 24 | B |
| 7 | B | 16 | B | 25 | C |
| 8 | C | 17 | C | | |
| 9 | B | 18 | D | | |
