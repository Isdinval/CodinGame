import sys
import math

def main():
    # Initialize a flag to check if BOOST is used
    boost_used = False
    
    # Dictionary to store checkpoints
    checkpoints = {}
    checkpoint_order = []
    
    # Variable to track if all checkpoints are known
    all_checkpoints_known = False

    # Game loop
    while True:
        # Read the position of your pod and the next checkpoint
        x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
        opponent_x, opponent_y = [int(i) for i in input().split()]
        
        # Check if the checkpoint is already known
        checkpoint_key = (next_checkpoint_x, next_checkpoint_y)
        if checkpoint_key not in checkpoints:
            checkpoints[checkpoint_key] = len(checkpoints)
            checkpoint_order.append(checkpoint_key)
        
        # If we have seen all checkpoints
        if len(checkpoints) > 1 and not all_checkpoints_known:
            if checkpoint_key == checkpoint_order[0] and len(checkpoints) > 1:
                all_checkpoints_known = True
                print(f"All checkpoints known: {checkpoints}", file=sys.stderr)
        
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

        # Output the command to steer towards the next checkpoint
        print(f"{target_x} {target_y} {command}")

if __name__ == "__main__":
    main()
