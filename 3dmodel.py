import vtk
import os

# Replace with the path to your DICOM images directory
dicom_directory = r'C:\pywork\Dentistry DataSet\Dentistry DataSet\Decompressed\[QUANTUMIQ 7,64]'

# Create a DICOM reader
reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName(dicom_directory)
reader.Update()

# Create a volume mapper
mapper = vtk.vtkSmartVolumeMapper()
mapper.SetInputConnection(reader.GetOutputPort())

# Create an opacity transfer function
opacity_transfer_function = vtk.vtkPiecewiseFunction()
opacity_transfer_function.AddPoint(0, 0.0)
opacity_transfer_function.AddPoint(255, 1.0)

# Create a color transfer function (rainbow colormap)
color_transfer_function = vtk.vtkColorTransferFunction()
color_transfer_function.AddRGBPoint(0, 0.0, 0.0, 0.0)
color_transfer_function.AddRGBPoint(64, 1.0, 0.0, 0.0)  # Red
color_transfer_function.AddRGBPoint(128, 1.0, 1.0, 0.0)  # Yellow
color_transfer_function.AddRGBPoint(192, 0.0, 1.0, 0.0)  # Green
color_transfer_function.AddRGBPoint(255, 0.0, 0.0, 1.0)  # Blue

# Create a volume property
volume_property = vtk.vtkVolumeProperty()
volume_property.SetColor(color_transfer_function)
volume_property.SetScalarOpacity(opacity_transfer_function)

# Create a volume
volume = vtk.vtkVolume()
volume.SetMapper(mapper)
volume.SetProperty(volume_property)

# Create a renderer
renderer = vtk.vtkRenderer()

# Create a render window
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Create a render window interactor
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# Add the volume to the renderer
renderer.AddVolume(volume)

# Set up the camera position and orientation
renderer.GetActiveCamera().Azimuth(30)
renderer.GetActiveCamera().Elevation(30)
renderer.ResetCamera()

# Set the background color
renderer.SetBackground(0.1, 0.1, 0.1)

# Render the scene
render_window.Render()
render_window_interactor.Start()