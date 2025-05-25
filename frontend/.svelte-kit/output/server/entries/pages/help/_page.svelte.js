import { n as spread_props, m as pop, p as push, w as attr_class, x as stringify } from "../../../chunks/index.js";
import { C as Camera, F as File_text, U as Users_round, H as Heart_handshake } from "../../../chunks/users-round.js";
import { I as Icon } from "../../../chunks/Icon.js";
function Smile($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "circle",
      { "cx": "12", "cy": "12", "r": "10" }
    ],
    ["path", { "d": "M8 14s1.5 2 4 2 4-2 4-2" }],
    [
      "line",
      {
        "x1": "9",
        "x2": "9.01",
        "y1": "9",
        "y2": "9"
      }
    ],
    [
      "line",
      {
        "x1": "15",
        "x2": "15.01",
        "y1": "9",
        "y2": "9"
      }
    ]
  ];
  Icon($$payload, spread_props([
    { name: "smile" },
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
  $$payload.out += `<div class="mx-auto max-w-7xl px-4 py-8"><h1 class="mb-8 text-3xl font-bold text-gray-900">Guide et Conseils</h1> <div class="mb-8 flex border-b"><button${attr_class(`mr-4 border-b-2 px-4 py-2 ${stringify("border-purple-600 text-purple-600")}`)}>Astuces de Vente</button> <button${attr_class(`border-b-2 px-4 py-2 ${stringify("border-transparent text-gray-500 hover:text-gray-700")}`)}>Mon Parcours</button></div> `;
  {
    $$payload.out += "<!--[-->";
    $$payload.out += `<div class="grid gap-6 md:grid-cols-2"><div class="rounded-lg bg-white p-6 shadow"><div class="mb-4 flex items-center">`;
    Camera($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
    $$payload.out += `<!----> <h2 class="text-xl font-semibold">Photos</h2></div> <div class="space-y-2 text-gray-600"><p>Prenez des photos de loin car elles apparaissent rognées sur Vinted.</p> <p>Des photos de qualité :</p> <ul class="list-inside list-disc pl-4"><li>Inspirent confiance</li> <li>Montrent le soin apporté aux articles</li> <li>Augmentent les chances de vente</li></ul></div></div> <div class="rounded-lg bg-white p-6 shadow"><div class="mb-4 flex items-center">`;
    File_text($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
    $$payload.out += `<!----> <h2 class="text-xl font-semibold">Description</h2></div> <div class="space-y-2 text-gray-600"><p>La clé d'une bonne description :</p> <ul class="list-inside list-disc pl-4"><li>Texte simple et structuré en liste</li> <li>Utilisation d'émojis pour plus de dynamisme `;
    Smile($$payload, { class: "inline h-4 w-4" });
    $$payload.out += `<!----></li> <li>Informations claires et précises</li></ul> <p>Une description soignée reflète la qualité de vos articles.</p></div></div> <div class="rounded-lg bg-white p-6 shadow"><div class="mb-4 flex items-center">`;
    Users_round($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
    $$payload.out += `<!----> <h2 class="text-xl font-semibold">Followers</h2></div> <div class="space-y-2 text-gray-600"><p>Développez votre réseau :</p> <ul class="list-inside list-disc pl-4"><li>Suivez d'autres vendeurs activement</li> <li>Gagnez en visibilité grâce aux abonnés</li> <li>Utilisez Follow Mass pour automatiser ce processus</li></ul> <p class="mt-2 text-sm italic">Plus d'abonnés = Plus de crédibilité</p></div></div> <div class="rounded-lg bg-white p-6 shadow"><div class="mb-4 flex items-center">`;
    Heart_handshake($$payload, { class: "mr-2 h-6 w-6 text-purple-600" });
    $$payload.out += `<!----> <h2 class="text-xl font-semibold">Remerciements</h2></div> <div class="space-y-2 text-gray-600"><p>Personnalisez l'expérience client :</p> <ul class="list-inside list-disc pl-4"><li>Ajoutez un message manuscrit dans le colis</li> <li>Créez une relation personnelle avec l'acheteur</li> <li>Encouragez les retours positifs et le bouche-à-oreille</li></ul> <p class="mt-2 text-sm italic">Un client satisfait reviendra et parlera de vous !</p></div></div></div>`;
  }
  $$payload.out += `<!--]--> `;
  {
    $$payload.out += "<!--[!-->";
  }
  $$payload.out += `<!--]--></div>`;
}
export {
  _page as default
};
