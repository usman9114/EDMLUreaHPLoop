import json
import pandas as pd

class Program:

    def predictCarbamateConcentration(self,inputJSON):
        objJSON = json.loads(inputJSON)
        dfInput = pd.DataFrame(objJSON)
        jsonOutPut='{"UreaPercentage ":75}'
        return jsonOutPut

if __name__ == "__main__":
    inputJSON = '{"CO2FlowToR01 ":[32.09561,32.43092],' \
                '"E01ShellSteamFlow ":[0.013046386,0.0119011495],' \
                '"NH3FlowtoR01":[31.752283,32.07501],' \
                '"CarbamateFlowA":[31.792337,31.531408],' \
                '"CarbamateFlowB":[31.646997,31.730537],' \
                '"R01OutletValveOpening":[15.627458,15.684682],' \
                '"Carbamateinletvalve":[14.8492565,14.8916],' \
                '"E01SteamChestPressure":[15.397433,15.461519],' \
                '"NH3toR01InletPressure":[37.015972,36.636665],' \
                '"CarbonDioxideInletTemperature":[996.2953,996.3502],' \
                '"R01BottomTemp":[28.555376,28.68149],' \
                '"Nh3CarbamatetoR01temperature":[0.24395289,0.24484555],' \
                '"ReactorOutletTemperature":[33.856438,33.3512],' \
                '"E01BottomTemp":[0.15753667,0.15759157],' \
                '"AmmoniaCarbamatetoR01temperature ":[996.2953,996.3502],' \
                '"R01BottomPress":[28.555376,28.68149],' \
                '"CarbamateFlowAB":[0.24395289,0.24484555],' \
                '"R01TempDelta":[33.856438,33.3512],' \
                '"Timestamp":[33.856438,33.3512]}'
    objProg = Program()
    outPutJSON=objProg.predictCarbamateConcentration(inputJSON=inputJSON)
    print(outPutJSON)