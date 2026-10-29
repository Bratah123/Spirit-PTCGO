from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    cursed_drop,
    vortex_of_pain,
)

card = PokemonCardDef(
    guid="3bac15c7-6ed0-53cf-93f8-4fe1af4a33b8",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=103,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=cursed_drop
        ),
        Attack(
            title="Vortex of Pain",
            game_text="This attack does 20 damage for each damage counter on all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            damage_operator="x",
            effect=vortex_of_pain
        ),
    ],
)