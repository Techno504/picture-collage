# picture-collage
Uses image link to generate collage of edits of the picture using OpenCV with Python.

Inspired by [Murtaza's Workshop - Robotics and AI](https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A) with this [video](https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=0s).

Uses urllib to process URL requests.

# How it works:
## Asks for image link
![image](https://user-images.githubusercontent.com/59362676/154111378-90617c20-7ea4-4364-a74c-9087d04608dd.png)

## User copies and inserts image link
![image](https://user-images.githubusercontent.com/59362676/154111631-58d77340-811c-4d86-a03c-7bb397f935ab.png)
![image](https://user-images.githubusercontent.com/59362676/154111723-2dcb108c-e15f-4676-a879-c2a8d0f00eb6.png)

## Displays Collage
Program displays various edits of the image, including: original, HSV, canny, blur, dialation, greyscale.

![image](https://user-images.githubusercontent.com/59362676/154112178-488b0879-5ff7-47ab-be40-cd50df610768.png)

## Trackbars
Program also displays moveable trackbars that can be implemeted in the future to alter the collage live.

![image](https://user-images.githubusercontent.com/59362676/154112490-66bd87a1-f220-4297-814d-9f59df4f676d.png)

# Future Improvements
Some possible future improvements include:
- Linking trackbars to collage to change it live.
- Displaying name of edit under each image.
- Ability to save colllage.
