import xml.etree.ElementTree as ET

class TaxonomyFunctions:
    def countSeverityOccurrences(self, errorTags, severity):
        severityTypes = self.listSeverities(errorTags)
        if severity not in severityTypes:
            print("Error! Type a valid severity.")
    
        count = 0
        
        for errorTag in errorTags:
            severityType = errorTag.get('severity')   

            if severity == severityType:
                count += 1

        return count;

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
        typesSet = set()
        typesDict = {} 

        for errorTag in errorTags:
            type = errorTag.get('id') #id == type

            if type in typesDict:
                typesDict[type] += 1 
            else:
                typesDict[type] = 1

            typesSet.add(type) 

        lengthTypes = len(typesSet)
        return lengthTypes, typesDict;

    def printSeveritiesOccurrences(self, errorTags):
        countWarning, countStyle, countPerformance, countPortability, countInformation, countError = self.countSeveritiesOccurrences(errorTags)

        print(f"Warnings: {countWarning}")
        print(f"Style issues: {countStyle}")
        print(f"Performance issues: {countPerformance}")
        print(f"Portability issues: {countPortability}")
        print(f"Information issues: {countInformation}")
        print(f"Errors: {countError}")