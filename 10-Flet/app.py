import flet as ft

def main(page: ft.Page):
    # Configurações para simular a tela de um celular no monitor
    page.title = "App Ortopedia"
    page.bgcolor = "#F4F6F9"
    page.padding = 15
    page.window.width = 390
    page.window.height = 844
    page.scroll = "auto" # Permite deslizar a tela para baixo

    # 1. APP BAR (Barra no topo da tela)
    page.appbar = ft.AppBar(
        title=ft.Text("Dashboard Clínico", size=18, weight="bold", color="white"),
        bgcolor="#1E293B",
        center_title=True,
        actions=[ft.IconButton(icon="person", icon_color="white")]
    )

    # 2. FILTROS (Compactados)
    filtros = ft.Column([
        ft.Text("Filtros Ativos", size=14, weight="bold", color="grey"),
        ft.Dropdown(label="Faixa Etária", options=[ft.dropdown.Option("Todas"), ft.dropdown.Option("60+ (Idosos)")], text_size=14, height=50),
        ft.Row([
            ft.Dropdown(label="IMC", options=[ft.dropdown.Option("Todos")], text_size=14, expand=1, height=50),
            ft.Dropdown(label="Teste", options=[ft.dropdown.Option("MMII")], text_size=14, expand=1, height=50),
        ])
    ])

    # 3. KPIs (Cartões Horizontais, mais limpos para celular)
    def criar_kpi_mobile(titulo, valor):
        return ft.Container(
            content=ft.Row([
                ft.Text(titulo, size=11, color="grey", weight="bold", expand=True),
                ft.Text(valor, size=22, weight="bold", color="#1E293B")
            ], alignment="spaceBetween"),
            bgcolor="white", padding=15, border_radius=10,
            shadow=ft.BoxShadow(blur_radius=8, color="black12")
        )

    kpis = ft.Column([
        criar_kpi_mobile("TOTAL DE AVALIAÇÕES", "142"),
        criar_kpi_mobile("TESTES POSITIVOS", "68%"),
        criar_kpi_mobile("IDADE MÉDIA", "45 Anos"),
    ], spacing=10)

    # 4. GRÁFICOS (Blocos verticais grandes)
    def criar_grafico_mobile(texto):
        return ft.Container(
            content=ft.Text(texto, color="white", text_align="center", size=13),
            bgcolor="#1E293B", height=200, border_radius=10, alignment=ft.Alignment(0, 0)
        )

    graficos = ft.Column([
        criar_grafico_mobile("Gráfico: Ranking de Testes Falhos\n(Barras Horizontais)"),
        criar_grafico_mobile("Gráfico: Perfil por Idade\n(Rosca/Pizza)"),
        criar_grafico_mobile("Gráfico: IMC x Lesões\n(Colunas)"),
    ], spacing=15)

    # 5. NAVEGAÇÃO INFERIOR (Padrão Mobile - Corrigido)
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon="check_box", label="Check-up"),
            ft.NavigationBarDestination(icon="dashboard", label="Dashboard"),
            ft.NavigationBarDestination(icon="search", label="Buscar"),
        ]
    )

    # Adicionando os blocos na tela
    page.add(
        filtros,
        ft.Divider(height=10, color="transparent"),
        kpis,
        ft.Divider(height=10, color="transparent"),
        graficos
    )

ft.run(main)