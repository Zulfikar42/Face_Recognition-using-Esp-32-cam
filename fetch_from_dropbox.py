import dropbox

# Dropbox access token (get it from Dropbox App console)
DROPBOX_ACCESS_TOKEN = 'your_dropbox_access_token'

def fetch_image_from_dropbox():
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    
    # Specify the image file path in Dropbox
    image_path = '/path_to_your_image_in_dropbox/suspect.jpg'
    
    # Download the file
    _, response = dbx.files_download(image_path)
    
    # Save the file locally
    local_path = '/tmp/suspect.jpg'  # Temporary path
    with open(local_path, 'wb') as f:
        f.write(response.content)
    
    return local_path

