import random

def sender(total_frames):
    frame = 0
    while frame < total_frames:
        print(f"Sender: Sending Frame {frame}")

        ack_received = receiver(frame)

        if ack_received:
            print(f"Sender: ACK received for Frame {frame}\n")
            frame += 1 
        else:
            print(f"Sender: Timeout! Resending Frame {frame}\n")

    print("Sender: All frames sent successfully!")


def receiver(frame):
    frame_lost = random.randint(0, 9) < 3

    if frame_lost:
        print(f"Receiver: Frame {frame} lost! No ACK sent.")
        return False 
    else:
        print(f"Receiver: Frame {frame} received. Sending ACK...")
        return True  

if __name__ == "__main__":
    total_frames = 5
    
    sender(total_frames)