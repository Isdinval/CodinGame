import sys
import math

def main():
    # Initialize a flag to check if BOOST is used
    boost_used = False
    
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
        
        # Determine thrust value dynamically
        # Thrust decreases with the increase of the angle to the target
        if abs(angle_to_target) > 90:
            thrust = 0  # Too sharp angle, slow down to turn
        else:
            angle_factor = max(0, (1 - abs(angle_to_target) / 90))
            distance_factor = min(1, distance_to_target / 1000)
            thrust = int(100 * angle_factor * distance_factor)

            
        # Check if we can use BOOST
        if not boost_used and abs(angle_to_target) < 30 and distance_to_target > 5000:
            command = "BOOST"
            boost_used = True
        else:
            command = str(thrust)
        
        # Collision avoidance logic
        opponent_dist = math.sqrt((opponent_x - x) ** 2 + (opponent_y - y) ** 2)
        if opponent_dist < 800:  # If the opponent is too close
            # Calculate distances to the checkpoint
            my_dist_to_checkpoint = math.sqrt((next_checkpoint_x - x) ** 2 + (next_checkpoint_y - y) ** 2)
            opponent_dist_to_checkpoint = math.sqrt((next_checkpoint_x - opponent_x) ** 2 + (next_checkpoint_y - opponent_y) ** 2)
            
            if my_dist_to_checkpoint < opponent_dist_to_checkpoint:
                # Case 1: We are closer to the checkpoint
                avoid_x = x - (opponent_x - x) * 0.5
                avoid_y = y - (opponent_y - y) * 0.5
            else:
                # Case 2: Opponent is closer to the checkpoint
                avoid_x = x - (opponent_x - x)
                avoid_y = y - (opponent_y - y)
            
            target_x = (target_x + avoid_x) // 2
            target_y = (target_y + avoid_y) // 2


        # Output the command to steer towards the next checkpoint
        print(f"{target_x} {target_y} {command}")

if __name__ == "__main__":
    main()
