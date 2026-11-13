<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>Relatório Diário de Rotina – Rede Via</title>
  <style>
    /* ==========================================================================
       VARIÁVEIS DE DESIGN E PALETA INSTITUCIONAL REDE VIA
       ========================================================================== */
    :root {
      --rv-red: #C8102E;
      --rv-red-dark: #9E0B23;
      --rv-red-soft: #FDF2F4;
      --rv-red-border: #F5C2CA;
      --rv-gold: #EAAA00;
      --rv-gold-dark: #B47D00;
      --rv-gold-soft: #FFFBEB;
      --rv-gold-border: #FDE68A;

      --wpp-green: #25D366;
      --wpp-green-dark: #128C7E;
      --wpp-bubble: #DCF8C6;
      --wpp-wall: #EFEAE2;

      --bg-page: #F3F4F6;
      --bg-card: #FFFFFF;
      --bg-subtle: #F9FAFB;
      --text-main: #111827;
      --text-secondary: #4B5563;
      --text-muted: #6B7280;
      --border-color: #E5E7EB;
      --border-input: #D1D5DB;

      --radius-sm: 10px;
      --radius-md: 14px;
      --radius-lg: 18px;
      --shadow-sm: 0 1px 3px rgba(17, 24, 39, 0.06), 0 1px 2px rgba(17, 24, 39, 0.04);
      --shadow-md: 0 4px 12px rgba(17, 24, 39, 0.08);
      --shadow-wpp: 0 6px 18px rgba(37, 211, 102, 0.28);
    }

    /* ==========================================================================
       RESET E BASE MOBILE-FIRST
       ========================================================================== */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      -webkit-tap-highlight-color: transparent;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    body {
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.5;
      padding-bottom: 48px;
      overflow-x: hidden;
    }

    /* ==========================================================================
       CABEÇALHO INSTITUCIONAL
       ========================================================================== */
    .app-header {
      background: linear-gradient(135deg, var(--rv-red) 0%, var(--rv-red-dark) 100%);
      color: #FFFFFF;
      border-bottom: 5px solid var(--rv-gold);
      box-shadow: var(--shadow-md);
      padding: 20px 16px;
    }

    .header-inner {
      max-width: 760px;
      margin: 0 auto;
    }

    .header-top {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-logo {
      width: 50px;
      height: 50px;
      border-radius: 14px;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.24);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .brand-badge {
      display: inline-block;
      background-color: var(--rv-gold);
      color: #111827;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      padding: 2px 10px;
      border-radius: 999px;
      margin-bottom: 4px;
    }

    .app-header h1 {
      font-size: 1.25rem;
      font-weight: 800;
      line-height: 1.25;
      letter-spacing: -0.01em;
    }

    .app-subtitle {
      font-size: 0.85rem;
      color: #FEF3C7;
      font-weight: 500;
      margin-top: 2px;
    }

    .header-rules {
      margin-top: 14px;
      background: rgba(0, 0, 0, 0.22);
      border: 1px solid rgba(255, 255, 255, 0.16);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      font-size: 0.78rem;
      color: #F9FAFB;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .header-rules span strong {
      color: var(--rv-gold);
    }

    /* ==========================================================================
       CONTAINER PRINCIPAL E CARTÕES
       ========================================================================== */
    .container {
      max-width: 760px;
      margin: 0 auto;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
      padding: 18px 16px;
    }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding-bottom: 12px;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
    }

    .card-title-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .step-badge {
      width: 28px;
      height: 28px;
      border-radius: 8px;
      background-color: var(--rv-red);
      color: #FFFFFF;
      font-size: 0.85rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .step-badge.gold {
      background-color: var(--rv-gold);
      color: #111827;
    }

    .card-title {
      font-size: 1.02rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .card-desc {
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 2px;
    }

    /* ==========================================================================
       PAINEL COLAPSÁVEL DE CONFIGURAÇÃO RÁPIDA
       ========================================================================== */
    .config-card {
      border-left: 4px solid var(--rv-gold);
      padding: 0;
      overflow: hidden;
    }

    .config-summary {
      list-style: none;
      cursor: pointer;
      padding: 14px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      background-color: var(--bg-card);
      user-select: none;
    }

    .config-summary::-webkit-details-marker {
      display: none;
    }

    .config-status {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .pill-saved {
      font-size: 0.72rem;
      font-weight: 700;
      color: #065F46;
      background-color: #D1FAE5;
      border: 1px solid #A7F3D0;
      padding: 2px 9px;
      border-radius: 999px;
    }

    .pill-warning {
      font-size: 0.72rem;
      font-weight: 700;
      color: #991B1B;
      background-color: #FEE2E2;
      border: 1px solid #FECACA;
      padding: 2px 9px;
      border-radius: 999px;
    }

    .chevron-icon {
      width: 20px;
      height: 20px;
      color: var(--text-secondary);
      transition: transform 0.2s ease;
      flex-shrink: 0;
    }

    details[open] .chevron-icon {
      transform: rotate(180deg);
    }

    .config-body {
      padding: 0 16px 16px 16px;
      border-top: 1px solid var(--border-color);
      padding-top: 14px;
      background-color: var(--bg-subtle);
    }

    .config-actions-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-top: 12px;
      padding-top: 12px;
      border-top: 1px dashed var(--border-input);
    }

    /* ==========================================================================
       CAMPOS DE FORMULÁRIO E LAYOUT RESPONSIVO
       ========================================================================== */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }

    @media (min-width: 600px) {
      .app-header {
        padding: 24px 20px;
      }
      .app-header h1 {
        font-size: 1.45rem;
      }
      .header-rules {
        flex-direction: row;
        justify-content: space-between;
      }
      .card {
        padding: 22px 24px;
      }
      .grid-2 {
        grid-template-columns: 1fr 1fr;
      }
      .grid-3 {
        grid-template-columns: 1.2fr 1.2fr 0.9fr;
      }
    }

    .field-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    label.field-label, .field-label {
      font-size: 0.82rem;
      font-weight: 700;
      color: #374151;
    }

    .req {
      color: var(--rv-red);
    }

    .field-hint {
      font-size: 0.74rem;
      color: var(--text-muted);
    }

    input[type="text"],
    input[type="tel"],
    input[type="date"],
    select,
    textarea {
      width: 100%;
      min-height: 46px;
      padding: 10px 13px;
      font-family: inherit;
      font-size: 0.94rem;
      color: var(--text-main);
      background-color: #FFFFFF;
      border: 1.5px solid var(--border-input);
      border-radius: var(--radius-sm);
      transition: border-color 0.18s ease, box-shadow 0.18s ease;
    }

    textarea {
      min-height: 76px;
      resize: vertical;
      line-height: 1.45;
    }

    input:focus, select:focus, textarea:focus {
      outline: none;
      border-color: var(--rv-red);
      box-shadow: 0 0 0 3px rgba(200, 16, 46, 0.14);
    }

    input.input-error, select.input-error {
      border-color: var(--rv-red);
      background-color: var(--rv-red-soft);
    }

    /* ==========================================================================
       BOTÕES DE OPÇÃO EM PÍLULA (SIM / NÃO)
       ========================================================================== */
    .pill-group {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }

    .pill-option {
      position: relative;
      cursor: pointer;
      user-select: none;
    }

    .pill-option input {
      position: absolute;
      opacity: 0;
      width: 0;
      height: 0;
    }

    .pill-option span {
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 46px;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      border: 1.5px solid var(--border-input);
      background-color: #FFFFFF;
      color: var(--text-secondary);
      font-size: 0.9rem;
      font-weight: 700;
      transition: all 0.16s ease;
    }

    .pill-option input:checked + span {
      background-color: var(--rv-red);
      border-color: var(--rv-red);
      color: #FFFFFF;
      box-shadow: 0 2px 6px rgba(200, 16, 46, 0.25);
    }

    .pill-option.neutral input:checked + span {
      background-color: #1F2937;
      border-color: #1F2937;
      color: #FFFFFF;
      box-shadow: 0 2px 6px rgba(31, 41, 55, 0.22);
    }

    .pill-option.gold input:checked + span {
      background-color: var(--rv-gold-dark);
      border-color: var(--rv-gold-dark);
      color: #FFFFFF;
      box-shadow: 0 2px 6px rgba(180, 125, 0, 0.25);
    }

    /* ==========================================================================
       CAIXA CONDICIONAL MOTIVO CRONOGRAMA
       ========================================================================== */
    .conditional-box {
      margin-top: 14px;
      padding: 14px;
      border-radius: var(--radius-md);
      background-color: var(--rv-red-soft);
      border: 1.5px dashed var(--rv-red-border);
    }

    .hidden {
      display: none !important;
    }

    /* ==========================================================================
       SUB-CARTÕES DINÂMICOS (POSTOS E PENDÊNCIAS)
       ========================================================================== */
    .dynamic-list {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .sub-card {
      background-color: var(--bg-subtle);
      border: 1.5px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 15px;
      display: flex;
      flex-direction: column;
      gap: 13px;
      animation: slideIn 0.2s ease-out;
    }

    @keyframes slideIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .sub-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-color);
    }

    .sub-card-title {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.92rem;
      font-weight: 800;
      color: var(--text-main);
    }

    .mini-badge {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background-color: var(--rv-red);
      color: #FFFFFF;
      font-size: 0.78rem;
      font-weight: 800;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }

    .recolhimento-box {
      padding-top: 10px;
      border-top: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    @media (min-width: 600px) {
      .recolhimento-box {
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
      }
      .recolhimento-box .pill-group {
        width: 190px;
        flex-shrink: 0;
      }
    }

    .warning-note {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 0.75rem;
      font-weight: 700;
      color: #92400E;
      background-color: var(--rv-gold-soft);
      border: 1px solid var(--rv-gold-border);
      padding: 3px 8px;
      border-radius: 6px;
      margin-top: 2px;
    }

    /* ==========================================================================
       CHECKLIST DE ITENS (TOQUE GRANDE PARA CELULAR)
       ========================================================================== */
    .info-banner {
      background-color: var(--rv-gold-soft);
      border: 1px solid var(--rv-gold-border);
      color: #78350F;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 10px 12px;
      border-radius: var(--radius-sm);
      margin-bottom: 14px;
    }

    .guide-banner {
      background-color: var(--bg-subtle);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      font-size: 0.8rem;
      padding: 10px 12px;
      border-radius: var(--radius-sm);
      margin-bottom: 14px;
    }

    .guide-banner strong {
      color: var(--text-main);
    }

    .checklist-grid {
      display: flex;
      flex-direction: column;
      gap: 9px;
      margin-bottom: 14px;
    }

    .check-item {
      display: flex;
      align-items: center;
      gap: 12px;
      min-height: 50px;
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border: 1.5px solid var(--border-color);
      background-color: var(--bg-subtle);
      cursor: pointer;
      user-select: none;
      transition: all 0.15s ease;
    }

    .check-item:hover {
      background-color: #F3F4F6;
    }

    .check-item.checked {
      background-color: var(--rv-red-soft);
      border-color: var(--rv-red);
    }

    .check-item input[type="checkbox"] {
      width: 22px;
      height: 22px;
      accent-color: var(--rv-red);
      flex-shrink: 0;
      cursor: pointer;
    }

    .check-item span {
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.35;
    }

    /* ==========================================================================
       BOTÕES DE AÇÃO
       ========================================================================== */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      min-height: 48px;
      padding: 12px 18px;
      font-family: inherit;
      font-size: 0.92rem;
      font-weight: 700;
      border-radius: var(--radius-md);
      border: none;
      cursor: pointer;
      text-decoration: none;
      transition: transform 0.1s ease, background-color 0.18s ease, box-shadow 0.18s ease;
      user-select: none;
    }

    .btn:active {
      transform: scale(0.985);
    }

    .btn-add-red {
      width: 100%;
      margin-top: 12px;
      background-color: var(--rv-red-soft);
      color: var(--rv-red);
      border: 2px dashed rgba(200, 16, 46, 0.42);
    }

    .btn-add-red:hover {
      background-color: #FCE7EB;
    }

    .btn-add-neutral {
      width: 100%;
      margin-top: 12px;
      background-color: var(--bg-subtle);
      color: var(--text-main);
      border: 2px dashed var(--border-input);
    }

    .btn-add-neutral:hover {
      background-color: #F3F4F6;
    }

    .btn-remove {
      min-height: 34px;
      padding: 5px 11px;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--rv-red);
      background-color: #FEE2E2;
      border-radius: 8px;
      border: none;
      cursor: pointer;
    }

    .btn-remove:hover {
      background-color: #FECACA;
    }

    .btn-text-link {
      background: none;
      border: none;
      color: var(--rv-red);
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      padding: 4px 6px;
      text-decoration: underline;
    }

    .btn-clear-day {
      min-height: 40px;
      padding: 8px 14px;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--rv-red);
      background-color: #FFFFFF;
      border: 1.5px solid var(--rv-red-border);
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .btn-clear-day:hover {
      background-color: var(--rv-red-soft);
    }

    /* Botão Principal WhatsApp (Tag <a> estilizada) */
    .btn-whatsapp {
      width: 100%;
      min-height: 56px;
      padding: 14px 20px;
      background-color: var(--wpp-green);
      color: #FFFFFF;
      font-size: 1rem;
      font-weight: 800;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-wpp);
      text-align: center;
    }

    .btn-whatsapp:hover {
      background-color: var(--wpp-green-dark);
    }

    .btn-copy {
      width: 100%;
      margin-top: 10px;
      background-color: #FFFFFF;
      color: var(--text-main);
      border: 1.5px solid var(--border-input);
    }

    .btn-copy:hover {
      background-color: var(--bg-subtle);
    }

    .btn-copy.copied {
      background-color: #D1FAE5;
      border-color: #10B981;
      color: #065F46;
    }

    /* ==========================================================================
       ASSINATURA E PRÉ-VISUALIZAÇÃO WHATSAPP
       ========================================================================== */
    .declaration-box {
      padding: 14px;
      border-radius: var(--radius-md);
      border: 1.5px solid var(--border-input);
      background-color: var(--bg-subtle);
      margin-bottom: 18px;
      transition: all 0.2s ease;
    }

    .declaration-box.error {
      border-color: var(--rv-red);
      background-color: var(--rv-red-soft);
    }

    .declaration-label {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      cursor: pointer;
      user-select: none;
    }

    .declaration-label input[type="checkbox"] {
      width: 22px;
      height: 22px;
      margin-top: 2px;
      accent-color: var(--rv-red);
      flex-shrink: 0;
      cursor: pointer;
    }

    .declaration-label span {
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.4;
    }

    .error-msg {
      margin-top: 8px;
      padding-left: 34px;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--rv-red);
    }

    .preview-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }

    .preview-title {
      font-size: 0.76rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .dot-live {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: var(--wpp-green);
      display: inline-block;
    }

    .wpp-wall-container {
      background-color: var(--wpp-wall);
      border: 1px solid #D6D1C7;
      border-radius: var(--radius-md);
      padding: 14px;
      margin-bottom: 18px;
    }

    .wpp-bubble {
      background-color: var(--wpp-bubble);
      color: #111B21;
      border-radius: 12px;
      border-top-right-radius: 2px;
      padding: 12px 14px;
      font-size: 0.84rem;
      line-height: 1.48;
      white-space: pre-wrap;
      word-break: break-word;
      max-height: 310px;
      overflow-y: auto;
      box-shadow: 0 1px 1px rgba(0, 0, 0, 0.08);
    }

    /* ==========================================================================
       NOTIFICAÇÕES FLUTUANTES (TOAST) E MODAL DE CONFIRMAÇÃO
       ========================================================================== */
    .toast-stack {
      position: fixed;
      top: 14px;
      left: 50%;
      transform: translateX(-50%);
      width: 92%;
      max-width: 440px;
      z-index: 9999;
      display: flex;
      flex-direction: column;
      gap: 8px;
      pointer-events: none;
    }

    .toast {
      pointer-events: auto;
      padding: 12px 16px;
      border-radius: var(--radius-sm);
      font-size: 0.86rem;
      font-weight: 700;
      color: #FFFFFF;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.22);
      animation: slideIn 0.2s ease-out;
    }

    .toast.success { background-color: #065F46; border-left: 5px solid #34D399; }
    .toast.error   { background-color: #991B1B; border-left: 5px solid #FCA5A5; }
    .toast.info    { background-color: #1F2937; border-left: 5px solid var(--rv-gold); }

    .modal-backdrop {
      position: fixed;
      inset: 0;
      background-color: rgba(17, 24, 39, 0.58);
      z-index: 9998;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }

    .modal-backdrop.open {
      display: flex;
    }

    .modal-box {
      background-color: #FFFFFF;
      border-radius: var(--radius-lg);
      max-width: 400px;
      width: 100%;
      padding: 22px;
      box-shadow: 0 20px 35px rgba(0, 0, 0, 0.25);
      animation: slideIn 0.18s ease-out;
    }

    .modal-box h3 {
      font-size: 1.08rem;
      font-weight: 800;
      margin-bottom: 8px;
      color: var(--text-main);
    }

    .modal-box p {
      font-size: 0.88rem;
      color: var(--text-secondary);
      margin-bottom: 18px;
      line-height: 1.5;
    }

    .modal-actions {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }

    .btn-modal-cancel {
      background-color: #F3F4F6;
      color: var(--text-main);
      border: 1px solid var(--border-input);
    }

    .btn-modal-confirm {
      background-color: var(--rv-red);
      color: #FFFFFF;
    }
  </style>
</head>
<body>

  <!-- Pilha de Notificações Toast -->
  <div id="toast-stack" class="toast-stack" aria-live="polite"></div>

  <!-- Modal Customizado de Confirmação (substitui confirm() nativo) -->
  <div id="clear-modal" class="modal-backdrop" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <div class="modal-box">
      <h3 id="modal-title">Iniciar Novo Dia / Limpar Campos?</h3>
      <p>
        Todos os postos, itens conferidos, pendências e observações preenchidos hoje serão apagados.
        O <strong>WhatsApp do Diretor</strong> continuará salvo no aparelho.
      </p>
      <div class="modal-actions">
        <button type="button" id="btn-modal-cancel" class="btn btn-modal-cancel">Cancelar</button>
        <button type="button" id="btn-modal-confirm" class="btn btn-modal-confirm">Sim, limpar</button>
      </div>
    </div>
  </div>

  <!-- ========================================================================
       CABEÇALHO INSTITUCIONAL REDE VIA
       ======================================================================== -->
  <header class="app-header">
    <div class="header-inner">
      <div class="header-top">
        <div class="brand-logo" aria-hidden="true">
          <!-- Ícone Chama Rede Via em SVG Inline -->
          <svg width="30" height="30" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19.5 3C19.5 3 11 10.5 11 19.5C11 24.8 14.8 29.2 19.8 30C17.2 28.2 15.8 25.1 16.5 21.8C17.1 19.1 19.2 16.8 19.2 16.8C19.2 16.8 18.8 20.4 20.9 22.3C22.4 23.6 23.1 25.6 22.3 27.6C25.6 26.1 27.5 22.6 27.5 18.5C27.5 11.8 19.5 3 19.5 3Z" fill="#EAAA00"/>
            <path d="M18.5 2C12 8.2 8.5 14.5 8.5 20.5C8.5 27.4 13.8 33 20.5 33C26.5 33 31 28.3 31 22C31 15.2 24.5 7.5 18.5 2Z" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div>
          <span class="brand-badge">REDE VIA • ROTINA OPERACIONAL</span>
          <h1>Relatório Diário de Rotina – Rede Via</h1>
          <p class="app-subtitle">Coordenadores e Supervisores • Envio Direto WhatsApp</p>
        </div>
      </div>

      <div class="header-rules">
        <span><strong>●</strong> Enviar 1 relatório por dia até o fim do expediente.</span>
        <span><strong>●</strong> Em recolhimento, marcar apenas Sim ou Não (sem detalhes).</span>
      </div>
    </div>
  </header>

  <!-- ========================================================================
       CONTEÚDO PRINCIPAL
       ======================================================================== -->
  <main class="container">

    <!-- PAINEL COLAPSÁVEL: CONFIGURAÇÃO RÁPIDA -->
    <details id="config-details" class="card config-card" open>
      <summary class="config-summary">
        <div class="card-title-group">
          <span class="step-badge gold">⚙</span>
          <div>
            <div class="card-title">Configuração Rápida</div>
            <div class="card-desc">Número do WhatsApp do Diretor salvo automaticamente</div>
          </div>
        </div>
        <div class="config-status">
          <span id="wpp-status-pill" class="pill-warning">Número pendente</span>
          <svg class="chevron-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
          </svg>
        </div>
      </summary>

      <div class="config-body">
        <div class="field-group">
          <label class="field-label" for="input-diretor-wpp">
            WhatsApp do Diretor (com DDI 55 + DDD + número) <span class="req">*</span>
          </label>
          <input
            type="tel"
            id="input-diretor-wpp"
            inputmode="numeric"
            placeholder="Ex.: 5531999999999"
            autocomplete="tel"
          />
          <span class="field-hint">
            Digite apenas números com DDI e DDD (exemplo: <strong>5531999999999</strong>). Fica memorizado no aparelho.
          </span>
        </div>

        <div class="config-actions-row">
          <span id="draft-save-indicator" class="field-hint">✓ Rascunho salvo automaticamente no navegador</span>
          <button type="button" id="btn-open-clear-modal" class="btn-clear-day">
            <span>↻ Novo Dia / Limpar Campos</span>
          </button>
        </div>
      </div>
    </details>

    <!-- SEÇÃO 1 – IDENTIFICAÇÃO -->
    <section class="card">
      <div class="card-header">
        <div class="card-title-group">
          <span class="step-badge">1</span>
          <div>
            <h2 class="card-title">Identificação</h2>
            <p class="card-desc">Dados do coordenador/supervisor e cumprimento do cronograma</p>
          </div>
        </div>
      </div>

      <div class="grid-2">
        <div class="field-group">
          <label class="field-label" for="input-nome">Nome <span class="req">*</span></label>
          <input
            type="text"
            id="input-nome"
            value="Hitalo Gustavo Mendes Pinheiro"
            placeholder="Digite seu nome completo"
          />
        </div>

        <div class="field-group">
          <label class="field-label" for="input-data">Data</label>
          <input type="date" id="input-data" />
        </div>
      </div>

      <div class="field-group" style="margin-top: 14px;">
        <span class="field-label">Seguiu o cronograma da semana?</span>
        <div class="pill-group">
          <label class="pill-option">
            <input type="radio" name="seguiu-cronograma" value="Sim" checked />
            <span>Sim</span>
          </label>
          <label class="pill-option">
            <input type="radio" name="seguiu-cronograma" value="Não" />
            <span>Não</span>
          </label>
        </div>
      </div>

      <div id="motivo-cronograma-box" class="conditional-box hidden">
        <div class="field-group">
          <label class="field-label" for="input-motivo-cronograma">
            Se não seguiu ou mudou algo, explique o motivo:
          </label>
          <textarea
            id="input-motivo-cronograma"
            rows="2"
            placeholder="Descreva o motivo da alteração no cronograma da semana..."
          ></textarea>
        </div>
      </div>
    </section>

    <!-- SEÇÃO 2 – POSTOS VISITADOS E O QUE FOI FEITO -->
    <section class="card">
      <div class="card-header">
        <div class="card-title-group">
          <span class="step-badge">2</span>
          <div>
            <h2 class="card-title">Postos Visitados e O Que Foi Feito</h2>
            <p class="card-desc">Registre todos os postos visitados, inclusive fora do cronograma</p>
          </div>
        </div>
        <span id="postos-badge" class="pill-saved">1 posto</span>
      </div>

      <div id="postos-container" class="dynamic-list"></div>

      <button type="button" id="btn-add-posto" class="btn btn-add-red">
        <span>+ Adicionar Outro Posto</span>
      </button>
    </section>

    <!-- SEÇÃO 3 – ITENS CONFERIDOS NA VISITA -->
    <section class="card">
      <div class="card-header">
        <div class="card-title-group">
          <span class="step-badge">3</span>
          <div>
            <h2 class="card-title">Itens Conferidos na Visita</h2>
          </div>
        </div>
        <button type="button" id="btn-toggle-itens" class="btn-text-link">Marcar todos</button>
      </div>

      <div class="info-banner">
        Resumo para o dia a dia — não substitui o checklist bimestral
      </div>

      <div id="checklist-container" class="checklist-grid"></div>

      <div class="field-group">
        <label class="field-label" for="input-outros-itens">Outros itens conferidos (opcional)</label>
        <input
          type="text"
          id="input-outros-itens"
          placeholder="Descreva outros pontos verificados na visita..."
        />
      </div>
    </section>

    <!-- SEÇÃO 4 – PENDÊNCIAS E PRÓXIMOS PASSOS -->
    <section class="card">
      <div class="card-header">
        <div class="card-title-group">
          <span class="step-badge">4</span>
          <div>
            <h2 class="card-title">Pendências e Próximos Passos</h2>
            <p class="card-desc">Registre o que ficou pendente, o responsável e o prazo</p>
          </div>
        </div>
      </div>

      <!-- Autocomplete de unidades para o campo Posto das pendências -->
      <datalist id="lista-unidades-datalist"></datalist>

      <div id="pendencias-container" class="dynamic-list"></div>

      <button type="button" id="btn-add-pendencia" class="btn btn-add-neutral">
        <span>+ Adicionar Pendência</span>
      </button>

      <div class="field-group" style="margin-top: 16px; padding-top: 14px; border-top: 1px solid var(--border-color);">
        <label class="field-label" for="input-obs-gerais">Observações gerais do dia</label>
        <textarea
          id="input-obs-gerais"
          rows="3"
          placeholder="Anotações complementares sobre a rotina de hoje..."
        ></textarea>
      </div>
    </section>

    <!-- SEÇÃO 5 – OPORTUNIDADES DE MELHORIA -->
    <section class="card">
      <div class="card-header">
        <div class="card-title-group">
          <span class="step-badge">5</span>
          <div>
            <h2 class="card-title">Oportunidades de Melhoria</h2>
            <p class="card-desc">Seu olhar no posto ajuda a rede a evoluir. Não precisa ter a solução pronta.</p>
          </div>
        </div>
      </div>

      <div class="guide-banner">
        <strong>Áreas guia:</strong> Atendimento (fila, tempo de espera, cordialidade) ·
        Vendas e serviços (troca de óleo, lavagem, conveniência, aditivos) ·
        Equipe (escala, distribuição de tarefas, horários com pouco movimento) ·
        Operação e estrutura (bombas, estoque, pista, loja, banheiros).
      </div>

      <div class="dynamic-list">
        <div class="field-group">
          <label class="field-label" for="input-melhoria-1">1. O que você observou que pode melhorar</label>
          <textarea id="input-melhoria-1" rows="2" placeholder="Descreva o ponto de melhoria observado..."></textarea>
        </div>

        <div class="field-group">
          <label class="field-label" for="input-melhoria-2">2. O que deu certo e vale repetir</label>
          <textarea id="input-melhoria-2" rows="2" placeholder="Boa prática ou solução que pode ser levada para outros postos..."></textarea>
        </div>

        <div class="field-group">
          <label class="field-label" for="input-melhoria-3">3. Sua ideia para a rede</label>
          <textarea id="input-melhoria-3" rows="2" placeholder="Um serviço novo, ação com clientes ou melhoria na rotina..."></textarea>
        </div>

        <div class="field-group">
          <label class="field-label" for="input-melhoria-4">4. Precisa de apoio? (material, manutenção, treinamento, decisão)</label>
          <textarea id="input-melhoria-4" rows="2" placeholder="Algo que você ou o posto precisa do escritório..."></textarea>
        </div>
      </div>
    </section>

    <!-- SEÇÃO 6 – ASSINATURA E ENVIO DIRETO PARA WHATSAPP -->
    <section class="card">
      <div class="card-header">
        <div class="card-title-group">
          <span class="step-badge">6</span>
          <div>
            <h2 class="card-title">Assinatura e Envio Direto para WhatsApp</h2>
            <p class="card-desc">Revise a pré-visualização e envie com 1 toque para o diretor</p>
          </div>
        </div>
      </div>

      <!-- Declaração Obrigatória -->
      <div id="declaration-box" class="declaration-box">
        <label class="declaration-label" for="check-declaracao">
          <input type="checkbox" id="check-declaracao" />
          <span>Declaro que as informações acima correspondem às atividades realizadas no dia.</span>
        </label>
        <p id="declaration-error" class="error-msg hidden">
          ⚠️ Marque a declaração acima antes de enviar o relatório no WhatsApp.
        </p>
      </div>

      <!-- Pré-visualização em Tempo Real -->
      <div class="preview-header">
        <span class="preview-title">
          <span class="dot-live"></span>
          Pré-visualização do texto no WhatsApp
        </span>
        <span id="preview-char-count" class="field-hint">0 caracteres</span>
      </div>

      <div class="wpp-wall-container">
        <div id="wpp-preview-text" class="wpp-bubble"></div>
      </div>

      <!-- Botão Principal: Tag <a> estilizada atualizada em tempo real -->
      <a
        id="btn-whatsapp-link"
        href="https://wa.me/"
        target="_blank"
        rel="noopener noreferrer"
        class="btn btn-whatsapp"
      >
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824zm-3.423-14.416c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm.029 18.88c-1.161 0-2.305-.292-3.318-.844l-3.677.964.984-3.595c-.607-1.052-.927-2.246-.926-3.468.001-3.825 3.113-6.937 6.937-6.937 1.856.001 3.598.723 4.907 2.034 1.31 1.311 2.031 3.054 2.03 4.908-.001 3.825-3.113 6.938-6.937 6.938z"/>
        </svg>
        <span>Enviar Relatório no WhatsApp do Diretor</span>
      </a>

      <!-- Botão Secundário: Copiar Texto -->
      <button type="button" id="btn-copy-report" class="btn btn-copy">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true">
          <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
          <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
        </svg>
        <span id="btn-copy-label">Copiar Texto do Relatório</span>
      </button>
    </section>

  </main>

  <script>
    (function () {
      'use strict';

      /* ========================================================================
         CONSTANTES INSTITUCIONAIS
         ======================================================================== */
      var STORAGE_DIRETOR = 'redevia_diretor_whatsapp_v2';
      var STORAGE_DRAFT   = 'redevia_rotina_rascunho_v2';
      var DEFAULT_NAME    = 'Hitalo Gustavo Mendes Pinheiro';

      var UNIDADES_REDE_VIA = [
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
        'Palmeiras'
      ];

      var ITENS_CONFERENCIA = [
        'Pista e equipamentos (bombas, canaletas, vazamentos)',
        'Estoque de combustível (diferenças, sobras e faltas)',
        'Limpeza e conservação do posto como um todo (pátio, pista, banheiros, loja)',
        'Equipe (escala, uniformes, atendimento)',
        'Segurança e meio ambiente',
        'Conversa com o gerente'
      ];

      /* ========================================================================
         UTILITÁRIOS DE DATA E ESCAPE
         ======================================================================== */
      function getTodayISO() {
        var d = new Date();
        var year = d.getFullYear();
        var month = String(d.getMonth() + 1).padStart(2, '0');
        var day = String(d.getDate()).padStart(2, '0');
        return year + '-' + month + '-' + day;
      }

      function getTomorrowISO() {
        var d = new Date();
        d.setDate(d.getDate() + 1);
        var year = d.getFullYear();
        var month = String(d.getMonth() + 1).padStart(2, '0');
        var day = String(d.getDate()).padStart(2, '0');
        return year + '-' + month + '-' + day;
      }

      function formatISOToBR(isoStr) {
        if (!isoStr || isoStr.indexOf('-') === -1) return '__/__/____';
        var parts = isoStr.split('-');
        if (parts.length !== 3) return isoStr;
        return parts[2] + '/' + parts[1] + '/' + parts[0];
      }

      function escapeHTML(str) {
        return String(str == null ? '' : str)
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/"/g, '&quot;')
          .replace(/'/g, '&#039;');
      }

      function sanitizePhone(raw) {
        return String(raw || '').replace(/\D/g, '');
      }

      /* ========================================================================
         NOTIFICAÇÕES VISUAIS (TOAST)
         ======================================================================== */
      function showToast(text, type) {
        var stack = document.getElementById('toast-stack');
        if (!stack) return;
        var el = document.createElement('div');
        el.className = 'toast ' + (type || 'info');
        el.textContent = text;
        stack.appendChild(el);

        setTimeout(function () {
          el.style.opacity = '0';
          el.style.transition = 'opacity 0.25s ease';
          setTimeout(function () {
            if (el.parentNode) el.parentNode.removeChild(el);
          }, 260);
        }, 3400);
      }

      /* ========================================================================
         ESTADO CENTRAL DO FORMULÁRIO
         ======================================================================== */
      function newEmptyPosto() {
        return {
          uid: 'p_' + Date.now() + '_' + Math.floor(Math.random() * 100000),
          postoSelect: '',
          postoManual: '',
          noCronograma: 'Sim',
          motivo: '',
          conversa: '',
          verificou: '',
          resolveu: '',
          recolhimento: 'Não'
        };
      }

      function newEmptyPendencia() {
        return {
          uid: 'd_' + Date.now() + '_' + Math.floor(Math.random() * 100000),
          posto: '',
          responsavel: '',
          prazo: getTomorrowISO(),
          descricao: ''
        };
      }

      var state = {
        diretorWpp: '',
        nome: DEFAULT_NAME,
        data: getTodayISO(),
        seguiuCronograma: 'Sim',
        motivoCronograma: '',
        postos: [newEmptyPosto()],
        itensConferidos: [],
        outrosItens: '',
        pendencias: [newEmptyPendencia()],
        obsGerais: '',
        melhoria1: '',
        melhoria2: '',
        melhoria3: '',
        melhoria4: '',
        declaracaoOk: false
      };

      /* ========================================================================
         PERSISTÊNCIA SEGURA COM LOCALSTORAGE (TRY / CATCH)
         ======================================================================== */
      function loadFromStorage() {
        try {
          var savedPhone = localStorage.getItem(STORAGE_DIRETOR);
          if (savedPhone) {
            state.diretorWpp = savedPhone;
          }
        } catch (err) {
          // Navegador restrito ou iframe sem acesso ao localStorage
        }

        try {
          var rawDraft = localStorage.getItem(STORAGE_DRAFT);
          if (rawDraft) {
            var parsed = JSON.parse(rawDraft);
            if (parsed && typeof parsed === 'object') {
              state.nome = typeof parsed.nome === 'string' && parsed.nome.trim() !== '' ? parsed.nome : DEFAULT_NAME;
              state.data = parsed.data || getTodayISO();
              state.seguiuCronograma = parsed.seguiuCronograma === 'Não' ? 'Não' : 'Sim';
              state.motivoCronograma = parsed.motivoCronograma || '';
              state.postos = Array.isArray(parsed.postos) && parsed.postos.length > 0
                ? parsed.postos
                : [newEmptyPosto()];
              state.itensConferidos = Array.isArray(parsed.itensConferidos) ? parsed.itensConferidos : [];
              state.outrosItens = parsed.outrosItens || '';
              state.pendencias = Array.isArray(parsed.pendencias) ? parsed.pendencias : [newEmptyPendencia()];
              state.obsGerais = parsed.obsGerais || '';
              state.melhoria1 = parsed.melhoria1 || '';
              state.melhoria2 = parsed.melhoria2 || '';
              state.melhoria3 = parsed.melhoria3 || '';
              state.melhoria4 = parsed.melhoria4 || '';
              state.declaracaoOk = Boolean(parsed.declaracaoOk);
            }
          }
        } catch (err) {
          // Ignora falha de leitura do rascunho
        }
      }

      function saveToStorage() {
        try {
          localStorage.setItem(STORAGE_DIRETOR, state.diretorWpp);
        } catch (err) {
          // Ignora erro em ambiente restrito
        }

        try {
          var draftCopy = {
            nome: state.nome,
            data: state.data,
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
            declaracaoOk: state.declaracaoOk
          };
          localStorage.setItem(STORAGE_DRAFT, JSON.stringify(draftCopy));

          var indicator = document.getElementById('draft-save-indicator');
          if (indicator) {
            indicator.textContent = '✓ Salvo agora no aparelho';
            clearTimeout(indicator._timer);
            indicator._timer = setTimeout(function () {
              indicator.textContent = '✓ Rascunho salvo automaticamente no navegador';
            }, 1600);
          }
        } catch (err) {
          // Ignora erro em ambiente restrito
        }
      }

      /* ========================================================================
         GERAÇÃO DO TEXTO FORMATADO PARA WHATSAPP E ATUALIZAÇÃO DO LINK <a>
         ======================================================================== */
      function buildWhatsAppText() {
        var nomeFinal = state.nome.trim() || DEFAULT_NAME;
        var dataBR = formatISOToBR(state.data);
        var lines = [
          '*RELATÓRIO DIÁRIO DE ROTINA – REDE VIA*',
          '*Coordenador/Supervisor:* ' + nomeFinal,
          '*Data:* ' + dataBR,
          '*Seguiu cronograma:* ' + state.seguiuCronograma
        ];

        if (state.seguiuCronograma === 'Não' && state.motivoCronograma.trim()) {
          lines.push('*Motivo da alteração:* ' + state.motivoCronograma.trim());
        }

        lines.push('');
        lines.push('━━━━━━━━━━━━━━━━━━━━');
        lines.push('*POSTOS VISITADOS E ATIVIDADES*');

        state.postos.forEach(function (posto, idx) {
          var nomePosto = 'Não selecionado';
          if (posto.postoSelect === 'OUTRO') {
            nomePosto = posto.postoManual.trim() || 'Outro (não especificado)';
          } else if (posto.postoSelect) {
            nomePosto = posto.postoSelect;
          }

          lines.push('');
          lines.push('*Posto ' + (idx + 1) + ': ' + nomePosto + '* (No cronograma: ' + posto.noCronograma + ')');
          if (posto.motivo.trim()) {
            lines.push('• *Motivo:* ' + posto.motivo.trim());
          }
          if (posto.conversa.trim()) {
            lines.push('• *Conversou com:* ' + posto.conversa.trim());
          }
          if (posto.verificou.trim()) {
            lines.push('• *Verificou:* ' + posto.verificou.trim());
          }
          if (posto.resolveu.trim()) {
            lines.push('• *Resolveu:* ' + posto.resolveu.trim());
          }
          // Regra obrigatória: apenas Sim ou Não, sem detalhes
          lines.push('• *Recolhimento:* ' + (posto.recolhimento === 'Sim' ? 'Sim' : 'Não'));
        });

        lines.push('');
        lines.push('━━━━━━━━━━━━━━━━━━━━');
        lines.push('*ITENS CONFERIDOS NA VISITA*');
        if (state.itensConferidos.length > 0) {
          state.itensConferidos.forEach(function (item) {
            lines.push('✅ ' + item);
          });
        } else {
          lines.push('• Nenhum item marcado');
        }
        if (state.outrosItens.trim()) {
          lines.push('✅ Outros: ' + state.outrosItens.trim());
        }

        lines.push('');
        lines.push('━━━━━━━━━━━━━━━━━━━━');
        lines.push('*PENDÊNCIAS E PRÓXIMOS PASSOS*');

        var pendenciasValidas = state.pendencias.filter(function (p) {
          return p.posto.trim() || p.responsavel.trim() || p.descricao.trim();
        });

        if (pendenciasValidas.length > 0) {
          pendenciasValidas.forEach(function (pend, idx) {
            var pPosto = pend.posto.trim() || '-';
            var pResp = pend.responsavel.trim() || '-';
            var pPrazo = pend.prazo ? formatISOToBR(pend.prazo) : '-';
            lines.push('');
            lines.push('*Pendência ' + (idx + 1) + '* — Posto: ' + pPosto + ' | Resp.: ' + pResp + ' | Prazo: ' + pPrazo);
            if (pend.descricao.trim()) {
              lines.push('• ' + pend.descricao.trim());
            }
          });
        } else {
          lines.push('• Sem pendências registradas.');
        }

        if (state.obsGerais.trim()) {
          lines.push('');
          lines.push('*Observações gerais:* ' + state.obsGerais.trim());
        }

        var temMelhoria =
          state.melhoria1.trim() ||
          state.melhoria2.trim() ||
          state.melhoria3.trim() ||
          state.melhoria4.trim();

        if (temMelhoria) {
          lines.push('');
          lines.push('━━━━━━━━━━━━━━━━━━━━');
          lines.push('*OPORTUNIDADES DE MELHORIA*');
          if (state.melhoria1.trim()) {
            lines.push('• *Pode melhorar:* ' + state.melhoria1.trim());
          }
          if (state.melhoria2.trim()) {
            lines.push('• *Deu certo / repetir:* ' + state.melhoria2.trim());
          }
          if (state.melhoria3.trim()) {
            lines.push('• *Ideia para a rede:* ' + state.melhoria3.trim());
          }
          if (state.melhoria4.trim()) {
            lines.push('• *Apoio necessário:* ' + state.melhoria4.trim());
          }
        }

        lines.push('');
        lines.push('━━━━━━━━━━━━━━━━━━━━');
        lines.push('✍️ _Declaro que as informações acima correspondem às atividades realizadas no dia._');
        lines.push('_Assinado por: ' + nomeFinal + ' • ' + dataBR + '_');

        return lines.join('\n');
      }

      function updatePreviewAndWhatsAppHref() {
        var message = buildWhatsAppText();
        var previewEl = document.getElementById('wpp-preview-text');
        var countEl = document.getElementById('preview-char-count');
        var linkEl = document.getElementById('btn-whatsapp-link');
        var statusPill = document.getElementById('wpp-status-pill');

        if (previewEl) {
          previewEl.textContent = message;
        }
        if (countEl) {
          countEl.textContent = message.length + ' caracteres';
        }

        var cleanPhone = sanitizePhone(state.diretorWpp);
        if (statusPill) {
          if (cleanPhone.length >= 12) {
            statusPill.className = 'pill-saved';
            statusPill.textContent = '✓ Diretor: +' + cleanPhone;
          } else {
            statusPill.className = 'pill-warning';
            statusPill.textContent = 'Número pendente';
          }
        }

        if (linkEl) {
          var targetPhone = cleanPhone.length >= 10 ? cleanPhone : '';
          linkEl.href = 'https://wa.me/' + targetPhone + '?text=' + encodeURIComponent(message);
        }
      }

      /* ========================================================================
         RENDERIZAÇÃO DOS COMPONENTES DINÂMICOS
         ======================================================================== */
      function renderPostos() {
        var container = document.getElementById('postos-container');
        var badge = document.getElementById('postos-badge');
        if (!container) return;

        if (badge) {
          badge.textContent = state.postos.length === 1 ? '1 posto' : state.postos.length + ' postos';
        }

        var html = state.postos.map(function (posto, idx) {
          var optionsHtml = UNIDADES_REDE_VIA.map(function (u) {
            var selected = posto.postoSelect === u ? ' selected' : '';
            return '<option value="' + escapeHTML(u) + '"' + selected + '>' + escapeHTML(u) + '</option>';
          }).join('');

          var isOutro = posto.postoSelect === 'OUTRO';
          var removeBtnHtml = state.postos.length > 1
            ? '<button type="button" class="btn-remove" data-action="remove-posto" data-index="' + idx + '">Remover</button>'
            : '';

          return (
            '<div class="sub-card" data-posto-uid="' + posto.uid + '">' +
              '<div class="sub-card-header">' +
                '<div class="sub-card-title">' +
                  '<span class="mini-badge">' + (idx + 1) + '</span>' +
                  '<span>Posto Visitado #' + (idx + 1) + '</span>' +
                '</div>' +
                removeBtnHtml +
              '</div>' +

              '<div class="grid-2">' +
                '<div class="field-group">' +
                  '<label class="field-label">Posto (nome / bairro)</label>' +
                  '<select data-posto-field="postoSelect" data-index="' + idx + '">' +
                    '<option value="">Selecione o posto...</option>' +
                    optionsHtml +
                    '<option value="OUTRO"' + (isOutro ? ' selected' : '') + '>Outro (digitar manualmente)</option>' +
                  '</select>' +
                  '<div class="' + (isOutro ? '' : 'hidden') + '" style="margin-top: 6px;">' +
                    '<input type="text" data-posto-field="postoManual" data-index="' + idx + '" value="' + escapeHTML(posto.postoManual) + '" placeholder="Digite o nome/bairro do posto..." />' +
                  '</div>' +
                '</div>' +

                '<div class="field-group">' +
                  '<span class="field-label">Estava no cronograma?</span>' +
                  '<div class="pill-group">' +
                    '<label class="pill-option">' +
                      '<input type="radio" name="crono_' + posto.uid + '" value="Sim" data-posto-field="noCronograma" data-index="' + idx + '"' + (posto.noCronograma === 'Sim' ? ' checked' : '') + ' />' +
                      '<span>Sim</span>' +
                    '</label>' +
                    '<label class="pill-option">' +
                      '<input type="radio" name="crono_' + posto.uid + '" value="Não" data-posto-field="noCronograma" data-index="' + idx + '"' + (posto.noCronograma === 'Não' ? ' checked' : '') + ' />' +
                      '<span>Não</span>' +
                    '</label>' +
                  '</div>' +
                '</div>' +
              '</div>' +

              '<div class="grid-2">' +
                '<div class="field-group">' +
                  '<label class="field-label">Motivo da visita</label>' +
                  '<input type="text" data-posto-field="motivo" data-index="' + idx + '" value="' + escapeHTML(posto.motivo) + '" placeholder="Ex.: Rotina, vazamento, alinhamento..." />' +
                '</div>' +
                '<div class="field-group">' +
                  '<label class="field-label">Com quem conversou</label>' +
                  '<input type="text" data-posto-field="conversa" data-index="' + idx + '" value="' + escapeHTML(posto.conversa) + '" placeholder="Ex.: Gerente, Chefe de Pista..." />' +
                '</div>' +
              '</div>' +

              '<div class="grid-2">' +
                '<div class="field-group">' +
                  '<label class="field-label">O que verificou</label>' +
                  '<textarea rows="2" data-posto-field="verificou" data-index="' + idx + '" placeholder="Ex.: Verificou a pista e canaletas...">' + escapeHTML(posto.verificou) + '</textarea>' +
                '</div>' +
                '<div class="field-group">' +
                  '<label class="field-label">O que resolveu</label>' +
                  '<textarea rows="2" data-posto-field="resolveu" data-index="' + idx + '" placeholder="Ex.: Acionou limpeza e orientou equipe...">' + escapeHTML(posto.resolveu) + '</textarea>' +
                '</div>' +
              '</div>' +

              '<div class="recolhimento-box">' +
                '<div>' +
                  '<div class="field-label">Recolhimento?</div>' +
                  '<div class="warning-note">⚠️ Marque apenas Sim ou Não, sem detalhes</div>' +
                '</div>' +
                '<div class="pill-group">' +
                  '<label class="pill-option neutral">' +
                    '<input type="radio" name="recolh_' + posto.uid + '" value="Não" data-posto-field="recolhimento" data-index="' + idx + '"' + (posto.recolhimento !== 'Sim' ? ' checked' : '') + ' />' +
                    '<span>Não</span>' +
                  '</label>' +
                  '<label class="pill-option gold">' +
                    '<input type="radio" name="recolh_' + posto.uid + '" value="Sim" data-posto-field="recolhimento" data-index="' + idx + '"' + (posto.recolhimento === 'Sim' ? ' checked' : '') + ' />' +
                    '<span>Sim</span>' +
                  '</label>' +
                '</div>' +
              '</div>' +
            '</div>'
          );
        }).join('');

        container.innerHTML = html;
      }

      function renderChecklist() {
        var container = document.getElementById('checklist-container');
        var toggleBtn = document.getElementById('btn-toggle-itens');
        if (!container) return;

        container.innerHTML = ITENS_CONFERENCIA.map(function (item, idx) {
          var isChecked = state.itensConferidos.indexOf(item) !== -1;
          return (
            '<label class="check-item' + (isChecked ? ' checked' : '') + '">' +
              '<input type="checkbox" data-check-idx="' + idx + '"' + (isChecked ? ' checked' : '') + ' />' +
              '<span>' + escapeHTML(item) + '</span>' +
            '</label>'
          );
        }).join('');

        if (toggleBtn) {
          toggleBtn.textContent = state.itensConferidos.length === ITENS_CONFERENCIA.length
            ? 'Desmarcar todos'
            : 'Marcar todos';
        }
      }

      function renderPendencias() {
        var container = document.getElementById('pendencias-container');
        if (!container) return;

        if (state.pendencias.length === 0) {
          container.innerHTML =
            '<div class="field-hint" style="text-align:center; padding: 14px; border: 1.5px dashed var(--border-input); border-radius: 12px;">' +
              'Nenhuma pendência adicionada. Use o botão abaixo caso queira registrar alguma.' +
            '</div>';
          return;
        }

        container.innerHTML = state.pendencias.map(function (pend, idx) {
          return (
            '<div class="sub-card" data-pend-uid="' + pend.uid + '">' +
              '<div class="sub-card-header">' +
                '<div class="sub-card-title">' +
                  '<span class="mini-badge">' + (idx + 1) + '</span>' +
                  '<span>Pendência #' + (idx + 1) + '</span>' +
                '</div>' +
                '<button type="button" class="btn-remove" data-action="remove-pendencia" data-index="' + idx + '">Remover</button>' +
              '</div>' +

              '<div class="grid-3">' +
                '<div class="field-group">' +
                  '<label class="field-label">Posto</label>' +
                  '<input type="text" list="lista-unidades-datalist" data-pend-field="posto" data-index="' + idx + '" value="' + escapeHTML(pend.posto) + '" placeholder="Nome do posto" />' +
                '</div>' +
                '<div class="field-group">' +
                  '<label class="field-label">Responsável</label>' +
                  '<input type="text" data-pend-field="responsavel" data-index="' + idx + '" value="' + escapeHTML(pend.responsavel) + '" placeholder="Quem vai resolver" />' +
                '</div>' +
                '<div class="field-group">' +
                  '<label class="field-label">Prazo</label>' +
                  '<input type="date" data-pend-field="prazo" data-index="' + idx + '" value="' + escapeHTML(pend.prazo) + '" />' +
                '</div>' +
              '</div>' +

              '<div class="field-group">' +
                '<label class="field-label">O que ficou pendente</label>' +
                '<textarea rows="2" data-pend-field="descricao" data-index="' + idx + '" placeholder="Descreva o que ficou pendente e a próxima ação...">' + escapeHTML(pend.descricao) + '</textarea>' +
              '</div>' +
            '</div>'
          );
        }).join('');
      }

      function syncStaticFields() {
        document.getElementById('input-diretor-wpp').value = state.diretorWpp;
        document.getElementById('input-nome').value = state.nome;
        document.getElementById('input-data').value = state.data;

        var radios = document.querySelectorAll('input[name="seguiu-cronograma"]');
        for (var i = 0; i < radios.length; i++) {
          radios[i].checked = radios[i].value === state.seguiuCronograma;
        }

        var motivoBox = document.getElementById('motivo-cronograma-box');
        if (state.seguiuCronograma === 'Não') {
          motivoBox.classList.remove('hidden');
        } else {
          motivoBox.classList.add('hidden');
        }

        document.getElementById('input-motivo-cronograma').value = state.motivoCronograma;
        document.getElementById('input-outros-itens').value = state.outrosItens;
        document.getElementById('input-obs-gerais').value = state.obsGerais;
        document.getElementById('input-melhoria-1').value = state.melhoria1;
        document.getElementById('input-melhoria-2').value = state.melhoria2;
        document.getElementById('input-melhoria-3').value = state.melhoria3;
        document.getElementById('input-melhoria-4').value = state.melhoria4;
        document.getElementById('check-declaracao').checked = state.declaracaoOk;
      }

      /* ========================================================================
         EVENTOS E INTERATIVIDADE
         ======================================================================== */
      function bindAllEvents() {
        // Preenche datalist de unidades
        var datalist = document.getElementById('lista-unidades-datalist');
        if (datalist) {
          datalist.innerHTML = UNIDADES_REDE_VIA.map(function (u) {
            return '<option value="' + escapeHTML(u) + '"></option>';
          }).join('');
        }

        // Configuração Rápida: WhatsApp do Diretor
        var inputDiretor = document.getElementById('input-diretor-wpp');
        inputDiretor.addEventListener('input', function (e) {
          state.diretorWpp = e.target.value;
          inputDiretor.classList.remove('input-error');
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        // Seção 1: Identificação
        document.getElementById('input-nome').addEventListener('input', function (e) {
          state.nome = e.target.value;
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        document.getElementById('input-data').addEventListener('change', function (e) {
          state.data = e.target.value;
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        var cronoRadios = document.querySelectorAll('input[name="seguiu-cronograma"]');
        for (var i = 0; i < cronoRadios.length; i++) {
          cronoRadios[i].addEventListener('change', function (e) {
            state.seguiuCronograma = e.target.value;
            var box = document.getElementById('motivo-cronograma-box');
            if (state.seguiuCronograma === 'Não') {
              box.classList.remove('hidden');
            } else {
              box.classList.add('hidden');
            }
            saveToStorage();
            updatePreviewAndWhatsAppHref();
          });
        }

        document.getElementById('input-motivo-cronograma').addEventListener('input', function (e) {
          state.motivoCronograma = e.target.value;
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        // Seção 2: Postos Visitados (Delegação)
        var postosContainer = document.getElementById('postos-container');
        postosContainer.addEventListener('change', function (e) {
          var target = e.target;
          var field = target.getAttribute('data-posto-field');
          var idx = parseInt(target.getAttribute('data-index'), 10);
          if (!field || isNaN(idx) || !state.postos[idx]) return;

          state.postos[idx][field] = target.value;
          if (field === 'postoSelect') {
            renderPostos();
          }
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        postosContainer.addEventListener('input', function (e) {
          var target = e.target;
          if (target.tagName === 'SELECT' || target.type === 'radio') return;
          var field = target.getAttribute('data-posto-field');
          var idx = parseInt(target.getAttribute('data-index'), 10);
          if (!field || isNaN(idx) || !state.postos[idx]) return;

          state.postos[idx][field] = target.value;
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        postosContainer.addEventListener('click', function (e) {
          var btn = e.target.closest('[data-action="remove-posto"]');
          if (!btn) return;
          var idx = parseInt(btn.getAttribute('data-index'), 10);
          if (state.postos.length > 1 && !isNaN(idx)) {
            state.postos.splice(idx, 1);
            renderPostos();
            saveToStorage();
            updatePreviewAndWhatsAppHref();
            showToast('Posto removido do relatório.', 'info');
          }
        });

        document.getElementById('btn-add-posto').addEventListener('click', function () {
          state.postos.push(newEmptyPosto());
          renderPostos();
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        // Seção 3: Itens Conferidos
        document.getElementById('checklist-container').addEventListener('change', function (e) {
          var cb = e.target;
          var idx = parseInt(cb.getAttribute('data-check-idx'), 10);
          if (isNaN(idx)) return;
          var label = ITENS_CONFERENCIA[idx];

          if (cb.checked) {
            if (state.itensConferidos.indexOf(label) === -1) {
              state.itensConferidos.push(label);
            }
          } else {
            state.itensConferidos = state.itensConferidos.filter(function (item) {
              return item !== label;
            });
          }

          renderChecklist();
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        document.getElementById('btn-toggle-itens').addEventListener('click', function () {
          if (state.itensConferidos.length === ITENS_CONFERENCIA.length) {
            state.itensConferidos = [];
          } else {
            state.itensConferidos = ITENS_CONFERENCIA.slice();
          }
          renderChecklist();
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        document.getElementById('input-outros-itens').addEventListener('input', function (e) {
          state.outrosItens = e.target.value;
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        // Seção 4: Pendências (Delegação)
        var pendenciasContainer = document.getElementById('pendencias-container');
        pendenciasContainer.addEventListener('input', function (e) {
          var target = e.target;
          var field = target.getAttribute('data-pend-field');
          var idx = parseInt(target.getAttribute('data-index'), 10);
          if (!field || isNaN(idx) || !state.pendencias[idx]) return;

          state.pendencias[idx][field] = target.value;
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        pendenciasContainer.addEventListener('change', function (e) {
          var target = e.target;
          var field = target.getAttribute('data-pend-field');
          var idx = parseInt(target.getAttribute('data-index'), 10);
          if (!field || isNaN(idx) || !state.pendencias[idx]) return;

          state.pendencias[idx][field] = target.value;
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        pendenciasContainer.addEventListener('click', function (e) {
          var btn = e.target.closest('[data-action="remove-pendencia"]');
          if (!btn) return;
          var idx = parseInt(btn.getAttribute('data-index'), 10);
          if (!isNaN(idx)) {
            state.pendencias.splice(idx, 1);
            renderPendencias();
            saveToStorage();
            updatePreviewAndWhatsAppHref();
          }
        });

        document.getElementById('btn-add-pendencia').addEventListener('click', function () {
          state.pendencias.push(newEmptyPendencia());
          renderPendencias();
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        document.getElementById('input-obs-gerais').addEventListener('input', function (e) {
          state.obsGerais = e.target.value;
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        // Seção 5: Oportunidades de Melhoria
        ['melhoria1', 'melhoria2', 'melhoria3', 'melhoria4'].forEach(function (key, idx) {
          var el = document.getElementById('input-melhoria-' + (idx + 1));
          el.addEventListener('input', function (e) {
            state[key] = e.target.value;
            saveToStorage();
            updatePreviewAndWhatsAppHref();
          });
        });

        // Seção 6: Declaração Obrigatória
        var checkDeclaracao = document.getElementById('check-declaracao');
        checkDeclaracao.addEventListener('change', function (e) {
          state.declaracaoOk = e.target.checked;
          if (state.declaracaoOk) {
            document.getElementById('declaration-box').classList.remove('error');
            document.getElementById('declaration-error').classList.add('hidden');
          }
          saveToStorage();
          updatePreviewAndWhatsAppHref();
        });

        // Validação ao clicar no Link Direto WhatsApp (<a href="https://wa.me/...">)
        var wppLink = document.getElementById('btn-whatsapp-link');
        wppLink.addEventListener('click', function (e) {
          updatePreviewAndWhatsAppHref();

          var cleanPhone = sanitizePhone(state.diretorWpp);
          if (cleanPhone.length < 12) {
            e.preventDefault();
            var details = document.getElementById('config-details');
            if (details) details.open = true;
            inputDiretor.classList.add('input-error');
            inputDiretor.scrollIntoView({ behavior: 'smooth', block: 'center' });
            inputDiretor.focus();
            showToast('Informe o WhatsApp do Diretor com DDI 55 + DDD (ex: 5531999999999).', 'error');
            return;
          }

          if (!state.declaracaoOk) {
            e.preventDefault();
            var declBox = document.getElementById('declaration-box');
            var declErr = document.getElementById('declaration-error');
            declBox.classList.add('error');
            declErr.classList.remove('hidden');
            declBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
            showToast('Marque a declaração de assinatura antes de enviar.', 'error');
            return;
          }

          showToast('Abrindo WhatsApp do Diretor com o relatório pronto!', 'success');
        });

        // Botão Secundário: Copiar Texto do Relatório
        var copyBtn = document.getElementById('btn-copy-report');
        var copyLabel = document.getElementById('btn-copy-label');

        function markCopiedFeedback() {
          copyBtn.classList.add('copied');
          copyLabel.textContent = '✓ Copiado!';
          showToast('Texto do relatório copiado com sucesso!', 'success');
          clearTimeout(copyBtn._timer);
          copyBtn._timer = setTimeout(function () {
            copyBtn.classList.remove('copied');
            copyLabel.textContent = 'Copiar Texto do Relatório';
          }, 2400);
        }

        function fallbackExecCommandCopy(text) {
          var ta = document.createElement('textarea');
          ta.value = text;
          ta.setAttribute('readonly', '');
          ta.style.position = 'fixed';
          ta.style.left = '-9999px';
          ta.style.top = '0';
          document.body.appendChild(ta);
          ta.focus();
          ta.select();
          ta.setSelectionRange(0, 99999);
          var ok = false;
          try {
            ok = document.execCommand('copy');
          } catch (err) {
            ok = false;
          }
          document.body.removeChild(ta);
          return ok;
        }

        copyBtn.addEventListener('click', function () {
          var textToCopy = buildWhatsAppText();
          if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
            navigator.clipboard.writeText(textToCopy).then(
              function () {
                markCopiedFeedback();
              },
              function () {
                if (fallbackExecCommandCopy(textToCopy)) {
                  markCopiedFeedback();
                } else {
                  showToast('Não foi possível copiar automaticamente. Selecione o texto acima.', 'error');
                }
              }
            );
          } else if (fallbackExecCommandCopy(textToCopy)) {
            markCopiedFeedback();
          } else {
            showToast('Não foi possível copiar automaticamente. Selecione o texto acima.', 'error');
          }
        });

        // Modal: Novo Dia / Limpar Campos
        var modal = document.getElementById('clear-modal');
        document.getElementById('btn-open-clear-modal').addEventListener('click', function () {
          modal.classList.add('open');
        });

        document.getElementById('btn-modal-cancel').addEventListener('click', function () {
          modal.classList.remove('open');
        });

        modal.addEventListener('click', function (e) {
          if (e.target === modal) modal.classList.remove('open');
        });

        document.getElementById('btn-modal-confirm').addEventListener('click', function () {
          var keptPhone = state.diretorWpp;
          var keptName = state.nome.trim() || DEFAULT_NAME;

          state = {
            diretorWpp: keptPhone,
            nome: keptName,
            data: getTodayISO(),
            seguiuCronograma: 'Sim',
            motivoCronograma: '',
            postos: [newEmptyPosto()],
            itensConferidos: [],
            outrosItens: '',
            pendencias: [newEmptyPendencia()],
            obsGerais: '',
            melhoria1: '',
            melhoria2: '',
            melhoria3: '',
            melhoria4: '',
            declaracaoOk: false
          };

          document.getElementById('declaration-box').classList.remove('error');
          document.getElementById('declaration-error').classList.add('hidden');

          saveToStorage();
          syncStaticFields();
          renderPostos();
          renderChecklist();
          renderPendencias();
          updatePreviewAndWhatsAppHref();

          modal.classList.remove('open');
          window.scrollTo({ top: 0, behavior: 'smooth' });
          showToast('Campos limpos! Número do diretor mantido.', 'info');
        });
      }

      /* ========================================================================
         INICIALIZAÇÃO DO APP
         ======================================================================== */
      loadFromStorage();
      syncStaticFields();
      renderPostos();
      renderChecklist();
      renderPendencias();
      updatePreviewAndWhatsAppHref();
      bindAllEvents();
    })();
  </script>
</body>
</
