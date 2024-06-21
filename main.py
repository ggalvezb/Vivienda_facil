from fastapi import FastAPI
#from fastapi.staticfiles import StaticFiles
from routers import administrador,beneficiario,carrito,casa, perfil,usuario_serviu, usuario

# Inicia el servidor: uvicorn main:app --reload

app=FastAPI()

#routers
app.include_router(administrador.router)
app.include_router(beneficiario.router)
app.include_router(carrito.router)
app.include_router(casa.router)
app.include_router(perfil.router)
app.include_router(usuario_serviu.router)
app.include_router(usuario.router)

@app.get("/")
async def root():
    return{"message":"Hello World"}