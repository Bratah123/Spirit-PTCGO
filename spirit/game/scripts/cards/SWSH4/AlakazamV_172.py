from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    count_hand, damage_per, place_counters,
)

card = PokemonCardDef(
    guid="437c158a-9906-5ac2-8fce-3e3ae7706a96",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamV.Name",
    display_name="Alakazam V",
    searchable_by=["Alakazam V", "Basic", "V", "AlakazamV"],
    subtypes=["Basic", "V"],
    collector_number=172,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=65,
    abilities=[
        Attack(
            title="Zen Spoon",
            game_text="Put 3 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(3, "choose_any_opponent"),
        ),
        Attack(
            title="Mind Ruler",
            game_text="This attack does 30 damage for each card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_hand("opponent"), 30),
        ),
    ],
)
