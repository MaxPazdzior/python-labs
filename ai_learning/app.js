  (() => {
    const taskData = window.AUFGABEN_DATA || {};
    const MODULES = taskData.MODULES || [];
    const QUESTION_BANK = taskData.QUESTION_BANK || [];
    const IDE_TASKS = taskData.IDE_TASKS || [];
    const DIFF_BADGE_STYLE = taskData.DIFF_BADGE_STYLE || {};
    'use strict';

    /* ========================================================================
     * 1. HILFSFUNKTIONEN: ESCAPING, PYTHON-SEMANTIK, HIGHLIGHTER, SHUFFLE
     * ======================================================================== */

    function escapeHtml(str) {
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }

    function fisherYates(arr) {
      const a = arr.slice();
      for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
      }
      return a;
    }

    function highlightPython(code, withLineNumbers = false) {
      const tokenRegex = /(#[^\n]*)|([fFrRbB]{1,2}(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|(\.)([a-zA-Z_]\w*)(?=\s*\()|\b(if|elif|else|while|for|in|break|continue|pass|return|import|from|as|try|except|finally|with|raise|yield)\b|\b(True|False|None|and|or|not|is|del|def|class|lambda|global|nonlocal)\b|\b(int|float|str|bool|list|dict|tuple|set|type)\b|\b(print|len|range|sum|min|max|sorted|round|abs|input|enumerate|zip|any|all|open|id|isinstance|ord|chr|bin|hex|oct)\b|\b(\d+(?:\.\d+)?)\b|\b([a-zA-Z_]\w*)\b/g;

      function highlightFString(rawStr) {
        const quoteIdx = rawStr.search(/["']/);
        const prefix = rawStr.slice(0, quoteIdx);
        const quote = rawStr[quoteIdx];
        const inner = rawStr.slice(quoteIdx + 1, rawStr.length - 1);
        let html = `<span class="py-kw-blue">${escapeHtml(prefix)}</span><span class="py-str">${escapeHtml(quote)}</span>`;
        let i = 0;
        let buf = '';

        const flushBuf = () => {
          if (buf) {
            html += `<span class="py-str">${escapeHtml(buf)}</span>`;
            buf = '';
          }
        };

        while (i < inner.length) {
          if (inner[i] === '{' && inner[i + 1] === '{') {
            buf += '{{';
            i += 2;
          } else if (inner[i] === '}' && inner[i + 1] === '}') {
            buf += '}}';
            i += 2;
          } else if (inner[i] === '{') {
            flushBuf();
            let depth = 1;
            let j = i + 1;
            while (j < inner.length && depth > 0) {
              if (inner[j] === '{') depth++;
              else if (inner[j] === '}') depth--;
              j++;
            }
            if (depth === 0) {
              const exprFull = inner.slice(i + 1, j - 1);
              let colonIdx = -1;
              let brDepth = 0;
              let inQ = null;
              for (let k = 0; k < exprFull.length; k++) {
                const ch = exprFull[k];
                if (inQ) {
                  if (ch === '\\') { k++; continue; }
                  if (ch === inQ) inQ = null;
                } else {
                  if (ch === '"' || ch === "'") inQ = ch;
                  else if (ch === '(' || ch === '[' || ch === '{') brDepth++;
                  else if (ch === ')' || ch === ']' || ch === '}') brDepth = Math.max(0, brDepth - 1);
                  else if (ch === ':' && brDepth === 0) { colonIdx = k; break; }
                }
              }
              const exprPart = colonIdx >= 0 ? exprFull.slice(0, colonIdx) : exprFull;
              const fmtPart = colonIdx >= 0 ? exprFull.slice(colonIdx) : '';
              html += `<span class="py-kw-blue">{</span>${highlightLine(exprPart)}${fmtPart ? `<span class="py-str">${escapeHtml(fmtPart)}</span>` : ''}<span class="py-kw-blue">}</span>`;
              i = j;
            } else {
              buf += inner.slice(i);
              break;
            }
          } else {
            buf += inner[i];
            i++;
          }
        }
        flushBuf();
        html += `<span class="py-str">${escapeHtml(quote)}</span>`;
        return html;
      }

      function highlightLine(line) {
        let result = '';
        let lastIndex = 0;
        const rx = new RegExp(tokenRegex.source, 'g');
        let match;
        while ((match = rx.exec(line)) !== null) {
          if (match.index > lastIndex) {
            result += `<span class="py-punct">${escapeHtml(line.slice(lastIndex, match.index))}</span>`;
          }
          if (match[1]) {
            result += `<span class="py-cm">${escapeHtml(match[1])}</span>`;
          } else if (match[2]) {
            const rawStr = match[2];
            if (/^[fF]/.test(rawStr) && rawStr.length >= 3) {
              result += highlightFString(rawStr);
            } else {
              result += `<span class="py-str">${escapeHtml(rawStr)}</span>`;
            }
          } else if (match[3] && match[4]) {
            result += `<span class="py-punct">.</span><span class="py-fn">${escapeHtml(match[4])}</span>`;
          } else if (match[5]) {
            result += `<span class="py-kw-ctrl">${escapeHtml(match[5])}</span>`;
          } else if (match[6]) {
            result += `<span class="py-kw-blue">${escapeHtml(match[6])}</span>`;
          } else if (match[7]) {
            result += `<span class="py-type">${escapeHtml(match[7])}</span>`;
          } else if (match[8]) {
            result += `<span class="py-fn">${escapeHtml(match[8])}</span>`;
          } else if (match[9]) {
            result += `<span class="py-num">${escapeHtml(match[9])}</span>`;
          } else if (match[10]) {
            result += `<span class="py-var">${escapeHtml(match[10])}</span>`;
          } else {
            result += escapeHtml(match[0]);
          }
          lastIndex = rx.lastIndex;
        }
        if (lastIndex < line.length) {
          result += `<span class="py-punct">${escapeHtml(line.slice(lastIndex))}</span>`;
        }
        return result;
      }

      const raw = String(code);
      const lines = raw.split('\n');
      if (!withLineNumbers) {
        return lines.map(highlightLine).join('\n') + (raw.endsWith('\n') ? ' ' : '');
      }
      return lines.map((line, idx) =>
        `<div class="flex"><span class="select-none text-[#9a9a9a] w-7 pr-3 text-right shrink-0">${idx + 1}</span><span class="flex-1">${highlightLine(line) || ' '}</span></div>`
      ).join('');
    }

    /* ========================================================================
     * 1B. VS CODE MINI-IDE CONTROLLER (AUTO-BRACKETS, INDENT, INTELLISENSE, RESIZE)
     * ======================================================================== */

    const PY_AUTOCOMPLETE_METHODS = [
      // List-Methoden
      { label: 'append', kind: 'list', isCallable: true, sig: 'list.append(obj)', params: ['obj'], doc: 'Hängt ein Element ans Ende der Liste an.' },
      { label: 'extend', kind: 'list', isCallable: true, sig: 'list.extend(iterable)', params: ['iterable'], doc: 'Hängt alle Elemente eines Iterables an die Liste an.' },
      { label: 'insert', kind: 'list', isCallable: true, sig: 'list.insert(index, obj)', params: ['index', 'obj'], doc: 'Fügt ein Element an der angegebenen Indexposition ein.' },
      { label: 'pop', kind: 'list / dict', isCallable: true, sig: 'pop([index / key, default])', params: ['index / key', 'default'], doc: 'Entfernt ein Element (Standard: letztes) und gibt es zurück.' },
      { label: 'remove', kind: 'list', isCallable: true, sig: 'list.remove(value)', params: ['value'], doc: 'Entfernt das erste Vorkommen von value aus der Liste.' },
      { label: 'sort', kind: 'list', isCallable: true, sig: 'list.sort(reverse=False)', params: ['reverse=False'], doc: 'Sortiert die Liste in-place aufsteigend (oder absteigend).' },
      { label: 'reverse', kind: 'list', isCallable: true, sig: 'list.reverse()', params: [], doc: 'Kehrt die Reihenfolge der Listenelemente in-place um.' },
      { label: 'index', kind: 'list / str', isCallable: true, sig: 'index(value, start=0)', params: ['value', 'start=0'], doc: 'Gibt den ersten Index von value zurück.' },
      { label: 'count', kind: 'list / str', isCallable: true, sig: 'count(value)', params: ['value'], doc: 'Zählt, wie oft value vorkommt.' },
      { label: 'copy', kind: 'list / dict', isCallable: true, sig: 'copy()', params: [], doc: 'Erzeugt eine flache Kopie (Shallow Copy).' },
      { label: 'clear', kind: 'list / dict', isCallable: true, sig: 'clear()', params: [], doc: 'Entfernt alle Elemente.' },
      // Dict-Methoden
      { label: 'keys', kind: 'dict', isCallable: true, sig: 'dict.keys()', params: [], doc: 'Gibt eine View aller Schlüssel (Keys) des Dictionaries zurück.' },
      { label: 'values', kind: 'dict', isCallable: true, sig: 'dict.values()', params: [], doc: 'Gibt eine View aller Werte (Values) des Dictionaries zurück.' },
      { label: 'items', kind: 'dict', isCallable: true, sig: 'dict.items()', params: [], doc: 'Gibt eine View aller (Key, Value)-Paare zurück.' },
      { label: 'get', kind: 'dict', isCallable: true, sig: 'dict.get(key, default=None)', params: ['key', 'default=None'], doc: 'Gibt den Wert zu key zurück oder default, ohne KeyError auszulösen.' },
      { label: 'update', kind: 'dict', isCallable: true, sig: 'dict.update(other)', params: ['other'], doc: 'Aktualisiert das Dictionary mit Schlüssel-Wert-Paaren aus other.' },
      { label: 'setdefault', kind: 'dict', isCallable: true, sig: 'dict.setdefault(key, default=None)', params: ['key', 'default=None'], doc: 'Gibt dict[key] zurück; setzt key auf default, falls noch nicht vorhanden.' },
      // String-Methoden
      { label: 'split', kind: 'str', isCallable: true, sig: 'str.split(sep=None, maxsplit=-1)', params: ['sep=None', 'maxsplit=-1'], doc: 'Zerlegt den String anhand von sep in eine Liste von Teilstrings.' },
      { label: 'join', kind: 'str', isCallable: true, sig: 'str.join(iterable)', params: ['iterable'], doc: 'Verbindet alle Strings eines Iterables mit dem Trennstring.' },
      { label: 'strip', kind: 'str', isCallable: true, sig: 'str.strip([chars])', params: ['chars'], doc: 'Entfernt führende und abschließende Leerzeichen (oder chars).' },
      { label: 'lstrip', kind: 'str', isCallable: true, sig: 'str.lstrip([chars])', params: ['chars'], doc: 'Entfernt führende Leerzeichen links.' },
      { label: 'rstrip', kind: 'str', isCallable: true, sig: 'str.rstrip([chars])', params: ['chars'], doc: 'Entfernt abschließende Leerzeichen rechts.' },
      { label: 'lower', kind: 'str', isCallable: true, sig: 'str.lower()', params: [], doc: 'Wandelt alle Buchstaben in Kleinbuchstaben um.' },
      { label: 'upper', kind: 'str', isCallable: true, sig: 'str.upper()', params: [], doc: 'Wandelt alle Buchstaben in Großbuchstaben um.' },
      { label: 'replace', kind: 'str', isCallable: true, sig: 'str.replace(old, new, count=-1)', params: ['old', 'new', 'count=-1'], doc: 'Ersetzt Vorkommen von old durch new.' },
      { label: 'find', kind: 'str', isCallable: true, sig: 'str.find(sub, start=0)', params: ['sub', 'start=0'], doc: 'Sucht sub im String und liefert den Index (oder -1).' },
      { label: 'startswith', kind: 'str', isCallable: true, sig: 'str.startswith(prefix)', params: ['prefix'], doc: 'Prüft, ob der String mit prefix beginnt (True/False).' },
      { label: 'endswith', kind: 'str', isCallable: true, sig: 'str.endswith(suffix)', params: ['suffix'], doc: 'Prüft, ob der String mit suffix endet (True/False).' },
      { label: 'isdigit', kind: 'str', isCallable: true, sig: 'str.isdigit()', params: [], doc: 'Gibt True zurück, wenn der String nur aus Ziffern besteht.' },
      { label: 'isalpha', kind: 'str', isCallable: true, sig: 'str.isalpha()', params: [], doc: 'Gibt True zurück, wenn der String nur aus Buchstaben besteht.' },
      // JSON-Modul
      { label: 'loads', kind: 'json', isCallable: true, sig: 'json.loads(s)', params: ['s'], doc: 'Parst einen JSON-String s in ein Python-Objekt (dict/list).' },
      { label: 'dumps', kind: 'json', isCallable: true, sig: 'json.dumps(obj, indent=None)', params: ['obj', 'indent=None'], doc: 'Serialisiert ein Python-Objekt in einen JSON-String.' }
    ];

    const PY_AUTOCOMPLETE_GLOBALS = [
      { label: 'print', kind: 'builtin', isCallable: true, sig: 'print(*values, sep=" ", end="\\n")', params: ['*values', 'sep=" "', 'end="\\n"'], doc: 'Gibt Werte auf der Standardausgabe aus.' },
      { label: 'len', kind: 'builtin', isCallable: true, sig: 'len(obj)', params: ['obj'], doc: 'Gibt die Anzahl der Elemente oder Zeichen zurück.' },
      { label: 'range', kind: 'builtin', isCallable: true, sig: 'range(start, stop[, step])', params: ['start', 'stop', 'step'], doc: 'Erzeugt eine Zahlenfolge von start (inkl.) bis stop (exkl.).' },
      { label: 'int', kind: 'type', isCallable: true, sig: 'int(x, base=10)', params: ['x', 'base=10'], doc: 'Wandelt x in eine Ganzzahl (Integer) um.' },
      { label: 'float', kind: 'type', isCallable: true, sig: 'float(x)', params: ['x'], doc: 'Wandelt x in eine Fließkommazahl um.' },
      { label: 'str', kind: 'type', isCallable: true, sig: 'str(obj)', params: ['obj'], doc: 'Wandelt obj in eine Zeichenkette (String) um.' },
      { label: 'bool', kind: 'type', isCallable: true, sig: 'bool(x)', params: ['x'], doc: 'Wertet x als Wahrheitswert (True oder False) aus.' },
      { label: 'list', kind: 'type', isCallable: true, sig: 'list([iterable])', params: ['iterable'], doc: 'Erzeugt eine neue Liste.' },
      { label: 'dict', kind: 'type', isCallable: true, sig: 'dict(**kwargs)', params: ['**kwargs'], doc: 'Erzeugt ein neues Dictionary.' },
      { label: 'type', kind: 'builtin', isCallable: true, sig: 'type(obj)', params: ['obj'], doc: 'Gibt den Datentyp von obj zurück.' },
      { label: 'isinstance', kind: 'builtin', isCallable: true, sig: 'isinstance(obj, classinfo)', params: ['obj', 'classinfo'], doc: 'Prüft, ob obj eine Instanz des angegebenen Typs ist.' },
      { label: 'sum', kind: 'builtin', isCallable: true, sig: 'sum(iterable, start=0)', params: ['iterable', 'start=0'], doc: 'Summiert alle Zahlen eines Iterables.' },
      { label: 'min', kind: 'builtin', isCallable: true, sig: 'min(iterable)', params: ['iterable'], doc: 'Gibt das kleinste Element zurück.' },
      { label: 'max', kind: 'builtin', isCallable: true, sig: 'max(iterable)', params: ['iterable'], doc: 'Gibt das größte Element zurück.' },
      { label: 'sorted', kind: 'builtin', isCallable: true, sig: 'sorted(iterable, reverse=False)', params: ['iterable', 'reverse=False'], doc: 'Gibt eine neu sortierte Liste zurück.' },
      { label: 'round', kind: 'builtin', isCallable: true, sig: 'round(number, ndigits=None)', params: ['number', 'ndigits=None'], doc: 'Rundet number (Round-Half-to-Even).' },
      { label: 'abs', kind: 'builtin', isCallable: true, sig: 'abs(x)', params: ['x'], doc: 'Gibt den Betrag einer Zahl zurück.' },
      { label: 'enumerate', kind: 'builtin', isCallable: true, sig: 'enumerate(iterable, start=0)', params: ['iterable', 'start=0'], doc: 'Liefert Paare aus (Index, Element).' },
      { label: 'zip', kind: 'builtin', isCallable: true, sig: 'zip(*iterables)', params: ['*iterables'], doc: 'Kombiniert mehrere Iterables elementweise zu Tupeln.' },
      { label: 'any', kind: 'builtin', isCallable: true, sig: 'any(iterable)', params: ['iterable'], doc: 'True, wenn mindestens ein Element wahr ist.' },
      { label: 'all', kind: 'builtin', isCallable: true, sig: 'all(iterable)', params: ['iterable'], doc: 'True, wenn alle Elemente wahr sind.' },
      { label: 'ord', kind: 'builtin', isCallable: true, sig: 'ord(c)', params: ['c'], doc: 'Gibt den Unicode-Codepoint eines einzelnen Zeichens zurück.' },
      { label: 'chr', kind: 'builtin', isCallable: true, sig: 'chr(i)', params: ['i'], doc: 'Gibt das Zeichen zum Unicode-Codepoint i zurück.' },
      { label: 'bin', kind: 'builtin', isCallable: true, sig: 'bin(x)', params: ['x'], doc: 'Gibt die Binärdarstellung einer Ganzzahl mit Präfix 0b zurück.' },
      { label: 'hex', kind: 'builtin', isCallable: true, sig: 'hex(x)', params: ['x'], doc: 'Gibt die Hexadezimaldarstellung einer Ganzzahl mit Präfix 0x zurück.' },
      { label: 'oct', kind: 'builtin', isCallable: true, sig: 'oct(x)', params: ['x'], doc: 'Gibt die Oktaldarstellung einer Ganzzahl mit Präfix 0o zurück.' },
      { label: 'if', kind: 'keyword', isCallable: false },
      { label: 'elif', kind: 'keyword', isCallable: false },
      { label: 'else', kind: 'keyword', isCallable: false },
      { label: 'while', kind: 'keyword', isCallable: false },
      { label: 'for', kind: 'keyword', isCallable: false },
      { label: 'in', kind: 'keyword', isCallable: false },
      { label: 'not', kind: 'keyword', isCallable: false },
      { label: 'and', kind: 'keyword', isCallable: false },
      { label: 'or', kind: 'keyword', isCallable: false },
      { label: 'is', kind: 'keyword', isCallable: false },
      { label: 'break', kind: 'keyword', isCallable: false },
      { label: 'continue', kind: 'keyword', isCallable: false },
      { label: 'pass', kind: 'keyword', isCallable: false },
      { label: 'def', kind: 'keyword', isCallable: false },
      { label: 'return', kind: 'keyword', isCallable: false },
      { label: 'True', kind: 'keyword', isCallable: false },
      { label: 'False', kind: 'keyword', isCallable: false },
      { label: 'None', kind: 'keyword', isCallable: false },
      { label: 'import', kind: 'keyword', isCallable: false },
      { label: 'from', kind: 'keyword', isCallable: false },
      { label: 'match', kind: 'keyword', isCallable: false },
      { label: 'case', kind: 'keyword', isCallable: false },
      { label: 'global', kind: 'keyword', isCallable: false }
    ];

    const SIGNATURE_MAP = new Map();
    for (const item of [...PY_AUTOCOMPLETE_METHODS, ...PY_AUTOCOMPLETE_GLOBALS]) {
      if (item.sig && !SIGNATURE_MAP.has(item.label)) {
        SIGNATURE_MAP.set(item.label, item);
      }
    }

    function isInsideStringOrComment(text, pos) {
      let inStr = null;
      let inComment = false;
      for (let i = 0; i < pos; i++) {
        const ch = text[i];
        if (inComment) {
          if (ch === '\n') inComment = false;
        } else if (inStr) {
          if (ch === '\\') {
            i++;
          } else if (ch === '\n') {
            inStr = null;
          } else if (ch === inStr) {
            inStr = null;
          }
        } else {
          if (ch === '#') {
            inComment = true;
          } else if (ch === '"' || ch === "'") {
            inStr = ch;
          }
        }
      }
      return Boolean(inStr || inComment);
    }

    function inferReceiverKind(code, receiverName) {
      if (!receiverName) return null;
      if (receiverName === 'json') return 'json';
      const esc = receiverName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const assignRx = new RegExp(`\\b${esc}\\s*=\\s*([^\\n#]+)`);
      const m = code.match(assignRx);
      if (!m) return null;
      const rhs = m[1].trim();
      if (rhs.startsWith('[')) return 'list';
      if (rhs.startsWith('{') || rhs.startsWith('json.loads')) return 'dict';
      if (rhs.startsWith('"') || rhs.startsWith("'") || rhs.startsWith('f"') || rhs.startsWith("f'")) return 'str';
      return null;
    }

    function extractBufferIdentifiers(code) {
      const ids = new Set();
      const rx = /\b([a-zA-Z_]\w*)\b/g;
      let m;
      while ((m = rx.exec(code)) !== null) {
        if (m[1].length >= 2) ids.add(m[1]);
      }
      return Array.from(ids);
    }

    function attachVscodeEditor({ textarea, highlightEl, gutterEl, cursorPosEl, mirrorEl, acEl, sigEl, bodyEl, resizeHandleEl, defaultHeight, onResize, onChange, onRun }) {
      const PAIRS = { '(': ')', '[': ']', '{': '}', '"': '"', "'": "'" };
      const CLOSERS = new Set([')', ']', '}', '"', "'"]);
      let acItems = [];
      let acIndex = 0;
      let acReplaceStart = 0;

      function hideAutocomplete() {
        acItems = [];
        acIndex = 0;
        if (acEl) acEl.classList.add('hidden');
      }

      function hideSigHelp() {
        if (sigEl) sigEl.classList.add('hidden');
      }

      function getCaretCoords() {
        if (!mirrorEl) return { left: 24, top: 28 };
        const pos = textarea.selectionStart || 0;
        const val = textarea.value;
        mirrorEl.innerHTML = escapeHtml(val.slice(0, pos)) + '<span id="__caret_span">|</span>';
        const span = mirrorEl.querySelector('#__caret_span');
        if (!span) return { left: 24, top: 28 };
        const left = Math.max(8, Math.min(textarea.clientWidth - 260, span.offsetLeft - textarea.scrollLeft));
        const top = Math.max(8, span.offsetTop - textarea.scrollTop);
        return { left, top };
      }

      function renderAutocompletePopup() {
        if (!acEl || acItems.length === 0) {
          hideAutocomplete();
          return;
        }
        const { left, top } = getCaretCoords();
        const showAbove = top > textarea.clientHeight - 170;
        acEl.style.left = `${left}px`;
        acEl.style.top = showAbove ? `${Math.max(6, top - Math.min(210, acItems.length * 28 + 8))}px` : `${top + 24}px`;

        acEl.innerHTML = acItems.map((item, idx) => `
          <div class="vscode-ac-item ${idx === acIndex ? 'active' : ''}" data-ac-idx="${idx}" role="option" aria-selected="${idx === acIndex}">
            <span class="truncate font-medium">${escapeHtml(item.label)}${item.isCallable ? '()' : ''}</span>
            <span class="vscode-ac-badge">${escapeHtml(item.kind)}</span>
          </div>
        `).join('');
        acEl.classList.remove('hidden');

        const activeRow = acEl.querySelector('.vscode-ac-item.active');
        if (activeRow) activeRow.scrollIntoView({ block: 'nearest' });

        acEl.querySelectorAll('.vscode-ac-item').forEach(row => {
          row.addEventListener('mousedown', e => {
            e.preventDefault();
            acIndex = Number(row.dataset.acIdx);
            acceptAutocomplete();
          });
        });
      }

      function acceptAutocomplete() {
        if (acItems.length === 0) return false;
        const chosen = acItems[acIndex];
        const pos = textarea.selectionStart || 0;
        const val = textarea.value;
        const insertText = chosen.isCallable ? `${chosen.label}()` : chosen.label;
        const newPos = chosen.isCallable ? acReplaceStart + chosen.label.length + 1 : acReplaceStart + chosen.label.length;

        textarea.value = val.slice(0, acReplaceStart) + insertText + val.slice(pos);
        textarea.selectionStart = textarea.selectionEnd = newPos;
        hideAutocomplete();
        sync();
        if (onChange) onChange();
        updateSignatureHelp();
        return true;
      }

      function updateAutocomplete() {
        if (!acEl) return;
        const pos = textarea.selectionStart || 0;
        if (pos !== textarea.selectionEnd) {
          hideAutocomplete();
          return;
        }
        const val = textarea.value;
        if (isInsideStringOrComment(val, pos)) {
          hideAutocomplete();
          return;
        }

        const before = val.slice(0, pos);
        const dotMatch = before.match(/([a-zA-Z_]\w*)\s*\.\s*([a-zA-Z_]\w*)?$/);
        if (dotMatch) {
          const receiver = dotMatch[1];
          const prefix = (dotMatch[2] || '').toLowerCase();
          acReplaceStart = pos - (dotMatch[2] ? dotMatch[2].length : 0);
          const inferred = inferReceiverKind(val, receiver);
          let pool = PY_AUTOCOMPLETE_METHODS.filter(m => m.label.toLowerCase().startsWith(prefix));
          if (inferred) {
            pool.sort((a, b) => {
              const aMatch = a.kind.includes(inferred) ? 0 : 1;
              const bMatch = b.kind.includes(inferred) ? 0 : 1;
              return aMatch - bMatch || a.label.localeCompare(b.label);
            });
          }
          acItems = pool.slice(0, 12);
          acIndex = 0;
          renderAutocompletePopup();
          return;
        }

        const wordMatch = before.match(/(?:^|[^a-zA-Z0-9_.])([a-zA-Z_]\w{1,})$/);
        if (wordMatch) {
          const typed = wordMatch[1];
          const lower = typed.toLowerCase();
          acReplaceStart = pos - typed.length;

          const baseLabels = new Set(PY_AUTOCOMPLETE_GLOBALS.map(g => g.label));
          const localVars = extractBufferIdentifiers(val)
            .filter(id => id !== typed && !baseLabels.has(id) && id.toLowerCase().startsWith(lower))
            .map(id => ({ label: id, kind: 'variable', isCallable: false }));

          const matches = [
            ...PY_AUTOCOMPLETE_GLOBALS.filter(g => g.label.toLowerCase().startsWith(lower) && g.label !== typed),
            ...localVars
          ];
          acItems = matches.slice(0, 12);
          acIndex = 0;
          renderAutocompletePopup();
          return;
        }

        hideAutocomplete();
      }

      function updateSignatureHelp() {
        if (!sigEl) return;
        const pos = textarea.selectionStart || 0;
        const val = textarea.value;
        if (isInsideStringOrComment(val, pos)) {
          hideSigHelp();
          return;
        }

        let depth = 0;
        let commaCount = 0;
        let openParenIdx = -1;
        let inQ = null;

        for (let i = pos - 1; i >= 0; i--) {
          const ch = val[i];
          if (inQ) {
            if (ch === inQ && val[i - 1] !== '\\') inQ = null;
            continue;
          }
          if (ch === '"' || ch === "'") {
            inQ = ch;
            continue;
          }
          if (ch === ')' || ch === ']' || ch === '}') {
            depth++;
          } else if (ch === '(' || ch === '[' || ch === '{') {
            if (depth === 0) {
              if (ch === '(') {
                openParenIdx = i;
              }
              break;
            }
            depth--;
          } else if (ch === ',' && depth === 0) {
            commaCount++;
          } else if (ch === '\n' && depth === 0) {
            break;
          }
        }

        if (openParenIdx <= 0) {
          hideSigHelp();
          return;
        }

        const beforeParen = val.slice(0, openParenIdx).trimEnd();
        const fnMatch = beforeParen.match(/([a-zA-Z_]\w*)$/);
        if (!fnMatch) {
          hideSigHelp();
          return;
        }

        const fnName = fnMatch[1];
        const info = SIGNATURE_MAP.get(fnName);
        if (!info) {
          hideSigHelp();
          return;
        }

        const { left, top } = getCaretCoords();
        const showBelow = top < 68;
        sigEl.style.left = `${left}px`;
        sigEl.style.top = showBelow ? `${top + 26}px` : `${Math.max(4, top - 56)}px`;

        let sigHtml = escapeHtml(info.sig);
        if (Array.isArray(info.params) && info.params.length > 0) {
          const activeParam = info.params[Math.min(commaCount, info.params.length - 1)];
          const escapedParam = escapeHtml(activeParam);
          sigHtml = sigHtml.replace(escapedParam, `<span class="text-[#4fc1ff] font-bold underline">${escapedParam}</span>`);
        }

        sigEl.innerHTML = `
          <div class="font-mono text-zinc-100 font-medium">${sigHtml}</div>
          <div class="text-[11px] text-zinc-400 mt-0.5">${escapeHtml(info.doc)}</div>
        `;
        sigEl.classList.remove('hidden');
      }

      function sync() {
        const val = textarea.value;
        if (highlightEl) {
          highlightEl.innerHTML = highlightPython(val, false);
          highlightEl.scrollTop = textarea.scrollTop;
          highlightEl.scrollLeft = textarea.scrollLeft;
        }
        if (gutterEl) {
          const lineCount = Math.max(1, val.split('\n').length);
          let nums = '';
          for (let i = 1; i <= lineCount; i++) nums += (i > 1 ? '\n' : '') + i;
          gutterEl.textContent = nums;
          gutterEl.scrollTop = textarea.scrollTop;
        }
        if (cursorPosEl) {
          const pos = textarea.selectionStart || 0;
          const before = val.slice(0, pos);
          const lines = before.split('\n');
          cursorPosEl.textContent = `Zeile ${lines.length}, Spalte ${lines[lines.length - 1].length + 1}`;
        }
      }

      textarea.addEventListener('input', () => {
        sync();
        if (onChange) onChange();
        updateAutocomplete();
        updateSignatureHelp();
      });

      textarea.addEventListener('scroll', () => {
        sync();
        hideAutocomplete();
        hideSigHelp();
      });

      textarea.addEventListener('click', () => {
        sync();
        hideAutocomplete();
        updateSignatureHelp();
      });

      textarea.addEventListener('blur', () => {
        setTimeout(() => {
          hideAutocomplete();
          hideSigHelp();
        }, 120);
      });

      textarea.addEventListener('keydown', e => {
        const start = textarea.selectionStart || 0;
        const end = textarea.selectionEnd || 0;
        const val = textarea.value;

        if (acEl && !acEl.classList.contains('hidden') && acItems.length > 0) {
          if (e.key === 'ArrowDown') {
            e.preventDefault();
            acIndex = (acIndex + 1) % acItems.length;
            renderAutocompletePopup();
            return;
          }
          if (e.key === 'ArrowUp') {
            e.preventDefault();
            acIndex = (acIndex - 1 + acItems.length) % acItems.length;
            renderAutocompletePopup();
            return;
          }
          if (e.key === 'Tab' || (e.key === 'Enter' && !(e.ctrlKey || e.metaKey))) {
            e.preventDefault();
            acceptAutocomplete();
            return;
          }
          if (e.key === 'Escape') {
            e.preventDefault();
            hideAutocomplete();
            return;
          }
        }

        if (e.key === 'Escape') {
          hideSigHelp();
          hideAutocomplete();
          return;
        }

        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
          e.preventDefault();
          hideAutocomplete();
          hideSigHelp();
          if (onRun) onRun();
          return;
        }

        if (e.key === 'Tab') {
          e.preventDefault();
          if (e.shiftKey) {
            const lineStart = val.lastIndexOf('\n', start - 1) + 1;
            const linePrefix = val.slice(lineStart, lineStart + 4);
            const matchSpaces = linePrefix.match(/^ {1,4}/);
            if (matchSpaces) {
              const removeLen = matchSpaces[0].length;
              textarea.value = val.slice(0, lineStart) + val.slice(lineStart + removeLen);
              textarea.selectionStart = Math.max(lineStart, start - removeLen);
              textarea.selectionEnd = Math.max(lineStart, end - removeLen);
              sync();
              if (onChange) onChange();
            }
          } else {
            textarea.value = val.slice(0, start) + '    ' + val.slice(end);
            textarea.selectionStart = textarea.selectionEnd = start + 4;
            sync();
            if (onChange) onChange();
          }
          return;
        }

        if (start === end && CLOSERS.has(e.key) && val[start] === e.key && val[start - 1] !== '\\') {
          e.preventDefault();
          textarea.selectionStart = textarea.selectionEnd = start + 1;
          sync();
          updateSignatureHelp();
          return;
        }

        if (Object.prototype.hasOwnProperty.call(PAIRS, e.key) && !e.ctrlKey && !e.metaKey && !e.altKey) {
          const openCh = e.key;
          const closeCh = PAIRS[openCh];
          const nextCh = val[start] || '';
          const prevCh = val[start - 1] || '';

          if (start !== end) {
            e.preventDefault();
            const selected = val.slice(start, end);
            textarea.value = val.slice(0, start) + openCh + selected + closeCh + val.slice(end);
            textarea.selectionStart = start + 1;
            textarea.selectionEnd = end + 1;
            sync();
            if (onChange) onChange();
            return;
          }

          const isQuote = openCh === '"' || openCh === "'";
          const validNext = nextCh === '' || /[\s)\]\},:;]/.test(nextCh);
          const validQuotePrev = !isQuote || prevCh === '' || /[\s(\[\{,:;=fFrRbBuU]/.test(prevCh);

          if (validNext && validQuotePrev && prevCh !== '\\') {
            e.preventDefault();
            textarea.value = val.slice(0, start) + openCh + closeCh + val.slice(end);
            textarea.selectionStart = textarea.selectionEnd = start + 1;
            sync();
            if (onChange) onChange();
            if (openCh === '(') updateSignatureHelp();
            return;
          }
        }

        if (e.key === 'Backspace' && start === end && start > 0) {
          const prevCh = val[start - 1];
          const nextCh = val[start];
          if (PAIRS[prevCh] && PAIRS[prevCh] === nextCh) {
            e.preventDefault();
            textarea.value = val.slice(0, start - 1) + val.slice(start + 1);
            textarea.selectionStart = textarea.selectionEnd = start - 1;
            sync();
            if (onChange) onChange();
            hideAutocomplete();
            updateSignatureHelp();
            return;
          }
        }

        if (e.key === 'Enter') {
          e.preventDefault();
          hideAutocomplete();
          const lineStart = val.lastIndexOf('\n', start - 1) + 1;
          const currentLineBeforeCursor = val.slice(lineStart, start);
          const indentMatch = currentLineBeforeCursor.match(/^[ \t]*/);
          let indent = indentMatch ? indentMatch[0] : '';

          const codeWithoutComment = currentLineBeforeCursor.replace(/#.*$/, '').trimEnd();
          const prevCh = val[start - 1] || '';
          const nextCh = val[start] || '';

          if ((prevCh === '{' && nextCh === '}') || (prevCh === '[' && nextCh === ']') || (prevCh === '(' && nextCh === ')')) {
            const innerIndent = indent + '    ';
            const insertion = '\n' + innerIndent + '\n' + indent;
            textarea.value = val.slice(0, start) + insertion + val.slice(end);
            textarea.selectionStart = textarea.selectionEnd = start + 1 + innerIndent.length;
          } else {
            if (codeWithoutComment.endsWith(':')) {
              indent += '    ';
            }
            const insertion = '\n' + indent;
            textarea.value = val.slice(0, start) + insertion + val.slice(end);
            textarea.selectionStart = textarea.selectionEnd = start + insertion.length;
          }
          sync();
          if (onChange) onChange();
          updateSignatureHelp();
          return;
        }
      });

      // Vertikales Ziehen zum Vergroessern/Verkleinern des Editor-Fensters (Maus & Touch)
      if (bodyEl && resizeHandleEl) {
        let isResizing = false;
        let startY = 0;
        let startHeight = 0;

        const applyHeight = newH => {
          const clamped = Math.max(180, Math.min(820, Math.round(newH)));
          bodyEl.style.height = `${clamped}px`;
          sync();
          hideAutocomplete();
          hideSigHelp();
          if (onResize) onResize(clamped);
        };

        const onPointerMove = clientY => {
          if (!isResizing) return;
          applyHeight(startHeight + (clientY - startY));
        };

        const onMouseMove = e => onPointerMove(e.clientY);
        const onTouchMove = e => {
          if (e.touches && e.touches.length > 0) onPointerMove(e.touches[0].clientY);
        };

        const stopResize = () => {
          if (!isResizing) return;
          isResizing = false;
          document.body.style.cursor = '';
          document.body.style.userSelect = '';
          window.removeEventListener('mousemove', onMouseMove);
          window.removeEventListener('mouseup', stopResize);
          window.removeEventListener('touchmove', onTouchMove);
          window.removeEventListener('touchend', stopResize);
        };

        resizeHandleEl.addEventListener('mousedown', e => {
          e.preventDefault();
          isResizing = true;
          startY = e.clientY;
          startHeight = bodyEl.getBoundingClientRect().height;
          document.body.style.cursor = 'ns-resize';
          document.body.style.userSelect = 'none';
          window.addEventListener('mousemove', onMouseMove);
          window.addEventListener('mouseup', stopResize);
        });

        resizeHandleEl.addEventListener('touchstart', e => {
          if (!e.touches || e.touches.length === 0) return;
          e.preventDefault();
          isResizing = true;
          startY = e.touches[0].clientY;
          startHeight = bodyEl.getBoundingClientRect().height;
          window.addEventListener('touchmove', onTouchMove, { passive: true });
          window.addEventListener('touchend', stopResize);
        }, { passive: false });

        resizeHandleEl.addEventListener('dblclick', () => {
          const lineCount = Math.max(1, textarea.value.split('\n').length);
          const autoHeight = Math.max(260, lineCount * 23 + 48);
          const currentH = bodyEl.getBoundingClientRect().height;
          const fallbackH = defaultHeight || 360;
          const targetH = Math.abs(currentH - autoHeight) < 24 ? fallbackH : autoHeight;
          applyHeight(targetH);
        });
      }

      return { sync, hideAutocomplete, hideSigHelp };
    }

    /* ========================================================================
     * 2. MODULE (11 AUFBAUENDE THEMENBEREICHE)
     * ======================================================================== */

    const IHK_SCALE = [
      { min: 92, grade: '1', label: 'sehr gut', passed: true },
      { min: 81, grade: '2', label: 'gut', passed: true },
      { min: 67, grade: '3', label: 'befriedigend', passed: true },
      { min: 50, grade: '4', label: 'ausreichend', passed: true },
      { min: 30, grade: '5', label: 'mangelhaft', passed: false },
      { min: 0, grade: '6', label: 'ungenügend', passed: false }
    ];

    function getIhkGrade(percent) {
      const rounded = Math.round(percent);
      for (const entry of IHK_SCALE) {
        if (rounded >= entry.min) return entry;
      }
      return IHK_SCALE[IHK_SCALE.length - 1];
    }

    function formatTime(sec) {
      const s = Math.max(0, Math.floor(sec));
      const m = Math.floor(s / 60);
      const r = s % 60;
      return `${String(m).padStart(2, '0')}:${String(r).padStart(2, '0')}`;
    }

    /* ========================================================================
     * 6. ANWENDUNGSZUSTAND & PERSISTENZ (LOCALSTORAGE)
     * ======================================================================== */

    const STORAGE_KEY = 'pylek_studio_ibb_v3';

    function loadProgress() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY) || localStorage.getItem('pylek_studio_ibb_v2');
        if (!raw) return { solvedIds: [], ideSolvedIds: [], examHistory: [], theme: null };
        const parsed = JSON.parse(raw);
        return {
          solvedIds: Array.isArray(parsed.solvedIds) ? parsed.solvedIds : [],
          ideSolvedIds: Array.isArray(parsed.ideSolvedIds) ? parsed.ideSolvedIds : [],
          examHistory: Array.isArray(parsed.examHistory) ? parsed.examHistory : [],
          theme: parsed.theme || null
        };
      } catch {
        return { solvedIds: [], ideSolvedIds: [], examHistory: [], theme: null };
      }
    }

    const PROGRESS = loadProgress();

    function saveProgress() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(PROGRESS));
      } catch {
        // Ignore storage quota errors
      }
    }

    const STATE = {
      activeTab: 'practice',
      selectedModuleId: 1,
      practiceOrder: {},
      practiceIndex: {},
      practiceAnswered: {},
      practiceHintShown: {},
      selectedIdeTaskId: IDE_TASKS[0].id,
      ideDrafts: {},
      ideEditorHeight: 360,
      examEditorHeight: 280,
      ideExpanded: false,
      sandboxCode: '# Freie Python 3.12 Sandbox\n# Beliebigen Python-Code hier ausführen.\n\nnamen = ["Max", "Anna", "Tom", "Lisa"]\nfor i, name in enumerate(namen, start=1):\n    print(f"{i}. {name}")\n',
      isSandbox: false,
      mainEditorCtrl: null,
      exam: null
    };

    /* ========================================================================
     * 7. DARK MODE / LIGHT MODE
     * ======================================================================== */

    function applyTheme(dark) {
      const root = document.documentElement;
      const iconEl = document.getElementById('theme-icon');
      const labelEl = document.getElementById('theme-label');
      if (dark) {
        root.classList.add('dark');
        if (labelEl) labelEl.textContent = 'Light Mode';
        if (iconEl) {
          iconEl.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="w-4 h-4"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>';
        }
      } else {
        root.classList.remove('dark');
        if (labelEl) labelEl.textContent = 'Dark Mode';
        if (iconEl) {
          iconEl.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="w-4 h-4"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>';
        }
      }
    }

    function initTheme() {
      const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      const useDark = PROGRESS.theme ? PROGRESS.theme === 'dark' : true;
      applyTheme(useDark);
    }

    function toggleTheme() {
      const isDark = document.documentElement.classList.contains('dark');
      const next = !isDark;
      PROGRESS.theme = next ? 'dark' : 'light';
      saveProgress();
      applyTheme(next);
    }

    /* ========================================================================
     * 8. TABS, MODAL & TOASTS
     * ======================================================================== */

    function switchTab(tabName) {
      STATE.activeTab = tabName;
      document.querySelectorAll('.tab-panel').forEach(panel => {
        panel.classList.toggle('hidden', panel.id !== `tab-${tabName}`);
      });
      document.querySelectorAll('.nav-tab').forEach(btn => {
        const active = btn.dataset.tab === tabName;
        btn.classList.toggle('border-blue-600', active);
        btn.classList.toggle('text-blue-600', active);
        btn.classList.toggle('dark:text-blue-400', active);
        btn.classList.toggle('border-transparent', !active);
        btn.classList.toggle('text-zinc-600', !active);
        btn.classList.toggle('dark:text-zinc-400', !active);
      });
      if (tabName === 'ide' && STATE.mainEditorCtrl) {
        requestAnimationFrame(() => STATE.mainEditorCtrl.sync());
      }
      if (tabName === 'stats') renderStatsTab();
    }

    function showModal(title, body, actions) {
      const modal = document.getElementById('app-modal');
      document.getElementById('modal-title').textContent = title;
      document.getElementById('modal-body').textContent = body;
      const actionsEl = document.getElementById('modal-actions');
      actionsEl.innerHTML = '';
      for (const act of actions) {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.textContent = act.label;
        btn.className = act.primary
          ? 'px-4 py-2 rounded-lg text-sm font-medium bg-blue-600 hover:bg-blue-700 text-white transition'
          : 'px-4 py-2 rounded-lg text-sm font-medium border border-zinc-300 dark:border-zinc-700 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition';
        btn.addEventListener('click', () => {
          closeModal();
          if (act.onClick) act.onClick();
        });
        actionsEl.appendChild(btn);
      }
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }

    function closeModal() {
      const modal = document.getElementById('app-modal');
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }

    function showToast(msg) {
      const container = document.getElementById('toast-container');
      const el = document.createElement('div');
      el.className = 'px-4 py-2.5 rounded-lg bg-zinc-900 dark:bg-zinc-100 text-white dark:text-zinc-900 text-xs font-medium shadow-lg border border-zinc-700 dark:border-zinc-300 transition-opacity duration-300';
      el.textContent = msg;
      container.appendChild(el);
      setTimeout(() => {
        el.style.opacity = '0';
        setTimeout(() => el.remove(), 300);
      }, 2600);
    }

    /* ========================================================================
     * 9. TAB 1: THEMEN-ÜBUNGEN
     * ======================================================================== */

    function getFilteredModuleQuestions(moduleId) {
      const diffFilter = document.getElementById('practice-filter-diff').value;
      const typeFilter = document.getElementById('practice-filter-type').value;
      const all = QUESTION_BANK.filter(q => {
        if (q.moduleId !== moduleId) return false;
        if (diffFilter !== 'all' && q.difficulty !== diffFilter) return false;
        if (typeFilter !== 'all' && q.type !== typeFilter) return false;
        return true;
      });
      const key = `${moduleId}|${diffFilter}|${typeFilter}`;
      if (!STATE.practiceOrder[key] || STATE.practiceOrder[key].length !== all.length) {
        STATE.practiceOrder[key] = fisherYates(all.map(q => q.id));
        STATE.practiceIndex[key] = 0;
      }
      const mapById = new Map(all.map(q => [q.id, q]));
      return {
        key,
        items: STATE.practiceOrder[key].map(id => mapById.get(id)).filter(Boolean)
      };
    }

    function renderModuleSidebar() {
      const sidebar = document.getElementById('module-sidebar');
      const solvedSet = new Set(PROGRESS.solvedIds);
      sidebar.innerHTML = MODULES.map(m => {
        const modQs = QUESTION_BANK.filter(q => q.moduleId === m.id);
        const solvedCount = modQs.filter(q => solvedSet.has(q.id)).length;
        const active = m.id === STATE.selectedModuleId;
        const pct = modQs.length ? Math.round((solvedCount / modQs.length) * 100) : 0;
        return `
          <button type="button" data-module-id="${m.id}"
            class="module-select-btn w-full text-left rounded-xl border p-3.5 transition ${
              active
                ? 'border-blue-600 bg-blue-50/50 dark:bg-blue-950/25'
                : 'border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900/70 hover:border-zinc-400 dark:hover:border-zinc-700'
            }">
            <div class="flex items-start justify-between gap-2">
              <div class="flex items-center gap-2.5 min-w-0">
                <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded ${
                  active ? 'bg-blue-600 text-white' : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300'
                }">${m.code}</span>
                <span class="font-semibold text-sm leading-snug truncate">${escapeHtml(m.title)}</span>
              </div>
              <span class="tabular-nums text-[11px] font-mono text-zinc-500 dark:text-zinc-400 shrink-0">${solvedCount}/${modQs.length}</span>
            </div>
            <p class="text-xs text-zinc-500 dark:text-zinc-400 mt-1.5 line-clamp-2">${escapeHtml(m.desc)}</p>
            <div class="mt-2.5 w-full h-1.5 rounded-full bg-zinc-200 dark:bg-zinc-800 overflow-hidden">
              <div class="h-full bg-emerald-600 transition-all" style="width: ${pct}%"></div>
            </div>
          </button>
        `;
      }).join('');

      sidebar.querySelectorAll('.module-select-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          STATE.selectedModuleId = Number(btn.dataset.moduleId);
          renderModuleSidebar();
          renderPracticeQuestion();
        });
      });
    }

    function renderPracticeQuestion() {
      const card = document.getElementById('practice-card');
      const mod = MODULES.find(m => m.id === STATE.selectedModuleId) || MODULES[0];
      const { key, items } = getFilteredModuleQuestions(mod.id);

      if (items.length === 0) {
        card.innerHTML = `
          <div class="py-10 text-center space-y-3">
            <h3 class="text-base font-semibold">Keine Aufgaben für diese Filterkombination</h3>
            <p class="text-sm text-zinc-500 dark:text-zinc-400">Setze den Schwierigkeits- oder Typfilter zurück, um alle ${QUESTION_BANK.filter(q => q.moduleId === mod.id).length} Aufgaben dieses Moduls zu sehen.</p>
          </div>
        `;
        return;
      }

      const idx = Math.min(STATE.practiceIndex[key] || 0, items.length - 1);
      STATE.practiceIndex[key] = idx;
      const q = items[idx];
      const answeredIdx = STATE.practiceAnswered[q.id];
      const isAnswered = answeredIdx !== undefined;
      const isCorrect = isAnswered && answeredIdx === q.correctIndex;
      const hintVisible = Boolean(STATE.practiceHintShown[q.id]);
      const badgeCls = DIFF_BADGE_STYLE[q.difficulty] || '';

      card.innerHTML = `
        <div class="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-zinc-200 dark:border-zinc-800">
          <div class="flex flex-wrap items-center gap-2">
            <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300">Modul ${mod.code}</span>
            <span class="text-xs font-medium px-2.5 py-0.5 rounded border ${badgeCls}">${escapeHtml(q.difficulty)}</span>
            <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400">${escapeHtml(q.type)}</span>
            <span class="tabular-nums text-xs font-mono text-zinc-500 dark:text-zinc-400">${q.points} Pkt.</span>
          </div>
          <div class="tabular-nums text-xs font-mono text-zinc-500 dark:text-zinc-400">
            Aufgabe ${idx + 1} / ${items.length} · ${q.id}
          </div>
        </div>

        <div class="mt-4 space-y-4">
          <p class="text-base font-medium leading-relaxed whitespace-pre-line">${escapeHtml(q.question)}</p>

          ${q.code ? `
            <div class="rounded-lg border border-zinc-300 dark:border-zinc-800 bg-[#080808] text-[#d4d4d4] overflow-hidden">
              <div class="flex items-center justify-between px-3.5 py-1.5 bg-[#0f0f0f] border-b border-[#1c1c1c] text-xs font-mono text-[#9cdcfe]">
                <span>Python 3.12</span>
                <button type="button" id="practice-open-ide-btn" class="text-blue-400 hover:text-blue-300 underline">Im IDE ausprobieren</button>
              </div>
              <pre class="p-3.5 text-sm font-mono overflow-x-auto leading-relaxed">${highlightPython(q.code, q.showLineNumbers !== false)}</pre>
            </div>
          ` : ''}

          <div class="space-y-2.5 pt-1">
            ${q.options.map((opt, oIdx) => {
              const letter = ['A', 'B', 'C', 'D'][oIdx] || String(oIdx + 1);
              let optStyle = 'border-zinc-200 dark:border-zinc-800 hover:border-blue-500 dark:hover:border-blue-500 bg-white dark:bg-zinc-900/50';
              let badge = '';
              if (isAnswered) {
                if (oIdx === q.correctIndex) {
                  optStyle = 'border-emerald-600 bg-emerald-50/70 dark:bg-emerald-950/35';
                  badge = '<span class="text-xs font-semibold text-emerald-700 dark:text-emerald-300">Richtig</span>';
                } else if (oIdx === answeredIdx) {
                  optStyle = 'border-rose-600 bg-rose-50/70 dark:bg-rose-950/35';
                  badge = '<span class="text-xs font-semibold text-rose-700 dark:text-rose-300">Falsch</span>';
                } else {
                  optStyle = 'border-zinc-200 dark:border-zinc-800 opacity-65';
                }
              }
              return `
                <button type="button" data-opt-idx="${oIdx}" ${isAnswered ? 'disabled' : ''}
                  class="practice-opt-btn w-full text-left rounded-lg border p-3.5 transition flex items-start justify-between gap-3 ${optStyle}">
                  <div class="flex items-start gap-3 min-w-0">
                    <span class="font-mono text-xs font-semibold w-6 h-6 rounded flex items-center justify-center bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 shrink-0 mt-0.5">${letter}</span>
                    <pre class="font-mono text-sm whitespace-pre-wrap break-words leading-snug text-zinc-900 dark:text-zinc-100">${escapeHtml(opt)}</pre>
                  </div>
                  ${badge}
                </button>
              `;
            }).join('')}
          </div>

          ${hintVisible ? `
            <div class="rounded-lg border border-amber-300 dark:border-amber-800/70 bg-amber-50/70 dark:bg-amber-950/30 p-3.5 text-sm text-amber-950 dark:text-amber-200">
              <strong class="font-semibold">Hinweis:</strong> ${escapeHtml(q.hint)}
            </div>
          ` : ''}

          ${isAnswered ? `
            <div class="rounded-lg border ${isCorrect ? 'border-emerald-300 dark:border-emerald-800 bg-emerald-50/60 dark:bg-emerald-950/25' : 'border-rose-300 dark:border-rose-800 bg-rose-50/60 dark:bg-rose-950/25'} p-4 text-sm space-y-1">
              <div class="font-semibold ${isCorrect ? 'text-emerald-800 dark:text-emerald-300' : 'text-rose-800 dark:text-rose-300'}">
                ${isCorrect ? `Richtig gelöst (+${q.points} Punkte)` : 'Nicht korrekt – Erklärung:'}
              </div>
              <p class="text-zinc-700 dark:text-zinc-300 leading-relaxed">${escapeHtml(q.explanation)}</p>
            </div>
          ` : ''}
        </div>

        <div class="flex flex-wrap items-center justify-between gap-3 mt-6 pt-4 border-t border-zinc-200 dark:border-zinc-800">
          <div class="flex items-center gap-2">
            <button type="button" id="practice-prev-btn" ${idx === 0 ? 'disabled' : ''}
              class="px-3.5 py-2 rounded-lg text-sm font-medium border border-zinc-300 dark:border-zinc-700 disabled:opacity-40 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition">
              Zurück
            </button>
            <button type="button" id="practice-hint-btn"
              class="px-3.5 py-2 rounded-lg text-sm font-medium border border-zinc-300 dark:border-zinc-700 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition">
              ${hintVisible ? 'Hinweis ausblenden' : 'Hinweis anzeigen'}
            </button>
          </div>
          <button type="button" id="practice-next-btn"
            class="px-4 py-2 rounded-lg text-sm font-semibold bg-blue-600 hover:bg-blue-700 text-white transition">
            ${idx + 1 < items.length ? 'Nächste Aufgabe' : 'Von vorne beginnen'}
          </button>
        </div>
      `;

      card.querySelectorAll('.practice-opt-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const chosen = Number(btn.dataset.optIdx);
          STATE.practiceAnswered[q.id] = chosen;
          if (chosen === q.correctIndex && !PROGRESS.solvedIds.includes(q.id)) {
            PROGRESS.solvedIds.push(q.id);
            saveProgress();
            renderModuleSidebar();
          }
          renderPracticeQuestion();
        });
      });

      const hintBtn = document.getElementById('practice-hint-btn');
      if (hintBtn) {
        hintBtn.addEventListener('click', () => {
          STATE.practiceHintShown[q.id] = !STATE.practiceHintShown[q.id];
          renderPracticeQuestion();
        });
      }

      const prevBtn = document.getElementById('practice-prev-btn');
      if (prevBtn) {
        prevBtn.addEventListener('click', () => {
          if (STATE.practiceIndex[key] > 0) {
            STATE.practiceIndex[key]--;
            renderPracticeQuestion();
          }
        });
      }

      const nextBtn = document.getElementById('practice-next-btn');
      if (nextBtn) {
        nextBtn.addEventListener('click', () => {
          STATE.practiceIndex[key] = (idx + 1) % items.length;
          renderPracticeQuestion();
        });
      }

      const openIdeBtn = document.getElementById('practice-open-ide-btn');
      if (openIdeBtn && q.code) {
        openIdeBtn.addEventListener('click', () => {
          STATE.isSandbox = true;
          STATE.sandboxCode = `# Aufgabe ${q.id} aus Modul ${mod.code}\n${q.code}\n`;
          switchTab('ide');
          loadIdeView();
          showToast('Code in die Python-Sandbox geladen.');
        });
      }
    }

    /* ========================================================================
     * 10. TAB 2: PYODIDE (PYTHON 3.12) & PRAXIS-IDE
     * ======================================================================== */

    let pyodideInstance = null;
    let pyodideLoadingPromise = null;

    function updatePyodideBadge(state, text) {
      const dot = document.getElementById('pyodide-dot');
      const label = document.getElementById('pyodide-text');
      if (!dot || !label) return;
      label.textContent = text;
      dot.className = 'w-2 h-2 rounded-full ' + (
        state === 'ready' ? 'bg-emerald-500' :
        state === 'error' ? 'bg-rose-500' : 'bg-amber-500'
      );
    }

    async function ensurePyodide() {
      if (pyodideInstance) return pyodideInstance;
      if (pyodideLoadingPromise) return pyodideLoadingPromise;
      pyodideLoadingPromise = (async () => {
        try {
          if (typeof loadPyodide !== 'function') {
            throw new Error('Pyodide-Skript konnte nicht geladen werden (Offline?).');
          }
          updatePyodideBadge('loading', 'Python 3.12 startet ...');
          pyodideInstance = await loadPyodide({
            indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/'
          });
          updatePyodideBadge('ready', 'Python 3.12 bereit');
          return pyodideInstance;
        } catch (err) {
          updatePyodideBadge('error', 'Python-Engine offline');
          pyodideLoadingPromise = null;
          throw err;
        }
      })();
      return pyodideLoadingPromise;
    }

    async function runPythonCode(userCode, tests = []) {
      const py = await ensurePyodide();
      py.globals.set('_USER_CODE', userCode);
      py.globals.set('_TESTS_JSON', JSON.stringify(tests));

      const harness = `
import sys, io, json, traceback

_stdout_buf = io.StringIO()
_stderr_buf = io.StringIO()
_old_out, _old_err = sys.stdout, sys.stderr
sys.stdout = _stdout_buf
sys.stderr = _stderr_buf

_steps = 0
def _trace_guard(frame, event, arg):
    global _steps
    if event == "line":
        _steps += 1
        if _steps > 250000:
            raise RuntimeError("Endlosschleife erkannt (Limit von 250.000 Schritten überschritten).")
    return _trace_guard

def _blocked_input(prompt=""):
    raise RuntimeError("input() wird in der Browser-Sandbox nicht interaktiv unterstützt – weise der Variable direkt einen Testwert zu.")

_ns = {"__name__": "__main__", "input": _blocked_input}
_exec_error = None

try:
    sys.settrace(_trace_guard)
    exec(_USER_CODE, _ns)
except Exception:
    _exec_error = traceback.format_exc()
finally:
    sys.settrace(None)
    sys.stdout = _old_out
    sys.stderr = _old_err

_out_text = _stdout_buf.getvalue()
_err_text = _stderr_buf.getvalue()
_tests = json.loads(_TESTS_JSON)
_test_results = []

if _exec_error is None and _tests:
    for _t in _tests:
        try:
            _ok = bool(eval(_t["check"], {
                "ns": _ns,
                "stdout": _out_text,
                "abs": abs,
                "type": type,
                "int": int,
                "float": float,
                "str": str,
                "bool": bool,
                "list": list,
                "dict": dict,
                "tuple": tuple,
                "len": len,
                "round": round,
                "callable": callable,
                "all": all,
                "any": any,
                "sum": sum,
                "min": min,
                "max": max,
                "__import__": __import__
            }))
            _test_results.append({
                "label": _t["label"],
                "passed": _ok,
                "detail": "OK" if _ok else "Erwartung nicht erfüllt"
            })
        except Exception as _te:
            _test_results.append({
                "label": _t["label"],
                "passed": False,
                "detail": f"Testfehler: {_te}"
            })
elif _exec_error is not None and _tests:
    for _t in _tests:
        _test_results.append({
            "label": _t["label"],
            "passed": False,
            "detail": "Code brach mit Fehler ab"
        })

json.dumps({
    "stdout": _out_text,
    "stderr": _err_text,
    "error": _exec_error,
    "tests": _test_results
})
`;
      const rawJson = await py.runPythonAsync(harness);
      return JSON.parse(rawJson);
    }

    function renderIdeSidebar() {
      const modFilter = document.getElementById('ide-filter-module').value;
      const diffFilter = document.getElementById('ide-filter-diff').value;
      const listEl = document.getElementById('ide-task-list');
      const solvedSet = new Set(PROGRESS.ideSolvedIds);

      const filtered = IDE_TASKS.filter(t => {
        if (modFilter !== 'all' && String(t.moduleId) !== modFilter) return false;
        if (diffFilter !== 'all' && t.difficulty !== diffFilter) return false;
        return true;
      });

      listEl.innerHTML = filtered.map(t => {
        const active = !STATE.isSandbox && t.id === STATE.selectedIdeTaskId;
        const solved = solvedSet.has(t.id);
        const mod = MODULES.find(m => m.id === t.moduleId);
        return `
          <button type="button" data-ide-id="${t.id}"
            class="ide-task-btn w-full text-left rounded-lg border p-2.5 transition ${
              active
                ? 'border-blue-600 bg-blue-50/50 dark:bg-blue-950/25'
                : 'border-zinc-200 dark:border-zinc-800 hover:border-zinc-400 dark:hover:border-zinc-700'
            }">
            <div class="flex items-center justify-between gap-2 text-xs">
              <span class="font-mono font-semibold text-zinc-500 dark:text-zinc-400">${t.id} · M${mod ? mod.code : '01'}</span>
              ${solved ? '<span class="text-[11px] font-semibold text-emerald-700 dark:text-emerald-400">Gelöst</span>' : `<span class="text-[11px] text-zinc-500">${escapeHtml(t.difficulty)}</span>`}
            </div>
            <div class="text-xs font-medium mt-1 leading-snug">${escapeHtml(t.title)}</div>
          </button>
        `;
      }).join('');

      listEl.querySelectorAll('.ide-task-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          STATE.isSandbox = false;
          STATE.selectedIdeTaskId = btn.dataset.ideId;
          loadIdeView();
        });
      });
    }

    function loadIdeView() {
      renderIdeSidebar();
      const headerEl = document.getElementById('ide-task-header');
      const editor = document.getElementById('ide-editor');
      const hintBox = document.getElementById('ide-hint-box');
      const testBtn = document.getElementById('ide-test-btn');
      const solBtn = document.getElementById('ide-solution-btn');
      const hintBtn = document.getElementById('ide-hint-btn');
      const fileEl = document.getElementById('ide-filename');

      hintBox.classList.add('hidden');

      if (STATE.isSandbox) {
        fileEl.textContent = 'sandbox.py';
        testBtn.classList.add('hidden');
        solBtn.classList.add('hidden');
        hintBtn.classList.add('hidden');
        headerEl.innerHTML = `
          <div class="flex items-center justify-between gap-2">
            <div>
              <span class="text-xs font-semibold uppercase tracking-wider text-blue-600 dark:text-blue-400">Freie Python-3.12-Umgebung</span>
              <h3 class="text-lg font-bold mt-0.5">Interaktive Sandbox</h3>
            </div>
          </div>
          <p class="text-sm text-zinc-600 dark:text-zinc-400 mt-1.5">
            Hier kannst du beliebigen Python-Code ausprobieren, Beispiele aus deinen IBB-Unterlagen testen oder eigene Algorithmen entwerfen.
          </p>
        `;
        editor.value = STATE.sandboxCode;
      } else {
        const task = IDE_TASKS.find(t => t.id === STATE.selectedIdeTaskId) || IDE_TASKS[0];
        const mod = MODULES.find(m => m.id === task.moduleId);
        const badgeCls = DIFF_BADGE_STYLE[task.difficulty] || '';
        fileEl.textContent = `${task.id.toLowerCase()}.py`;
        testBtn.classList.remove('hidden');
        solBtn.classList.remove('hidden');
        hintBtn.classList.remove('hidden');

        headerEl.innerHTML = `
          <div class="flex flex-wrap items-center justify-between gap-2">
            <div class="flex flex-wrap items-center gap-2">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800">${task.id} · Modul ${mod ? mod.code : ''}</span>
              <span class="text-xs font-medium px-2.5 py-0.5 rounded border ${badgeCls}">${escapeHtml(task.difficulty)}</span>
            </div>
            <span class="text-xs font-mono text-zinc-500">${task.tests.length} automatische(r) Test(s)</span>
          </div>
          <h3 class="text-lg font-bold mt-2">${escapeHtml(task.title)}</h3>
          <p class="text-sm text-zinc-600 dark:text-zinc-300 mt-1.5 leading-relaxed">${task.description}</p>
        `;
        editor.value = STATE.ideDrafts[task.id] !== undefined ? STATE.ideDrafts[task.id] : task.starter;
      }

      if (STATE.mainEditorCtrl) {
        STATE.mainEditorCtrl.hideAutocomplete();
        STATE.mainEditorCtrl.hideSigHelp();
        STATE.mainEditorCtrl.sync();
      }
    }

    async function executeCurrentIde(withTests) {
      const editor = document.getElementById('ide-editor');
      const consoleEl = document.getElementById('ide-console');
      const testResEl = document.getElementById('ide-test-results');
      const code = editor.value;
      const task = STATE.isSandbox ? null : (IDE_TASKS.find(t => t.id === STATE.selectedIdeTaskId) || IDE_TASKS[0]);

      consoleEl.textContent = 'Ausführung läuft ...';
      try {
        const res = await runPythonCode(code, withTests && task ? task.tests : []);
        let output = '';
        if (res.stdout) output += res.stdout;
        if (res.stderr) output += (output ? '\n' : '') + res.stderr;
        if (res.error) output += (output ? '\n' : '') + res.error;
        consoleEl.textContent = output || '# Programm beendet (keine Konsolenausgabe).';

        if (withTests && task) {
          const allPassed = res.tests.length > 0 && res.tests.every(t => t.passed);
          if (allPassed && !PROGRESS.ideSolvedIds.includes(task.id)) {
            PROGRESS.ideSolvedIds.push(task.id);
            saveProgress();
            renderIdeSidebar();
          }
          testResEl.innerHTML = res.tests.map(t => `
            <div class="rounded-lg border p-2.5 text-xs ${
              t.passed
                ? 'border-emerald-300 dark:border-emerald-800 bg-emerald-50/70 dark:bg-emerald-950/30 text-emerald-900 dark:text-emerald-200'
                : 'border-rose-300 dark:border-rose-800 bg-rose-50/70 dark:bg-rose-950/30 text-rose-900 dark:text-rose-200'
            }">
              <div class="font-semibold">${t.passed ? 'Bestanden' : 'Fehlgeschlagen'}: <span class="font-mono">${escapeHtml(t.label)}</span></div>
              <div class="mt-0.5 opacity-80">${escapeHtml(t.detail)}</div>
            </div>
          `).join('');
        }
      } catch (err) {
        consoleEl.textContent = `Fehler bei der Ausführung: ${err.message}`;
      }
    }

    /* ========================================================================
     * 11. TAB 3: LEK / PRÜFUNGSSIMULATION MIT IHK-NOTENSPIEGEL
     * ======================================================================== */

    function buildExamItems(mode, shortCount, includeIde, includeDev) {
      const totalTarget = mode === 'long' ? 30 : shortCount;
      const ideCount = includeIde ? (mode === 'long' ? 2 : 1) : 0;
      const mcTarget = totalTarget - ideCount;

      const allowedPool = QUESTION_BANK.filter(q => includeDev || q.difficulty !== 'Python Entwickler');
      const selectedMc = [];
      const usedIds = new Set();

      if (includeDev) {
        const devPool = fisherYates(allowedPool.filter(q => q.difficulty === 'Python Entwickler'));
        const devQuota = mode === 'long' ? 4 : 2;
        for (const dq of devPool.slice(0, devQuota)) {
          selectedMc.push(dq);
          usedIds.add(dq.id);
        }
      }

      const moduleIds = fisherYates(MODULES.map(m => m.id));
      let round = 0;
      while (selectedMc.length < mcTarget && round < 10) {
        for (const mId of moduleIds) {
          if (selectedMc.length >= mcTarget) break;
          const candidates = fisherYates(allowedPool.filter(q => q.moduleId === mId && !usedIds.has(q.id)));
          if (candidates.length > 0) {
            selectedMc.push(candidates[0]);
            usedIds.add(candidates[0].id);
          }
        }
        round++;
      }

      const items = fisherYates(selectedMc).map(q => ({
        kind: 'mc',
        data: q,
        maxPoints: q.points,
        answer: null,
        flagged: false,
        hintUsed: false
      }));

      if (ideCount > 0) {
        const idePool = IDE_TASKS.filter(t => includeDev || t.difficulty !== 'Python Entwickler');
        let chosenIde = [];
        if (includeDev) {
          const devIde = fisherYates(idePool.filter(t => t.difficulty === 'Python Entwickler'));
          if (devIde.length > 0) chosenIde.push(devIde[0]);
        }
        const remainingIde = fisherYates(idePool.filter(t => !chosenIde.some(c => c.id === t.id)));
        while (chosenIde.length < ideCount && remainingIde.length > 0) {
          chosenIde.push(remainingIde.shift());
        }
        for (const t of chosenIde) {
          items.push({
            kind: 'ide',
            data: t,
            maxPoints: t.difficulty === 'Python Entwickler' ? 8 : 6,
            code: t.starter,
            testResults: null,
            stdout: '',
            flagged: false,
            hintUsed: false
          });
        }
      }

      return items;
    }

    function startExam() {
      const participantNameInput = document.getElementById('exam-participant-name');
      const participantName = participantNameInput.value.trim();
      if (!participantName) {
        showToast('Bitte gib vor dem Start deinen Namen ein.');
        participantNameInput.focus();
        return;
      }
      participantNameInput.value = '';

      const mode = document.querySelector('input[name="exam-mode"]:checked')?.value || 'short';
      const shortCount = Number(document.getElementById('short-count-slider').value) || 12;
      const includeIde = document.getElementById('exam-include-ide').checked;
      const includeDev = document.getElementById('exam-include-dev').checked;
      const allowHints = document.getElementById('exam-allow-hints').checked;

      const items = buildExamItems(mode, shortCount, includeIde, includeDev);
      const durationSec = mode === 'long' ? 45 * 60 : 20 * 60;

      if (STATE.exam && STATE.exam.timerId) {
        clearInterval(STATE.exam.timerId);
      }

      STATE.exam = {
        participantName,
        startedAt: new Date().toISOString(),
        mode,
        allowHints,
        items,
        currentIndex: 0,
        remainingSec: durationSec,
        totalDurationSec: durationSec,
        timerId: null
      };

      document.getElementById('exam-setup-view').classList.add('hidden');
      document.getElementById('exam-result-view').classList.add('hidden');
      document.getElementById('exam-active-view').classList.remove('hidden');

      document.getElementById('exam-timer').textContent = formatTime(durationSec);
      STATE.exam.timerId = setInterval(() => {
        if (!STATE.exam) return;
        STATE.exam.remainingSec--;
        document.getElementById('exam-timer').textContent = formatTime(STATE.exam.remainingSec);
        if (STATE.exam.remainingSec <= 0) {
          submitExam(true);
        }
      }, 1000);

      renderExamNavGrid();
      updateExamProgress();
      renderExamQuestion();
    }

    function isExamItemAnswered(item) {
      if (item.kind === 'mc') return item.answer !== null;
      return item.code.trim() !== item.data.starter.trim() || item.testResults !== null;
    }

    function updateExamProgress() {
      if (!STATE.exam) return;
      const total = STATE.exam.items.length;
      const done = STATE.exam.items.filter(isExamItemAnswered).length;
      document.getElementById('exam-progress-text').textContent = `${done} / ${total}`;
      document.getElementById('exam-progress-bar').style.width = `${Math.round((done / total) * 100)}%`;
    }

    function renderExamNavGrid() {
      if (!STATE.exam) return;
      const grid = document.getElementById('exam-nav-grid');
      grid.innerHTML = STATE.exam.items.map((item, idx) => {
        const active = idx === STATE.exam.currentIndex;
        const answered = isExamItemAnswered(item);
        let cls = 'border-zinc-300 dark:border-zinc-700 bg-white dark:bg-zinc-900 text-zinc-700 dark:text-zinc-300';
        if (answered) cls = 'border-emerald-600 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-300';
        if (item.flagged) cls = 'border-amber-500 bg-amber-50 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300';
        if (active) cls += ' ring-2 ring-blue-600';

        return `
          <button type="button" data-exam-nav="${idx}"
            class="tabular-nums px-2.5 py-1.5 rounded-lg border text-xs font-mono font-semibold transition ${cls}">
            ${idx + 1}${item.kind === 'ide' ? '·IDE' : ''}
          </button>
        `;
      }).join('');

      grid.querySelectorAll('[data-exam-nav]').forEach(btn => {
        btn.addEventListener('click', () => {
          STATE.exam.currentIndex = Number(btn.dataset.examNav);
          renderExamNavGrid();
          renderExamQuestion();
        });
      });
    }

    function renderExamQuestion() {
      if (!STATE.exam) return;
      const card = document.getElementById('exam-question-card');
      const idx = STATE.exam.currentIndex;
      const total = STATE.exam.items.length;
      const item = STATE.exam.items[idx];
      const mod = MODULES.find(m => m.id === item.data.moduleId);
      const badgeCls = DIFF_BADGE_STYLE[item.data.difficulty] || '';

      if (item.kind === 'mc') {
        const q = item.data;
        card.innerHTML = `
          <div class="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-zinc-200 dark:border-zinc-800">
            <div class="flex flex-wrap items-center gap-2">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800">Aufgabe ${idx + 1} von ${total}</span>
              <span class="text-xs font-medium px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400">Modul ${mod ? mod.code : ''}</span>
              <span class="text-xs font-medium px-2.5 py-0.5 rounded border ${badgeCls}">${escapeHtml(q.difficulty)}</span>
              <span class="tabular-nums text-xs font-mono text-zinc-500">${item.maxPoints} Pkt.</span>
            </div>
            <button type="button" id="exam-flag-btn"
              class="px-2.5 py-1 rounded-md text-xs font-medium border ${item.flagged ? 'border-amber-500 bg-amber-50 dark:bg-amber-950/30 text-amber-800 dark:text-amber-300' : 'border-zinc-300 dark:border-zinc-700'}">
              ${item.flagged ? 'Markierung entfernen' : 'Zur Kontrolle markieren'}
            </button>
          </div>

          <div class="mt-4 space-y-4">
            <p class="text-base font-medium leading-relaxed whitespace-pre-line">${escapeHtml(q.question)}</p>
            ${q.code ? `
              <div class="rounded-lg border border-zinc-300 dark:border-zinc-800 bg-[#080808] text-[#d4d4d4] overflow-hidden">
                <pre class="p-3.5 text-sm font-mono overflow-x-auto leading-relaxed">${highlightPython(q.code, q.showLineNumbers !== false)}</pre>
              </div>
            ` : ''}

            <div class="space-y-2.5">
              ${q.options.map((opt, oIdx) => {
                const letter = ['A', 'B', 'C', 'D'][oIdx] || String(oIdx + 1);
                const selected = item.answer === oIdx;
                return `
                  <button type="button" data-exam-opt="${oIdx}"
                    class="exam-opt-btn w-full text-left rounded-lg border p-3.5 transition flex items-start gap-3 ${
                      selected
                        ? 'border-blue-600 bg-blue-50/60 dark:bg-blue-950/30'
                        : 'border-zinc-200 dark:border-zinc-800 hover:border-zinc-400 dark:hover:border-zinc-600'
                    }">
                    <span class="font-mono text-xs font-semibold w-6 h-6 rounded flex items-center justify-center ${
                      selected ? 'bg-blue-600 text-white' : 'bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300'
                    } shrink-0 mt-0.5">${letter}</span>
                    <pre class="font-mono text-sm whitespace-pre-wrap break-words leading-snug">${escapeHtml(opt)}</pre>
                  </button>
                `;
              }).join('')}
            </div>

            ${item.hintUsed ? `
              <div class="rounded-lg border border-amber-300 dark:border-amber-800 bg-amber-50/70 dark:bg-amber-950/30 p-3.5 text-sm">
                <strong>Hinweis (-0,5 Pkt.):</strong> ${escapeHtml(q.hint)}
              </div>
            ` : ''}
          </div>

          <div class="flex flex-wrap items-center justify-between gap-3 mt-6 pt-4 border-t border-zinc-200 dark:border-zinc-800">
            <div class="flex items-center gap-2">
              <button type="button" id="exam-prev-btn" ${idx === 0 ? 'disabled' : ''}
                class="px-3.5 py-2 rounded-lg text-sm font-medium border border-zinc-300 dark:border-zinc-700 disabled:opacity-40">
                Zurück
              </button>
              ${STATE.exam.allowHints && !item.hintUsed ? `
                <button type="button" id="exam-hint-btn"
                  class="px-3.5 py-2 rounded-lg text-sm font-medium border border-zinc-300 dark:border-zinc-700">
                  Hinweis (-0,5 Pkt.)
                </button>
              ` : ''}
            </div>
            <button type="button" id="exam-next-btn"
              class="px-4 py-2 rounded-lg text-sm font-semibold bg-blue-600 hover:bg-blue-700 text-white transition">
              ${idx + 1 < total ? 'Weiter' : 'Zur Abgabe prüfen'}
            </button>
          </div>
        `;

        card.querySelectorAll('.exam-opt-btn').forEach(btn => {
          btn.addEventListener('click', () => {
            item.answer = Number(btn.dataset.examOpt);
            updateExamProgress();
            renderExamNavGrid();
            renderExamQuestion();
          });
        });
      } else {
        const t = item.data;
        card.innerHTML = `
          <div class="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-zinc-200 dark:border-zinc-800">
            <div class="flex flex-wrap items-center gap-2">
              <span class="font-mono text-xs font-semibold px-2 py-0.5 rounded bg-zinc-100 dark:bg-zinc-800">Aufgabe ${idx + 1} von ${total} · Praxis-IDE</span>
              <span class="text-xs font-medium px-2.5 py-0.5 rounded border ${badgeCls}">${escapeHtml(t.difficulty)}</span>
              <span class="tabular-nums text-xs font-mono text-zinc-500">${item.maxPoints} Pkt.</span>
            </div>
            <button type="button" id="exam-flag-btn"
              class="px-2.5 py-1 rounded-md text-xs font-medium border ${item.flagged ? 'border-amber-500 bg-amber-50 dark:bg-amber-950/30 text-amber-800 dark:text-amber-300' : 'border-zinc-300 dark:border-zinc-700'}">
              ${item.flagged ? 'Markierung entfernen' : 'Zur Kontrolle markieren'}
            </button>
          </div>

          <div class="mt-4 space-y-4">
            <h3 class="text-base font-bold">${escapeHtml(t.title)}</h3>
            <p class="text-sm text-zinc-600 dark:text-zinc-300 leading-relaxed">${t.description}</p>

            <div class="editor-shell rounded-xl border border-zinc-300 dark:border-zinc-800 bg-[#080808] text-[#d4d4d4] overflow-visible">
              <div class="flex flex-wrap items-center justify-between gap-2 px-4 py-2 bg-[#0f0f0f] border-b border-[#1c1c1c] rounded-t-xl">
                <span class="text-xs font-mono text-zinc-200">${t.id.toLowerCase()}.py · Python 3.12 · IntelliSense</span>
                <button type="button" id="exam-ide-run-btn"
                  class="px-3 py-1 rounded-md text-xs font-medium bg-emerald-700 hover:bg-emerald-600 text-white transition">
                  Code testen &amp; prüfen
                </button>
              </div>
              <div id="exam-ide-editor-body" class="flex bg-[#080808] relative" style="height: ${STATE.examEditorHeight}px;">
                <pre id="exam-ide-gutter" class="editor-gutter w-12 text-right text-[#9a9a9a] bg-[#080808] border-r border-[#1c1c1c] shrink-0 select-none">1</pre>
                <div class="code-editor-wrap">
                  <div id="exam-ide-mirror" class="caret-mirror" aria-hidden="true"></div>
                  <pre id="exam-ide-highlight" class="code-highlight-layer" aria-hidden="true"></pre>
                  <textarea id="exam-ide-editor" spellcheck="false" autocomplete="off" class="code-input"></textarea>
                  <div id="exam-ide-autocomplete" class="vscode-autocomplete hidden" role="listbox"></div>
                  <div id="exam-ide-sig-help" class="vscode-sig-help hidden" role="tooltip"></div>
                </div>
              </div>
              <div id="exam-ide-resize-handle" class="editor-resize-handle rounded-b-xl" role="separator" aria-orientation="horizontal"
                title="Ziehen zum Vergrößern/Verkleinern · Doppelklick: An Codehöhe anpassen">
                <span class="editor-resize-grip"></span>
              </div>
            </div>

            <pre id="exam-ide-out" class="rounded-lg border border-zinc-300 dark:border-zinc-800 bg-[#080808] text-zinc-300 p-3 text-xs font-mono whitespace-pre-wrap">${escapeHtml(item.stdout || '# Klicke auf "Code testen & prüfen", um deinen Code auszuführen.')}</pre>

            ${item.hintUsed ? `
              <div class="rounded-lg border border-amber-300 dark:border-amber-800 bg-amber-50/70 dark:bg-amber-950/30 p-3.5 text-sm">
                <strong>Hinweis (-0,5 Pkt.):</strong> ${escapeHtml(t.hint)}
              </div>
            ` : ''}
          </div>

          <div class="flex flex-wrap items-center justify-between gap-3 mt-6 pt-4 border-t border-zinc-200 dark:border-zinc-800">
            <div class="flex items-center gap-2">
              <button type="button" id="exam-prev-btn" ${idx === 0 ? 'disabled' : ''}
                class="px-3.5 py-2 rounded-lg text-sm font-medium border border-zinc-300 dark:border-zinc-700 disabled:opacity-40">
                Zurück
              </button>
              ${STATE.exam.allowHints && !item.hintUsed ? `
                <button type="button" id="exam-hint-btn"
                  class="px-3.5 py-2 rounded-lg text-sm font-medium border border-zinc-300 dark:border-zinc-700">
                  Hinweis (-0,5 Pkt.)
                </button>
              ` : ''}
            </div>
            <button type="button" id="exam-next-btn"
              class="px-4 py-2 rounded-lg text-sm font-semibold bg-blue-600 hover:bg-blue-700 text-white transition">
              ${idx + 1 < total ? 'Weiter' : 'Zur Abgabe prüfen'}
            </button>
          </div>
        `;

        const exEditor = document.getElementById('exam-ide-editor');
        exEditor.value = item.code;
        const examCtrl = attachVscodeEditor({
          textarea: exEditor,
          highlightEl: document.getElementById('exam-ide-highlight'),
          gutterEl: document.getElementById('exam-ide-gutter'),
          cursorPosEl: null,
          mirrorEl: document.getElementById('exam-ide-mirror'),
          acEl: document.getElementById('exam-ide-autocomplete'),
          sigEl: document.getElementById('exam-ide-sig-help'),
          bodyEl: document.getElementById('exam-ide-editor-body'),
          resizeHandleEl: document.getElementById('exam-ide-resize-handle'),
          defaultHeight: 280,
          onResize: h => { STATE.examEditorHeight = h; },
          onChange: () => {
            item.code = exEditor.value;
            updateExamProgress();
            renderExamNavGrid();
          },
          onRun: () => document.getElementById('exam-ide-run-btn').click()
        });
        examCtrl.sync();

        document.getElementById('exam-ide-run-btn').addEventListener('click', async () => {
          const outEl = document.getElementById('exam-ide-out');
          outEl.textContent = 'Tests werden ausgeführt ...';
          try {
            const res = await runPythonCode(item.code, t.tests);
            item.testResults = res.tests;
            const passed = res.tests.filter(x => x.passed).length;
            let text = res.stdout ? `Ausgabe:\n${res.stdout}\n` : '';
            if (res.error) text += `Fehler:\n${res.error}\n`;
            text += `Tests bestanden: ${passed} / ${res.tests.length}`;
            for (const tr of res.tests) {
              text += `\n  - ${tr.passed ? '[OK]' : '[FEHLER]'} ${tr.label}`;
            }
            item.stdout = text;
            outEl.textContent = text;
            updateExamProgress();
            renderExamNavGrid();
          } catch (err) {
            outEl.textContent = `Fehler: ${err.message}`;
          }
        });
      }

      document.getElementById('exam-flag-btn').addEventListener('click', () => {
        item.flagged = !item.flagged;
        renderExamNavGrid();
        renderExamQuestion();
      });

      const prevBtn = document.getElementById('exam-prev-btn');
      if (prevBtn) {
        prevBtn.addEventListener('click', () => {
          if (STATE.exam.currentIndex > 0) {
            STATE.exam.currentIndex--;
            renderExamNavGrid();
            renderExamQuestion();
          }
        });
      }

      const hintBtn = document.getElementById('exam-hint-btn');
      if (hintBtn) {
        hintBtn.addEventListener('click', () => {
          item.hintUsed = true;
          renderExamQuestion();
        });
      }

      document.getElementById('exam-next-btn').addEventListener('click', () => {
        if (idx + 1 < total) {
          STATE.exam.currentIndex++;
          renderExamNavGrid();
          renderExamQuestion();
        } else {
          confirmSubmitExam();
        }
      });
    }

    function confirmSubmitExam() {
      if (!STATE.exam) return;
      const unanswered = STATE.exam.items.filter(it => !isExamItemAnswered(it)).length;
      const msg = unanswered > 0
        ? `Es sind noch ${unanswered} Aufgabe(n) unbearbeitet. Möchtest du die Prüfung jetzt trotzdem abgeben und auswerten?`
        : 'Alle Aufgaben wurden bearbeitet. Prüfung jetzt abgeben und IHK-Notenspiegel berechnen?';
      showModal('LEK abgeben', msg, [
        { label: 'Weiter bearbeiten', primary: false },
        { label: 'Jetzt auswerten', primary: true, onClick: () => submitExam(false) }
      ]);
    }

    async function submitExam(timeExpired = false) {
      if (!STATE.exam) return;
      const exam = STATE.exam;
      if (exam.timerId) {
        clearInterval(exam.timerId);
        exam.timerId = null;
      }

      let earnedPoints = 0;
      let maxPoints = 0;
      const moduleStats = {};
      for (const m of MODULES) {
        moduleStats[m.id] = { earned: 0, max: 0 };
      }

      for (const item of exam.items) {
        maxPoints += item.maxPoints;
        const mId = item.data.moduleId;
        if (moduleStats[mId]) moduleStats[mId].max += item.maxPoints;

        let itemEarned = 0;
        if (item.kind === 'mc') {
          if (item.answer === item.data.correctIndex) {
            itemEarned = item.maxPoints;
          }
        } else {
          if (item.testResults === null && item.code.trim() !== item.data.starter.trim()) {
            try {
              const res = await runPythonCode(item.code, item.data.tests);
              item.testResults = res.tests;
            } catch {
              item.testResults = [];
            }
          }
          if (Array.isArray(item.testResults) && item.testResults.length > 0) {
            const passedCount = item.testResults.filter(t => t.passed).length;
            itemEarned = (passedCount / item.testResults.length) * item.maxPoints;
          }
        }

        if (item.hintUsed && itemEarned > 0) {
          itemEarned = Math.max(0, itemEarned - 0.5);
        }

        item.earnedPoints = Number(itemEarned.toFixed(2));
        earnedPoints += item.earnedPoints;
        if (moduleStats[mId]) moduleStats[mId].earned += item.earnedPoints;
      }

      earnedPoints = Number(earnedPoints.toFixed(2));
      const percent = maxPoints > 0 ? (earnedPoints / maxPoints) * 100 : 0;
      const ihk = getIhkGrade(percent);

      const completedAt = new Date();
      const elapsedSec = Math.max(0, exam.totalDurationSec - exam.remainingSec);
      const review = exam.items.map(item => {
        const data = item.data;
        const isMc = item.kind === 'mc';
        const plainDescription = isMc
          ? data.question
          : String(data.description || data.title || '').replace(/<[^>]*>/g, ' ');
        return {
          kind: item.kind,
          id: data.id,
          title: data.title || '',
          moduleId: data.moduleId,
          moduleTitle: MODULES.find(module => module.id === data.moduleId)?.title || '',
          difficulty: data.difficulty || 'Unbekannt',
          type: isMc ? (data.type || 'Multiple Choice') : 'Praxis-IDE',
          question: plainDescription,
          promptCode: isMc ? (data.code || '') : (data.starter || ''),
          options: isMc && Array.isArray(data.options) ? data.options.slice() : [],
          answer: isMc
            ? (item.answer === null ? 'Keine Antwort' : data.options[item.answer])
            : (item.code || ''),
          correctAnswer: isMc ? data.options[data.correctIndex] : (data.solution || ''),
          explanation: isMc ? (data.explanation || '') : '',
          solution: isMc ? '' : (data.solution || ''),
          stdout: item.stdout || '',
          testResults: Array.isArray(item.testResults)
            ? item.testResults.map(test => ({ label: test.label, passed: Boolean(test.passed) }))
            : [],
          earnedPoints: item.earnedPoints,
          maxPoints: item.maxPoints
        };
      });
      const difficulties = [...new Set(review.map(item => item.difficulty))];
      const taskTypes = [...new Set(review.map(item => item.type))];

      PROGRESS.examHistory.unshift({
        id: `${completedAt.getTime()}-${Math.random().toString(36).slice(2, 8)}`,
        name: exam.participantName,
        date: completedAt.toLocaleString('de-DE'),
        completedAt: completedAt.toISOString(),
        elapsedSec,
        mode: exam.mode === 'long' ? 'Lang-LEK (30 Fragen)' : `Kurz-LEK (${exam.items.length} Fragen)`,
        earnedPoints,
        maxPoints,
        percent: Math.round(percent * 10) / 10,
        grade: ihk.grade,
        label: ihk.label,
        passed: ihk.passed,
        difficulties,
        taskTypes,
        review
      });
      if (PROGRESS.examHistory.length > 25) PROGRESS.examHistory.length = 25;
      saveProgress();

      document.getElementById('exam-active-view').classList.add('hidden');
      const resView = document.getElementById('exam-result-view');
      resView.classList.remove('hidden');

      resView.innerHTML = `
        <div class="rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900/70 p-6 sm:p-8 space-y-6">
          <div class="flex flex-wrap items-start justify-between gap-4 border-b border-zinc-200 dark:border-zinc-800 pb-5">
            <div>
              <span class="text-xs font-semibold uppercase tracking-wider text-blue-600 dark:text-blue-400">
                ${timeExpired ? 'Zeit abgelaufen · Automatische Abgabe' : 'Prüfungsergebnis'}
              </span>
              <h2 class="text-2xl font-bold mt-1">IHK-Notenspiegel &amp; Auswertung</h2>
            </div>
            <button type="button" id="exam-restart-btn"
              class="px-4 py-2 rounded-lg text-sm font-semibold bg-blue-600 hover:bg-blue-700 text-white transition">
              Neue LEK starten
            </button>
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div class="rounded-lg border border-zinc-200 dark:border-zinc-800 p-4">
              <div class="text-xs text-zinc-500">Erreichte Punkte</div>
              <div class="tabular-nums text-xl font-bold mt-1">${earnedPoints} / ${maxPoints}</div>
            </div>
            <div class="rounded-lg border border-zinc-200 dark:border-zinc-800 p-4">
              <div class="text-xs text-zinc-500">IHK-Prozentwert</div>
              <div class="tabular-nums text-xl font-bold mt-1">${percent.toFixed(1)} %</div>
            </div>
            <div class="rounded-lg border border-zinc-200 dark:border-zinc-800 p-4">
              <div class="text-xs text-zinc-500">IHK-Note</div>
              <div class="tabular-nums text-xl font-bold mt-1">Note ${ihk.grade} (${ihk.label})</div>
            </div>
            <div class="rounded-lg border ${ihk.passed ? 'border-emerald-300 dark:border-emerald-800 bg-emerald-50/60 dark:bg-emerald-950/25' : 'border-rose-300 dark:border-rose-800 bg-rose-50/60 dark:bg-rose-950/25'} p-4">
              <div class="text-xs text-zinc-500">Status</div>
              <div class="text-xl font-bold mt-1 ${ihk.passed ? 'text-emerald-700 dark:text-emerald-300' : 'text-rose-700 dark:text-rose-300'}">
                ${ihk.passed ? 'Bestanden' : 'Nicht bestanden'}
              </div>
            </div>
          </div>

          <div>
            <h3 class="text-sm font-bold uppercase tracking-wider text-zinc-500 dark:text-zinc-400 mb-2.5">Offizieller IHK-Notenschlüssel (100-Punkte-Schema)</h3>
            <div class="overflow-x-auto rounded-lg border border-zinc-200 dark:border-zinc-800">
              <table class="w-full text-left text-xs">
                <thead class="bg-zinc-100 dark:bg-zinc-800/80 text-zinc-600 dark:text-zinc-300">
                  <tr>
                    <th class="px-3.5 py-2.5">Note</th>
                    <th class="px-3.5 py-2.5">Bewertung</th>
                    <th class="px-3.5 py-2.5">Prozentbereich</th>
                    <th class="px-3.5 py-2.5">Ergebnis</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-zinc-200 dark:divide-zinc-800">
                  ${[
                    { g: '1', l: 'sehr gut', r: '100 – 92 %', p: true },
                    { g: '2', l: 'gut', r: '91 – 81 %', p: true },
                    { g: '3', l: 'befriedigend', r: '80 – 67 %', p: true },
                    { g: '4', l: 'ausreichend', r: '66 – 50 %', p: true },
                    { g: '5', l: 'mangelhaft', r: '49 – 30 %', p: false },
                    { g: '6', l: 'ungenügend', r: '29 – 0 %', p: false }
                  ].map(row => `
                    <tr class="${row.g === ihk.grade ? 'bg-blue-50/70 dark:bg-blue-950/35 font-semibold' : ''}">
                      <td class="px-3.5 py-2 font-mono">Note ${row.g}</td>
                      <td class="px-3.5 py-2">${row.l}</td>
                      <td class="px-3.5 py-2 tabular-nums font-mono">${row.r}</td>
                      <td class="px-3.5 py-2">${row.g === ihk.grade ? 'Deine Einstufung' : (row.p ? 'Bestanden' : 'Nicht bestanden')}</td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          </div>

          <div>
            <h3 class="text-sm font-bold uppercase tracking-wider text-zinc-500 dark:text-zinc-400 mb-2.5">Auswertung nach Themenbereich</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              ${MODULES.filter(m => moduleStats[m.id].max > 0).map(m => {
                const st = moduleStats[m.id];
                const mPct = Math.round((st.earned / st.max) * 100);
                return `
                  <div class="rounded-lg border border-zinc-200 dark:border-zinc-800 p-3 text-xs">
                    <div class="flex justify-between font-medium">
                      <span>${m.code} · ${escapeHtml(m.title)}</span>
                      <span class="tabular-nums font-mono">${st.earned.toFixed(1)}/${st.max} Pkt. (${mPct}%)</span>
                    </div>
                    <div class="mt-1.5 w-full h-1.5 rounded-full bg-zinc-200 dark:bg-zinc-800 overflow-hidden">
                      <div class="h-full ${mPct >= 50 ? 'bg-emerald-600' : 'bg-rose-600'}" style="width: ${mPct}%"></div>
                    </div>
                  </div>
                `;
              }).join('')}
            </div>
          </div>

          <div class="space-y-3">
            <h3 class="text-sm font-bold uppercase tracking-wider text-zinc-500 dark:text-zinc-400">Einzelauswertung aller Aufgaben</h3>
            ${exam.items.map((item, idx) => {
              const full = item.earnedPoints >= item.maxPoints - 0.5 && item.earnedPoints > 0;
              if (item.kind === 'mc') {
                const q = item.data;
                const userAns = item.answer !== null ? q.options[item.answer] : 'Keine Antwort';
                const corrAns = q.options[q.correctIndex];
                return `
                  <div class="rounded-lg border ${item.answer === q.correctIndex ? 'border-emerald-200 dark:border-emerald-900/60' : 'border-rose-200 dark:border-rose-900/60'} p-4 text-xs space-y-1.5">
                    <div class="flex justify-between font-semibold">
                      <span>Aufgabe ${idx + 1} (${q.id})</span>
                      <span class="tabular-nums font-mono">${item.earnedPoints} / ${item.maxPoints} Pkt.</span>
                    </div>
                    <p class="text-sm font-medium">${escapeHtml(q.question)}</p>
                    <div>Deine Antwort: <span class="font-mono">${escapeHtml(userAns)}</span></div>
                    <div>Richtige Lösung: <span class="font-mono text-emerald-700 dark:text-emerald-300">${escapeHtml(corrAns)}</span></div>
                    <p class="text-zinc-500 dark:text-zinc-400 pt-1">${escapeHtml(q.explanation)}</p>
                  </div>
                `;
              } else {
                const t = item.data;
                return `
                  <div class="rounded-lg border ${full ? 'border-emerald-200 dark:border-emerald-900/60' : 'border-amber-200 dark:border-amber-900/60'} p-4 text-xs space-y-1.5">
                    <div class="flex justify-between font-semibold">
                      <span>Aufgabe ${idx + 1} · Praxis-IDE (${t.id}: ${escapeHtml(t.title)})</span>
                      <span class="tabular-nums font-mono">${item.earnedPoints} / ${item.maxPoints} Pkt.</span>
                    </div>
                    <details class="pt-1">
                      <summary class="cursor-pointer font-medium text-blue-600 dark:text-blue-400">Musterlösung anzeigen</summary>
                      <pre class="mt-2 p-3 rounded bg-[#080808] text-[#d4d4d4] font-mono overflow-x-auto">${highlightPython(t.solution, true)}</pre>
                    </details>
                  </div>
                `;
              }
            }).join('')}
          </div>
        </div>
      `;

      document.getElementById('exam-restart-btn').addEventListener('click', () => {
        STATE.exam = null;
        resView.classList.add('hidden');
        document.getElementById('exam-setup-view').classList.remove('hidden');
      });
    }

    /* ========================================================================
     * 12. TAB 4: STATISTIK & IHK-VERLAUF
     * ======================================================================== */

    function renderStatsTab() {
      const container = document.getElementById('stats-content');
      const totalQ = QUESTION_BANK.length;
      const solvedQ = PROGRESS.solvedIds.length;
      const totalIde = IDE_TASKS.length;
      const solvedIde = PROGRESS.ideSolvedIds.length;
      const leaderboard = [...PROGRESS.examHistory].sort((a, b) => {
        const scoreDiff = Number(b.percent || 0) - Number(a.percent || 0);
        if (scoreDiff !== 0) return scoreDiff;
        const timeDiff = Number(a.elapsedSec || Infinity) - Number(b.elapsedSec || Infinity);
        if (Number.isFinite(timeDiff) && timeDiff !== 0) return timeDiff;
        return String(b.completedAt || '').localeCompare(String(a.completedAt || ''));
      });

      container.innerHTML = `
        <div class="rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900/70 p-6 space-y-6">
          <div class="flex flex-wrap items-center justify-between gap-3 border-b border-zinc-200 dark:border-zinc-800 pb-4">
            <div>
              <h2 class="text-xl font-bold">Lernstand &amp; Prüfungsverlauf</h2>
              <p class="text-sm text-zinc-500 dark:text-zinc-400 mt-0.5">Dein Fortschritt wird lokal im Browser gespeichert.</p>
            </div>
            <button type="button" id="stats-reset-btn"
              class="px-3.5 py-2 rounded-lg text-xs font-medium border border-rose-300 dark:border-rose-800 text-rose-700 dark:text-rose-300 hover:bg-rose-50 dark:hover:bg-rose-950/30 transition">
              Fortschritt zurücksetzen
            </button>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div class="rounded-lg border border-zinc-200 dark:border-zinc-800 p-4">
              <div class="text-xs text-zinc-500">Gelöste Übungsaufgaben</div>
              <div class="tabular-nums text-2xl font-bold mt-1">${solvedQ} / ${totalQ}</div>
            </div>
            <div class="rounded-lg border border-zinc-200 dark:border-zinc-800 p-4">
              <div class="text-xs text-zinc-500">Gelöste Python-IDE-Aufgaben</div>
              <div class="tabular-nums text-2xl font-bold mt-1">${solvedIde} / ${totalIde}</div>
            </div>
            <div class="rounded-lg border border-zinc-200 dark:border-zinc-800 p-4">
              <div class="text-xs text-zinc-500">Abgelegte LEK-Prüfungen</div>
              <div class="tabular-nums text-2xl font-bold mt-1">${PROGRESS.examHistory.length}</div>
            </div>
          </div>

          <section class="space-y-3">
            <div class="flex flex-wrap items-end justify-between gap-2">
              <div>
                <h3 class="text-sm font-bold uppercase tracking-wider text-zinc-500 dark:text-zinc-400">Bestenliste</h3>
                <p class="text-xs text-zinc-500 dark:text-zinc-400 mt-1">Sortiert nach Prozentwert, bei Gleichstand nach Bearbeitungszeit. Klicke eine LEK an, um Aufgaben und Lösungen anzusehen.</p>
              </div>
            </div>
            ${leaderboard.length === 0 ? `
              <p class="text-sm text-zinc-500 dark:text-zinc-400">Noch keine LEK abgeschlossen. Starte eine Prüfung im Reiter <strong>LEK / Prüfung</strong>.</p>
            ` : `
              <div class="space-y-2">
                ${leaderboard.map((h, index) => {
                  const difficulties = Array.isArray(h.difficulties) ? h.difficulties : [];
                  const taskTypes = Array.isArray(h.taskTypes) ? h.taskTypes : [];
                  const review = Array.isArray(h.review) ? h.review : [];
                  return `
                    <details class="rounded-lg border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950/40 overflow-hidden">
                      <summary class="cursor-pointer list-none p-4 hover:bg-zinc-50 dark:hover:bg-zinc-800/40">
                        <div class="flex flex-wrap items-center justify-between gap-3">
                          <div class="flex min-w-0 items-center gap-3">
                            <span class="flex h-9 w-9 shrink-0 items-center justify-center rounded-full ${index === 0 ? 'bg-amber-100 text-amber-800 dark:bg-amber-900/40 dark:text-amber-300' : 'bg-zinc-100 text-zinc-600 dark:bg-zinc-800 dark:text-zinc-300'} font-bold">${index + 1}</span>
                            <div class="min-w-0">
                              <div class="font-semibold">${escapeHtml(h.name || 'Name unbekannt')}</div>
                              <div class="text-xs text-zinc-500 dark:text-zinc-400">${escapeHtml(h.date || 'Datum unbekannt')} · ${escapeHtml(h.mode || 'LEK')} · ${Number.isFinite(Number(h.elapsedSec)) ? formatTime(h.elapsedSec) : 'Zeit nicht gespeichert'}</div>
                            </div>
                          </div>
                          <div class="text-right">
                            <div class="text-lg font-bold tabular-nums">${Number(h.percent || 0).toFixed(1)} %</div>
                            <div class="text-xs ${h.passed ? 'text-emerald-700 dark:text-emerald-300' : 'text-rose-700 dark:text-rose-300'}">Note ${escapeHtml(h.grade || '–')} · ${h.passed ? 'Bestanden' : 'Nicht bestanden'}</div>
                          </div>
                        </div>
                        <div class="mt-3 flex flex-wrap gap-x-4 gap-y-1 text-xs text-zinc-500 dark:text-zinc-400">
                          <span>Punkte: <span class="font-mono">${Number(h.earnedPoints || 0)} / ${Number(h.maxPoints || 0)}</span></span>
                          <span>Niveau: ${escapeHtml(difficulties.join(', ') || 'keine Detaildaten')}</span>
                          <span>Aufgaben: ${escapeHtml(taskTypes.join(', ') || 'keine Detaildaten')}</span>
                        </div>
                      </summary>
                      <div class="border-t border-zinc-200 dark:border-zinc-800 p-4 space-y-3">
                        ${review.length === 0 ? `
                          <p class="text-sm text-zinc-500 dark:text-zinc-400">Für diese ältere LEK wurden noch keine Aufgaben- und Antwortdetails gespeichert.</p>
                        ` : review.map((item, taskIndex) => `
                          <article class="rounded-lg border border-zinc-200 dark:border-zinc-800 p-4 space-y-2 text-sm">
                            <div class="flex flex-wrap justify-between gap-2">
                              <h4 class="font-semibold">Aufgabe ${taskIndex + 1}: ${escapeHtml(item.title || item.id || item.type || 'Aufgabe')}</h4>
                              <span class="text-xs text-zinc-500 dark:text-zinc-400">${escapeHtml(item.difficulty || '')} · ${escapeHtml(item.type || '')} · ${Number(item.earnedPoints || 0)} / ${Number(item.maxPoints || 0)} Pkt.</span>
                            </div>
                            <p>${escapeHtml(item.question || '')}</p>
                            ${item.moduleTitle ? `<p class="text-xs text-zinc-500 dark:text-zinc-400">Themenbereich: ${escapeHtml(item.moduleTitle)}</p>` : ''}
                            ${item.promptCode ? `<div><div class="text-xs font-medium text-zinc-500 dark:text-zinc-400">Startcode</div><pre class="mt-1 overflow-x-auto rounded bg-zinc-100 dark:bg-zinc-900 p-3 text-xs font-mono">${escapeHtml(item.promptCode)}</pre></div>` : ''}
                            ${item.kind === 'mc' ? `
                              ${item.options.length ? `<ul class="space-y-1 text-xs">${item.options.map(option => `<li class="rounded px-2 py-1 ${option === item.correctAnswer ? 'bg-emerald-50 text-emerald-800 dark:bg-emerald-950/40 dark:text-emerald-300' : option === item.answer ? 'bg-rose-50 text-rose-800 dark:bg-rose-950/40 dark:text-rose-300' : ''}">${option === item.answer ? 'Deine Auswahl: ' : ''}${escapeHtml(option)}${option === item.correctAnswer ? ' ✓' : ''}</li>`).join('')}</ul>` : ''}
                              <p><span class="font-medium">Deine Antwort:</span> ${escapeHtml(item.answer || 'Keine Antwort')}</p>
                              <p><span class="font-medium">Richtige Lösung:</span> <span class="text-emerald-700 dark:text-emerald-300">${escapeHtml(item.correctAnswer || '')}</span></p>
                              ${item.explanation ? `<p class="text-zinc-500 dark:text-zinc-400">${escapeHtml(item.explanation)}</p>` : ''}
                            ` : `
                              <div><div class="text-xs font-medium text-zinc-500 dark:text-zinc-400">Dein Code</div><pre class="mt-1 overflow-x-auto rounded bg-zinc-100 dark:bg-zinc-900 p-3 text-xs font-mono">${escapeHtml(item.answer || 'Kein Code eingereicht')}</pre></div>
                              <div><div class="text-xs font-medium text-zinc-500 dark:text-zinc-400">Musterlösung</div><pre class="mt-1 overflow-x-auto rounded bg-zinc-100 dark:bg-zinc-900 p-3 text-xs font-mono">${escapeHtml(item.solution || item.correctAnswer || '')}</pre></div>
                              ${item.stdout ? `<p><span class="font-medium">Deine Ausgabe:</span> <code>${escapeHtml(item.stdout)}</code></p>` : ''}
                              ${item.testResults.length ? `<ul class="text-xs space-y-1">${item.testResults.map(test => `<li class="${test.passed ? 'text-emerald-700 dark:text-emerald-300' : 'text-rose-700 dark:text-rose-300'}">${test.passed ? '✓' : '✗'} ${escapeHtml(test.label || 'Test')}</li>`).join('')}</ul>` : ''}
                            `}
                          </article>
                        `).join('')}
                      </div>
                    </details>
                  `;
                }).join('')}
              </div>
            `}
          </section>
        </div>
      `;

      document.getElementById('stats-reset-btn').addEventListener('click', () => {
        showModal('Fortschritt zurücksetzen', 'Möchtest du wirklich alle gelösten Aufgaben und den gesamten Prüfungsverlauf unwiderruflich löschen?', [
          { label: 'Abbrechen', primary: false },
          {
            label: 'Zurücksetzen',
            primary: true,
            onClick: () => {
              PROGRESS.solvedIds = [];
              PROGRESS.ideSolvedIds = [];
              PROGRESS.examHistory = [];
              STATE.practiceAnswered = {};
              saveProgress();
              renderModuleSidebar();
              renderPracticeQuestion();
              renderIdeSidebar();
              renderStatsTab();
              showToast('Lernstand wurde zurückgesetzt.');
            }
          }
        ]);
      });
    }

    /* ========================================================================
     * 13. INITIALISIERUNG & EVENT-LISTENER
     * ======================================================================== */

    function initApp() {
      if (!window.AUFGABEN_DATA || !Array.isArray(window.AUFGABEN_DATA.MODULES) ||
          !Array.isArray(window.AUFGABEN_DATA.QUESTION_BANK) || !Array.isArray(window.AUFGABEN_DATA.IDE_TASKS)) {
        document.body.innerHTML = `
          <main style="max-width:760px;margin:10vh auto;padding:2rem;font:16px/1.5 system-ui,sans-serif;color:#18181b">
            <h1 style="font-size:1.5rem;font-weight:700">Aufgabendaten konnten nicht geladen werden</h1>
            <p>Die Datei <code>aufgaben.js</code> fehlt, wurde verschoben oder enthält keine gültigen Aufgabendaten.</p>
            <p>Lege <code>aufgaben.js</code> in denselben Ordner wie <code>index.html</code> und öffne die HTML-Datei erneut.</p>
          </main>`;
        return;
      }
      initTheme();

      // Badges aktualisieren
      document.getElementById('nav-pool-badge').textContent = String(QUESTION_BANK.length);
      document.getElementById('nav-ide-badge').textContent = String(IDE_TASKS.length);
      const ideCountLabel = document.getElementById('ide-count-label');
      if (ideCountLabel) ideCountLabel.textContent = String(IDE_TASKS.length);

      // Modul-Filter in IDE befüllen
      const ideModSelect = document.getElementById('ide-filter-module');
      for (const m of MODULES) {
        const opt = document.createElement('option');
        opt.value = String(m.id);
        opt.textContent = `${m.code} – ${m.title}`;
        ideModSelect.appendChild(opt);
      }

      // Navigation & Theme
      document.getElementById('theme-toggle').addEventListener('click', toggleTheme);
      document.querySelectorAll('.nav-tab').forEach(btn => {
        btn.addEventListener('click', () => switchTab(btn.dataset.tab));
      });

      // Tab 1 Filter & Shuffle
      document.getElementById('practice-filter-diff').addEventListener('change', renderPracticeQuestion);
      document.getElementById('practice-filter-type').addEventListener('change', renderPracticeQuestion);
      document.getElementById('practice-shuffle-btn').addEventListener('click', () => {
        const modId = STATE.selectedModuleId;
        const diffFilter = document.getElementById('practice-filter-diff').value;
        const typeFilter = document.getElementById('practice-filter-type').value;
        const key = `${modId}|${diffFilter}|${typeFilter}`;
        delete STATE.practiceOrder[key];
        renderPracticeQuestion();
        showToast('Aufgabenreihenfolge neu gemischt.');
      });

      // Tab 2 VS Code Mini-IDE initialisieren
      const editor = document.getElementById('ide-editor');
      STATE.mainEditorCtrl = attachVscodeEditor({
        textarea: editor,
        highlightEl: document.getElementById('ide-highlight'),
        gutterEl: document.getElementById('ide-gutter'),
        cursorPosEl: document.getElementById('ide-cursor-pos'),
        mirrorEl: document.getElementById('ide-mirror'),
        acEl: document.getElementById('ide-autocomplete'),
        sigEl: document.getElementById('ide-sig-help'),
        bodyEl: document.getElementById('ide-editor-body'),
        resizeHandleEl: document.getElementById('ide-resize-handle'),
        defaultHeight: 360,
        onResize: h => { STATE.ideEditorHeight = h; },
        onChange: () => {
          if (STATE.isSandbox) {
            STATE.sandboxCode = editor.value;
          } else {
            STATE.ideDrafts[STATE.selectedIdeTaskId] = editor.value;
          }
        },
        onRun: () => executeCurrentIde(false)
      });

      const expandBtn = document.getElementById('ide-expand-btn');
      if (expandBtn) {
        expandBtn.addEventListener('click', () => {
          STATE.ideExpanded = !STATE.ideExpanded;
          const sidebarCol = document.getElementById('ide-sidebar-col');
          const mainCol = document.getElementById('ide-main-col');
          if (sidebarCol && mainCol) {
            sidebarCol.classList.toggle('hidden', STATE.ideExpanded);
            mainCol.classList.toggle('lg:col-span-8', !STATE.ideExpanded);
            mainCol.classList.toggle('lg:col-span-12', STATE.ideExpanded);
          }
          expandBtn.textContent = STATE.ideExpanded ? 'Breite: Standard' : 'Breite: Vollbild';
          if (STATE.mainEditorCtrl) STATE.mainEditorCtrl.sync();
        });
      }

      document.getElementById('ide-filter-module').addEventListener('change', renderIdeSidebar);
      document.getElementById('ide-filter-diff').addEventListener('change', renderIdeSidebar);
      document.getElementById('ide-sandbox-btn').addEventListener('click', () => {
        STATE.isSandbox = true;
        loadIdeView();
      });
      document.getElementById('ide-run-btn').addEventListener('click', () => executeCurrentIde(false));
      document.getElementById('ide-test-btn').addEventListener('click', () => executeCurrentIde(true));
      document.getElementById('ide-hint-btn').addEventListener('click', () => {
        const task = IDE_TASKS.find(t => t.id === STATE.selectedIdeTaskId);
        const hintBox = document.getElementById('ide-hint-box');
        if (!task) return;
        hintBox.innerHTML = `<strong class="text-amber-400">Hinweis:</strong> ${escapeHtml(task.hint)}`;
        hintBox.classList.toggle('hidden');
      });
      document.getElementById('ide-solution-btn').addEventListener('click', () => {
        const task = IDE_TASKS.find(t => t.id === STATE.selectedIdeTaskId);
        if (!task) return;
        STATE.ideDrafts[task.id] = task.solution;
        editor.value = task.solution;
        if (STATE.mainEditorCtrl) STATE.mainEditorCtrl.sync();
        showToast('Musterlösung in den Editor geladen.');
      });
      document.getElementById('ide-reset-btn').addEventListener('click', () => {
        if (STATE.isSandbox) {
          editor.value = STATE.sandboxCode;
        } else {
          const task = IDE_TASKS.find(t => t.id === STATE.selectedIdeTaskId);
          if (!task) return;
          delete STATE.ideDrafts[task.id];
          editor.value = task.starter;
        }
        if (STATE.mainEditorCtrl) {
          STATE.mainEditorCtrl.hideAutocomplete();
          STATE.mainEditorCtrl.hideSigHelp();
          STATE.mainEditorCtrl.sync();
        }
        document.getElementById('ide-test-results').innerHTML = 'Zurückgesetzt.';
      });
      document.getElementById('ide-clear-console').addEventListener('click', () => {
        document.getElementById('ide-console').textContent = '';
      });

      // Tab 3 LEK-Konfiguration
      const slider = document.getElementById('short-count-slider');
      const sliderLabel = document.getElementById('short-count-label');
      slider.addEventListener('input', () => {
        sliderLabel.textContent = `${slider.value} Fragen`;
      });

      document.querySelectorAll('input[name="exam-mode"]').forEach(radio => {
        radio.addEventListener('change', () => {
          document.querySelectorAll('.exam-mode-card').forEach(card => {
            const checked = card.querySelector('input[type="radio"]').checked;
            card.classList.toggle('border-blue-600', checked);
            card.classList.toggle('bg-blue-50/40', checked);
            card.classList.toggle('dark:bg-blue-950/20', checked);
            card.classList.toggle('border-zinc-200', !checked);
            card.classList.toggle('dark:border-zinc-800', !checked);
          });
        });
      });

      document.getElementById('exam-start-btn').addEventListener('click', startExam);
      document.getElementById('exam-submit-btn').addEventListener('click', confirmSubmitExam);

      // Modal-Klick auf Hintergrund schließt Modal
      document.getElementById('app-modal').addEventListener('click', e => {
        if (e.target.id === 'app-modal') closeModal();
      });

      // Initiale Ansichten rendern & Pyodide im Hintergrund vorladen
      renderModuleSidebar();
      renderPracticeQuestion();
      loadIdeView();
      switchTab('practice');
      setTimeout(() => { ensurePyodide().catch(() => {}); }, 600);
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initApp);
    } else {
      initApp();
    }
  })();
