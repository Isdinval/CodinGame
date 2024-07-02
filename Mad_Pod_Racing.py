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
        
        # Determine thrust value
        if abs(angle_to_target) > 90:
            thrust = 0  # Too sharp angle, slow down to turn
        elif distance_to_target < 1000:
            thrust = 50  # Slow down as we approach the checkpoint
        else:
            thrust = 100  # Full speed ahead
        
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
