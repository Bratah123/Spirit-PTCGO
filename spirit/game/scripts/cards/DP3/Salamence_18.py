"""STUB: effect not implemented — do not guess mechanics.
Salamence (DP3 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7b5539cb-3d94-5c77-9c04-9ca942e2740f",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name",
    display_name="Salamence",
    searchable_by=["Salamence", "Stage 2", "Salamence"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Attack(
            title="Direct Hit",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Finish",
            game_text="Discard 2 basic Fire Energy cards or 2 basic Water Energy cards attached to Salamence. If you discarded 2 basic Fire Energy cards, this attack does 100 damage to the Defending Pok\u00e9mon. If you discarded 2 Basic Water Energy cards, this attack does 100 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (If you can't discard cards, this attack does nothing.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)