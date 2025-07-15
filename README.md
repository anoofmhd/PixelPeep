PixelPeep

This project compares two images to determine whether they are similar or different using:

- **SSIM (Structural Similarity Index)** for pixel-level similarity  
- **ORB (Oriented FAST and Rotated BRIEF)** feature matching for structural or keypoint similarity

It is useful for detecting tampering, comparing edited vs original images, or general image matching tasks.

---

## Features

-  Compares two grayscale images
-  Uses **SSIM** for structural similarity
-  Falls back to **ORB keypoint matching** if SSIM is low or sizes differ
-  Prints similarity results based on threshold logic
-  Handles errors like missing or unreadable images

---

##  How It Works

1. Loads two grayscale images using OpenCV  
2. Checks if both images are of the same size:
   - If yes: calculates SSIM score
     - If score ≥ 0.5 → images considered similar
     - Else → falls back to ORB comparison
   - If not the same size → directly uses ORB feature matching
3. ORB uses keypoint descriptors and a ratio test to determine similarity

---

##  Example Output

```bash
Image 1 bringed successfully
Image 2 bringed successfully
Images are similar
