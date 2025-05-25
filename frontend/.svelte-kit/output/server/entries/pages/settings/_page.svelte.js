import { n as spread_props, m as pop, p as push, v as attr } from "../../../chunks/index.js";
import { I as Icon } from "../../../chunks/Icon.js";
import { M as Mail } from "../../../chunks/mail.js";
import { K as Key } from "../../../chunks/key.js";
function Globe($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "circle",
      { "cx": "12", "cy": "12", "r": "10" }
    ],
    [
      "path",
      {
        "d": "M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"
      }
    ],
    ["path", { "d": "M2 12h20" }]
  ];
  Icon($$payload, spread_props([
    { name: "globe" },
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
function Shield($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"
      }
    ]
  ];
  Icon($$payload, spread_props([
    { name: "shield" },
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
function Wrench($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"
      }
    ]
  ];
  Icon($$payload, spread_props([
    { name: "wrench" },
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
  let settings = {
    emailSettings: {
      host: "",
      port: "",
      username: "",
      password: ""
    },
    vintedToken: ""
  };
  $$payload.out += `<div class="mx-auto max-w-4xl px-4 py-8"><div class="mb-8 flex items-center justify-between"><h1 class="text-3xl font-bold text-gray-900">Paramètres</h1> <button class="inline-flex items-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2">`;
  Wrench($$payload, { class: "mr-2 h-4 w-4" });
  $$payload.out += `<!----> Sauvegarder</button></div> <div class="grid gap-6 md:grid-cols-2"><div class="rounded-lg bg-white p-6 shadow"><div class="mb-6 flex items-center border-b pb-4">`;
  Globe($$payload, { class: "mr-2 h-5 w-5 text-purple-600" });
  $$payload.out += `<!----> <h2 class="text-xl font-semibold text-gray-900">Préférences Générales</h2></div> <div class="space-y-4"><div><p>Langue</p> <select class="mt-1 block w-full rounded-md border border-gray-300 bg-white py-2 px-3 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"><option value="fr">Français</option><option value="en">English</option></select></div></div></div> <div class="rounded-lg bg-white p-6 shadow"><div class="mb-6 flex items-center border-b pb-4">`;
  Mail($$payload, { class: "mr-2 h-5 w-5 text-purple-600" });
  $$payload.out += `<!----> <h2 class="text-xl font-semibold text-gray-900">Configuration Email</h2></div> <div class="space-y-4"><div class="grid grid-cols-2 gap-4"><div><p class="block text-sm font-medium text-gray-700">Serveur IMAP</p> <input type="text"${attr("value", settings.emailSettings.host)} placeholder="imap.gmail.com" class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"/></div> <div><p class="block text-sm font-medium text-gray-700">Port</p> <input type="text"${attr("value", settings.emailSettings.port)} placeholder="993" class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"/></div></div> <div><p class="block text-sm font-medium text-gray-700">Email</p> <input type="email"${attr("value", settings.emailSettings.username)} placeholder="exemple@gmail.com" class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"/></div> <div><p class="block text-sm font-medium text-gray-700">Mot de passe</p> <input type="password"${attr("value", settings.emailSettings.password)} placeholder="••••••••" class="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus:border-purple-500 focus:outline-none focus:ring-purple-500"/></div></div></div> <div class="rounded-lg bg-white p-6 shadow md:col-span-2"><div class="mb-6 flex items-center border-b pb-4">`;
  Shield($$payload, { class: "mr-2 h-5 w-5 text-purple-600" });
  $$payload.out += `<!----> <h2 class="text-xl font-semibold text-gray-900">Token Vinted</h2></div> <div class="space-y-4"><div><p class="block text-sm font-medium text-gray-700">Token d'authentification</p> <div class="mt-1 flex rounded-md shadow-sm"><input type="password"${attr("value", settings.vintedToken)} placeholder="Collez votre token Vinted ici" class="block w-full flex-1 rounded-none rounded-l-md border border-gray-300 px-3 py-2 focus:border-purple-500 focus:outline-none focus:ring-purple-500"/> <button class="inline-flex items-center rounded-r-md border border-l-0 border-gray-300 bg-gray-50 px-3 text-gray-500 hover:bg-gray-100">`;
  Key($$payload, { class: "h-5 w-5" });
  $$payload.out += `<!----></button></div> <p class="mt-2 text-sm text-gray-500">Le token est nécessaire pour automatiser les actions sur Vinted</p></div></div></div></div></div>`;
}
export {
  _page as default
};
