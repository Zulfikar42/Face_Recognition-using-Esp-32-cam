from deepface import DeepFace

def recognize_face(image_path):
    try:
        # Use DeepFace to find the person in the image
        result = DeepFace.find(img_path=image_path, db_path='/content/faces')
        
        if len(result) > 0:
            # If a match is found, return the identity
            matched_img_path = result[0].iloc[0]["identity"]
            return f"Match found: {matched_img_path}"
        else:
            return "No match found."
    
    except Exception as e:
        return f"Error in recognition: {str(e)}"

