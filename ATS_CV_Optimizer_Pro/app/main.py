import tkinter as tk
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tkinter import scrolledtext, messagebox, filedialog
from ai.white_keywords_generator import generate_white_keywords
from ai.resume_optimizer import optimize_cv
from ai.resume_auditor import generate_audit
from core.parsers import extract_text
from app.license_check import check_license
from core.parsers import extract_text

def load_file_into_textbox(text_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Documents", "*.pdf *.docx")])
    if not file_path:
        return
    try:
        content = extract_text(file_path)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, content)
    except Exception as e:
        messagebox.showerror("Ошибка загрузки", str(e))

def save_result():
    result = result_output.get("1.0", tk.END).strip()
    if not result:
        messagebox.showwarning("Нет данных", "Нет текста для сохранения.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(result)
        messagebox.showinfo("Сохранено", f"Результат сохранён: {file_path}")

def run_generation():
    cv_text = cv_input.get("1.0", tk.END).strip()
    industry = industry_input.get("1.0", tk.END).strip()
    if not cv_text or not industry:
        messagebox.showwarning("Недостаточно данных", "Введите резюме и отрасль.")
        return
    keywords = generate_white_keywords(cv_text, industry)
    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, "\n".join(keywords if isinstance(keywords, list) else [str(keywords)]))

def run_optimization():
    cv_text = cv_input.get("1.0", tk.END).strip()
    jd_text = jd_input.get("1.0", tk.END).strip()
    if not cv_text or not jd_text:
        messagebox.showwarning("Недостаточно данных", "Введите резюме и описание вакансии.")
        return
    optimized = optimize_cv(cv_text, jd_text)
    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, optimized)

def run_audit():
    cv_text = cv_input.get("1.0", tk.END).strip()
    jd_text = jd_input.get("1.0", tk.END).strip()
    if not cv_text or not jd_text:
        messagebox.showwarning("Недостаточно данных", "Введите резюме и описание вакансии.")
        return
    audit = generate_audit(cv_text, jd_text)
    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, audit)


if not check_license():
    exit()

root = tk.Tk()
root.title("ATS CV Optimizer Pro – AI Assistant")
root.geometry("1000x850")

top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X, pady=5)
tk.Button(top_frame, text="📂 Загрузить CV", command=lambda: load_file_into_textbox(cv_input)).pack(side=tk.LEFT, padx=10)
tk.Button(top_frame, text="📂 Загрузить JD", command=lambda: load_file_into_textbox(jd_input)).pack(side=tk.LEFT, padx=10)
tk.Button(top_frame, text="💾 Сохранить результат", command=save_result).pack(side=tk.RIGHT, padx=10)


tk.Label(root, text="📝 Введите резюме (CV):").pack(anchor="w", padx=10)
cv_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10)
cv_input.pack(fill=tk.BOTH, expand=True, padx=10)

tk.Label(root, text="📄 Введите описание вакансии (Job Description):").pack(anchor="w", padx=10, pady=(10, 0))
jd_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=6)
jd_input.pack(fill=tk.BOTH, expand=True, padx=10)

tk.Label(root, text="🏭 Введите отрасль (например, Oil & Gas):").pack(anchor="w", padx=10, pady=(10, 0))
industry_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=2)
industry_input.pack(fill=tk.X, padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="🎯 White Keywords", command=run_generation, bg="#4CAF50", fg="white", width=20).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="✏️ Optimize CV", command=run_optimization, bg="#2196F3", fg="white", width=20).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="📊 AI Audit", command=run_audit, bg="#9C27B0", fg="white", width=20).pack(side=tk.LEFT, padx=5)

tk.Label(root, text="📌 Результат:").pack(anchor="w", padx=10)
result_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
result_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))



def clear_fields():
    cv_input.delete("1.0", tk.END)
    jd_input.delete("1.0", tk.END)
    industry_input.delete("1.0", tk.END)
    result_output.delete("1.0", tk.END)

tk.Button(top_frame, text="🗑 Очистить поля", command=clear_fields).pack(side=tk.RIGHT, padx=10)

root.mainloop()



def clear_fields():
    cv_input.delete("1.0", tk.END)
    jd_input.delete("1.0", tk.END)
    industry_input.delete("1.0", tk.END)
    result_output.delete("1.0", tk.END)
