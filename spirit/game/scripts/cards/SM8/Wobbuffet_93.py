from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus

from spirit.game.card_effects.sm8 import (
    shady_tail_passive,
)

card = PokemonCardDef(
    guid="2bf0ee15-ca6d-5c93-ae7a-746c64199ca2",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Ability(
            title="Shady Tail",
            game_text="As long as this Pok\u00e9mon is on your Bench, \u25c7 (Prism Star) Pok\u00e9mon in play (both yours and your opponent's) can't attack and have no Abilities.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=shady_tail_passive
        ),
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)