## summary script used to group data from the original files into more analitical ones.
## all indexed by date.
import pandas as pd 

data_path = "/Users/jguszr/AnacondaProjects/tsStudy/data/apple_health_export/"
out_path = "/Users/jguszr/AnacondaProjects/tsStudy/data/apple_health_export/summaries/"

dietary_files = [
    ("DietaryProtein.csv", "Protein_g"),
    ("DietaryFatTotal.csv", "FatTotal_g"),
    ("DietaryFatPolyunsaturated.csv", "Polyunsaturated_g"),
    ("DietaryFatMonounsaturated.csv", "FatMonounsaturated_g"),
    ("DietaryFatSaturated.csv", "FatSaturated_g"),
    ("DietaryCarbohydrates.csv", "Carbo_g"),
    ("DietarySodium.csv", "Sodium_mg"),
    ("DietarySugar.csv", "Sugar_g"),
    ("DietaryVitaminC.csv", "VitaminC_mg"),
    ("DietaryPotassium.csv", "Potassium_g"),
    ("DietaryIron.csv", "Iron_mg"),
    ("DietaryFiber.csv", "Fiber_g"),
    ("DietaryCholesterol.csv", "Cholesterol_mg"),
    ("DietaryCalcium.csv", "Calcium_mg"),
    
]

energy_files = [
    ("HeartRate.csv", "hrate"),
    ("BasalEnergyBurned.csv", "Basal_Energy"),
    ("DietaryEnergyConsumed.csv", "EnergyConsumed")
]

heart_files = [
    ("ActiveEnergyBurned.csv", "Active_Energy"),
    ("HeartRateVariabilitySDNN.csv", "rate_variability"),
    ("HeartRateVariabilitySDNN.csv", "rate_variability"),
    ("HighHeartRateEvent.csv", "high_rate"),
    ("RestingHeartRate.csv", "resting_rate"),
    ("WalkingHeartRateAverage.csv", "Walking_rate")

]

body_files = [
    ("BodyFatPercentage.csv", "fat_percentage"),
    ("BodyMass.csv", "bMass_kg"),
    ("BodyMassIndex.csv", "Bmi_c"),
    ("LeanBodyMass.csv", "lbm_kg")
]

distance_files = [
    ("DistanceWalkingRunning.csv", "distance_km")
]


workout_fields = [
        "creationDate",
        "workoutActivityType",
        "duration",
        "totalDistance",
        "totalEnergyBurned"
    ]

def single_file_handler(fname, outbound,field_list):
    df = pd.read_csv(filepath_or_buffer=data_path+fname)
    df[field_list].to_csv(outbound+fname)


def build_file(fname, outbound, lst):
    final_df = pd.DataFrame()
    for f in lst:
        df = pd.read_csv(data_path+f[0])
        df.creationDate = pd.to_datetime(df.creationDate)
        if "log)date" not in final_df.columns:
            final_df["log_date"] = df.creationDate
        final_df[f[1]] = df.value

    final_df.to_csv(header=True, path_or_buf= outbound+fname)


    
if __name__ == "__main__":
    print("generating stuff")

    build_file("dietary.csv",out_path, dietary_files)
    build_file("energy.csv", out_path, energy_files)
    build_file("heart_measures.csv",out_path,heart_files)
    build_file("body_measures.csv",out_path,body_files)
    build_file("distanceWalking.csv",out_path,distance_files)
    single_file_handler("workout.csv",out_path, workout_fields)