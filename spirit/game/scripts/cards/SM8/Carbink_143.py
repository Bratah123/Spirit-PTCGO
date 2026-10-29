from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    wonder_ray,
)

card = PokemonCardDef(
    guid="09ed8d6c-2cea-5b22-8f1e-bc06354fe7d3",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    display_name="Carbink",
    searchable_by=["Carbink", "Basic", "Carbink"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=703,
    abilities=[
        Attack(
            title="Wonder Ray",
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to this Pok\u00e9mon by any Pok\u00e9mon that has an Ability.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=wonder_ray
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)