"""STUB: effect not implemented — do not guess mechanics.
Eevee δ (EX11 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import metal_scoop_attach
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d1afa60f-1e41-537b-a9c4-a39ec516b0b2",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee δ",
    searchable_by=["Eevee \u03b4", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Metal Scoop",
            game_text="Search your discard pile for a Metal Energy card and attach it to Eevee.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=metal_scoop_attach(10),
        ),
    ],
)