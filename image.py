import cv2
from skimage.metrics import structural_similarity as ssim

def compare_ssim(img1, img2):
    #assert img.shape == img2.shape, "Images must be same size."
    if img1.shape == img2.shape:
        score, diff = ssim(img1, img2, full=True)
        if score >= 0.5:
            print('The given two images are similar.')
        else:
            #matches_count, matches = orb_feature_compare(img, img2)
            #print(f"Number of matches : {matches_count}")
            orb_feature_compare(img1, img2)

    else:
        #matches_count, matches = orb_feature_compare(img, img2)
        #print(f"Number of matches : {matches_count}")
        orb_feature_compare(img1, img2)

def orb_feature_compare(img1, img2):
    orb = cv2.ORB_create()

    kpA, desA = orb.detectAndCompute(img1, None)
    kpB, desB = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    matches = bf.knnMatch(desA, desB, k=2)

    #matches = sorted(matches, key=lambda x: x.distance)

    #return len(matches), matches
    good_matches = []

    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    if len(good_matches) > 30:
        print("Images are similar")
    else:
        print("Images are different")

img_a = cv2.imread('pictures/asus3.jpg', cv2.IMREAD_GRAYSCALE)
img_b = cv2.imread('pictures/asus.jpg', cv2.IMREAD_GRAYSCALE)

if img_a is None:
    print("Image 1 not found or path is incorrect!")
else:
    print("Image 1 bringed successfully")

if img_b is None:
    print("Image 2 not found or path is incorrect!")
else:
    print("Image 2 bringed successfully")

#ssim_score = compare_ssim(img, img2)
#print(f"SSIM Score : {ssim_score}")
compare_ssim(img_a, img_b)
