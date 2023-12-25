class Solution:
    def calPoints(self, operations: List[str]) -> int:
        totalSum = 0
        record = []
        recordIndex = -1 #cause index start from 0 in array 
        for i in range(len(operations)):
            if operations[i] == "C":
                totalSum -= record[recordIndex]
                record.pop()
                recordIndex -= 1
            elif operations[i] == "D":
                digit = record[recordIndex] * 2
                record.append(digit)
                recordIndex += 1
                totalSum += record[recordIndex]
            elif operations[i] == "+":
                recordSum = record[recordIndex] + record[recordIndex - 1]
                record.append(recordSum)
                recordIndex += 1
                totalSum += record[recordIndex]
            else:
                record.append(int(operations[i]))
                recordIndex += 1
                totalSum += record[recordIndex]
        return totalSum