from functions import calculate_calories_burned

print("Welcome to the Calories Burned Calculator!")
activity = input("Enter the activity (e.g., running, cycling, swimming): ")
duration = float(input("Enter the duration of activity in minutes: "))
weight = float(input("Enter your weight in kilograms: "))
calories_burned = calculate_calories_burned(activity, duration, weight)

if isinstance(calories_burned, str):
    print(calories_burned)
else:
    print("You burned calories.", calories_burned)

#test plan:
#Happy path:
#lietotājs ievada savu aktivitāti (piemērs: skriešana), ilgumu minūtēs (piemērs: 60 minūtes), svaru kilogramos (piemērs: 60 kg) un saņem izlietotās kalorijas = 600.0cal
    
#Use case
#1. uzzināt, cik daudz kaloriju lietotājs sadedzina stundā skriešanas. 2. uzzināt, cik daudz kaloriju lietotājs sadedzina vienā peldēšanas stundā. 
#3. uzzināt, cik daudz kaloriju lietotājs sadedzina vienā riteņbraukšanas stundā. 4. uzzināt, kur lietotājs sadedzina vairāk kaloriju stundā.
#5. noskaidrot, kur lietotājs sadedzina vismazāk kaloriju stundā.
    
#edge case
# 1. lietotājs neievada svaru kilogramos. 2. lietotājs ievada darbības ilgumu ne minūtēs. 3. lietotājs veic darbību, kas netiek piedāvāta.
#4. Lietotājs ievada svara daudzumu ar "kg" (60 kg) 5. Lietotājs ievada darbības ilgums ar "min" (60 min)
    