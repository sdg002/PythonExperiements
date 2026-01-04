"""
I was trying to a do a simple OpenTelemetry logging setup in Python.
As per VS Code suggestion, this should write logs to console.
But, it is not working as expected. 
The package opentelemetry-exporter-console does not exist in pypi.org.

"""
import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.logs import LoggingHandler, LogEmitterProvider
from opentelemetry.sdk.logs.export import ConsoleLogExporter, BatchLogProcessor
from opentelemetry.trace import set_tracer_provider
from opentelemetry.logs import set_log_emitter_provider

# Set up a resource to describe the service
resource = Resource.create({"service.name": "sample-service"})

# Set up the tracer provider
tracer_provider = TracerProvider(resource=resource)
set_tracer_provider(tracer_provider)

# Set up a span processor and exporter for tracing
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
tracer_provider.add_span_processor(span_processor)

# Set up the log emitter provider
log_emitter_provider = LogEmitterProvider(resource=resource)
set_log_emitter_provider(log_emitter_provider)

# Set up a log processor and exporter for logging
log_processor = BatchLogProcessor(ConsoleLogExporter())
log_emitter_provider.add_log_processor(log_processor)

# Set up the OpenTelemetry logging handler
otel_handler = LoggingHandler(
    level=logging.INFO, log_emitter_provider=log_emitter_provider)

# Configure Python's logging module to use the OpenTelemetry handler
logging.basicConfig(level=logging.INFO, handlers=[otel_handler])

# Create a logger
logger = logging.getLogger(__name__)

# Example usage
if __name__ == "__main__":
    # Start a span
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("example-span"):
        logger.info("This is an informational log message.")
        logger.warning("This is a warning log message.")
        logger.error("This is an error log message.")
