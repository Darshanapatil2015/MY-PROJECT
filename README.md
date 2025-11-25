# stegnography for beginners
Steganography is the practice of concealing information. It involves hiding data within an ordinary, non-secret file or message to prevent detection. The hidden information is being extracted at the receiving end. Often, steganography is combined with encryption to add an extra layer of security for the hidden data. With the help of Steganography, we can hide any digital content virtually like text, image, videotape, etc.

The term "steganography" is derived from the Greek word "steganos" which means "hidden or covered" and "graph" means "to write." It has been in use for centuries. For example, in ancient Greece, people carved messages onto wood and covered them with wax to hide it. Similarly, Romans used different types of invisible inks which could be revealed when exposed to heat or light.
How Steganography Works
Step 1: The first step in steganography is selecting a cover medium which is the file or message that will carry the hidden data. Common cover media include:

Images (JPEG, PNG, BMP, etc.)
Audio files (MP3, WAV, etc.)
Video files (MP4, AVI, etc.)
Text files or documents
Step 2: Sometimes, before embedding, the secret message is encrypted to add an additional layer of security. This ensures that even if someone detects the hidden data, they cannot read it without the decryption key.

Step 3: The secret message is then hidden using one of several techniques:

Least Significant Bit (LSB): The least significant bit of a byte is changed to hide the secret message. This method is often used in image and audio files.
Frequency Domain: Instead of modifying the raw data (like pixels or audio samples), the secret message can be embedded in the frequency components of an image or audio file.
Bit Planes: In this method, data is hidden in the higher-order bit planes of an image. This can be more secure because it uses bits that are less likely to be noticed.
The most common is Least Significant Bit (LSB) encoding.

Step 4: The modified data is then embedded into the cover medium. The resulting file which now contains both the cover data and the hidden message is referred to as the stego-object which can be safely transmitted or stored without raising suspicion.

Step 5: The receiver of the stego-object needs to know the method used for embedding the secret message. In some cases, a secret key is required to extract the data if encryption is used in combination with steganography.
