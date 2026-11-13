<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Relatório Diário de Rotina – Rede Via</title>

  <!-- Fonte Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
          },
          colors: {
            redevia: {
              red: '#C8102E',
              redDark: '#9E0B23',
              gold: '#EAAA00',
              goldLight: '#FFF8E1',
              bg: '#F4F5F7',
            },
            wpp: {
              green: '#25D366',
              dark: '#128C7E',
              bubble: '#DCF8C6',
            }
          }
        }
      }
    };
  </script>

  <style>
    /* Ajustes finos de usabilidade mobile e transição */
    html {
      scroll-behavior: smooth;
      -webkit-tap-highlight-color: transparent;
    }
    body {
      background-color: #F4F5F7;
      color: #1F2937;
    }
    /* Estilo customizado para botões de opção (rádio em formato de pílula) */
    .radio-pill input:checked + span {
      background-color: #C8102E;
      color: #FFFFFF;
      border-color: #C8102E;
      box-shadow: 0 2px 6px rgba(200, 16, 46, 0.25);
    }
    .radio-pill-neutral input:checked + span {
      background-color: #1F2937;
      color: #FFFFFF;
      border-color: #1F2937;
    }
    .radio-pill-warn input:checked + span {
      background-color: #D97706;
      color: #FFFFFF;
      border-color: #D97706;
    }
    /* Animação suave de entrada para novos cartões */
    @keyframes fadeSlideIn {
      from {
        opacity: 0;
        transform: translateY(8px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
    .animate-card {
      animation: fadeSlideIn 0.22s ease-out forwards;
    }
  </style>
</head>
<body class="min-h-screen pb-16 antialiased">

  <!-- Toast de Notificação Flutuante (substitui alert) -->
  <div id="toast-container" class="fixed top-4 left-1/2 -translate-x-1/2 z-50 w-[92%] max-w-md pointer-events-none flex flex-col gap-2"></div>

  <!-- Modal Customizado de Confirmação para Limpar Campos (substitui confirm) -->
  <div id="confirm-modal" class="fixed inset-0 z-50 hidden items-center justify-center bg-black/50 backdrop-blur-xs p-4">
    <div class="bg-white rounded-2xl max-w-sm w-full p-6 shadow-2xl border border-gray-100 animate-card">
      <div class="flex items-center gap-3 mb-3">
        <div class="w-10 h-10 rounded-full bg-red-100 text-redevia-red flex items-center justify-center shrink-0">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
        </div>
        <h3 class="text-lg font-bold text-gray-900">Limpar campos do dia?</h3>
      </div>
      <p class="text-sm text-gray-600 mb-6 leading-relaxed">
        Isso apagará os postos, itens conferidos, pendências e observações preenchidos hoje. Seu <strong>nome</strong> e o <strong>WhatsApp do diretor</strong> continuarão salvos.
      </p>
      <div class="flex gap-3">
        <button type="button" id="btn-cancel-clear" class="flex-1 py-3 px-4 rounded-xl border border-gray-300 text-gray-700 font-semibold text-sm hover:bg-gray-50 active:scale-[0.99] transition">
          Cancelar
        </button>
        <button type="button" id="btn-confirm-clear" class="flex-1 py-3 px-4 rounded-xl bg-redevia-red text-white font-semibold text-sm hover:bg-redevia-redDark active:scale-[0.99] transition">
          Sim, limpar
        </button>
      </div>
    </div>
  </div>

  <!-- Cabeçalho Principal Rede Via -->
  <header class="bg-redevia-red text-white border-b-4 border-redevia-gold shadow-md">
    <div class="max-w-3xl mx-auto px-4 py-5 sm:py-6">
      <div class="flex items-center gap-3.5">
        <!-- Ícone SVG inspirado na chama Rede Via -->
        <div class="w-12 h-12 rounded-2xl bg-white/10 border border-white/20 flex items-center justify-center shrink-0 shadow-inner">
          <svg class="w-7 h-7" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19.5 3C19.5 3 11 10.5 11 19.5C11 24.8 14.8 29.2 19.8 30C17.2 28.2 15.8 25.1 16.5 21.8C17.1 19.1 19.2 16.8 19.2 16.8C19.2 16.8 18.8 20.4 20.9 22.3C22.4 23.6 23.1 25.6 22.3 27.6C25.6 26.1 27.5 22.6 27.5 18.5C27.5 11.8 19.5 3 19.5 3Z" fill="#EAAA00"/>
            <path d="M18.5 2C12 8.2 8.5 14.5 8.5 20.5C8.5 27.4 13.8 33 20.5 33C26.5 33 31 28.3 31 22C31 15.2 24.5 7.5 18.5 2Z" stroke="white" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div>
          <span class="inline-block text-[11px] font-bold uppercase tracking-wider bg-redevia-gold text-gray-900 px-2.5 py-0.5 rounded-full mb-1">
            REDE VIA • OPERAÇÕES
          </span>
          <h1 class="text-xl sm:text-2xl font-extrabold tracking-tight leading-tight">
            Relatório Diário de Rotina – Rede Via
          </h1>
          <p class="text-xs sm:text-sm text-amber-100 font-medium mt-0.5">
            Coordenadores e Supervisores • Envio Direto para Diretoria
          </p>
        </div>
      </div>

      <!-- Selo / Aviso Discreto de Regras -->
      <div class="mt-4 bg-black/20 border border-white/15 rounded-xl px-3.5 py-2.5 text-xs text-white/95 flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-4">
        <div class="flex items-center gap-1.5">
          <span class="text-redevia-gold font-bold">●</span>
          <span>Enviar <strong>1 relatório por dia</strong> até o fim do expediente.</span>
        </div>
        <div class="flex items-center gap-1.5">
          <span class="text-redevia-gold font-bold">●</span>
          <span>Em recolhimento, marcar apenas <strong>Sim</strong> ou <strong>Não</strong> (sem detalhes).</span>
        </div>
      </div>
    </div>
  </header>

  <!-- Conteúdo Principal -->
  <main class="max-w-3xl mx-auto px-4 pt-5 space-y-5">

    <!-- Painel de Configuração Persistente (localStorage) -->
    <section id="config-section" class="bg-white rounded-2xl border border-gray-200 shadow-sm p-4 sm:p-5">
      <div class="flex items-center justify-between gap-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="w-7 h-7 rounded-lg bg-amber-100 text-amber-800 flex items-center justify-center font-bold text-sm">⚙️</span>
          <h2 class="text-sm sm:text-base font-bold text-gray-900">Configuração Rápida (Salva no Aparelho)</h2>
        </div>
        <span id="save-badge" class="text-[11px] font-semibold text-emerald-700 bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-full">
          ✓ Salvo automaticamente
        </span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label for="cfg-diretor-wpp" class="block text-xs font-semibold text-gray-700 mb-1.5">
            WhatsApp do Diretor (com DDI + DDD) <span class="text-redevia-red">*</span>
          </label>
          <input
            type="tel"
            id="cfg-diretor-wpp"
            placeholder="Ex.: 5531999999999"
            inputmode="numeric"
            class="w-full rounded-xl border border-gray-300 bg-gray-50 focus:bg-white px-3.5 py-3 text-sm font-medium text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
          />
          <p class="text-[11px] text-gray-500 mt-1">Ex.: 55 (Brasil) + 31 (DDD) + número.</p>
        </div>

        <div>
          <label for="cfg-coordenador-nome" class="block text-xs font-semibold text-gray-700 mb-1.5">
            Nome do Coordenador / Supervisor <span class="text-redevia-red">*</span>
          </label>
          <input
            type="text"
            id="cfg-coordenador-nome"
            placeholder="Seu nome completo"
            class="w-full rounded-xl border border-gray-300 bg-gray-50 focus:bg-white px-3.5 py-3 text-sm font-medium text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
          />
          <p class="text-[11px] text-gray-500 mt-1">Fica memorizado para os próximos dias.</p>
        </div>
      </div>
    </section>

    <!-- Seção 1: Identificação -->
    <section class="bg-white rounded-2xl border border-gray-200 shadow-sm p-4 sm:p-6">
      <div class="flex items-center gap-2.5 mb-4 pb-3 border-b border-gray-100">
        <span class="w-7 h-7 rounded-lg bg-redevia-red text-white flex items-center justify-center font-bold text-sm">1</span>
        <h2 class="text-base sm:text-lg font-bold text-gray-900">Identificação</h2>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label for="relatorio-data" class="block text-xs font-semibold text-gray-700 mb-1.5">
            Data do Relatório
          </label>
          <input
            type="date"
            id="relatorio-data"
            class="w-full rounded-xl border border-gray-300 px-3.5 py-3 text-sm font-medium text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
          />
        </div>

        <div>
          <span class="block text-xs font-semibold text-gray-700 mb-1.5">
            Seguiu o cronograma da semana?
          </span>
          <div class="grid grid-cols-2 gap-2.5">
            <label class="radio-pill cursor-pointer">
              <input type="radio" name="seguiu-cronograma" value="Sim" class="sr-only" checked />
              <span class="flex items-center justify-center py-3 px-4 rounded-xl border border-gray-300 text-sm font-bold text-gray-700 transition select-none">
                Sim
              </span>
            </label>
            <label class="radio-pill cursor-pointer">
              <input type="radio" name="seguiu-cronograma" value="Não" class="sr-only" />
              <span class="flex items-center justify-center py-3 px-4 rounded-xl border border-gray-300 text-sm font-bold text-gray-700 transition select-none">
                Não
              </span>
            </label>
          </div>
        </div>
      </div>

      <!-- Campo Condicional de Motivo -->
      <div id="motivo-cronograma-wrapper" class="hidden mt-4 pt-4 border-t border-dashed border-gray-200 animate-card">
        <label for="motivo-cronograma" class="block text-xs font-semibold text-gray-800 mb-1.5">
          Se não seguiu ou mudou algo, explique o motivo:
        </label>
        <textarea
          id="motivo-cronograma"
          rows="2"
          placeholder="Descreva o motivo da alteração no cronograma da semana..."
          class="w-full rounded-xl border border-gray-300 px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
        ></textarea>
      </div>
    </section>

    <!-- Seção 2: Postos Visitados e O Que Foi Feito -->
    <section class="bg-white rounded-2xl border border-gray-200 shadow-sm p-4 sm:p-6">
      <div class="flex items-center justify-between gap-2 mb-4 pb-3 border-b border-gray-100">
        <div class="flex items-center gap-2.5">
          <span class="w-7 h-7 rounded-lg bg-redevia-red text-white flex items-center justify-center font-bold text-sm">2</span>
          <div>
            <h2 class="text-base sm:text-lg font-bold text-gray-900">Postos Visitados e O Que Foi Feito</h2>
            <p class="text-xs text-gray-500">Inclua todos os postos visitados, mesmo fora do cronograma.</p>
          </div>
        </div>
        <span id="postos-count-badge" class="text-xs font-bold bg-gray-100 text-gray-700 px-2.5 py-1 rounded-full shrink-0">
          1 posto
        </span>
      </div>

      <!-- Lista Dinâmica de Postos -->
      <div id="postos-list" class="space-y-4"></div>

      <!-- Botão Adicionar Outro Posto -->
      <button
        type="button"
        id="btn-add-posto"
        class="mt-4 w-full py-3.5 px-4 rounded-xl border-2 border-dashed border-redevia-red/40 bg-red-50/50 hover:bg-red-50 text-redevia-red font-bold text-sm flex items-center justify-center gap-2 active:scale-[0.99] transition"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.4" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
        </svg>
        Adicionar outro posto visitado
      </button>
    </section>

    <!-- Seção 3: Itens Conferidos na Visita -->
    <section class="bg-white rounded-2xl border border-gray-200 shadow-sm p-4 sm:p-6">
      <div class="flex items-start justify-between gap-2 mb-2 pb-3 border-b border-gray-100">
        <div class="flex items-center gap-2.5">
          <span class="w-7 h-7 rounded-lg bg-redevia-red text-white flex items-center justify-center font-bold text-sm shrink-0">3</span>
          <div>
            <h2 class="text-base sm:text-lg font-bold text-gray-900">Itens Conferidos na Visita</h2>
          </div>
        </div>
        <button
          type="button"
          id="btn-toggle-all-itens"
          class="text-xs font-semibold text-redevia-red hover:underline shrink-0 py-1"
        >
          Marcar todos
        </button>
      </div>

      <p class="text-xs text-amber-900 bg-redevia-goldLight border border-amber-200 rounded-xl px-3.5 py-2 mb-4">
        ℹ️ Esta lista é um resumo para o dia a dia e não substitui o checklist bimestral.
      </p>

      <div id="itens-checklist" class="space-y-2.5">
        <!-- Preenchido via JS -->
      </div>

      <div class="mt-4">
        <label for="outros-itens" class="block text-xs font-semibold text-gray-700 mb-1.5">
          Outros itens conferidos (opcional)
        </label>
        <input
          type="text"
          id="outros-itens"
          placeholder="Descreva outros pontos verificados..."
          class="w-full rounded-xl border border-gray-300 px-3.5 py-3 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
        />
      </div>
    </section>

    <!-- Seção 4: Pendências e Próximos Passos -->
    <section class="bg-white rounded-2xl border border-gray-200 shadow-sm p-4 sm:p-6">
      <div class="flex items-center justify-between gap-2 mb-4 pb-3 border-b border-gray-100">
        <div class="flex items-center gap-2.5">
          <span class="w-7 h-7 rounded-lg bg-redevia-red text-white flex items-center justify-center font-bold text-sm">4</span>
          <div>
            <h2 class="text-base sm:text-lg font-bold text-gray-900">Pendências e Próximos Passos</h2>
            <p class="text-xs text-gray-500">Registre o que ficou pendente e quem é o responsável.</p>
          </div>
        </div>
      </div>

      <!-- Datalist de postos para agilizar digitação -->
      <datalist id="datalist-postos"></datalist>

      <!-- Lista Dinâmica de Pendências -->
      <div id="pendencias-list" class="space-y-4"></div>

      <button
        type="button"
        id="btn-add-pendencia"
        class="mt-4 w-full py-3 px-4 rounded-xl border-2 border-dashed border-gray-300 bg-gray-50 hover:bg-gray-100 text-gray-800 font-bold text-sm flex items-center justify-center gap-2 active:scale-[0.99] transition"
      >
        <svg class="w-5 h-5 text-redevia-red" fill="none" stroke="currentColor" stroke-width="2.4" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
        </svg>
        Adicionar pendência
      </button>

      <div class="mt-5 pt-4 border-t border-gray-100">
        <label for="obs-gerais" class="block text-xs font-semibold text-gray-700 mb-1.5">
          Observações gerais do dia
        </label>
        <textarea
          id="obs-gerais"
          rows="3"
          placeholder="Anotações complementares sobre a rotina de hoje..."
          class="w-full rounded-xl border border-gray-300 px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
        ></textarea>
      </div>
    </section>

    <!-- Seção 5: Oportunidades de Melhoria -->
    <section class="bg-white rounded-2xl border border-gray-200 shadow-sm p-4 sm:p-6">
      <div class="flex items-center gap-2.5 mb-2 pb-3 border-b border-gray-100">
        <span class="w-7 h-7 rounded-lg bg-redevia-red text-white flex items-center justify-center font-bold text-sm shrink-0">5</span>
        <div>
          <h2 class="text-base sm:text-lg font-bold text-gray-900">Oportunidades de Melhoria</h2>
          <p class="text-xs text-gray-500">Seu olhar no posto ajuda a rede a evoluir. Não precisa ter a solução pronta.</p>
        </div>
      </div>

      <div class="bg-gray-50 border border-gray-200 rounded-xl p-3 text-xs text-gray-600 leading-relaxed mb-4">
        <strong class="text-gray-800">Áreas guia:</strong> Atendimento (fila, tempo de espera, cordialidade) · Vendas e serviços (troca de óleo, lavagem, conveniência, aditivos) · Equipe (escala, distribuição de tarefas, horários com pouco movimento) · Operação e estrutura (bombas, estoque, pista, loja, banheiros).
      </div>

      <div class="space-y-4">
        <div>
          <label for="melhoria-1" class="block text-xs font-bold text-gray-800 mb-1.5">
            1. O que você observou que pode melhorar
          </label>
          <textarea
            id="melhoria-1"
            rows="2"
            placeholder="Ex.: Fila no caixa da conveniência no horário de pico..."
            class="w-full rounded-xl border border-gray-300 px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
          ></textarea>
        </div>

        <div>
          <label for="melhoria-2" class="block text-xs font-bold text-gray-800 mb-1.5">
            2. O que deu certo e vale repetir (boa prática para outros postos)
          </label>
          <textarea
            id="melhoria-2"
            rows="2"
            placeholder="Ex.: Abordagem ativa para oferta de aditivos no Posto..."
            class="w-full rounded-xl border border-gray-300 px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
          ></textarea>
        </div>

        <div>
          <label for="melhoria-3" class="block text-xs font-bold text-gray-800 mb-1.5">
            3. Sua ideia para a rede
          </label>
          <textarea
            id="melhoria-3"
            rows="2"
            placeholder="Algum serviço novo, ação com clientes ou forma de organizar o trabalho..."
            class="w-full rounded-xl border border-gray-300 px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
          ></textarea>
        </div>

        <div>
          <label for="melhoria-4" class="block text-xs font-bold text-gray-800 mb-1.5">
            4. Precisa de apoio? (material, manutenção, treinamento, decisão)
          </label>
          <textarea
            id="melhoria-4"
            rows="2"
            placeholder="Algo que você ou o posto precisa do escritório..."
            class="w-full rounded-xl border border-gray-300 px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
          ></textarea>
        </div>
      </div>
    </section>

    <!-- Seção 6: Assinatura, Pré-visualização e Envio para WhatsApp -->
    <section class="bg-white rounded-2xl border border-gray-200 shadow-sm p-4 sm:p-6">
      <div class="flex items-center gap-2.5 mb-4 pb-3 border-b border-gray-100">
        <span class="w-7 h-7 rounded-lg bg-redevia-red text-white flex items-center justify-center font-bold text-sm">6</span>
        <h2 class="text-base sm:text-lg font-bold text-gray-900">Assinatura e Envio para WhatsApp</h2>
      </div>

      <!-- Declaração Obrigatória -->
      <div id="assinatura-box" class="rounded-xl border-2 border-gray-200 bg-gray-50 p-3.5 transition">
        <label class="flex items-start gap-3 cursor-pointer select-none">
          <input
            type="checkbox"
            id="assinatura-check"
            class="mt-0.5 w-5 h-5 rounded border-gray-300 text-redevia-red focus:ring-redevia-red shrink-0 cursor-pointer"
          />
          <span class="text-sm font-semibold text-gray-800 leading-snug">
            Declaro que as informações acima correspondem às atividades realizadas no dia.
          </span>
        </label>
        <p id="assinatura-erro" class="hidden text-xs font-bold text-redevia-red mt-2 pl-8">
          ⚠️ Marque a declaração acima antes de enviar o relatório ao diretor.
        </p>
      </div>

      <!-- Pré-visualização em Tempo Real -->
      <div class="mt-5">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-bold uppercase tracking-wider text-gray-500 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-wpp-green"></span>
            Pré-visualização da Mensagem no WhatsApp
          </span>
          <span id="char-count" class="text-[11px] text-gray-400 font-medium">0 caracteres</span>
        </div>

        <!-- Bolha estilo WhatsApp -->
        <div class="bg-[#EFEAE2] rounded-2xl p-3.5 sm:p-4 border border-gray-200">
          <div class="bg-wpp-bubble rounded-xl rounded-tr-none p-3.5 shadow-xs text-[13px] leading-relaxed text-gray-900 whitespace-pre-wrap font-sans break-words max-h-80 overflow-y-auto" id="wpp-preview"></div>
        </div>
      </div>

      <!-- Botões de Ação -->
      <div class="mt-6 space-y-3">
        <!-- Botão Principal WhatsApp -->
        <button
          type="button"
          id="btn-enviar-wpp"
          class="w-full py-4 px-5 rounded-2xl bg-wpp-green hover:bg-wpp-dark text-white font-extrabold text-base shadow-lg shadow-emerald-500/25 flex items-center justify-center gap-2.5 active:scale-[0.99] transition cursor-pointer"
        >
          <!-- Ícone WhatsApp SVG -->
          <svg class="w-6 h-6 fill-current shrink-0" viewBox="0 0 24 24">
            <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824zm-3.423-14.416c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm.029 18.88c-1.161 0-2.305-.292-3.318-.844l-3.677.964.984-3.595c-.607-1.052-.927-2.246-.926-3.468.001-3.825 3.113-6.937 6.937-6.937 1.856.001 3.598.723 4.907 2.034 1.31 1.311 2.031 3.054 2.03 4.908-.001 3.825-3.113 6.938-6.937 6.938z"/>
          </svg>
          <span>Enviar Relatório no WhatsApp do Diretor</span>
        </button>

        <!-- Link Direto Alternativo (exibido após validação caso pop-up seja bloqueado) -->
        <div id="direct-link-fallback" class="hidden rounded-xl bg-emerald-50 border border-emerald-200 p-3 text-center">
          <p class="text-xs text-emerald-900 mb-1.5 font-medium">Se o WhatsApp não abriu automaticamente, toque no link direto abaixo:</p>
          <a id="direct-wpp-anchor" href="#" target="_blank" rel="noopener noreferrer" class="inline-block text-xs font-extrabold text-wpp-dark underline">
            Abrir conversa no WhatsApp (wa.me) ↗
          </a>
        </div>

        <!-- Botões Secundários -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
          <button
            type="button"
            id="btn-copy-text"
            class="py-3 px-4 rounded-xl border border-gray-300 bg-white hover:bg-gray-50 text-gray-800 font-bold text-sm flex items-center justify-center gap-2 active:scale-[0.99] transition cursor-pointer"
          >
            <svg class="w-4 h-4 text-gray-600" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
            Copiar Texto do Relatório
          </button>

          <button
            type="button"
            id="btn-clear-day"
            class="py-3 px-4 rounded-xl border border-gray-300 bg-white hover:bg-red-50 hover:border-red-200 hover:text-redevia-red text-gray-600 font-semibold text-sm flex items-center justify-center gap-2 active:scale-[0.99] transition cursor-pointer"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            Limpar Campos do Dia
          </button>
        </div>
      </div>
    </section>

  </main>

  <script>
    (function () {
      'use strict';

      // --- CONSTANTES E DADOS DA REDE ---
      const STORAGE_KEYS = {
        DIRETOR_WPP: 'redevia_diretor_wpp',
        COORD_NOME: 'redevia_coordenador_nome',
        DRAFT: 'redevia_relatorio_draft_v1',
      };

      const UNIDADES_REDE = [
        'Bel',
        'Mario Campos',
        'Demetrios',
        'Jardim das Rosas',
        'MM040',
        'Rio Acima',
        'Esmeraldas',
        'Itabira',
        'Toronto',
        'Veneza',
        'Vianópolis',
        'Caldas',
        'Via Rodovia',
        'Via Industrial',
        'Via Centro',
        'Via Cajuri',
        'Acaiaca',
        'Waam',
        'Guarapiranga',
        'Palmeiras',
      ];

      const ITENS_CHECKLIST = [
        'Pista e equipamentos (bombas, canaletas, vazamentos)',
        'Estoque de combustível (diferenças, sobras e faltas)',
        'Limpeza e conservação do posto como um todo (pátio, pista, banheiros, loja)',
        'Equipe (escala, uniformes, atendimento)',
        'Segurança e meio ambiente',
        'Conversa com o gerente',
      ];

      // --- UTILITÁRIOS DE DATA ---
      function getTodayISO() {
        const now = new Date();
        const offset = now.getTimezoneOffset();
        const local = new Date(now.getTime() - offset * 60000);
        return local.toISOString().split('T')[0];
      }

      function getTomorrowISO() {
        const now = new Date();
        now.setDate(now.getDate() + 1);
        const offset = now.getTimezoneOffset();
        const local = new Date(now.getTime() - offset * 60000);
        return local.toISOString().split('T')[0];
      }

      function formatISOToBR(isoDate) {
        if (!isoDate || !isoDate.includes('-')) return '__/__/____';
        const [y, m, d] = isoDate.split('-');
        return `${d}/${m}/${y}`;
      }

      function escapeHTML(str) {
        return String(str || '')
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/"/g, '&quot;');
      }

      // --- NOTIFICAÇÕES VISUAIS (TOAST) ---
      function showToast(message, type = 'success') {
        const container = document.getElementById('toast-container');
        const toast = document.createElement('div');
        const colors = {
          success: 'bg-emerald-800 text-white border-emerald-600',
          error: 'bg-redevia-red text-white border-red-800',
          info: 'bg-gray-900 text-white border-gray-700',
        };
        toast.className = `pointer-events-auto px-4 py-3 rounded-xl shadow-lg border text-sm font-semibold flex items-center justify-between gap-3 animate-card ${colors[type] || colors.info}`;
        toast.innerHTML = `<span>${escapeHTML(message)}</span>`;
        container.appendChild(toast);

        setTimeout(() => {
          toast.style.opacity = '0';
          toast.style.transition = 'opacity 0.25s ease';
          setTimeout(() => toast.remove(), 260);
        }, 3400);
      }

      // --- ESTADO DA APLICAÇÃO ---
      let state = {
        diretorWpp: '',
        coordenadorNome: 'Hitalo Gustavo Mendes Pinheiro',
        dataRelatorio: getTodayISO(),
        seguiuCronograma: 'Sim',
        motivoCronograma: '',
        postos: [],
        itensConferidos: [],
        outrosItens: '',
        pendencias: [],
        obsGerais: '',
        melhoria1: '',
        melhoria2: '',
        melhoria3: '',
        melhoria4: '',
        assinaturaOk: false,
      };

      function createEmptyPosto() {
        return {
          id: 'posto_' + Date.now() + '_' + Math.random().toString(36).slice(2, 7),
          postoSelect: '',
          postoManual: '',
          noCronograma: 'Sim',
          motivo: '',
          conversa: '',
          verificou: '',
          resolveu: '',
          recolhimento: 'Não',
        };
      }

      function createEmptyPendencia() {
        return {
          id: 'pend_' + Date.now() + '_' + Math.random().toString(36).slice(2, 7),
          posto: '',
          responsavel: '',
          prazo: getTomorrowISO(),
          descricao: '',
        };
      }

      // --- PERSISTÊNCIA (LOCALSTORAGE) ---
      function loadPersistentSettings() {
        try {
          const savedWpp = localStorage.getItem(STORAGE_KEYS.DIRETOR_WPP);
          const savedNome = localStorage.getItem(STORAGE_KEYS.COORD_NOME);

          if (savedWpp !== null) {
            state.diretorWpp = savedWpp;
          }
          if (savedNome !== null && savedNome.trim() !== '') {
            state.coordenadorNome = savedNome;
          }

          // Carregar rascunho do dia se existir
          const draftRaw = localStorage.getItem(STORAGE_KEYS.DRAFT);
          if (draftRaw) {
            const draft = JSON.parse(draftRaw);
            state.dataRelatorio = draft.dataRelatorio || getTodayISO();
            state.seguiuCronograma = draft.seguiuCronograma || 'Sim';
            state.motivoCronograma = draft.motivoCronograma || '';
            state.postos = Array.isArray(draft.postos) && draft.postos.length > 0 ? draft.postos : [createEmptyPosto()];
            state.itensConferidos = Array.isArray(draft.itensConferidos) ? draft.itensConferidos : [];
            state.outrosItens = draft.outrosItens || '';
            state.pendencias = Array.isArray(draft.pendencias) ? draft.pendencias : [createEmptyPendencia()];
            state.obsGerais = draft.obsGerais || '';
            state.melhoria1 = draft.melhoria1 || '';
            state.melhoria2 = draft.melhoria2 || '';
            state.melhoria3 = draft.melhoria3 || '';
            state.melhoria4 = draft.melhoria4 || '';
            state.assinaturaOk = Boolean(draft.assinaturaOk);
          } else {
            state.postos = [createEmptyPosto()];
            state.pendencias = [createEmptyPendencia()];
          }
        } catch (e) {
          state.postos = [createEmptyPosto()];
          state.pendencias = [createEmptyPendencia()];
        }
      }

      function saveToStorage() {
        try {
          localStorage.setItem(STORAGE_KEYS.DIRETOR_WPP, state.diretorWpp);
          localStorage.setItem(STORAGE_KEYS.COORD_NOME, state.coordenadorNome);

          const draft = {
            dataRelatorio: state.dataRelatorio,
            seguiuCronograma: state.seguiuCronograma,
            motivoCronograma: state.motivoCronograma,
            postos: state.postos,
            itensConferidos: state.itensConferidos,
            outrosItens: state.outrosItens,
            pendencias: state.pendencias,
            obsGerais: state.obsGerais,
            melhoria1: state.melhoria1,
            melhoria2: state.melhoria2,
            melhoria3: state.melhoria3,
            melhoria4: state.melhoria4,
            assinaturaOk: state.assinaturaOk,
          };
          localStorage.setItem(STORAGE_KEYS.DRAFT, JSON.stringify(draft));

          // Feedback visual rápido no selo de salvamento
          const badge = document.getElementById('save-badge');
          if (badge) {
            badge.textContent = '✓ Salvo agora';
            clearTimeout(badge._timer);
            badge._timer = setTimeout(() => {
              badge.textContent = '✓ Salvo automaticamente';
            }, 1500);
          }
        } catch (e) {
          // Ignora erro caso armazenamento privado esteja bloqueado
        }
      }

      // --- GERAÇÃO DO TEXTO FORMATADO PARA WHATSAPP ---
      function buildWhatsAppMessage() {
        const dataBR = formatISOToBR(state.dataRelatorio);
        const nomeCoord = state.coordenadorNome.trim() || 'Não informado';
        const lines = [
          '*RELATÓRIO DIÁRIO DE ROTINA – REDE VIA*',
          `*Coordenador/Supervisor:* ${nomeCoord}`,
          `*Data:* ${dataBR}`,
          `*Seguiu cronograma:* ${state.seguiuCronograma}`,
        ];

        if (state.seguiuCronograma === 'Não' && state.motivoCronograma.trim()) {
          lines.push(`*Motivo da alteração:* ${state.motivoCronograma.trim()}`);
        }

        lines.push('');
        lines.push('━━━━━━━━━━━━━━━━━━━━');
        lines.push('*POSTOS VISITADOS E ATIVIDADES*');

        state.postos.forEach((p, idx) => {
          const nomePosto =
            p.postoSelect === 'OUTRO'
              ? p.postoManual.trim() || 'Outro (não especificado)'
              : p.postoSelect || 'Não selecionado';

          lines.push('');
          lines.push(`*Posto ${idx + 1}: ${nomePosto}* (No cronograma: ${p.noCronograma})`);
          if (p.motivo.trim()) lines.push(`• *Motivo:* ${p.motivo.trim()}`);
          if (p.conversa.trim()) lines.push(`• *Conversou com:* ${p.conversa.trim()}`);
          if (p.verificou.trim()) lines.push(`• *Verificou:* ${p.verificou.trim()}`);
          if (p.resolveu.trim()) lines.push(`• *Resolveu:* ${p.resolveu.trim()}`);
          lines.push(`• *Recolhimento:* ${p.recolhimento}`);
        });

        lines.push('');
        lines.push('━━━━━━━━━━━━━━━━━━━━');
        lines.push('*ITENS CONFERIDOS NA VISITA*');
        if (state.itensConferidos.length > 0) {
          state.itensConferidos.forEach((item) => {
            lines.push(`✅ ${item}`);
          });
        } else {
          lines.push('• Nenhum item marcado');
        }
        if (state.outrosItens.trim()) {
          lines.push(`✅ Outros: ${state.outrosItens.trim()}`);
        }

        lines.push('');
        lines.push('━━━━━━━━━━━━━━━━━━━━');
        lines.push('*PENDÊNCIAS E PRÓXIMOS PASSOS*');

        const pendenciasValidas = state.pendencias.filter(
          (pend) => pend.posto.trim() || pend.responsavel.trim() || pend.descricao.trim()
        );

        if (pendenciasValidas.length > 0) {
          pendenciasValidas.forEach((pend, idx) => {
            const pPosto = pend.posto.trim() || '-';
            const pResp = pend.responsavel.trim() || '-';
            const pPrazo = pend.prazo ? formatISOToBR(pend.prazo) : '-';
            lines.push('');
            lines.push(`*Pendência ${idx + 1}* — Posto: ${pPosto} | Resp.: ${pResp} | Prazo: ${pPrazo}`);
            if (pend.descricao.trim()) {
              lines.push(`• ${pend.descricao.trim()}`);
            }
          });
        } else {
          lines.push('• Sem pendências registradas.');
        }

        if (state.obsGerais.trim()) {
          lines.push('');
          lines.push(`*Observações gerais:* ${state.obsGerais.trim()}`);
        }

        const temMelhorias =
          state.melhoria1.trim() ||
          state.melhoria2.trim() ||
          state.melhoria3.trim() ||
          state.melhoria4.trim();

        if (temMelhorias) {
          lines.push('');
          lines.push('━━━━━━━━━━━━━━━━━━━━');
          lines.push('*OPORTUNIDADES DE MELHORIA*');
          if (state.melhoria1.trim()) lines.push(`• *Pode melhorar:* ${state.melhoria1.trim()}`);
          if (state.melhoria2.trim()) lines.push(`• *Deu certo / repetir:* ${state.melhoria2.trim()}`);
          if (state.melhoria3.trim()) lines.push(`• *Ideia para a rede:* ${state.melhoria3.trim()}`);
          if (state.melhoria4.trim()) lines.push(`• *Apoio necessário:* ${state.melhoria4.trim()}`);
        }

        lines.push('');
        lines.push('━━━━━━━━━━━━━━━━━━━━');
        lines.push(`✍️ _Assinado digitalmente por ${nomeCoord} em ${dataBR}_`);

        return lines.join('\n');
      }

      function updatePreview() {
        const msg = buildWhatsAppMessage();
        const previewEl = document.getElementById('wpp-preview');
        const charCountEl = document.getElementById('char-count');
        if (previewEl) previewEl.textContent = msg;
        if (charCountEl) charCountEl.textContent = `${msg.length} caracteres`;
      }

      // --- RENDERIZAÇÃO DE COMPONENTES DINÂMICOS ---
      function renderPostos() {
        const container = document.getElementById('postos-list');
        const badge = document.getElementById('postos-count-badge');
        badge.textContent = state.postos.length === 1 ? '1 posto' : `${state.postos.length} postos`;

        container.innerHTML = state.postos
          .map((posto, index) => {
            const optionsHTML = UNIDADES_REDE.map(
              (u) => `<option value="${escapeHTML(u)}" ${posto.postoSelect === u ? 'selected' : ''}>${escapeHTML(u)}</option>`
            ).join('');

            const isOutro = posto.postoSelect === 'OUTRO';
            const canRemove = state.postos.length > 1;

            return `
              <div class="rounded-2xl border border-gray-200 bg-gray-50/70 p-4 sm:p-5 space-y-4 animate-card" data-posto-id="${posto.id}">
                <div class="flex items-center justify-between gap-2 pb-2.5 border-b border-gray-200/80">
                  <div class="flex items-center gap-2">
                    <span class="w-6 h-6 rounded-full bg-redevia-red text-white text-xs font-extrabold flex items-center justify-center">
                      ${index + 1}
                    </span>
                    <h3 class="text-sm font-extrabold text-gray-900">Posto Visitado #${index + 1}</h3>
                  </div>
                  ${
                    canRemove
                      ? `<button type="button" data-action="remove-posto" data-index="${index}" class="text-xs font-bold text-redevia-red hover:bg-red-100 px-2.5 py-1.5 rounded-lg transition cursor-pointer">
                          Remover
                        </button>`
                      : ''
                  }
                </div>

                <!-- Seleção do Posto + Estava no Cronograma -->
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3.5">
                  <div class="sm:col-span-2">
                    <label class="block text-xs font-semibold text-gray-700 mb-1.5">
                      Posto (nome / bairro)
                    </label>
                    <select
                      data-field="postoSelect"
                      data-index="${index}"
                      class="w-full rounded-xl border border-gray-300 bg-white px-3.5 py-3 text-sm font-semibold text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
                    >
                      <option value="">Selecione o posto...</option>
                      ${optionsHTML}
                      <option value="OUTRO" ${isOutro ? 'selected' : ''}>Outro (digitar manualmente)</option>
                    </select>

                    <div class="${isOutro ? 'mt-2.5' : 'hidden'}">
                      <input
                        type="text"
                        data-field="postoManual"
                        data-index="${index}"
                        value="${escapeHTML(posto.postoManual)}"
                        placeholder="Digite o nome ou bairro do posto..."
                        class="w-full rounded-xl border border-gray-300 bg-white px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
                      />
                    </div>
                  </div>

                  <div>
                    <span class="block text-xs font-semibold text-gray-700 mb-1.5">
                      Estava no cronograma?
                    </span>
                    <div class="grid grid-cols-2 gap-2">
                      <label class="radio-pill cursor-pointer">
                        <input type="radio" name="crono_posto_${posto.id}" value="Sim" data-field="noCronograma" data-index="${index}" class="sr-only" ${posto.noCronograma === 'Sim' ? 'checked' : ''} />
                        <span class="flex items-center justify-center py-3 px-2 rounded-xl border border-gray-300 bg-white text-xs font-bold text-gray-700 transition select-none">
                          Sim
                        </span>
                      </label>
                      <label class="radio-pill cursor-pointer">
                        <input type="radio" name="crono_posto_${posto.id}" value="Não" data-field="noCronograma" data-index="${index}" class="sr-only" ${posto.noCronograma === 'Não' ? 'checked' : ''} />
                        <span class="flex items-center justify-center py-3 px-2 rounded-xl border border-gray-300 bg-white text-xs font-bold text-gray-700 transition select-none">
                          Não
                        </span>
                      </label>
                    </div>
                  </div>
                </div>

                <!-- Motivo e Com quem conversou -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1.5">
                      Motivo da visita
                    </label>
                    <input
                      type="text"
                      data-field="motivo"
                      data-index="${index}"
                      value="${escapeHTML(posto.motivo)}"
                      placeholder="Ex.: Rotina, vazamento, alinhamento..."
                      class="w-full rounded-xl border border-gray-300 bg-white px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
                    />
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1.5">
                      Com quem conversou
                    </label>
                    <input
                      type="text"
                      data-field="conversa"
                      data-index="${index}"
                      value="${escapeHTML(posto.conversa)}"
                      placeholder="Ex.: Gerente João, Chefe de Pista..."
                      class="w-full rounded-xl border border-gray-300 bg-white px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
                    />
                  </div>
                </div>

                <!-- O que verificou e O que resolveu -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1.5">
                      O que verificou
                    </label>
                    <textarea
                      rows="2"
                      data-field="verificou"
                      data-index="${index}"
                      placeholder="Ex.: Verificou a pista e encontrou canaleta entupida..."
                      class="w-full rounded-xl border border-gray-300 bg-white px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
                    >${escapeHTML(posto.verificou)}</textarea>
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1.5">
                      O que resolveu
                    </label>
                    <textarea
                      rows="2"
                      data-field="resolveu"
                      data-index="${index}"
                      placeholder="Ex.: Acionou limpeza imediata e orientou equipe..."
                      class="w-full rounded-xl border border-gray-300 bg-white px-3.5 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
                    >${escapeHTML(posto.resolveu)}</textarea>
                  </div>
                </div>

                <!-- Recolhimento (Apenas Sim ou Não) -->
                <div class="pt-2 border-t border-gray-200/80 flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
                  <div>
                    <span class="block text-xs font-bold text-gray-800">
                      Recolhimento?
                    </span>
                    <span class="text-[11px] text-amber-800 font-medium">
                      Atenção: marque apenas Sim ou Não, sem detalhes.
                    </span>
                  </div>
                  <div class="grid grid-cols-2 gap-2 sm:w-44 shrink-0">
                    <label class="radio-pill-neutral cursor-pointer">
                      <input type="radio" name="recolh_${posto.id}" value="Não" data-field="recolhimento" data-index="${index}" class="sr-only" ${posto.recolhimento === 'Não' ? 'checked' : ''} />
                      <span class="flex items-center justify-center py-2.5 px-3 rounded-xl border border-gray-300 bg-white text-xs font-bold text-gray-700 transition select-none">
                        Não
                      </span>
                    </label>
                    <label class="radio-pill-warn cursor-pointer">
                      <input type="radio" name="recolh_${posto.id}" value="Sim" data-field="recolhimento" data-index="${index}" class="sr-only" ${posto.recolhimento === 'Sim' ? 'checked' : ''} />
                      <span class="flex items-center justify-center py-2.5 px-3 rounded-xl border border-gray-300 bg-white text-xs font-bold text-gray-700 transition select-none">
                        Sim
                      </span>
                    </label>
                  </div>
                </div>
              </div>
            `;
          })
          .join('');
      }

      function renderItensChecklist() {
        const container = document.getElementById('itens-checklist');
        container.innerHTML = ITENS_CHECKLIST.map((item, idx) => {
          const checked = state.itensConferidos.includes(item);
          return `
            <label class="flex items-center gap-3 p-3 rounded-xl border ${checked ? 'border-redevia-red bg-red-50/40' : 'border-gray-200 bg-gray-50/50 hover:bg-gray-50'} cursor-pointer transition select-none">
              <input
                type="checkbox"
                data-item-index="${idx}"
                ${checked ? 'checked' : ''}
                class="w-5 h-5 rounded border-gray-300 text-redevia-red focus:ring-redevia-red shrink-0 cursor-pointer"
              />
              <span class="text-sm font-medium text-gray-800 leading-snug">${escapeHTML(item)}</span>
            </label>
          `;
        }).join('');

        const btnToggleAll = document.getElementById('btn-toggle-all-itens');
        if (btnToggleAll) {
          btnToggleAll.textContent =
            state.itensConferidos.length === ITENS_CHECKLIST.length ? 'Desmarcar todos' : 'Marcar todos';
        }
      }

      function renderPendencias() {
        const container = document.getElementById('pendencias-list');

        if (state.pendencias.length === 0) {
          container.innerHTML = `
            <div class="text-center py-4 px-3 rounded-xl border border-dashed border-gray-200 bg-gray-50/60 text-xs text-gray-500">
              Nenhuma pendência adicionada hoje. Clique abaixo se precisar registrar alguma.
            </div>
          `;
          return;
        }

        container.innerHTML = state.pendencias
          .map((pend, index) => {
            return `
              <div class="rounded-2xl border border-gray-200 bg-gray-50/70 p-4 space-y-3 animate-card" data-pend-id="${pend.id}">
                <div class="flex items-center justify-between gap-2 pb-2 border-b border-gray-200/80">
                  <span class="text-xs font-extrabold uppercase tracking-wide text-gray-700">
                    Pendência #${index + 1}
                  </span>
                  <button
                    type="button"
                    data-action="remove-pendencia"
                    data-index="${index}"
                    class="text-xs font-bold text-redevia-red hover:bg-red-100 px-2.5 py-1 rounded-lg transition cursor-pointer"
                  >
                    Remover
                  </button>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Posto</label>
                    <input
                      type="text"
                      list="datalist-postos"
                      data-pend-field="posto"
                      data-index="${index}"
                      value="${escapeHTML(pend.posto)}"
                      placeholder="Nome do posto"
                      class="w-full rounded-xl border border-gray-300 bg-white px-3 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
                    />
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Responsável</label>
                    <input
                      type="text"
                      data-pend-field="responsavel"
                      data-index="${index}"
                      value="${escapeHTML(pend.responsavel)}"
                      placeholder="Quem vai resolver"
                      class="w-full rounded-xl border border-gray-300 bg-white px-3 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
                    />
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Prazo</label>
                    <input
                      type="date"
                      data-pend-field="prazo"
                      data-index="${index}"
                      value="${escapeHTML(pend.prazo)}"
                      class="w-full rounded-xl border border-gray-300 bg-white px-3 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
                    />
                  </div>
                </div>

                <div>
                  <label class="block text-xs font-semibold text-gray-700 mb-1">O que ficou pendente</label>
                  <textarea
                    rows="2"
                    data-pend-field="descricao"
                    data-index="${index}"
                    placeholder="Descreva a pendência e a ação esperada..."
                    class="w-full rounded-xl border border-gray-300 bg-white px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-redevia-red focus:border-redevia-red transition"
                  >${escapeHTML(pend.descricao)}</textarea>
                </div>
              </div>
            `;
          })
          .join('');
      }

      function syncStaticInputsFromState() {
        document.getElementById('cfg-diretor-wpp').value = state.diretorWpp;
        document.getElementById('cfg-coordenador-nome').value = state.coordenadorNome;
        document.getElementById('relatorio-data').value = state.dataRelatorio;

        const radiosCrono = document.querySelectorAll('input[name="seguiu-cronograma"]');
        radiosCrono.forEach((r) => {
          r.checked = r.value === state.seguiuCronograma;
        });

        const motivoWrapper = document.getElementById('motivo-cronograma-wrapper');
        if (state.seguiuCronograma === 'Não') {
          motivoWrapper.classList.remove('hidden');
        } else {
          motivoWrapper.classList.add('hidden');
        }

        document.getElementById('motivo-cronograma').value = state.motivoCronograma;
        document.getElementById('outros-itens').value = state.outrosItens;
        document.getElementById('obs-gerais').value = state.obsGerais;
        document.getElementById('melhoria-1').value = state.melhoria1;
        document.getElementById('melhoria-2').value = state.melhoria2;
        document.getElementById('melhoria-3').value = state.melhoria3;
        document.getElementById('melhoria-4').value = state.melhoria4;
        document.getElementById('assinatura-check').checked = state.assinaturaOk;
      }

      // --- VINCULAÇÃO DE EVENTOS ---
      function bindEvents() {
        // Datalist de postos
        const datalist = document.getElementById('datalist-postos');
        datalist.innerHTML = UNIDADES_REDE.map((u) => `<option value="${escapeHTML(u)}"></option>`).join('');

        // Configuração persistente
        document.getElementById('cfg-diretor-wpp').addEventListener('input', (e) => {
          state.diretorWpp = e.target.value;
          saveToStorage();
        });

        document.getElementById('cfg-coordenador-nome').addEventListener('input', (e) => {
          state.coordenadorNome = e.target.value;
          saveToStorage();
          updatePreview();
        });

        // Seção 1: Identificação
        document.getElementById('relatorio-data').addEventListener('change', (e) => {
          state.dataRelatorio = e.target.value;
          saveToStorage();
          updatePreview();
        });

        document.querySelectorAll('input[name="seguiu-cronograma"]').forEach((radio) => {
          radio.addEventListener('change', (e) => {
            state.seguiuCronograma = e.target.value;
            const wrapper = document.getElementById('motivo-cronograma-wrapper');
            if (state.seguiuCronograma === 'Não') {
              wrapper.classList.remove('hidden');
            } else {
              wrapper.classList.add('hidden');
            }
            saveToStorage();
            updatePreview();
          });
        });

        document.getElementById('motivo-cronograma').addEventListener('input', (e) => {
          state.motivoCronograma = e.target.value;
          saveToStorage();
          updatePreview();
        });

        // Seção 2: Delegação de eventos para lista dinâmica de postos
        const postosList = document.getElementById('postos-list');

        postosList.addEventListener('change', (e) => {
          const target = e.target;
          const idx = Number(target.dataset.index);
          const field = target.dataset.field;
          if (Number.isNaN(idx) || !field || !state.postos[idx]) return;

          state.postos[idx][field] = target.value;
          if (field === 'postoSelect') {
            renderPostos();
          }
          saveToStorage();
          updatePreview();
        });

        postosList.addEventListener('input', (e) => {
          const target = e.target;
          if (target.tagName === 'SELECT' || target.type === 'radio') return;
          const idx = Number(target.dataset.index);
          const field = target.dataset.field;
          if (Number.isNaN(idx) || !field || !state.postos[idx]) return;

          state.postos[idx][field] = target.value;
          saveToStorage();
          updatePreview();
        });

        postosList.addEventListener('click', (e) => {
          const btn = e.target.closest('[data-action="remove-posto"]');
          if (!btn) return;
          const idx = Number(btn.dataset.index);
          if (state.postos.length > 1) {
            state.postos.splice(idx, 1);
            renderPostos();
            saveToStorage();
            updatePreview();
            showToast('Posto removido do relatório.', 'info');
          }
        });

        document.getElementById('btn-add-posto').addEventListener('click', () => {
          state.postos.push(createEmptyPosto());
          renderPostos();
          saveToStorage();
          updatePreview();
        });

        // Seção 3: Itens Conferidos
        document.getElementById('itens-checklist').addEventListener('change', (e) => {
          const checkbox = e.target;
          const idx = Number(checkbox.dataset.itemIndex);
          if (Number.isNaN(idx)) return;
          const label = ITENS_CHECKLIST[idx];

          if (checkbox.checked) {
            if (!state.itensConferidos.includes(label)) {
              state.itensConferidos.push(label);
            }
          } else {
            state.itensConferidos = state.itensConferidos.filter((i) => i !== label);
          }

          renderItensChecklist();
          saveToStorage();
          updatePreview();
        });

        document.getElementById('btn-toggle-all-itens').addEventListener('click', () => {
          if (state.itensConferidos.length === ITENS_CHECKLIST.length) {
            state.itensConferidos = [];
          } else {
            state.itensConferidos = [...ITENS_CHECKLIST];
          }
          renderItensChecklist();
          saveToStorage();
          updatePreview();
        });

        document.getElementById('outros-itens').addEventListener('input', (e) => {
          state.outrosItens = e.target.value;
          saveToStorage();
          updatePreview();
        });

        // Seção 4: Pendências Dinâmicas
        const pendenciasList = document.getElementById('pendencias-list');

        pendenciasList.addEventListener('input', (e) => {
          const target = e.target;
          const idx = Number(target.dataset.index);
          const field = target.dataset.pendField;
          if (Number.isNaN(idx) || !field || !state.pendencias[idx]) return;

          state.pendencias[idx][field] = target.value;
          saveToStorage();
          updatePreview();
        });

        pendenciasList.addEventListener('change', (e) => {
          const target = e.target;
          const idx = Number(target.dataset.index);
          const field = target.dataset.pendField;
          if (Number.isNaN(idx) || !field || !state.pendencias[idx]) return;

          state.pendencias[idx][field] = target.value;
          saveToStorage();
          updatePreview();
        });

        pendenciasList.addEventListener('click', (e) => {
          const btn = e.target.closest('[data-action="remove-pendencia"]');
          if (!btn) return;
          const idx = Number(btn.dataset.index);
          state.pendencias.splice(idx, 1);
          renderPendencias();
          saveToStorage();
          updatePreview();
        });

        document.getElementById('btn-add-pendencia').addEventListener('click', () => {
          state.pendencias.push(createEmptyPendencia());
          renderPendencias();
          saveToStorage();
          updatePreview();
        });

        document.getElementById('obs-gerais').addEventListener('input', (e) => {
          state.obsGerais = e.target.value;
          saveToStorage();
          updatePreview();
        });

        // Seção 5: Oportunidades de Melhoria
        ['melhoria1', 'melhoria2', 'melhoria3', 'melhoria4'].forEach((key, idx) => {
          const el = document.getElementById(`melhoria-${idx + 1}`);
          el.addEventListener('input', (e) => {
            state[key] = e.target.value;
            saveToStorage();
            updatePreview();
          });
        });

        // Seção 6: Assinatura
        document.getElementById('assinatura-check').addEventListener('change', (e) => {
          state.assinaturaOk = e.target.checked;
          if (state.assinaturaOk) {
            document.getElementById('assinatura-erro').classList.add('hidden');
            document.getElementById('assinatura-box').classList.remove('border-redevia-red', 'bg-red-50');
          }
          saveToStorage();
        });

        // Botão Enviar WhatsApp
        document.getElementById('btn-enviar-wpp').addEventListener('click', () => {
          const numeroLimpo = state.diretorWpp.replace(/\D/g, '');

          // Validação do telefone do diretor
          if (numeroLimpo.length < 12) {
            showToast('Informe o WhatsApp do diretor com DDI e DDD (ex: 5531999999999).', 'error');
            const inputWpp = document.getElementById('cfg-diretor-wpp');
            inputWpp.scrollIntoView({ behavior: 'smooth', block: 'center' });
            inputWpp.focus();
            inputWpp.classList.add('ring-2', 'ring-redevia-red');
            return;
          }

          // Validação da declaração de assinatura
          if (!state.assinaturaOk) {
            const box = document.getElementById('assinatura-box');
            const erro = document.getElementById('assinatura-erro');
            erro.classList.remove('hidden');
            box.classList.add('border-redevia-red', 'bg-red-50');
            box.scrollIntoView({ behavior: 'smooth', block: 'center' });
            showToast('Marque a declaração de assinatura antes de enviar.', 'error');
            return;
          }

          const textoFinal = buildWhatsAppMessage();
          const urlWpp = `https://wa.me/${numeroLimpo}?text=${encodeURIComponent(textoFinal)}`;

          // Atualiza o fallback direto e abre o WhatsApp
          const fallbackDiv = document.getElementById('direct-link-fallback');
          const fallbackAnchor = document.getElementById('direct-wpp-anchor');
          fallbackAnchor.href = urlWpp;
          fallbackDiv.classList.remove('hidden');

          window.open(urlWpp, '_blank', 'noopener,noreferrer');
          showToast('Abrindo WhatsApp do diretor com o relatório pronto!', 'success');
        });

        // Botão Copiar Texto
        document.getElementById('btn-copy-text').addEventListener('click', () => {
          const textoFinal = buildWhatsAppMessage();
          const tempTextarea = document.createElement('textarea');
          tempTextarea.value = textoFinal;
          tempTextarea.style.position = 'fixed';
          tempTextarea.style.left = '-9999px';
          document.body.appendChild(tempTextarea);
          tempTextarea.select();
          tempTextarea.setSelectionRange(0, 99999);

          try {
            const ok = document.execCommand('copy');
            if (ok) {
              showToast('✓ Texto do relatório copiado para a área de transferência!', 'success');
            } else {
              showToast('Não foi possível copiar automaticamente. Selecione o texto na pré-visualização.', 'error');
            }
          } catch (err) {
            showToast('Erro ao copiar texto. Tente selecionar manualmente.', 'error');
          } finally {
            document.body.removeChild(tempTextarea);
          }
        });

        // Modal Limpar Campos do Dia
        const modal = document.getElementById('confirm-modal');
        document.getElementById('btn-clear-day').addEventListener('click', () => {
          modal.classList.remove('hidden');
          modal.classList.add('flex');
        });

        document.getElementById('btn-cancel-clear').addEventListener('click', () => {
          modal.classList.add('hidden');
          modal.classList.remove('flex');
        });

        document.getElementById('btn-confirm-clear').addEventListener('click', () => {
          state.dataRelatorio = getTodayISO();
          state.seguiuCronograma = 'Sim';
          state.motivoCronograma = '';
          state.postos = [createEmptyPosto()];
          state.itensConferidos = [];
          state.outrosItens = '';
          state.pendencias = [createEmptyPendencia()];
          state.obsGerais = '';
          state.melhoria1 = '';
          state.melhoria2 = '';
          state.melhoria3 = '';
          state.melhoria4 = '';
          state.assinaturaOk = false;

          document.getElementById('direct-link-fallback').classList.add('hidden');
          document.getElementById('assinatura-erro').classList.add('hidden');
          document.getElementById('assinatura-box').classList.remove('border-redevia-red', 'bg-red-50');

          saveToStorage();
          syncStaticInputsFromState();
          renderPostos();
          renderItensChecklist();
          renderPendencias();
          updatePreview();

          modal.classList.add('hidden');
          modal.classList.remove('flex');
          window.scrollTo({ top: 0, behavior: 'smooth' });
          showToast('Campos do dia limpos! Pronto para um novo relatório.', 'info');
        });
      }

      // --- INICIALIZAÇÃO ---
      loadPersistentSettings();
      syncStaticInputsFromState();
      renderPostos();
      renderItensChecklist();
      renderPendencias();
      updatePreview();
      bindEvents();
    })();
  </script>
</body>
</html>
