from PySide6.QtWidgets import QGraphicsScene,QGraphicsView
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
def load_img_bob(img_path,img_object,parent,x_ratio,y_ratio):
    sence = QGraphicsScene(parent)
    pixMap = QPixmap(img_path)
    sence.addPixmap(pixMap)
    img_object.setScene(sence)
    img_object.fitInView(sence.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
    img_object.scale(x_ratio,y_ratio)
    # Kích hoạt kéo tay và zoom dưới con trỏ
    img_object.setDragMode(img_object.DragMode.ScrollHandDrag)
    img_object.setTransformationAnchor(img_object.ViewportAnchor.AnchorUnderMouse) 