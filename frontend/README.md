# 🖥️ Frontend – AI Support Desk  
### React + TailwindCSS

Frontend for the **AI Support Desk** platform, built with **React** and **TailwindCSS**, designed to integrate with an Azure Functions backend.

---

## 🚀 Technologies

- React 18  
- Vite  
- TailwindCSS  
- React Router DOM  
- Axios  
- React Icons  

---

## ⚙️ Installation

```bash
git clone https://github.com/your-user/your-frontend.git
cd your-frontend
npm install


```
## ▶️ Development Server

    npm run dev


## Application runs at:

    http://localhost:5173


## 🔌 Backend Configuration

Create a .env file in the project root:

    VITE_API_URL=https://your-backend.azurewebsites.net/api/chat


Usage example:

    axios.post(import.meta.env.VITE_API_URL, { message });

## 📦 Production Build
    npm run build


Output files will be generated in:

    dist/

## 📁 Project Structure
        src/
        │── components/
        │── pages/
        │── context/
        │── hooks/
        │── App.jsx
        │── main.jsx

## 🎨 TailwindCSS Configuration

    tailwind.config.js:

    export default {
    content: [
        "./index.html",
        "./src/**/*.{js,jsx,ts,tsx}",
    ],
    theme: {
        extend: {},
    },
    plugins: [],
    }

## 📄 License

MIT License.


---

If you want, I can also generate:

✅ A more corporate version  
✅ A version with shields/badges  
✅ A version including screenshots  
✅ Deployment instructions (Azure, Netlify, Vercel, etc.)

Just tell me!
