START PROGRAM

DISPLAY "Basketball Shot Trainer"

SET perfectAngle to a random number between 35 and 55
SET perfectPower to a random number between 40 and 80

SET number_of_rounds to 10

FOR each round from 1 to number_of_rounds DO
    PROMPT user to enter shot angle
    PROMPT user to enter shot power

    CALCULATE error as the distance between
        (angle, power) and (perfectAngle, perfectPower)

    IF error is less than or equal to 1 THEN
        DISPLAY "Swish! Perfect shot!"
        EXIT loop
    ELSE IF error is less than or equal to 2 THEN
        DISPLAY "So close!"
    ELSE IF error is less than or equal to 5 THEN
        DISPLAY "Close"
    ELSE
        DISPLAY "Way off"
    END IF

    DISPLAY error score
    DISPLAY number of shots left
END FOR

DISPLAY perfectAngle
DISPLAY perfectPower

END PROGRAM
