console.log("JavaScript Successfully Connected")
var formulas = {'Area of a Circle': "AreaCircle.jpg", 'Area of a Cube': 'AreaCube.png', 'Area of a Rectangle': 'AreaRectangle.jpg', 'Area of a Rhombus': 'AreaRhombus.png', 'Area of a Square': 'AreaSquare.jpg', 'Area of a Trapezoid': 'AreaTrapezoid.png', 'Area of a Triangle': 'AreaTriangle.png', 'Equation of a Circle': 'CircleEquation.png', 'Combination Formula': 'CombinationFormula.png', 'Complex Numbers': 'ComplexNumber.jpg', 'Distance Formula': 'Distance.png', 'Law of Cosines': 'LawCosines.png', 'Law of Sines': 'LawSines.png', 'Permutation Formula': 'PermutationFormula.jpg', 'Probability Density': 'ProbabilityDensity.jpg', 'Pythagorean Theorum': 'PythagoreanTheorum.png', 'Quadratic Formula': 'QuadraticFormula.png', 'Slope Intercept Form': 'SlopeInterceptForm.png', 'Surface Area of a Rectangular Prism': 'SurfaceAreaRectangularPrism.jpg', 'Surface Area of a Sphere': 'SurfaceAreaSphere.jpg', 'Volume of a Triangular Prism': 'VolmeTriangularPrism.png', 'Volume of a Pyramid': 'VolumePyramid.jpg', 'Volume of a Rectangular Prism': 'VolumeRectangularPrism.png'}
var basedir = "------Enter the Path to Your Images Here------"  
var items;
function search() {
    var characters = document.getElementById("search").value
    if (characters == ""){
        characters = " "
    }
    var results = []
    for (x in formulas) {
        lowerx = x.toLowerCase()
        if (lowerx.search( characters.toLowerCase()) != -1) {
            results.push(x)
        }
    }
    items = results
}

function searchbar(){
    search()
    var a = document.getElementById("Results");
    while (a.firstChild)  {
        a.removeChild(a.firstChild)
    }


    var characters = document.getElementById("search").value

    
    var iterator = 1

    for (let x in items){
        var td = document.createElement('td');
        var tr = document.createElement("tr")
        var text = items[x]
        var textChild = document.createTextNode(text)
        td.setAttribute('id', items[x])
        td.setAttribute("onclick", 'displayImage(formulas[this.id])')
        td.setAttribute("style", "color: white;")

        td.appendChild(textChild)
        tr.appendChild(td)
        a.appendChild(tr)
        iterator += 1
    }

    // Adding Blank Cell to Maintain Size
    var td = document.createElement('td');
    var tr = document.createElement("tr")
    var text = "Surface Area of a Rectangular Prism"
    var text = "--------------------------------------------"
    var textChild = document.createTextNode(text)
    td.setAttribute('id', "---")
    td.setAttribute("style", "color: white;")

    td.appendChild(textChild)
    tr.appendChild(td)
    a.appendChild(tr)
}


function displayImage(path) {
    console.log(path)
    img = document.getElementById("img")
    img.src = basedir + path 
}


