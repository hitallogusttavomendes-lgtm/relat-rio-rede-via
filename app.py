import datetime
import json
import re
import urllib.parse
import urllib.request
import streamlit as st

# --- CONFIGURACAO DA PAGINA ---
st.set_page_config(
    page_title="Relatorio Diario - Rede Via",
    page_icon="⛽",
    layout="centered",
)

# --- ESTILO VISUAL REDE VIA ---
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
        font-size: 1.4rem;
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
        <p>Coordenadores e Supervisores • Envio Direto para Diretoria</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- BARRA LATERAL: CONFIGURACAO DO WHATSAPP DO DIRETOR ---
with st.sidebar:
    st.header("⚙️ Configuração de Envio")
    numero_diretor_raw = st.text_input(
        "WhatsApp do Diretor (com DDI e DDD)",
        value="5531999999999",
        help="Exemplo: 5531988887777 (55 = Brasil, 31 = DDD)",
    )
    numero_diretor = re.sub(r"\D", "", numero_diretor_raw)

    modo_envio = st.radio(
        "Modo de disparo",
        ["Link Direto WhatsApp (1 clique)", "API Automática (Webhook)"],
    )

    api_url = ""
    api_token = ""
    if modo_envio == "API Automática (Webhook)":
        api_url = st.text_input("URL da API (Z-API / Evolution)")
        api_token = st.text_input("Token / Client-Token", type="password")

    st.divider()
    st.caption(
        "📌 **Lembretes da Rotina:**\n"
        "- Preencher 1 relatório por dia até o fim do expediente.\n"
        "- Incluir postos fora do cronograma.\n"
        "- Recolhimento: marcar apenas **Sim** ou **Não**, sem detalhes."
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

# --- 1. IDENTIFICACAO ---
st.subheader("1. Identificação")
col1, col2 = st.columns([2, 1])
with col1:
    nome = st.text_input("Nome", value="Hitalo Gustavo Mendes Pinheiro")
with col2:
    data_relatorio = st.date_input(
        "Data",
        value=datetime.date.today(),
        format="DD/MM/YYYY",
    )

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

# --- 2. POSTOS VISITADOS E O QUE FOI FEITO ---
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

# --- 3. ITENS CONFERIDOS NA VISITA ---
st.subheader("3. Itens Conferidos na Visita")
st.caption("Resumo para o dia a dia (não substitui o checklist bimestral).")

itens_padrao = [
    "Pista e equipamentos (bombas, canaletas, vazamentos)",
    "Estoque de combustível (diferenças, sobras e faltas)",
    "Limpeza e conservação do posto como um todo (pátio, pista, banheiros, loja)",
    "Equipe (escala, uniformes, atendimento)",
    "Segurança e meio ambiente",
    "Conversa com o gerente",
]

itens_marcados = []
for item in itens_padrao:
    if st.checkbox(item, key=f"chk_{item}"):
        itens_marcados.append(item)

outros_itens = st.text_input(
    "Outros itens conferidos (opcional):",
    placeholder="Descreva outros pontos verificados...",
)

st.divider()

# --- 4. PENDENCIAS E PROXIMOS PASSOS ---
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
    with st.container(border=True):
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
                format="DD/MM/YYYY",
                key=f"p_prazo_{p}",
            )
        p_desc = st.text_area(
            "O que ficou pendente",
            key=f"p_desc_{p}",
            height=70,
        )
        if p_posto or p_desc:
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

# --- 5. OPORTUNIDADES DE MELHORIA ---
st.subheader("5. Oportunidades de Melhoria")
st.caption(
    "Áreas guia: Atendimento • Vendas e serviços (troca de óleo, lavagem, conveniência, aditivos) • "
    "Equipe • Operação e estrutura"
)

melhoria_1 = st.text_area(
    "1. O que você observou que pode melhorar",
    height=75,
)
melhoria_2 = st.text_area(
    "2. O que deu certo e vale repetir (boa prática para outros postos)",
    height=75,
)
melhoria_3 = st.text_area(
    "3. Sua ideia para a rede",
    height=75,
)
melhoria_4 = st.text_area(
    "4. Precisa de apoio do escritório? (material, manutenção, treinamento, decisão)",
    height=75,
)

st.divider()

# --- 6. DECLARACAO / ASSINATURA ---
assinatura_ok = st.checkbox(
    "Declaro que as informações acima correspondem às atividades realizadas no dia."
)


