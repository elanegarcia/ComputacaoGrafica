import math
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData

# funcao responsavel por carregar os .obj:
loadPrcFileData ("", "load-file-type p3assimp")

# desativa o caching:
cache = BamCache.get_global_ptr()
cache.set_active(False)

class MeuApp(ShowBase):
  def __init__(self):
    ShowBase.__init__(self)
    self.loadModels()

    # definicao da difencao da luz do ambiente
    alight = AmbientLight("Ambient")
    alight.setColor((0.8, 0.8, 0.8, 1))
    alnp = self.render.attachNewNode(alight)
    self.render.setLight(alnp)

    # definicao de como as sombras sao projetadas
    plight = PointLight("plight")
    plight.setColor((0.6, 0.6, 0.6, 1))
    plight.setShadowCaster(True, 2048, 2048)
    self.render.setShaderAuto()
    plnp = self.render.attachNewNode(plight)
    plnp.setPos(2, 6, 3)
    self.render.setLight(plnp)
  
    # desativar trackball controle de camera:
    base.disableMouse()
    # chamar o método duckZoomTask cada frame:
    self.taskMgr.add(self.duckZoomTask, "DuckZoomTask")

  ##========== Método que carrega as malhas ==========##
  def loadModels(self):

    ## ======= background ======= ## 
    self.background = self.loader.loadModel("background.obj")
    tex = loader.loadTexture("background.png")
    self.background.setTexture(tex,1)
    self.background.reparentTo(self.render) # fazendo a malha visível

    ## ======= Patinho ======= ## 
    self.duck = self.loader.loadModel("duck.obj")  
    tex = loader.loadTexture("duck.png") #usa a textura das imagens .png
    self.duck.setTexture(tex,1)
    self.duck.setScale(0.25, 0.25, 0.25) # escalonamento X, Y, Z
    self.duck.setHpr(60,0,0) # rotacao em volta de Z, X, Y
    self.duck.setPos(0.75, -3.725, 1.5) # posicao (X,Y,Z)
    self.duck.reparentTo(self.render)
  
    ## ======= Vaquinhas Marrons ======= ##

    self.spot2 = self.loader.loadModel("cow.obj")
    tex = loader.loadTexture("cow_brown.png")
    self.spot2.setTexture(tex,1)
    self.spot2.setHpr(78,0,0) # rotacao em volta de Z, X, Y
    self.spot2.setPos(1, -4, 0)
    self.spot2.reparentTo(self.render)

    self.background_spot3 = self.loader.loadModel("cow.obj")
    tex = loader.loadTexture("cow_brown.png")
    self.background_spot3.setTexture(tex,1)
    self.background_spot3.setScale(0.5, 0.5, 0.5) # escalonamento X, Y, Z
    self.background_spot3.setPos(5.5, -11.75, 0)
    self.background_spot3.reparentTo(self.render)

    self.background_spot3 = self.loader.loadModel("cow.obj")
    tex = loader.loadTexture("cow_brown.png")
    self.background_spot3.setTexture(tex,1)
    self.background_spot3.setScale(0.5, 0.5, 0.5) # escalonamento X, Y, Z
    self.background_spot3.setPos(-3, -11.75, 0)
    self.background_spot3.reparentTo(self.render)

    ## ======= Vaquinhas Brancas ======= ##
    self.spot1 = self.loader.loadModel("cow.obj")
    tex = loader.loadTexture("cow_white.png")
    self.spot1.setTexture(tex,1)
    self.spot1.setHpr(-78,0,0) # rotacao em volta de Z, X, Y
    self.spot1.setPos(-1, -4, 0)
    self.spot1.reparentTo(self.render)

    self.background_spot1 = self.loader.loadModel("cow.obj")
    tex = loader.loadTexture("cow_white.png")
    self.background_spot1.setTexture(tex,1)
    self.background_spot1.setScale(0.5, 0.5, 0.5) # escalonamento X, Y, Z
    self.background_spot1.setHpr(-127,0,0) # rotacao em volta de Z, X, Y
    self.background_spot1.setPos(5, -11, 0)
    self.background_spot1.reparentTo(self.render)

    self.background_spot2 = self.loader.loadModel("cow.obj")
    tex = loader.loadTexture("cow_white.png")
    self.background_spot2.setTexture(tex,1)
    self.background_spot2.setScale(0.5, 0.5, 0.5) # escalonamento X, Y, Z
    self.background_spot2.setHpr(127,0,0) # rotacao em volta de Z, X, Y
    self.background_spot2.setPos(6, -11, 0)
    self.background_spot2.reparentTo(self.render)

  ##========== Método que define o movimento de camera ========== 
  def duckZoomTask(self, zoom):

    # Referência da posição atual no ciclo [0, 1]
    t = (1+math.cos(math.pi*zoom.time/6))/2

    # Câmera
    # Posição
    self.camera.lookAt(0.75, -3.8, 1.5)
    self.camera.setPos(-1.25*t+0.5, 0.75, 2+3*t)

    # Campo de visão e aletrado de acordo com os frames
    base.camLens.setFov(10 + 45*(1-t))

    # funcao que define o movimento que o pato faz no seu próprio eixo de acordo com a posição da camera
    self.duck.setHpr(45*(math.cos(math.pi*zoom.time)), 0, 0)

    return zoom.cont

project3D = MeuApp()
project3D.run()
