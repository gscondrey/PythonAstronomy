#Determining telescope focal length and magnification
aperture = float(input ("What is the telescope's aperture? "))
aperture = aperture * 25.4
f = float(input ("What is the telescope's f-number? "))
eyepiece = float(input ("What size is the eyepiece? "))
fl = f*aperture
mag = fl/eyepiece
print ("The telescope has a", fl, "mm focal length and will deliver", int(mag), "power magnification.")
