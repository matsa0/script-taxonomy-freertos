import xml.etree.ElementTree as ET
from taxonomyFunctions import TaxonomyFunctions

tf = TaxonomyFunctions()

#rootSourceXml = tf.findElementRoot("logAllErrors.xml")
#sourceErrorsTags = tf.findErrorTags(rootSourceXml)

rootFreeRTOSXml = tf.findElementRoot("logAllErrorsFreeRTOS.xml")
freeRTOSErrorsTags = tf.findErrorTags(rootFreeRTOSXml)

#sourceSeveritiesLength = tf.listSeverities(sourceErrorsTags)
freeRTOSSeveritiesLength = tf.listSeverities(freeRTOSErrorsTags)

#print("Source severities Length: ", sourceSeveritiesLength)
print("FreeRTOS severities Length: ", freeRTOSSeveritiesLength)

print("\n\n")

""" sourceTypesLength = tf.listTypes(sourceErrorsTags)
print("Source types count: ", sourceTypesLength) 

print("\n\n")"""

freeRTOSTypesLength = tf.listTypes(freeRTOSErrorsTags)
print("FreeRTOS types count: ", freeRTOSTypesLength)

print("\n\n")

""" print("Source: ")
tf.printSeveritiesOccurrences(sourceErrorsTags) """
print("\nFreeRTOS: ")
tf.printSeveritiesOccurrences(freeRTOSErrorsTags)