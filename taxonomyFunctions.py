import xml.etree.ElementTree as ET

class TaxonomyFunctions:
    def countSeveritiesOccurrences(self, errorTags):
        countWarning = 0
        countStyle = 0
        countPerformance = 0
        countPortability = 0
        countInformation = 0
        countError = 0

        for severity in errorTags:
            severityType = severity.get('severity')

            if severityType == "warning":
                countWarning += 1
            if severityType == "style":
                countStyle += 1
            if severityType == "performance":
                countPerformance += 1
            if severityType == "portability":
                countPortability += 1
            if severityType == "information":
                countInformation += 1
            if severityType == "error":
                countError += 1

        return countWarning, countStyle, countPerformance, countPortability, countInformation, countError;

    def findErrorTags(self, root):
        return root.findall(".//error")

    def findElementRoot(self, xml):
        if not isinstance(xml, str):
            print("Invalid XML! Try again.") 
            return;
        tree = ET.parse(xml)
        root = tree.getroot()

        return root;

    def listSeverities(self, errorTags):
        severities = set()  

        for severity in errorTags:
            severities.add(severity.get('severity'))
        print(severities)

        lengthSeverities = len(severities)
        return lengthSeverities;


    def listTypes(self, errorTags):
        categories = set()

        for category in errorTags:
            categories.add(category.get('id')) #id == type
        print(categories)

        lengthTypes = len(categories)
        return lengthTypes;

    def printSeveritiesOccurrences(self, errorTags):
        countWarning, countStyle, countPerformance, countPortability, countInformation, countError = self.countSeveritiesOccurrences(errorTags)

        print(f"Warnings: {countWarning}")
        print(f"Style issues: {countStyle}")
        print(f"Performance issues: {countPerformance}")
        print(f"Portability issues: {countPortability}")
        print(f"Information issues: {countInformation}")
        print(f"Errors: {countError}")