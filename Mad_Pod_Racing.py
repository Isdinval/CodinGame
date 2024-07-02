import sys
import math

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    def calculate(self, setpoint, measured_value):
        error = setpoint - measured_value
        self.integral += error
        derivative = error - self.previous_error
        self.previous_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative

def main():
    # Initialize a flag to check if BOOST is used
    boost_used = False

    # Initialize PID controllers for angle and thrust
    pid_angle = PIDController(kp=0.4, ki=0.0, kd=0.03)  # Fine-tune these values
    pid_thrust = PIDController(kp=0.9, ki=0.0, kd=0.05)  # Fine-tune these values
    
    # Game loop
    while True:
        # Read the position of your pod and the next checkpoint
        x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
        opponent_x, opponent_y = [int(i) for i in input().split()]
        
        # Calculate the direction to the next checkpoint
        target_x = next_checkpoint_x
        target_y = next_checkpoint_y

        # Calculate the angle and distance to the target
        angle_to_target = next_checkpoint_angle
        distance_to_target = next_checkpoint_dist
        
        # Use PID controller to calculate the thrust dynamically
        if abs(angle_to_target) > 90:
            thrust = 0  # Too sharp angle, slow down to turn
        else:
            thrust = pid_thrust.calculate(0, abs(angle_to_target))  # Target is 0 degrees error
            thrust = min(max(int(thrust), 95), 100)  # Ensure a minimum thrust of 20 to start

        # Check if we can use BOOST
        if not boost_used and abs(angle_to_target) < 10 and distance_to_target > 5000:
            command = "BOOST"
            boost_used = True
        else:
            command = str(thrust)
        
        # Use PID controller to adjust the target position for smoother turns
        adjusted_angle = pid_angle.calculate(0, angle_to_target)  # Target is 0 degrees error
        radian_adjustment = math.radians(adjusted_angle)
        target_x += int(distance_to_target * math.cos(radian_adjustment) * 0.01)  # Apply a smaller adjustment
        target_y += int(distance_to_target * math.sin(radian_adjustment) * 0.01)  # Apply a smaller adjustment

        # Output the command to steer towards the next checkpoint
        print(f"{target_x} {target_y} {command}")

if __name__ == "__main__":
    main()
