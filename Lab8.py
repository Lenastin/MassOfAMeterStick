def calcWeight(mass):
    w = mass * 9.82
    print("The weight of the mass is:", w, "N")
    return w
def calcTorque(weight, leverArmLen):
    torque = weight * leverArmLen
    print("The torque of the mass is:", torque, "Nm")
    return torque
def calcForce(torque, leverArmLen):
    force = torque / leverArmLen
    print("The force caused by the meter stick is:", force, "N")
    return force
def calcMass(addedMass, leverArmLen1, leverArmLen2):
    weightOfMass = calcWeight(addedMass)
    torqueOfMass = calcTorque(weightOfMass, leverArmLen1)
    force = calcForce(torqueOfMass, leverArmLen2)
    mass = force / 9.82
    return mass
def calcLeverArm1(centerOfSystem, massLocation):
    if massLocation < centerOfSystem:
        leverArmLen1 = centerOfSystem - massLocation
    else:
        leverArmLen1 = massLocation - centerOfSystem
    print("The length of the lever arm for the mass is:", leverArmLen1, "m")
    return leverArmLen1
def calcLeverArm2(centerOfSystem, centerOfStick):
    if centerOfStick < centerOfSystem:
        leverArmLen2 = centerOfSystem - centerOfStick
    else:
        leverArmLen2 = centerOfStick - centerOfSystem
    print("The length of the lever arm for the meter stick is:", leverArmLen2, "m")
    return leverArmLen2

centerOfStick = float(input("Where is the center of mass of the meter stick? (m): "))
addedMassLocation = float(input("Where did you put the added mass at? (m): "))
centerOfSystem = float(input("Where is the center of mass of the system? (m): "))
addedMass = float(input("How much mass did you add? (kg): "))
leverArmLen1 = calcLeverArm1(centerOfSystem, addedMassLocation)
leverArmLen2 = calcLeverArm2(centerOfSystem, centerOfStick)
massOfStick = calcMass(addedMass, leverArmLen1, leverArmLen2)
print("Mass of the stick is:", massOfStick, "kg")
k = input("Enter something to quit!")