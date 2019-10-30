import cv2
import argparse


FPS = 10


def load_message_images(message: str, path_to_images: str) -> list:
    list_of_images = [cv2.imread(f"{path_to_images}{char}.png") for char in message]
    return list_of_images


def write_image(video_writer, image, n_times):
    for _ in range(n_times):
        # Write the image into the file
        video_writer.write(image)


def make_light_message(message: str, path_to_images: str, save_video_at: str,
                       image_duration: float, interval_duration: float):
    message = message.lower()
    list_of_images = load_message_images(message, path_to_images)
    frame_height, frame_width = list_of_images[0].shape[:2]

    none = cv2.imread(f"{path_to_images}0.png")

    frames_per_image = int(FPS * image_duration)
    frames_between_images = int(FPS * interval_duration)

    # Define the codec and create VideoWriter object
    video_writer = cv2.VideoWriter(save_video_at, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), FPS, (frame_width, frame_height))
    write_image(video_writer, list_of_images[0], frames_per_image)
    for image in list_of_images[1:]:
        write_image(video_writer, none, frames_between_images)
        write_image(video_writer, image, frames_per_image)

    video_writer.release()


def main(_):
    parser = argparse.ArgumentParser()
    parser.add_argument('--message', help='message to be displayed')
    parser.add_argument('--path_to_images', help='path to image folder')
    parser.add_argument('--save_video_at', help='file path to save resulting video')
    parser.add_argument('--letter_duration', help='duration of lighted letter (seconds)')
    parser.add_argument('--interval_duration', help='duration between letters (seconds)')
    args = parser.parse_args()

    make_light_message(args.message, args.path_to_images, args.save_video_at, args.letter_duration, args.interval_duration)


"""
if __name__ == "__main__":
    message = "00heLLo0"
    path_to_images = "images/"
    save_video_at = f"videos/{message.lower()}.avi"
    image_duration = 1.25
    interval_duration = 1

    make_light_message(message, path_to_images, save_video_at, image_duration, interval_duration)
"""
