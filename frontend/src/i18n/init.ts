import { addMessages, init, getLocaleFromNavigator } from "svelte-i18n";

import en from "./en-US.json";
import fr from "./fr.json";

addMessages("en-US", en);
addMessages("fr", fr);

init({
    fallbackLocale: "en-US",
    initialLocale: getLocaleFromNavigator(),
});