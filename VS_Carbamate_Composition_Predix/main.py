import json
import pandas as pd

class Program:

    def predictCarbamateConcentration(self,inputJSON):
        objJSON = json.loads(inputJSON)
        dfInput = pd.DataFrame(objJSON)
        jsonOutPut='{"H2O":25,"CO2":45,"NH3":30}'
        return jsonOutPut

if __name__ == "__main__":
    inputJSON = '{"DateTime":[32.09561,32.43092],' \
                '"NH3RefluxFlowToC01":[0.013046386,0.0119011495],' \
                '"Water_flow_to_C-01":[31.752283,32.07501],' \
                '"Carbamate_flow_to_P-02A":[31.792337,31.531408],' \
                '"Carbamate_flow_to P-02B":[31.646997,31.730537],' \
                '"MP_Loop Pressure_Indicator":[15.627458,15.684682],' \
                '"C-01_4th_Tray_Temperature":[14.8492565,14.8916],' \
                '"C-01_3th_Tray_Temperature":[15.397433,15.461519],' \
                '"C-01_2th_Tray_Temperature":[37.015972,36.636665],' \
                '"Carbamate_Gases_Outlet_Temperature":[996.2953,996.3502],' \
                '"C-01_Outlet_Temperature":[28.555376,28.68149],' \
                '"Ammonical_Water_Temperature":[0.24395289,0.24484555],' \
                '"Carbamate_Bottom_Pressure":[33.856438,33.3512],' \
                '"MP-02_A_Pump_Amperes":[0.15753667,0.15759157],' \
                '"MP-02_B_Pump_Amperes":[996.2953,996.3502],' \
                '"Pump_Discharge_Pressure":[28.555376,28.68149],' \
                '"Water_flow_to_C-03":[0.24395289,0.24484555],' \
                '"Water_flow_to_C-04":[33.856438,33.3512]}'
    objProg = Program()
    outPutJSON=objProg.predictCarbamateConcentration(inputJSON=inputJSON)
    print(outPutJSON)