import { n as spread_props, m as pop, p as push } from "./index.js";
import { I as Icon } from "./Icon.js";
function Mail($$payload, $$props) {
  push();
  let { $$slots, $$events, ...props } = $$props;
  const iconNode = [
    [
      "path",
      { "d": "m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7" }
    ],
    [
      "rect",
      {
        "x": "2",
        "y": "4",
        "width": "20",
        "height": "16",
        "rx": "2"
      }
    ]
  ];
  Icon($$payload, spread_props([
    { name: "mail" },
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
export {
  Mail as M
};
