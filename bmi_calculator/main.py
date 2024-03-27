from functions import calculate_bmi, interpret_bmi

print("Welcome to the BMI Calculator!")
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight_kg, height_m)
interpretation = interpret_bmi(bmi)
print("Your BMI is {:.2f}".format(bmi))
print("Interpretation: ", interpretation)


#Test plan:
#Happy path: Lietotājs vada savu svaru un augumu, piemēram, 67 kg un 1,8 m, un iegūst savu bmu = 20,68.

#Use case: 1. novērtēt korelācijas pakāpi starp svaru un augumu. 2. noskaidrot, vai svars ir normāls, nepietiekams svars vai liekais svars.
#3. noskaidrot citas personas ķermeņa masas indeksu. 4. uzzināt, kāds ir normālais svars noteiktam augumam. 
#5. noskaidrot, kāds svars ir aptaukošanās, ņemot vērā personas augumu.


#Edge case
# 1. Lietotājs ievadīja cilvēka augumu nevis metros 2. Lietotājs ievadīja svaru nevis kilogramos 3. lietotājs raksta augumu svara vietā un otrādi.
#4. lietotājs, ievadot daļskaitļus, lieto komatus, nevis punktu. 5. ķermeņa masas indekss ir lielāks par 30. 