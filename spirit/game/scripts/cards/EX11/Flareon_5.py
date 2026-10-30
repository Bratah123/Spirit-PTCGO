"""STUB: effect not implemented — do not guess mechanics.
Flareon δ (EX11 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import delta_search_holon_attach_self, return_burn
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6892386a-3aba-5124-b4a8-0094766be0cb",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon δ",
    searchable_by=["Flareon \u03b4", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Delta Search",
            game_text="Search your deck for a Holon Energy card and attach it to Flareon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=delta_search_holon_attach_self(),
        ),
        Attack(
            title="Return Burn",
            game_text="You may return an Energy card attached to Flareon to your hand. If you do, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=return_burn(),
        ),
    ],
)