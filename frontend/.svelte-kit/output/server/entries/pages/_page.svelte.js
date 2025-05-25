import "clsx";
import { S as Shopping_bag } from "../../chunks/shopping-bag.js";
import { n as spread_props, m as pop, p as push } from "../../chunks/index.js";
import { I as Icon } from "../../chunks/Icon.js";
import { C as Copy } from "../../chunks/copy.js";
import { T as Trash_2 } from "../../chunks/trash-2.js";
import { U as Users_round, C as Camera, F as File_text, H as Heart_handshake } from "../../chunks/users-round.js";
import { M as Mail } from "../../chunks/mail.js";
import { M as Message_square } from "../../chunks/message-square.js";
function Circle_arrow_up($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "circle",
      { "cx": "12", "cy": "12", "r": "10" }
    ],
    ["path", { "d": "m16 12-4-4-4 4" }],
    ["path", { "d": "M12 16V8" }]
  ];
  Icon($$payload, spread_props([
    { name: "circle-arrow-up" },
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
function Inbox($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "polyline",
      { "points": "22 12 16 12 14 15 10 15 8 12 2 12" }
    ],
    [
      "path",
      {
        "d": "M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"
      }
    ]
  ];
  Icon($$payload, spread_props([
    { name: "inbox" },
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
function Lightbulb($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"
      }
    ],
    ["path", { "d": "M9 18h6" }],
    ["path", { "d": "M10 22h4" }]
  ];
  Icon($$payload, spread_props([
    { name: "lightbulb" },
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
function Mail_check($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M22 13V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h8"
      }
    ],
    [
      "path",
      {
        "d": "m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"
      }
    ],
    ["path", { "d": "m16 19 2 2 4-4" }]
  ];
  Icon($$payload, spread_props([
    { name: "mail-check" },
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
function Network($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "rect",
      {
        "x": "16",
        "y": "16",
        "width": "6",
        "height": "6",
        "rx": "1"
      }
    ],
    [
      "rect",
      {
        "x": "2",
        "y": "16",
        "width": "6",
        "height": "6",
        "rx": "1"
      }
    ],
    [
      "rect",
      {
        "x": "9",
        "y": "2",
        "width": "6",
        "height": "6",
        "rx": "1"
      }
    ],
    [
      "path",
      {
        "d": "M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"
      }
    ],
    ["path", { "d": "M12 12V8" }]
  ];
  Icon($$payload, spread_props([
    { name: "network" },
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
function Save($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      {
        "d": "M15.2 3a2 2 0 0 1 1.4.6l3.8 3.8a2 2 0 0 1 .6 1.4V19a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"
      }
    ],
    [
      "path",
      {
        "d": "M17 21v-7a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1v7"
      }
    ],
    ["path", { "d": "M7 3v4a1 1 0 0 0 1 1h7" }]
  ];
  Icon($$payload, spread_props([
    { name: "save" },
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
function User_round_plus($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    ["path", { "d": "M2 21a8 8 0 0 1 13.292-6" }],
    ["circle", { "cx": "10", "cy": "8", "r": "5" }],
    ["path", { "d": "M19 16v6" }],
    ["path", { "d": "M22 19h-6" }]
  ];
  Icon($$payload, spread_props([
    { name: "user-round-plus" },
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
  $$payload.out += `<div class="mx-auto max-w-7xl px-4 py-12"><h1 class="mb-12 text-center text-4xl font-bold text-gray-900">Vinted Automation Tools</h1> <div class="grid gap-8"><a href="/ads-management" class="group relative overflow-hidden rounded-xl bg-white p-8 shadow-md transition-all hover:-translate-y-1 hover:shadow-xl"><div class="absolute right-0 top-0 h-32 w-32 translate-x-8 translate-y-[-50%] transform opacity-5 transition-transform group-hover:translate-x-4">`;
  Shopping_bag($$payload, { class: "h-full w-full" });
  $$payload.out += `<!----></div> <div class="relative"><div class="mb-6 flex items-center">`;
  Shopping_bag($$payload, { class: "mr-3 h-8 w-8 text-purple-600" });
  $$payload.out += `<!----> <h2 class="text-2xl font-semibold text-gray-900 group-hover:text-purple-600">Gérer les annonces</h2></div> <div class="grid gap-4 md:grid-cols-3"><div class="flex items-start space-x-3">`;
  Circle_arrow_up($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Remonter vos annonces en tête de liste</p></div> <div class="flex items-start space-x-3">`;
  Copy($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Automatiser la vente de vos doublons</p></div> <div class="flex items-start space-x-3">`;
  Trash_2($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Supprimer vos articles vendus</p></div></div></div></a> <a href="/follow-mass" class="group relative overflow-hidden rounded-xl bg-white p-8 shadow-md transition-all hover:-translate-y-1 hover:shadow-xl"><div class="absolute right-0 top-0 h-32 w-32 translate-x-8 translate-y-[-50%] transform opacity-5 transition-transform group-hover:translate-x-4">`;
  Users_round($$payload, { class: "h-full w-full" });
  $$payload.out += `<!----></div> <div class="relative"><div class="mb-6 flex items-center">`;
  Users_round($$payload, { class: "mr-3 h-8 w-8 text-purple-600" });
  $$payload.out += `<!----> <h2 class="text-2xl font-semibold text-gray-900 group-hover:text-purple-600">Suivez en masse</h2></div> <div class="grid gap-4 md:grid-cols-3"><div class="flex items-start space-x-3">`;
  User_round_plus($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Suivez des dizaines d'utilisateurs en un clic</p></div> <div class="flex items-start space-x-3">`;
  Save($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Sauvegarde d'abonnements automatique</p></div> <div class="flex items-start space-x-3">`;
  Network($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Augmentez vos relations</p></div></div></div></a> <a href="/accounting" class="group relative overflow-hidden rounded-xl bg-white p-8 shadow-md transition-all hover:-translate-y-1 hover:shadow-xl"><div class="absolute right-0 top-0 h-32 w-32 translate-x-8 translate-y-[-50%] transform opacity-5 transition-transform group-hover:translate-x-4">`;
  Mail_check($$payload, { class: "h-full w-full" });
  $$payload.out += `<!----></div> <div class="relative"><div class="mb-6 flex items-center">`;
  Mail_check($$payload, { class: "mr-3 h-8 w-8 text-purple-600" });
  $$payload.out += `<!----> <h2 class="text-2xl font-semibold text-gray-900 group-hover:text-purple-600">Secrétariat</h2></div> <div class="grid gap-4 md:grid-cols-3"><div class="flex items-start space-x-3">`;
  Mail($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Paramétrer la gestion de vos mails</p></div> <div class="flex items-start space-x-3">`;
  Inbox($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Trier vos mails de manière passive</p></div> <div class="flex items-start space-x-3">`;
  Message_square($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-purple-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Supprimer vos anciennes conversations</p></div></div></div></a> <a href="/help" class="group relative overflow-hidden rounded-xl bg-white p-8 shadow-md transition-all hover:-translate-y-1 hover:shadow-xl"><div class="absolute right-0 top-0 h-32 w-32 translate-x-8 translate-y-[-50%] transform opacity-5 transition-transform group-hover:translate-x-4">`;
  Lightbulb($$payload, { class: "h-full w-full" });
  $$payload.out += `<!----></div> <div class="relative"><div class="mb-6 flex items-center">`;
  Lightbulb($$payload, { class: "mr-3 h-8 w-8 text-yellow-500" });
  $$payload.out += `<!----> <h2 class="text-2xl font-semibold text-gray-900 group-hover:text-yellow-500">Conseils de Vente</h2></div> <div class="grid gap-4 md:grid-cols-3"><div class="flex items-start space-x-3">`;
  Camera($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-yellow-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Astuces pour des photos qui convertissent</p></div> <div class="flex items-start space-x-3">`;
  File_text($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-yellow-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Rédiger des descriptions efficaces</p></div> <div class="flex items-start space-x-3">`;
  Heart_handshake($$payload, {
    class: "mt-0.5 h-5 w-5 flex-shrink-0 text-yellow-500"
  });
  $$payload.out += `<!----> <p class="text-sm text-gray-600">Retours d'expérience et conseils personnalisés</p></div></div></div></a></div></div>`;
}
export {
  _page as default
};
