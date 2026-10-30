from spirit.game.card_effects.ex import energy_link_self
"""STUB: effect not implemented — do not guess mechanics.
Dark Steelix (EX7 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f2a50caf-8032-5371-b3a8-521922788445",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkSteelix.Name",
    display_name="Dark Steelix",
    searchable_by=["Dark Steelix", "Stage 1", "DarkSteelix"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Attack(
            title="Energy Link",
            game_text="Search your discard pile for an Energy card and attach it to Dark Steelix.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=energy_link_self(),
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)