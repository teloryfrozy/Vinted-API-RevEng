import { n as spread_props, m as pop, p as push, u as escape_html, v as attr } from "../../../chunks/index.js";
import { C as Circle_alert } from "../../../chunks/circle-alert.js";
import { M as Mail } from "../../../chunks/mail.js";
import { I as Icon } from "../../../chunks/Icon.js";
import { M as Message_square } from "../../../chunks/message-square.js";
import { T as Trash_2 } from "../../../chunks/trash-2.js";
function Printer($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"
      }
    ],
    [
      "path",
      { "d": "M6 9V3a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v6" }
    ],
    [
      "rect",
      {
        "x": "6",
        "y": "14",
        "width": "12",
        "height": "8",
        "rx": "1"
      }
    ]
  ];
  Icon($$payload, spread_props([
    { name: "printer" },
    props,
    {
      iconNode,
      children: ($$payload2) => {
        props.children?.($$payload2);
        $$payload2.out += `<!---->`;
      },
      $$slots: { default: true }
    }
  ]));
  pop();
}
function Settings_2($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    ["path", { "d": "M20 7h-9" }],
    ["path", { "d": "M14 17H5" }],
    [
      "circle",
      { "cx": "17", "cy": "17", "r": "3" }
    ],
    ["circle", { "cx": "7", "cy": "7", "r": "3" }]
  ];
  Icon($$payload, spread_props([
    { name: "settings-2" },
    props,
    {
      iconNode,
      children: ($$payload2) => {
        props.children?.($$payload2);
        $$payload2.out += `<!---->`;
      },
      $$slots: { default: true }
    }
  ]));
  pop();
}
function Star($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"
      }
    ]
  ];
  Icon($$payload, spread_props([
    { name: "star" },
    props,
    {
      iconNode,
      children: ($$payload2) => {
        props.children?.($$payload2);
        $$payload2.out += `<!---->`;
      },
      $$slots: { default: true }
    }
  ]));
  pop();
}
function _page($$payload) {
  let monthsToKeep = 2;
  let autoMessage = "Merci pour votre achat ! N'oubliez pas de laisser un avis 😊";
  $$payload.out += `<div class="mx-auto max-w-7xl px-4 py-8"><div class="mb-8 flex items-center justify-between"><h1 class="text-3xl font-bold text-gray-900">Secrétariat</h1></div> `;
  {
    $$payload.out += "<!--[-->";
    $$payload.out += `<div class="mb-6 rounded-md bg-yellow-50 p-4"><div class="flex"><div class="flex-shrink-0">`;
    Circle_alert($$payload, { class: "h-5 w-5 text-yellow-400" });
    $$payload.out += `<!----></div> <div class="ml-3"><h3 class="text-sm font-medium text-yellow-800">Configuration requise</h3> <div class="mt-2 text-sm text-yellow-700"><p>Certaines fonctionnalités nécessitent votre token Vinted et/ou vos identifiants IMAP. Configurez-les dans les <a href="/settings" class="font-medium text-yellow-800 underline hover:text-yellow-900">paramètres</a>.</p></div></div> <div class="ml-auto pl-3"><div class="-mx-1.5 -my-1.5"><button type="button" class="inline-flex rounded-md bg-yellow-50 p-1.5 text-yellow-500 hover:bg-yellow-100"><span class="sr-only">Dismiss</span> <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"></path></svg></button></div></div></div></div>`;
  }
  $$payload.out += `<!--]--> <div class="grid gap-6 md:grid-cols-2"><div class="rounded-lg bg-white p-6 shadow"><div class="mb-4"><div class="flex items-center text-lg font-medium text-gray-900">`;
  Mail($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
  $$payload.out += `<!----> <h2>Gestion des Mails</h2></div> <div class="mt-2 flex flex-wrap gap-2"><div class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800">`;
  Settings_2($$payload, { class: "mr-1 h-3 w-3" });
  $$payload.out += `<!----> Token Vinted requis</div> <div class="inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800">`;
  Mail($$payload, { class: "mr-1 h-3 w-3" });
  $$payload.out += `<!----> IMAP requis</div></div></div> <div class="space-y-4"><div><p class="mb-2 text-sm font-medium text-gray-700">Message de remerciement</p> <textarea rows="3" class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500" placeholder="Message à inclure dans le colis...">`;
  const $$body = escape_html(autoMessage);
  if ($$body) {
    $$payload.out += `${$$body}`;
  }
  $$payload.out += `</textarea></div> <div class="grid grid-cols-2 gap-3"><button class="inline-flex items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">`;
  Mail($$payload, { class: "h-4 w-4" });
  $$payload.out += `<!----> <span>Traiter les mails</span></button> <button class="inline-flex items-center justify-center space-x-2 rounded-md border border-purple-600 px-4 py-2 text-sm font-medium text-purple-600 transition-colors hover:bg-purple-50 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">`;
  Printer($$payload, { class: "h-4 w-4" });
  $$payload.out += `<!----> <span>Imprimer bordereaux</span></button></div></div></div> <div class="rounded-lg bg-white p-6 shadow"><div class="mb-4"><div class="flex items-center text-lg font-medium text-gray-900">`;
  Message_square($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
  $$payload.out += `<!----> <h2>Gestion des Conversations</h2></div> <div class="mt-2"><div class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800">`;
  Settings_2($$payload, { class: "mr-1 h-3 w-3" });
  $$payload.out += `<!----> Token Vinted requis</div></div></div> <div class="space-y-4"><div><p class="mb-2 text-sm font-medium text-gray-700">Supprimer les conversations plus anciennes que</p> <div class="flex items-center space-x-2"><input type="number"${attr("value", monthsToKeep)} min="1" max="12" class="block w-20 rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"/> <span class="text-sm text-gray-600">mois</span></div></div> <div><p class="mb-2 text-sm font-medium text-gray-700">Évaluation automatique</p> <textarea rows="2" class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500" placeholder="Message d'évaluation personnalisé..."></textarea></div> <div class="grid grid-cols-2 gap-3"><button class="inline-flex items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">`;
  Star($$payload, { class: "h-4 w-4" });
  $$payload.out += `<!----> <span>Évaluer</span></button> <button class="inline-flex items-center justify-center space-x-2 rounded-md border border-red-600 px-4 py-2 text-sm font-medium text-red-600 transition-colors hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2">`;
  Trash_2($$payload, { class: "h-4 w-4" });
  $$payload.out += `<!----> <span>Nettoyer</span></button></div></div></div></div></div>`;
}
export {
  _page as default
};
