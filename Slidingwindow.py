import random
import time

# Simulation parameters
TOTAL_FRAMES = 10
WINDOW_SIZE = 4
LOSS_PROBABILITY = 0.2     # 20% chance a frame/ACK is lost
TIMEOUT = 2                # Seconds

def send_frame(frame_no):
    """Simulate sending a frame with chance of loss."""
    print(f"Sender: Sending Frame {frame_no}")
    
    # Simulate random loss
    if random.random() < LOSS_PROBABILITY:
        print(f"Channel: Frame {frame_no} LOST")
        return False
    else:
        print(f"Channel: Frame {frame_no} delivered successfully")
        return True

def send_ack(frame_no):
    """Simulate sending an ACK with chance of loss."""
    print(f"Receiver: Sending ACK {frame_no}")
    
    if random.random() < LOSS_PROBABILITY:
        print(f"Channel: ACK {frame_no} LOST")
        return False
    else:
        print(f"Channel: ACK {frame_no} delivered successfully")
        return True

def sliding_window():
    base = 0          # First frame in window
    next_seq = 0      # Next frame to send
    
    print("\n=== Sliding Window Protocol Simulation (Go-Back-N) ===\n")
    
    while base < TOTAL_FRAMES:
        # Send frames as long as window is not full
        while next_seq < base + WINDOW_SIZE and next_seq < TOTAL_FRAMES:
            delivered = send_frame(next_seq)
            next_seq += 1
            time.sleep(0.5)
        
        print(f"\nSender waiting for ACKs... Window = [{base} .. {next_seq-1}]\n")
        time.sleep(1)
        
        # Simulate ACK reception
        ack_received = False
        for frame in range(base, next_seq):
            if random.random() > LOSS_PROBABILITY:
                print(f"Receiver: Frame {frame} received")
                if send_ack(frame):
                    ack_received = True
                    base = frame + 1  # Slide window
                    print(f"Sender: Sliding window, new base = {base}\n")
                    time.sleep(1)
                else:
                    print("Sender: ACK lost, timeout will occur")
                    time.sleep(TIMEOUT)
                    break
            else:
                print(f"Receiver: Frame {frame} LOST before processing")
                time.sleep(TIMEOUT)
                break
        
        # Timeout → retransmit from base frame
        if not ack_received:
            print("\n*** TIMEOUT! Retransmitting from frame", base, "***\n")
            next_seq = base
    
    print("\n=== All frames sent and acknowledged successfully! ===")

# Run the simulation
sliding_window() 
