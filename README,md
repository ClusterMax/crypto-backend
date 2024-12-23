
# **Crypto Dashboard Backend** ⚙️

Este es el backend del **Crypto Dashboard**, desarrollado con **FastAPI**, para proporcionar datos en tiempo real de criptomonedas utilizando la API pública de CoinCap.io.

---

## **Requisitos previos**  
1. **Python**: Asegúrate de tener Python 3.8+ instalado.  
2. **Instalación de dependencias**:  
   Instala las librerías requeridas ejecutando:  
   ```bash
   pip install fastapi uvicorn httpx
   ```  

---

## **Cómo iniciar el servidor**  
### 1️⃣ **Clona el repositorio**  
Clona este proyecto en tu máquina local:  
```bash
git clone https://github.com/ClusterMax/crypto-backend
cd crypto-backend
```

### 2️⃣ **Ejecuta el servidor FastAPI**  
Inicia el servidor utilizando Uvicorn:  
```bash
uvicorn main:app --reload
```

> **Nota**: Este comando sirve la API en `http://127.0.0.1:8000`.

### 3️⃣ **Prueba la API**  
Puedes probar los endpoints en:  
- **Documentación interactiva**: `http://127.0.0.1:8000/docs`  
- **Documentación alternativa**: `http://127.0.0.1:8000/redoc`  

---

## **Endpoints disponibles**  
### **GET /crypto**  
Obtén datos de las principales criptomonedas con la siguiente estructura:  
```json
[
  {
    "id": "bitcoin",
    "name": "Bitcoin",
    "symbol": "BTC",
    "priceUsd": 30000.00
  },
  {
    "id": "ethereum",
    "name": "Ethereum",
    "symbol": "ETH",
    "priceUsd": 2000.00
  }
]
```
