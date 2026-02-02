import json
import sqlite3
import tkinter as tk
import os
import smtplib
import threading


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos_locales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        folio TEXT,
        fecha TEXT,
        pedido_json TEXT,
        estado TEXT,
        ultimo_intento TEXT,
        error TEXT
    )
    """)
    print("Tabla 'pedidos_locales' creada o ya existente.")

    conn.commit()
    conn.close()
