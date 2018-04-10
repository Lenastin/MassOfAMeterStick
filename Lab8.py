def calcWeight(mass):
    w = mass * 9.82
    return w
def calcTorque(weight, leverArmLen):
    torque = weight * leverArmLen
    return torque
def calcForce(torque, leverArmLen):
    force = torque / leverArmLen
    return force
def calcMass(addedMass, leverArmLen1, leverArmLen2):
    weightOfMass = calcWeight(addedMass)
    torqueOfMass = calcTorque(weightOfMass, leverArmLen1)
    force = calcForce(torqueOfMass, leverArmLen2)
    mass = force / 9.82
    return mass

addedMass = float(input("How much mass did you add?: "))
leverArmLen1 = float(input("How far from the center of mass of the system is the added mass?: "))
leverArmLen2 = float(input("How far away is the center of mass of the meter stick from the center of mass of the system?: "))

massOfStick = calcMass(addedMass, leverArmLen1, leverArmLen2)
print(massOfStick)