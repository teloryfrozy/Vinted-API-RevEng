import { n as spread_props, m as pop, p as push, v as attr, u as escape_html } from "../../../chunks/index.js";
import { C as Circle_alert } from "../../../chunks/circle-alert.js";
import { I as Icon } from "../../../chunks/Icon.js";
import { K as Key } from "../../../chunks/key.js";
function History($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"
      }
    ],
    ["path", { "d": "M3 3v5h5" }],
    ["path", { "d": "M12 7v5l4 2" }]
  ];
  Icon($$payload, spread_props([
    { name: "history" },
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
function Users($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"
      }
    ],
    [
      "path",
      { "d": "M16 3.128a4 4 0 0 1 0 7.744" }
    ],
    ["path", { "d": "M22 21v-2a4 4 0 0 0-3-3.87" }],
    ["circle", { "cx": "9", "cy": "7", "r": "4" }]
  ];
  Icon($$payload, spread_props([
    { name: "users" },
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
  let targetCount = 50;
  $$payload.out += `<div class="mx-auto max-w-7xl px-4 py-8"><div class="mb-8 flex items-center justify-between"><h1 class="text-3xl font-bold text-gray-900">Suivi en Masse</h1></div> `;
  {
    $$payload.out += "<!--[-->";
    $$payload.out += `<div class="mb-6 rounded-md bg-yellow-50 p-4"><div class="flex"><div class="flex-shrink-0">`;
    Circle_alert($$payload, { class: "h-5 w-5 text-yellow-400" });
    $$payload.out += `<!----></div> <div class="ml-3"><h3 class="text-sm font-medium text-yellow-800">Configuration requise</h3> <div class="mt-2 text-sm text-yellow-700"><p>Cette fonctionnalité nécessite votre token Vinted. Configurez-le dans les <a href="/settings" class="font-medium text-yellow-800 underline hover:text-yellow-900">paramètres</a>.</p></div></div> <div class="ml-auto pl-3"><div class="-mx-1.5 -my-1.5"><button type="button" class="inline-flex rounded-md bg-yellow-50 p-1.5 text-yellow-500 hover:bg-yellow-100"><span class="sr-only">Dismiss</span> <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"></path></svg></button></div></div></div></div>`;
  }
  $$payload.out += `<!--]--> <div class="grid gap-6 md:grid-cols-2"><div class="rounded-lg bg-white p-6 shadow"><div class="mb-4"><div class="flex items-center text-lg font-medium text-gray-900">`;
  Users($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
  $$payload.out += `<!----> <h2>Suivi Automatique</h2></div> <div class="mt-2"><div class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800">`;
  Key($$payload, { class: "mr-1 h-3 w-3" });
  $$payload.out += `<!----> Token Vinted requis</div></div></div> <div class="mb-6 space-y-4"><div><p class="mb-1 block text-sm font-medium text-gray-700">Nombre d'utilisateurs à suivre</p> <input type="number"${attr("value", targetCount)} min="1" max="100" class="block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"/></div> `;
  {
    $$payload.out += "<!--[!-->";
  }
  $$payload.out += `<!--]--> <button class="inline-flex w-full items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">`;
  Users($$payload, { class: "h-5 w-5" });
  $$payload.out += `<!----> <span>${escape_html("Démarrer")} le suivi</span></button></div></div> <div class="rounded-lg bg-white p-6 shadow"><div class="mb-4 flex items-center text-lg font-medium text-gray-900">`;
  History($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
  $$payload.out += `<!----> <h2>Historique des Suivis</h2></div> <div class="space-y-4"><div class="rounded-lg border border-gray-200 p-4"><div class="flex items-center justify-between"><div><p class="font-medium text-gray-900">Suivi automatique</p> <p class="text-sm text-gray-500">50 utilisateurs suivis</p></div> <span class="text-sm text-gray-500">Il y a 2 heures</span></div></div> <div class="rounded-lg border border-gray-200 p-4"><div class="flex items-center justify-between"><div><p class="font-medium text-gray-900">Suivi automatique</p> <p class="text-sm text-gray-500">25 utilisateurs suivis</p></div> <span class="text-sm text-gray-500">Hier</span></div></div> <div class="rounded-lg border border-gray-200 p-4"><div class="flex items-center justify-between"><div><p class="font-medium text-gray-900">Suivi automatique</p> <p class="text-sm text-gray-500">75 utilisateurs suivis</p></div> <span class="text-sm text-gray-500">Il y a 2 jours</span></div></div></div></div></div></div>`;
}
export {
  _page as default
};
