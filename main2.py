import flet as ft

def main(page: ft.Page):
    
    page.title = "Calculadora TAP"
    page.window_width = 250    # Ancho estrecho, estilo móvil
    page.window_height = 400    # Altura definida
    page.padding = 20           # Espacio interno para que nada toque los bordes

    display = ft.Container(
        content=ft.Text("0", size=30),  # El texto inicial es "0"
        bgcolor=ft.Colors.BLACK12,      # Fondo gris oscuro
        border_radius=8,                # Bordes redondeados
        alignment=ft.alignment.Alignment(1, 0), # Alinear texto a la derecha
        padding=10,     # ... otras configuraciones de tamaño
        width=210,
        height=70,
    )

    def on_button_click(e):
        
        if display.content.value == "0":
            # Si hay un 0 solito, lo reemplazamos por el nuevo número
            display.content.value = e.control.content.value
        else:
            # Si ya hay números, agregamos el nuevo al final (concatenar)
            display.content.value += e.control.content.value
        page.update()   # ¡IMPORTANTE! Refrescar la pantalla

    def on_clear_click(e):
        
        display.content.value = "0" # Reiniciar a 0
        page.update()

    grid = ft.GridView(
        runs_count=2,   # Define que habrá 2 columnas
        spacing=10,     # Espacio entre botones
        run_spacing=10, 
        width=210,
        height=200,
        expand=False
    )

    
    grid.controls.append(
        ft.ElevatedButton(
            content=ft.Text(" 1", color=ft.Colors.WHITE),
            width=100,
            height=50,
            bgcolor=ft.Colors.PRIMARY,
            on_click=on_button_click
        )
    )
    
    grid.controls.append(
        ft.ElevatedButton(
            content=ft.Text(" 2", color=ft.Colors.WHITE),
            width=100,
            height=50,
            bgcolor=ft.Colors.SECONDARY,
            on_click=on_button_click
        )
    )
    
    grid.controls.append(
        ft.ElevatedButton(
            content=ft.Text(" 3", color=ft.Colors.WHITE),
            width=100,
            height=50,
            bgcolor=ft.Colors.TERTIARY,
            on_click=on_button_click
        )
    )
    
    grid.controls.append(
        ft.ElevatedButton(
            content=ft.Text(" 4", color=ft.Colors.WHITE),
            width=100,
            height=50,
            bgcolor=ft.Colors.ERROR,
            on_click=on_button_click
        )
    )

    
    clear_button = ft.ElevatedButton(
        content=ft.Text("Clear", color=ft.Colors.WHITE),
        width=210,  # Ancho total para coincidir con la rejilla
        height=50,
        bgcolor=ft.Colors.RED_700,  # Color rojo para indicar "Borrar"
        on_click=on_clear_click     # Conectado a la función de borrar
    )

    layout_principal = ft.Column(
        controls=[ 
            display, # 1. La pantalla arriba
            grid,   # 2. Los números en medio
            clear_button  # 3. El botón borrar abajo
        ],
        tight=True      # Ajustar los elementos para que estén pegaditos
    )
    
    page.add(layout_principal)  # Agregar todo a la ventana
    page.update()

ft.app(target=main)
