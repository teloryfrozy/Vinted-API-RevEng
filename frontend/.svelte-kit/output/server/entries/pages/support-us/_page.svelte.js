import "clsx";
import { H as Heart } from "../../../chunks/heart.js";
import { n as spread_props, m as pop, p as push } from "../../../chunks/index.js";
import { I as Icon } from "../../../chunks/Icon.js";
import { C as Copy } from "../../../chunks/copy.js";
function Credit_card($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "rect",
      {
        "width": "20",
        "height": "14",
        "x": "2",
        "y": "5",
        "rx": "2"
      }
    ],
    [
      "line",
      {
        "x1": "2",
        "x2": "22",
        "y1": "10",
        "y2": "10"
      }
    ]
  ];
  Icon($$payload, spread_props([
    { name: "credit-card" },
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
function Gift($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "rect",
      {
        "x": "3",
        "y": "8",
        "width": "18",
        "height": "4",
        "rx": "1"
      }
    ],
    ["path", { "d": "M12 8v13" }],
    [
      "path",
      {
        "d": "M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"
      }
    ],
    [
      "path",
      {
        "d": "M7.5 8a2.5 2.5 0 0 1 0-5A4.8 8 0 0 1 12 8a4.8 8 0 0 1 4.5-5 2.5 2.5 0 0 1 0 5"
      }
    ]
  ];
  Icon($$payload, spread_props([
    { name: "gift" },
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
  $$payload.out += `<div class="mx-auto max-w-4xl px-4 py-8"><div class="mb-8 rounded-lg bg-white p-6 shadow"><div class="mb-4 flex items-center">`;
  Heart($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
  $$payload.out += `<!----> <h2 class="text-xl font-semibold">Nous Soutenir</h2></div> <p class="text-gray-600">C'est une app de logistique qu'on a développée pour notre business Vinted il y a 2 ans, à côté de nos études. Si elle vous est utile, vous pouvez nous soutenir via ces offres avantageuses !</p></div> <div class="mb-6 rounded-lg bg-white p-6 shadow"><div class="mb-4 flex items-center justify-between"><h3 class="text-lg font-medium text-gray-900">Coupert</h3> <span class="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-800">10€ offerts</span></div> <p class="mb-4 text-gray-600">Extension qui trouve automatiquement les meilleurs codes promo. Gagnez 10€ en créant un compte et en dépensant 30€ sur l'un des 15 000 sites partenaires.</p> <a href="https://www.coupert.com/ref/ju51oa" target="_blank" rel="noopener noreferrer" class="inline-flex items-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700">`;
  Gift($$payload, { class: "mr-2 h-4 w-4" });
  $$payload.out += `<!----> Profiter de l'offre</a></div> <div class="rounded-lg bg-white p-6 shadow"><div class="mb-4 flex items-center justify-between"><h3 class="text-lg font-medium text-gray-900">Boursorama Banque</h3> <span class="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-800">Jusqu'à 170€ offerts</span></div> <ul class="mb-4 list-inside list-disc text-gray-600"><li>80€ à 120€ de prime de bienvenue</li> <li>50€ supplémentaires avec EasyMove</li> <li>Carte bancaire gratuite avec 1 utilisation par mois (sinon 5€)</li></ul> <div class="flex items-center gap-4"><a href="https://bour.so/FHnn31mt9L" target="_blank" rel="noopener noreferrer" class="inline-flex items-center rounded-md bg-purple-600 px-4 py-2 text-sm font-medium text-white hover:bg-purple-700">`;
  Credit_card($$payload, { class: "mr-2 h-4 w-4" });
  $$payload.out += `<!----> Ouvrir un compte</a> <button class="inline-flex items-center rounded-md border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">`;
  {
    $$payload.out += "<!--[!-->";
    Copy($$payload, { class: "mr-2 h-4 w-4" });
    $$payload.out += `<!----> Copier le code AURO2755`;
  }
  $$payload.out += `<!--]--></button></div></div></div>`;
}
export {
  _page as default
};
