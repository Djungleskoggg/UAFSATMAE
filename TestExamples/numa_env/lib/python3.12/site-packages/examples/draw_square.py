from roarm_ik.arm import m3Arm

def main():
    print("Connecting to RoArm-M3...")
    arm = m3Arm(port="/dev/ttyUSB0")

    print("Moving to start of square...")
    # Move to the bottom-left corner of the square before drawing
    arm.move_to_xyz(0, 10, -5, 5, wait=True)

    print("Drawing 10x10 square in the Y-Z plane...")
    # draw_line(phi, x1, y1, z1, x2, y2, z2)
    
    # Bottom edge (Right to Left)
    arm.draw_line(0, 10, -5, 5, 10, 5, 5)
    
    # Right edge (Bottom to Top)
    arm.draw_line(0, 10, 5, 5, 10, 5, 15)
    
    # Top edge (Left to Right)
    arm.draw_line(0, 10, 5, 15, 10, -5, 15)
    
    # Left edge (Top to Bottom)
    arm.draw_line(0, 10, -5, 15, 10, -5, 5)

    print("Square complete. Returning to center.")
    arm.move_to_xyz(0, 10, 0, 10, wait=True)

if __name__ == "__main__":
    main()