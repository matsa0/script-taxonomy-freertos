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

        return severities;

    def listTypesBySeverity(self, errorTags, severityTarget):
        typesBySeverity = {}
        validSeverities = self.listSeverities(errorTags)
        severityTarget = severityTarget.lower() 

        if severityTarget not in validSeverities:
            print("\n")
            print(f"***{severityTarget} is not present in severities!***")

        for error in errorTags:
            severity = error.get('severity')
            type = error.get('id')

            if severity == severityTarget:
                if type in typesBySeverity:
                    typesBySeverity[type] += 1 #key type = value
                else:
                    typesBySeverity[type] = 1

        return typesBySeverity

    def listTypes(self, errorTags):
        types = set()

        for type in errorTags:
            types.add(type.get('id')) #id == type
        print(types)

        lengthTypes = len(types)

        return lengthTypes, types;

    def printSeveritiesOccurrences(self, errorTags):
        countWarning, countStyle, countPerformance, countPortability, countInformation, countError = self.countSeveritiesOccurrences(errorTags)

        print(f"Warnings: {countWarning}")
        print(f"Style issues: {countStyle}")
        print(f"Performance issues: {countPerformance}")
        print(f"Portability issues: {countPortability}")
        print(f"Information issues: {countInformation}")
        print(f"Errors: {countError}")