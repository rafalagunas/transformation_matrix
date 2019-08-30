import numpy as np


#el ultimo uno de cada vector no cuenta no cuenta
m_one = np.array([[1,2,1,1],[2,4,3,1],[2,4,3,1]])

#Escalar en zoom +
m_two = np.array([[4,0,0,0],[0,4,0,0],[0,0,4,0],[0,0,0,1]])

# Escalar en zoom -
m_three = np.array([[-0.4,0,0,0],[0,-0.4,0,0],[0,0,-0.4,1],[0,0,0,1]])

#Mover izquierda
m_four = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[-0.1,0,0,1]])

#Mover derecha
m_five = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[1,0,0,1]])

#Mover abajo
m_six = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,-0.1,0,1]])

#Mover arriba
m_seven =  np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,1,0,1]])


#Acercar
m_eight = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,1]])


#Alejar
m_nine =  np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,-0.1,1]])

print("Initial matrix")
print(m_one)

zoom_in = m_one.dot(m_two)
zoom_inText = "Zoom in"

print("\n")
print(zoom_inText)
print(zoom_in)


zoom_out = m_one.dot(m_three)
zoom_outText = "Zoom out"

print("\n")
print(zoom_outText)
print(zoom_out)



left = m_one.dot(m_four)
leftText = "To left"

print("\n")
print(leftText)
print(left)


right = m_one.dot(m_five)
rightText = "To right"

print("\n")
print(rightText)
print(right)

down = m_one.dot(m_six)
downText = "To down"

print("\n")
print(downText)
print(down)


up = m_one.dot(m_seven)
upText = "To up"

print("\n")
print(upText)
print(up)

closeUp = m_one.dot(m_eight)
closeUpText = "To closeUp"

print("\n")
print(closeUpText)
print(closeUp)

closedown = m_one.dot(m_nine)
closedownText = "To closedown"

print("\n")
print(closedownText)
print(closedown)


