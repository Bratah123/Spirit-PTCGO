"""STUB: effect not implemented — do not guess mechanics.
Arceus (DPP #DP50): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="945dbd86-1c96-5502-861e-7648a7893d82",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name",
    display_name="Arceus",
    searchable_by=["Arceus", "Basic", "Arceus"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Attack(
            title="Judgment",
            game_text="Discard all Energy cards attached to Arceus and this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)