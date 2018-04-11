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
def calcLeverArm1(centerOfSystem, massLocation):
    if massLocation < centerOfSystem:
        leverArmLen1 = centerOfSystem - massLocation
    else:
        leverArmLen1 = massLocation - centerOfSystem
    return leverArmLen1
def calcLeverArm2(centerOfSystem, centerOfStick):
    if centerOfStick < centerOfSystem:
        leverArmLen2 = centerOfSystem - centerOfStick
    else:
        leverArmLen2 = centerOfStick - centerOfSystem
    return leverArmLen2

centerOfStick = float(input("Where is the center of mass of the meter stick?: "))
addedMassLocation = float(input("Where did you put the added mass at?: "))
centerOfSystem = float(input("Where is the center of mass of the system?: "))
addedMass = float(input("How much mass did you add?: "))
leverArmLen1 = calcLeverArm1(centerOfSystem, addedMassLocation)
leverArmLen2 = calcLeverArm2(centerOfSystem, centerOfStick)
massOfStick = calcMass(addedMass, leverArmLen1, leverArmLen2)
print(massOfStick, "kg")