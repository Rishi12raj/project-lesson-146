import cv2


def main():
    image = cv2.imread("example.jpg")
    if image is None:
        raise FileNotFoundError("Could not load example.jpg")

    sizes = {
        "small": 200,
        "medium": 400,
        "large": 600,
    }

    for name, dimension in sizes.items():
        resized_image = cv2.resize(image, (dimension, dimension))
        output_filename = f"example_{name}.jpg"
        if not cv2.imwrite(output_filename, resized_image):
            raise OSError(f"Could not save {output_filename}")
        cv2.imshow(f"{name.capitalize()} - {dimension}x{dimension}", resized_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()