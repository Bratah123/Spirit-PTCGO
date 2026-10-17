"""STUB: effect not implemented — do not guess mechanics.
Chesnaught (XY1 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f34bbe2e-661f-5d77-a20b-34c30e8d55f1",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chesnaught.Name",
    display_name="Chesnaught",
    searchable_by=["Chesnaught", "Stage 2", "Chesnaught"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name",
    family_id=650,
    abilities=[
        Ability(
            title="Spiky Shield",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Touchdown",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)