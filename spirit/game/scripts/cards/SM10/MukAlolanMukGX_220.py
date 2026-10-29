from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm10 import (
    nasty_goo_mix_gx,
    poison_absorption,
    severe_poison_eight,
)

card = PokemonCardDef(
    guid="ee654ceb-f514-503c-b295-e4828fa3ccf3",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MukAlolanMukGX.Name",
    display_name="Muk & Alolan Muk-GX",
    searchable_by=["Muk & Alolan Muk-GX", "Basic", "TAG TEAM", "GX", "MukAlolanMukGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=220,
    set_code="SM10",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=89,
    abilities=[
        Attack(
            title="Severe Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 8 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=severe_poison_eight
        ),
        Attack(
            title="Poison Absorption",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, heal 100 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=poison_absorption
        ),
        Attack(
            title="Nasty Goo Mix-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned. If this Pok\u00e9mon has at least 4 extra Energy attached to it (in addition to this attack's cost), put 15 damage counters instead of 1 on that Pok\u00e9mon between turns. (You can't use more than 1 GX attack in a game.)",
            cost={},
            effect=nasty_goo_mix_gx
        ),
    ],
)