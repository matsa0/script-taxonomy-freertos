import xml.etree.ElementTree as ET
from taxonomyFunctions import TaxonomyFunctions

tf = TaxonomyFunctions()

xmlRoot = tf.findElementRoot("logAllErrorsFreeRTOS.xml")
errorsTags = tf.findErrorTags(xmlRoot)

lengthOfTypes, types = tf.listTypes(errorsTags)
print("\nFreeRTOS types count: ", lengthOfTypes)


print("\n")

warningTypes = tf.listTypesBySeverity(errorsTags, "warning")
print("\n***Warning Types: " , warningTypes)

styleTypes = tf.listTypesBySeverity(errorsTags, "style")
print("\n***Style Types: " , styleTypes)

performanceTypes = tf.listTypesBySeverity(errorsTags, "performance")
print("\n***Performance Types: " , performanceTypes)

portabilityTypes = tf.listTypesBySeverity(errorsTags, "portability")
print("\n***Portability Types: " , portabilityTypes)

informationTypes = tf.listTypesBySeverity(errorsTags, "information")
print("\n***Information Types: " , informationTypes)

errorTypes = tf.listTypesBySeverity(errorsTags, "error")
print("\n***Error Types: " , errorTypes)

print("\n")

print("Occurrences of each severity:\n ")
tf.printSeveritiesOccurrences(errorsTags)
