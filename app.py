import datetime
import re
from fpdf import FPDF
import streamlit as st

# --- CONFIGURACAO DA PAGINA ---
st.set_page_config(
    page_title="Relatório Diário - Rede Via",
    page_icon="⛽",
    layout="centered",
)

# --- ESTILO VISUAL REDE VIA NO APP ---
st.markdown(
    """
    <style>
    .header-box {
        background-color: #C8102E;
        padding: 18px 22px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
        border-bottom: 5px solid #EAAA00;
    }
    .header-box h2 {
        margin: 0;
        font-size: 1.45rem;
        color: white;
    }
    .header-box p {
        margin: 4px 0 0 0;
        font-size: 0.9rem;
        color: #FFE8A3;
    }
    </style>
    <div class="header-box">
        <h2>⛽ Relatório Diário de Rotina - Rede Via</h2>
        <p>Coordenadores e Supervisores • Geração de PDF Oficial</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- LISTA DE UNIDADES REDE VIA ---
UNIDADES_REDE = [
    "Selecione o posto...",
    "Bel",
    "Mario Campos",
    "Demetrios",
    "Jardim das Rosas",
    "MM040",
    "Rio Acima",
    "Esmeraldas",
    "Itabira",
    "Toronto",
    "Veneza",
    "Vianópolis",
    "Caldas",
    "Via Rodovia",
    "Via Industrial",
    "Via Centro",
    "Via Cajuri",
    "Acaiaca",
    "Waam",
    "Guarapiranga",
    "Palmeiras",
    "Outro (digitar manualmente)",
]


# --- FUNCOES AUXILIARES PARA O PDF ---
def limpar_texto(texto) -> str:
    if texto is None:
        return ""
    s = str(texto)
    substituicoes = {
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2022": "-",
        "\u2026": "...",
        "\u00a0": " ",
    }
    for k, v in substituicoes.items():
        s = s.replace(k, v)
    return s.encode("latin-1", errors="ignore").decode("latin-1")


class RelatorioRedeViaPDF(FPDF):
    def __init__(self, data_str: str):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.data_str = data_str
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(12, 12, 12)

    def header(self):
        if self.page_no() == 1:
            # Banner superior vermelho Rede Via (#C8102E)
            self.set_fill_color(200, 16, 46)
            self.rect(0, 0, 210, 31, style="F")
            # Faixa dourada inferior (#EAAA00)
            self.set_fill_color(234, 170, 0)
            self.rect(0, 31, 210, 2.5, style="F")

            self.set_xy(12, 6)
            self.set_font("Helvetica", "B", 18)
            self.set_text_color(255, 255, 255)
            self.cell(0, 7, limpar_texto("REDE VIA"), ln=True)

            self.set_x(12)
            self.set_font("Helvetica", "B", 7.5)
            self.set_text_color(255, 232, 163)
            self.cell(0, 4, limpar_texto("MAIS PERTO, TE LEVAMOS MAIS LONGE"), ln=True)

            self.set_x(12)
            self.set_font("Helvetica", "B", 11)
            self.set_text_color(255, 255, 255)
            self.cell(
                0,
                7,
                limpar_texto("Relatório Diário de Rotina - Coordenadores e Supervisores"),
                ln=True,
            )
            self.set_y(38)
        else:
            self.set_fill_color(200, 16, 46)
            self.rect(0, 0, 210, 10, style="F")
            self.set_xy(12, 2.5)
            self.set_font("Helvetica", "B", 8.5)
            self.set_text_color(255, 255, 255)
            self.cell(
                0,
                5,
                limpar_texto(f"REDE VIA | Relatório Diário de Rotina - {self.data_str}"),
                align="L",
            )
            self.set_y(14)

    def footer(self):
        self.set_y(-11)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(
            0,
            6,
            limpar_texto(f"Rede Via - Documento Operacional | Página {self.page_no()}/{{nb}}"),
            align="C",
        )

    def titulo_secao(self, titulo: str):
        if self.get_y() > 262:
            self.add_page()
        self.ln(2)
        y = self.get_y()
        self.set_fill_color(252, 241, 243)
        self.rect(12, y, 186, 7.5, style="F")
        self.set_fill_color(200, 16, 46)
        self.rect(12, y, 2.5, 7.5, style="F")

        self.set_xy(16.5, y + 1.2)
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(200, 16, 46)
        self.cell(0, 5, limpar_texto(titulo), ln=True)
        self.ln(2)

    def calcular_linhas(self, texto: str, largura: float) -> int:
        texto = limpar_texto(texto)
        if not texto:
            return 1
        largura_util = max(largura - 3, 5)
        total_linhas = 0
        for paragrafo in texto.split("\n"):
            if not paragrafo.strip():
                total_linhas += 1
                continue
            palavras = paragrafo.split(" ")
            linha_atual = ""
            for palavra in palavras:
                teste = f"{linha_atual} {palavra}".strip()
                if self.get_string_width(teste) <= largura_util:
                    linha_atual = teste
                else:
                    if linha_atual:
                        total_linhas += 1
                    w_pal = self.get_string_width(palavra)
                    if w_pal > largura_util:
                        chars = max(1, int(len(palavra) * (largura_util / w_pal)))
                        total_linhas += max(1, (len(palavra) + chars - 1) // chars)
                        linha_atual = ""
                    else:
                        linha_atual = palavra
            if linha_atual:
                total_linhas += 1
        return max(1, total_linhas)

    def linha_tabela(
        self,
        valores: list,
        larguras: list,
        alinhamentos: list = None,
        cabecalho: bool = False,
        altura_linha: float = 4.5,
    ):
        if alinhamentos is None:
            alinhamentos = ["L"] * len(valores)

        self.set_font("Helvetica", "B" if cabecalho else "", 8.2 if cabecalho else 8.0)
        max_linhas = 1
        for val, larg in zip(valores, larguras):
            n = self.calcular_linhas(val, larg)
            if n > max_linhas:
                max_linhas = n

        altura_total = max_linhas * altura_linha + 3.0

        if self.get_y() + altura_total > 280:
            self.add_page()

        x_inicio = 12
        y_inicio = self.get_y()

        if cabecalho:
            self.set_fill_color(200, 16, 46)
            self.set_text_color(255, 255, 255)
            self.set_draw_color(200, 16, 46)
        else:
            self.set_fill_color(255, 255, 255)
            self.set_text_color(35, 35, 35)
            self.set_draw_color(205, 205, 205)

        x_atual = x_inicio
        for val, larg, alin in zip(valores, larguras, alinhamentos):
            self.rect(x_atual, y_inicio, larg, altura_total, style="DF" if cabecalho else "D")
            self.set_xy(x_atual + 1.5, y_inicio + 1.5)
            self.multi_cell(larg - 3, altura_linha, limpar_texto(val), border=0, align=alin)
            x_atual += larg

        self.set_y(y_inicio + altura_total)

    def item_checkbox(self, texto: str, marcado: bool):
        if self.get_y() > 276:
            self.add_page()
        y = self.get_y()
        x = 14
        if marcado:
            self.set_draw_color(200, 16, 46)
            self.set_fill_color(200, 16, 46)
        else:
            self.set_draw_color(130, 130, 130)
            self.set_fill_color(255, 255, 255)

        self.rect(x, y + 0.7, 3.6, 3.6, style="DF" if marcado else "D")
        if marcado:
            self.set_xy(x - 0.2, y + 0.2)
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(255, 255, 255)
            self.cell(4, 4.5, "X", align="C")

        self.set_xy(x + 6, y)
        self.set_font("Helvetica", "B" if marcado else "", 8.8)
        self.set_text_color(30, 30, 30)
        self.multi_cell(174, 4.8, limpar_texto(texto))
        self.ln(0.8)

    def bloco_texto(self, rotulo: str, conteudo: str):
        if self.get_y() > 270:
            self.add_page()
        self.set_font("Helvetica", "B", 8.8)
        self.set_text_color(55, 55, 55)
        self.cell(0, 5, limpar_texto(rotulo), ln=True)
        texto_exibir = conteudo.strip() if conteudo and conteudo.strip() else "Não informado."
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(35, 35, 35)
        self.set_fill_color(249, 249, 249)
        self.set_draw_color(215, 215, 215)
        self.multi_cell(186, 4.6, limpar_texto(texto_exibir), border=1, fill=True)
        self.ln(2)


# --- FORMULARIO NA TELA ---

# 1. IDENTIFICACAO
st.subheader("1. Identificação")
col1, col2 = st.columns([2, 1])
with col1:
    nome = st.text_input("Nome", value="Hitalo Gustavo Mendes Pinheiro")
with col2:
    data_relatorio = st.date_input("Data", value=datetime.date.today())

seguiu_cronograma = st.radio(
    "Seguiu o cronograma da semana?",
    options=["Sim", "Não"],
    horizontal=True,
)

motivo_cronograma = ""
if seguiu_cronograma == "Não":
    motivo_cronograma = st.text_area(
        "Se não seguiu ou mudou algo, explique o motivo:",
        placeholder="Descreva o motivo da alteração no cronograma...",
    )

st.divider()

# 2. POSTOS VISITADOS E O QUE FOI FEITO
st.subheader("2. Postos Visitados e Atividades")
qtd_postos = st.number_input(
    "Quantos postos você visitou hoje?",
    min_value=1,
    max_value=15,
    value=1,
    step=1,
)

postos_dados = []
for i in range(int(qtd_postos)):
    with st.expander(f"📍 Posto {i + 1}", expanded=True):
        c1, c2 = st.columns([2, 1])
        with c1:
            posto_sel = st.selectbox(
                f"Posto (nome / bairro) #{i + 1}",
                options=UNIDADES_REDE,
                key=f"posto_sel_{i}",
            )
            if posto_sel == "Outro (digitar manualmente)":
                posto_nome = st.text_input(
                    f"Digite o nome/bairro do Posto #{i + 1}",
                    key=f"posto_txt_{i}",
                )
            else:
                posto_nome = "" if posto_sel == "Selecione o posto..." else posto_sel

        with c2:
            no_cronograma = st.radio(
                "Estava no cronograma?",
                options=["Sim", "Não"],
                horizontal=True,
                key=f"crono_{i}",
            )

        motivo_visita = st.text_input(
            "Motivo da visita",
            placeholder="Ex.: Rotina, vazamento, alinhamento de equipe...",
            key=f"motivo_{i}",
        )
        com_quem = st.text_input(
            "Com quem conversou",
            placeholder="Ex.: Gerente João, Chefe de Pista...",
            key=f"conversa_{i}",
        )
        o_que_verificou = st.text_area(
            "O que verificou",
            placeholder="Ex.: Verificou a pista e encontrou canaleta entupida...",
            key=f"verif_{i}",
            height=80,
        )
        o_que_resolveu = st.text_area(
            "O que resolveu",
            placeholder="Ex.: Acionou limpeza imediata e orientou equipe...",
            key=f"resolv_{i}",
            height=80,
        )
        recolhimento = st.radio(
            "Recolhimento? (Atenção: marque apenas Sim ou Não, sem detalhes)",
            options=["Não", "Sim"],
            horizontal=True,
            key=f"recolh_{i}",
        )

        postos_dados.append(
            {
                "posto": posto_nome,
                "no_cronograma": no_cronograma,
                "motivo": motivo_visita,
                "conversa": com_quem,
                "verificou": o_que_verificou,
                "resolveu": o_que_resolveu,
                "recolhimento": recolhimento,
            }
        )

st.divider()

# 3. ITENS PARA CONFERIR NA VISITA
st.subheader("3. Itens para Conferir na Visita")
st.caption("Esta lista é um resumo para o dia a dia e não substitui o checklist bimestral.")

itens_padrao = [
    "Pista e equipamentos (bombas, canaletas, vazamentos)",
    "Estoque de combustível (diferenças, sobras e faltas)",
    "Limpeza e conservação do posto como um todo (pátio, pista, banheiros, loja)",
    "Equipe (escala, uniformes, atendimento)",
    "Segurança e meio ambiente",
    "Conversa com o gerente",
]

itens_marcados = {}
for item in itens_padrao:
    itens_marcados[item] = st.checkbox(item, key=f"chk_{item}")

outros_itens = st.text_input(
    "Outros (descreva abaixo, se aplicável):",
    placeholder="Descreva outros pontos verificados...",
)

st.divider()

# 4. PENDENCIAS E PROXIMOS PASSOS
st.subheader("4. Pendências e Próximos Passos")
qtd_pendencias = st.number_input(
    "Quantidade de pendências a registrar",
    min_value=0,
    max_value=10,
    value=1,
    step=1,
)

pendencias_dados = []
for p in range(int(qtd_pendencias)):
    st.markdown(f"**Pendência {p + 1}**")
    pc1, pc2, pc3 = st.columns([2, 2, 1.3])
    with pc1:
        p_posto = st.text_input("Posto", key=f"p_posto_{p}")
    with pc2:
        p_resp = st.text_input("Responsável", key=f"p_resp_{p}")
    with pc3:
        p_prazo = st.date_input(
            "Prazo",
            value=datetime.date.today() + datetime.timedelta(days=1),
            key=f"p_prazo_{p}",
        )
    p_desc = st.text_area(
        "O que ficou pendente",
        key=f"p_desc_{p}",
        height=70,
    )
    pendencias_dados.append(
        {
            "posto": p_posto,
            "responsavel": p_resp,
            "prazo": p_prazo.strftime("%d/%m/%Y"),
            "descricao": p_desc,
        }
    )

obs_gerais = st.text_area(
    "Observações gerais do dia:",
    placeholder="Anotações complementares sobre a rotina...",
)

st.divider()

# 5. OPORTUNIDADES DE MELHORIA
st.subheader("5. Oportunidades de Melhoria")
st.caption(
    "Áreas guia: Atendimento • Vendas e serviços (troca de óleo, lavagem, conveniência, aditivos) • "
    "Equipe • Operação e estrutura"
)

melhoria_1 = st.text_area("1. O que você observou que pode melhorar", height=75)
melhoria_2 = st.text_area("2. O que deu certo e vale repetir (boa prática para outros postos)", height=75)
melhoria_3 = st.text_area("3. Sua ideia para a rede", height=75)
melhoria_4 = st.text_area("4. Precisa de apoio? (material, manutenção, treinamento, decisão)", height=75)

st.divider()

# 6. ASSINATURA
assinatura_ok = st.checkbox(
    "Declaro que as informações acima correspondem às atividades realizadas no dia."
)


# --- GERACAO DO PDF COM IDENTIDADE VISUAL REDE VIA ---
def construir_pdf_bytes() -> bytes:
    data_str = data_relatorio.strftime("%d/%m/%Y")
    pdf = RelatorioRedeViaPDF(data_str)
    pdf.alias_nb_pages()
    pdf.add_page()

    # 1. IDENTIFICACAO
    pdf.titulo_secao("1. Identificação")
    pdf.linha_tabela(["Campo", "Informação Preenchida"], [55, 131], ["L", "L"], cabecalho=True)
    pdf.linha_tabela(["Nome", nome or "-"], [55, 131], ["L", "L"])
    pdf.linha_tabela(["Data", data_str], [55, 131], ["L", "L"])
    marcacao_crono = "( X ) Sim     (   ) Não" if seguiu_cronograma == "Sim" else "(   ) Sim     ( X ) Não"
    pdf.linha_tabela(["Seguiu o cronograma da semana?", marcacao_crono], [55, 131], ["L", "L"])

    if seguiu_cronograma == "Não" or motivo_cronograma.strip():
        pdf.ln(1.5)
        pdf.bloco_texto("Se não seguiu ou mudou algo, explique o motivo:", motivo_cronograma)

    # 2. POSTOS VISITADOS NO DIA
    pdf.titulo_secao("2. Postos Visitados no Dia")
    pdf.linha_tabela(
        ["Nº", "Posto (nome / bairro)", "Estava no cronograma?"],
        [16, 122, 48],
        ["C", "L", "C"],
        cabecalho=True,
    )
    for idx, p in enumerate(postos_dados, start=1):
        pdf.linha_tabela(
            [str(idx), p["posto"] or "-", p["no_cronograma"]],
            [16, 122, 48],
            ["C", "L", "C"],
        )

    # 3. O QUE FOI FEITO EM CADA POSTO
    pdf.titulo_secao("3. O que foi feito em cada posto")
    larguras_ativ = [28, 30, 28, 42, 38, 20]
    alin_ativ = ["L", "L", "L", "L", "L", "C"]
    pdf.linha_tabela(
        [
            "Posto",
            "Motivo da visita",
            "Com quem conversou",
            "O que verificou",
            "O que resolveu",
            "Recolhimento?",
        ],
        larguras_ativ,
        alin_ativ,
        cabecalho=True,
    )
    for p in postos_dados:
        pdf.linha_tabela(
            [
                p["posto"] or "-",
                p["motivo"] or "-",
                p["conversa"] or "-",
                p["verificou"] or "-",
                p["resolveu"] or "-",
                p["recolhimento"],
            ],
            larguras_ativ,
            alin_ativ,
        )

    # 4. ITENS PARA CONFERIR NA VISITA
    pdf.titulo_secao("4. Itens Conferidos na Visita (Resumo Diário)")
    for item in itens_padrao:
        pdf.item_checkbox(item, itens_marcados.get(item, False))

    tem_outros = bool(outros_itens.strip())
    rotulo_outros = f"Outros: {outros_itens.strip()}" if tem_outros else "Outros: Nenhum item adicional informado."
    pdf.item_checkbox(rotulo_outros, tem_outros)

    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(
        0,
        5,
        limpar_texto("Nota: Esta lista é um resumo para o dia a dia e não substitui o checklist bimestral."),
        ln=True,
    )

    # 5. PENDENCIAS E PROXIMOS PASSOS
    pdf.titulo_secao("5. Pendências e Próximos Passos")
    pendencias_validas = [
        pd for pd in pendencias_dados if pd["posto"].strip() or pd["descricao"].strip()
    ]
    if pendencias_validas:
        for idx, pend in enumerate(pendencias_validas, start=1):
            cab = (
                f"Pendência {idx} - Posto: {pend['posto'] or '-'} | "
                f"Responsável: {pend['responsavel'] or '-'} | Prazo: {pend['prazo']}"
            )
            pdf.bloco_texto(cab, pend["descricao"])
    else:
        pdf.set_font("Helvetica", "", 8.8)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(0, 6, limpar_texto("Nenhuma pendência registrada nesta data."), ln=True)

    pdf.bloco_texto("Observações gerais do dia:", obs_gerais)

    # 6. OPORTUNIDADES DE MELHORIA
    pdf.titulo_secao("6. Oportunidades de Melhoria")
    pdf.bloco_texto("1. O que você observou que pode melhorar:", melhoria_1)
    pdf.bloco_texto("2. O que deu certo e vale repetir:", melhoria_2)
    pdf.bloco_texto("3. Sua ideia para a rede:", melhoria_3)
    pdf.bloco_texto("4. Precisa de apoio?", melhoria_4)

    # 7. ASSINATURA
    pdf.titulo_secao("7. Assinatura")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(35, 35, 35)
    pdf.cell(
        0,
        6,
        limpar_texto("Declaro que as informações acima correspondem às atividades realizadas no dia."),
        ln=True,
    )
    pdf.ln(3)
    pdf.linha_tabela(
        ["Assinatura Digital (Responsável)", "Data"],
        [136, 50],
        ["L", "C"],
        cabecalho=True,
    )
    pdf.linha_tabela(
        [nome or "-", data_str],
        [136, 50],
        ["L", "C"],
    )

    raw_out = pdf.output(dest="S")
    return raw_out.encode("latin-1") if isinstance(raw_out, str) else bytes(raw_out)


# --- BOTAO DE FINALIZACAO E DOWNLOAD DO PDF ---
st.subheader("📄 Finalizar e Baixar PDF")

if not assinatura_ok:
    st.warning("Marque a caixa de declaração de assinatura acima para gerar o PDF do relatório.")
else:
    pdf_pronto = construir_pdf_bytes()
    nome_limpo = re.sub(r"[^a-zA-Z0-9_-]", "_", nome.strip()) or "Coordenador"
    nome_arquivo = f"Relatorio_Diario_RedeVia_{data_relatorio.strftime('%Y-%m-%d')}_{nome_limpo}.pdf"

    st.success("✅ Relatório pronto! Clique abaixo para baixar o PDF e enviar no WhatsApp.")
    st.download_button(
        label="📥 Baixar Relatório em PDF (Identidade Visual Rede Via)",
        data=pdf_pronto,
        file_name=nome_arquivo,
        mime="application/pdf",
        use_container_width=True,
    )
