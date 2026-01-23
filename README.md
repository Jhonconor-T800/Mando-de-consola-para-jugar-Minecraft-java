# 🎮 Mando de consola para jugar Minecraft Java

Convierte un mando de consola en un control totalmente funcional para **Minecraft Java Edition**, emulando teclado y ratón desde Python.

> Pensado para quienes quieren jugar sin mods, con control total del mapeo y posibilidad de personalización avanzada.

---

## ✨ Características

* Soporte para mandos (Xbox, genéricos, compatibles con XInput/DirectInput).
* Emulación de **teclado y ratón** para Minecraft Java.
* Mapeo personalizable de botones y sticks.
* Sensibilidad configurable para cámara y movimiento.
* Perfil base listo para jugar.

---

## 🧰 Requisitos

* Windows 10/11
* Python 3.9+
* Un mando compatible

### Librerías necesarias

```bash
pip install pygame pynput
```

---

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Jhonconor-T800/Mando-de-consola-para-jugar-Minecraft-java.git
cd Mando-de-consola-para-jugar-Minecraft-java
```

2. Instala dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta el script principal:

```bash
python main.py
```

4. Abre Minecraft Java y disfruta 🎮

---

## 🎛️ Mapeo por defecto

| Mando           | Acción en Minecraft |
| --------------- | ------------------- |
| Stick izquierdo | Movimiento (WASD)   |
| Stick derecho   | Cámara (ratón)      |
| A / X           | Saltar              |
| B / Círculo     | Agacharse           |
| RT              | Romper / Atacar     |
| LT              | Usar                |

*(Editable desde el archivo de configuración)*

---

## ⚙️ Configuración

El archivo `config.py` permite:

* Cambiar botones
* Ajustar sensibilidad
* Activar/desactivar ejes

---

## 🧠 Cómo funciona

* `pygame` detecta entradas del mando
* `pynput` emula teclado y ratón
* Un bucle traduce cada input a acciones del juego

Sin mods. Sin inyecciones. Sin riesgos.

---

## 🗺️ Roadmap

* [ ] Selector de perfiles
* [ ] Interfaz gráfica (GUI)
* [ ] Soporte macOS/Linux
* [ ] Guardado automático de configuraciones
* [ ] Detección automática de mando

---

## 🤝 Contribuciones

¡Las PR son bienvenidas!

* Ideas
* Mejoras
* Nuevos perfiles

---

## 📜 Licencia

MIT

---

🔥 Proyecto creado con pasión por el gaming y la programación.
