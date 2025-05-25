import "clsx";
import { C as Circle_alert } from "../../../chunks/circle-alert.js";
import { n as spread_props, m as pop, p as push } from "../../../chunks/index.js";
import { I as Icon } from "../../../chunks/Icon.js";
import { K as Key } from "../../../chunks/key.js";
import { M as Mail } from "../../../chunks/mail.js";
import { S as Shopping_bag } from "../../../chunks/shopping-bag.js";
import { T as Trash_2 } from "../../../chunks/trash-2.js";
function Refresh_cw($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"
      }
    ],
    ["path", { "d": "M21 3v5h-5" }],
    [
      "path",
      {
        "d": "M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"
      }
    ],
    ["path", { "d": "M8 16H3v5" }]
  ];
  Icon($$payload, spread_props([
    { name: "refresh-cw" },
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
function Rotate_cw($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"
      }
    ],
    ["path", { "d": "M21 3v5h-5" }]
  ];
  Icon($$payload, spread_props([
    { name: "rotate-cw" },
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
  $$payload.out += `<div class="mx-auto max-w-7xl px-4 py-8"><div class="mb-8 flex items-center justify-between"><h1 class="text-3xl font-bold text-gray-900">Gestion des Annonces</h1></div> `;
  {
    $$payload.out += "<!--[-->";
    $$payload.out += `<div class="mb-6 rounded-md bg-yellow-50 p-4"><div class="flex"><div class="flex-shrink-0">`;
    Circle_alert($$payload, { class: "h-5 w-5 text-yellow-400" });
    $$payload.out += `<!----></div> <div class="ml-3"><h3 class="text-sm font-medium text-yellow-800">Configuration requise</h3> <div class="mt-2 text-sm text-yellow-700"><p>Certaines fonctionnalités nécessitent votre token Vinted et/ou vos identifiants IMAP. Configurez-les dans les <a href="/settings" class="font-medium text-yellow-800 underline hover:text-yellow-900">paramètres</a>.</p></div></div> <div class="ml-auto pl-3"><div class="-mx-1.5 -my-1.5"><button type="button" class="inline-flex rounded-md bg-yellow-50 p-1.5 text-yellow-500 hover:bg-yellow-100"><span class="sr-only">Dismiss</span> <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"></path></svg></button></div></div></div></div>`;
  }
  $$payload.out += `<!--]--> <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3"><div class="rounded-lg bg-white p-6 shadow"><div class="mb-4"><div class="flex items-center text-lg font-medium text-gray-900">`;
  Rotate_cw($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
  $$payload.out += `<!----> <h2>Vente Automatique</h2></div> <div class="mt-2 flex flex-wrap gap-2"><div class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800">`;
  Key($$payload, { class: "mr-1 h-3 w-3" });
  $$payload.out += `<!----> Token Vinted requis</div> <div class="inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800">`;
  Mail($$payload, { class: "mr-1 h-3 w-3" });
  $$payload.out += `<!----> IMAP requis</div></div></div> <p class="mb-4 text-sm text-gray-600">Automatisez la repose de vos annonces programmées en plusieurs exemplaires. Évitez les tâches répétitives et chronophages.</p> <button class="inline-flex w-full items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">`;
  Shopping_bag($$payload, { class: "h-5 w-5" });
  $$payload.out += `<!----> <span>Activer la vente auto</span></button></div> <div class="rounded-lg bg-white p-6 shadow"><div class="mb-4"><div class="flex items-center text-lg font-medium text-gray-900">`;
  Refresh_cw($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
  $$payload.out += `<!----> <h2>Rafraîchir les Annonces</h2></div> <div class="mt-2"><div class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800">`;
  Key($$payload, { class: "mr-1 h-3 w-3" });
  $$payload.out += `<!----> Token Vinted requis</div></div></div> <p class="mb-4 text-sm text-gray-600">Remontez vos annonces en tête de liste sur Vinted. Rafraîchissez une sélection ou toutes vos annonces en un clic.</p> <div class="grid grid-cols-2 gap-3"><button class="inline-flex items-center justify-center space-x-2 rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">`;
  Refresh_cw($$payload, { class: "h-4 w-4" });
  $$payload.out += `<!----> <span>Sélection</span></button> <button class="inline-flex items-center justify-center space-x-2 rounded-md border border-purple-600 px-4 py-2 text-sm font-medium text-purple-600 transition-colors hover:bg-purple-50 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">`;
  Refresh_cw($$payload, { class: "h-4 w-4" });
  $$payload.out += `<!----> <span>Tout</span></button></div></div> <div class="rounded-lg bg-white p-6 shadow"><div class="mb-4"><div class="flex items-center text-lg font-medium text-gray-900">`;
  Trash_2($$payload, { class: "mr-2 h-6 w-6 text-red-600" });
  $$payload.out += `<!----> <h2>Suppression des Annonces</h2></div> <div class="mt-2"><div class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800">`;
  Key($$payload, { class: "mr-1 h-3 w-3" });
  $$payload.out += `<!----> Token Vinted requis</div></div></div> <p class="mb-4 text-sm text-gray-600">Gérez efficacement vos annonces en supprimant les articles vendus ou en faisant un grand ménage de votre profil.</p> <div class="grid grid-cols-2 gap-3"><button class="inline-flex items-center justify-center space-x-2 rounded-md bg-red-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2">`;
  Trash_2($$payload, { class: "h-4 w-4" });
  $$payload.out += `<!----> <span>Vendus</span></button> <button class="inline-flex items-center justify-center space-x-2 rounded-md border border-red-600 px-4 py-2 text-sm font-medium text-red-600 transition-colors hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2">`;
  Trash_2($$payload, { class: "h-4 w-4" });
  $$payload.out += `<!----> <span>Tout</span></button></div></div></div></div>`;
}
export {
  _page as default
};
