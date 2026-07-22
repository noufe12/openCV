Face Recognition with OpenCV

This project detects and recognizes faces from an image using Python and OpenCV.

The program first finds a face in the image using a Haar Cascade classifier, which is a pre-trained model that looks for face-like patterns. Once a face is found, it’s converted to grayscale and used to train an LBPH (Local Binary Patterns Histograms) recognizer. LBPH works by looking at small patterns of pixel intensity around each point on the face, which makes it fairly good at handling small changes in lighting or angle.
When testing a new photo, the program compares the face it finds to the ones it was trained on and returns the closest match along with a confidence score. A lower score means a closer match. I used 70 as the cutoff — anything above that gets labeled “Unknown”.

Steps

	1.	Collect a few face photos and label them with a person ID.
	2.	Train the model on those photos, which creates a trainer.yml file.
	3.	Test the model on a new photo — it draws a box around the face and prints the predicted name.
    
Running it without a camera

Since I ran this in GitHub Codespaces (no webcam access), I used photo-based versions of the scripts instead of live video. I also had to install a missing system library (libgl1) and manually download the Haar Cascade file, since it wasn’t included with the OpenCV installation by default.

What could be improved

Right now the model only knows what it’s shown, so it needs a good number of training photos per person to be accurate. A logging feature (saving who was recognized and when) or a small interface for adding new people would make it more practical.
