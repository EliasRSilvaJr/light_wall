import cv2
import numpy as np


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


if __name__ == "__main__":
    message = "00heLLo0"
    path_to_images = "images/"
    save_video_at = f"videos/{message.lower()}.avi"
    image_duration = 1.25
    interval_duration = 1

    make_light_message(message, path_to_images, save_video_at, image_duration, interval_duration)
