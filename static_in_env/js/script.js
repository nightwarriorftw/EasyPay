Promise.all([
  faceapi.nets.faceRecognitionNet.loadFromUri('https://raw.githubusercontent.com/nightwarriorftw/face-detection-js/master/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('https://raw.githubusercontent.com/nightwarriorftw/face-detection-js/master/models'),
  faceapi.nets.ssdMobilenetv1.loadFromUri('https://raw.githubusercontent.com/nightwarriorftw/face-detection-js/master/models')
]).then(start)


// Detecting the image and labeling
async function start() {
  console.log('Models loaded');
  // created container for box
  const container = document.createElement('div');
  container.style.position = 'relative';
  document.body.append(container);

  // calling the 
  const labeledFaceDescriptors = await loadLabeledImages();
  const faceMatcher = new faceapi.FaceMatcher(labeledFaceDescriptors,
    0.6);

  let canvas;
  document.getElementById('startProcessing').addEventListener('click', async () => {
    console.log('Processing has started !!!');
    // delete the image uploaded
    if(canvas) canvas.remove();
    const image = document.getElementById('clickedImage');

    // For drawing boxes on the image
    // container.append(image);
    canvas = faceapi.createCanvasFromMedia(image);
    // container.append(canvas);

    // changing dimesions of the canvas
    const dimensions = { width: image.width, height: image.height };
    faceapi.matchDimensions(canvas, dimensions);


    const detections = await faceapi.detectAllFaces(image)
      .withFaceLandmarks().withFaceDescriptors()

    // resize all our detections for our dimensions
    const resizedDetections = await faceapi.resizeResults(detections, dimensions);

    const results = resizedDetections.map(d => faceMatcher.findBestMatch(d.descriptor));

    const customerNameField = document.getElementById('id_customer_name');

    // drawing the actual box for each face
    results.forEach((results, i) => {
      console.log(results.toString());
      customerNameField.value = results.toString().split(' ')[0];
    });

    if(customerNameField.value===""){
      console.log('Customer not verified !!');
      window.alert('Customer not verified !! Press ok to try again !!');
      location.reload();
    }
    
  })
}

// function to parse all the names from the images
function loadLabeledImages() {
  const labels = ['Aditya', 'Bittu', 'Jhalani'];

  // return all the promises for returning all the images
  return Promise.all(
    labels.map(async label => {
      const descriptions = [];
      for (let i = 1; i <= 3; i++) {
        const img = await faceapi.fetchImage(
          `https://raw.githubusercontent.com/nightwarriorftw/face-detection-js/master/labeled_images/${label}/${i}.jpeg`
          );
        const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor()
        descriptions.push(detections.descriptor)
      }

      return new faceapi.LabeledFaceDescriptors(label, descriptions);
    })
  )
}