# --- FUNCAO PARA MONTAR A MENSAGEM DO WHATSAPP ---
def gerar_texto_whatsapp() -> str:
    data_str = data_relatorio.strftime("%d/%m/%Y")
    linhas = [
        "*RELATÓRIO DIÁRIO DE ROTINA - REDE VIA*",
        f"*Coordenador/Supervisor:* {nome}",
        f"*Data:* {data_str}",
        f"*Seguiu cronograma:* {seguiu_cronograma}",
    ]
    if seguiu_cronograma == "Não" and motivo_cronograma.strip():
        linhas.append(f"*Motivo da alteração:* {motivo_cronograma.strip()}")

    linhas.append("\n--------------------")
    linhas.append("*POSTOS VISITADOS E ATIVIDADES*")
    for idx, p in enumerate(postos_dados, start=1):
        nome_p = p["posto"] if p["posto"] else "Não informado"
        linhas.append(f"\n*Posto {idx}: {nome_p}* (No cronograma: {p['no_cronograma']})")
        if p["motivo"]:
            linhas.append(f"- *Motivo:* {p['motivo']}")
        if p["conversa"]:
            linhas.append(f"- *Conversou com:* {p['conversa']}")
        if p["verificou"]:
            linhas.append(f"- *Verificou:* {p['verificou']}")
        if p["resolveu"]:
            linhas.append(f"- *Resolveu:* {p['resolveu']}")
        linhas.append(f"- *Recolhimento:* {p['recolhimento']}")

    linhas.append("\n--------------------")
    linhas.append("*ITENS CONFERIDOS NA VISITA*")
    if itens_marcados:
        for it in itens_marcados:
            linhas.append(f"✅ {it}")
    else:
        linhas.append("- Nenhum item marcado")
    if outros_itens.strip():
        linhas.append(f"✅ Outros: {outros_itens.strip()}")

    linhas.append("\n--------------------")
    linhas.append("*PENDÊNCIAS E PRÓXIMOS PASSOS*")
    if pendencias_dados:
        for idx, pend in enumerate(pendencias_dados, start=1):
            linhas.append(
                f"\n*Pendência {idx}* - Posto: {pend['posto'] or '-'} | "
                f"Resp.: {pend['responsavel'] or '-'} | Prazo: {pend['prazo']}"
            )
            linhas.append(f"- {pend['descricao']}")
    else:
        linhas.append("- Sem pendências registradas.")

    if obs_gerais.strip():
        linhas.append(f"\n*Observações gerais:* {obs_gerais.strip()}")

    if any([melhoria_1.strip(), melhoria_2.strip(), melhoria_3.strip(), melhoria_4.strip()]):
        linhas.append("\n--------------------")
        linhas.append("*OPORTUNIDADES DE MELHORIA*")
        if melhoria_1.strip():
            linhas.append(f"- *Pode melhorar:* {melhoria_1.strip()}")
        if melhoria_2.strip():
            linhas.append(f"- *Deu certo / repetir:* {melhoria_2.strip()}")
        if melhoria_3.strip():
            linhas.append(f"- *Ideia para a rede:* {melhoria_3.strip()}")
        if melhoria_4.strip():
            linhas.append(f"- *Apoio necessário:* {melhoria_4.strip()}")

    linhas.append("\n--------------------")
    linhas.append(f"_Assinado digitalmente por {nome} em {data_str}_")

    return "\n".join(linhas)


# --- DISPARO PARA O WHATSAPP ---
st.subheader("📲 Finalizar e Enviar")

if not assinatura_ok:
    st.warning("Marque a declaração de assinatura acima para liberar o envio ao diretor.")
elif not numero_diretor or len(numero_diretor) < 12:
    st.error("Informe um número válido do diretor na barra lateral (ex: 5531999999999).")
else:
    mensagem_final = gerar_texto_whatsapp()
    texto_codificado = urllib.parse.quote(mensagem_final)
    link_whatsapp = f"https://wa.me/{numero_diretor}?text={texto_codificado}"

    if modo_envio == "Link Direto WhatsApp (1 clique)":
        st.link_button(
            "🚀 Enviar Relatório Agora no WhatsApp do Diretor",
            url=link_whatsapp,
            type="primary",
            use_container_width=True,
        )
    else:
        if st.button("🚀 Disparar Automaticamente via API", type="primary", use_container_width=True):
            if not api_url:
                st.error("Preencha a URL da API na barra lateral.")
            else:
                try:
                    headers = {"Content-Type": "application/json"}
                    if api_token:
                        headers["Client-Token"] = api_token
                        headers["apikey"] = api_token
                    dados = json.dumps(
                        {"phone": numero_diretor, "message": mensagem_final}
                    ).encode("utf-8")
                    req = urllib.request.Request(
                        api_url, data=dados, headers=headers, method="POST"
                    )
                    with urllib.request.urlopen(req, timeout=15) as resp:
                        if resp.status in (200, 201):
                            st.success("✅ Relatório enviado com sucesso para o WhatsApp do diretor!")
                        else:
                            st.error(f"Erro na API ({resp.status})")
                except Exception as e:
                    st.error(f"Falha ao conectar na API: {e}")

    with st.expander("👁️ Pré-visualizar mensagem que chegará no WhatsApp"):
        st.text(mensagem_final)
