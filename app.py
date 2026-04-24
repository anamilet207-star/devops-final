from flask import Flask
import datetime
import random

app = Flask(__name__)

# Datos curiosos RANDOM (sin tecnología)
datos_curiosos = [
    "🐧 Los pingüinos tienen una glándula cerca del ojo que convierte el agua salada en agua dulce",
    "🍕 La pizza más cara del mundo cuesta $12,000 USD y tiene caviar y oro comestible",
    "😴 Los humanos somos los únicos animales que retrasamos voluntariamente el sueño",
    "🐘 Los elefantes no pueden saltar",
    "🍌 Las bananas son radioactivas por su alto contenido de potasio",
    "🦒 Las jirafas tienen la misma cantidad de vértebras en el cuello que los humanos (7)",
    "🐙 Los pulpos tienen tres corazones",
    "🍪 Las galletas Oreo fueron inspiradas en una galleta inglesa llamada 'Hydrox'",
    "🐱 Los gatos pasan el 70% de su vida durmiendo",
    "🦷 Los caracoles tienen más de 25,000 dientes",
    "🌊 El 90% del hielo de la Tierra está en la Antártida",
    "🐫 Los camellos tienen tres párpados para protegerse de la arena",
    "🍿 El microondas fue inventado por accidente mientras se probaba un radar",
    "🐬 Los delfines tienen nombres únicos entre ellos",
    "🌙 La Luna tiene terremotos lunares (temblores en la Luna)"
]

@app.route('/')
def home():
    dato_random = random.choice(datos_curiosos)
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Final</title>
        <style>
            body {{
                background: #0d0d0d;
                font-family: 'Segoe UI', Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                color: #e0e0e0;
            }}
            .panel {{
                background: #1a1a2e;
                border-radius: 20px;
                padding: 40px;
                text-align: center;
                box-shadow: 0 0 30px rgba(128, 0, 255, 0.3);
                border: 1px solid #7b2cbf;
                max-width: 500px;
            }}
            h1 {{
                color: #b14eff;
                font-size: 2em;
                margin-bottom: 10px;
            }}
            .devops-icon {{
                font-size: 4em;
                margin: 20px 0;
            }}
            .dato-curioso {{
                background: #0d0d1a;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
                border-left: 4px solid #b14eff;
                text-align: left;
                font-size: 0.9em;
            }}
            .status {{
                display: flex;
                justify-content: center;
                gap: 15px;
                margin-top: 20px;
                font-size: 0.8em;
                flex-wrap: wrap;
            }}
            .badge {{
                background: #2a2a3a;
                padding: 5px 12px;
                border-radius: 20px;
                color: #b14eff;
            }}
            .hora {{
                margin-top: 20px;
                font-size: 0.7em;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="panel">
            <div class="devops-icon">⚡📦</div>
            <h1>¡Hola Mundo DevOps!</h1>
            <p>Pipeline CI/CD funcionando </p>
            
            <div class="dato-curioso">
                <strong> Dato random:</strong><br>
                {dato_random}
            </div>
            
            <div class="status">
                <span class="badge"> Tests OK</span>
                <span class="badge"> Docker</span>
                <span class="badge"> GitHub Actions</span>
                <span class="badge"> Render</span>
            </div>
            
            <div class="hora">
                 {hora} UTC
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)