"""STUB: effect not implemented — do not guess mechanics.
Honchkrow LV.X (DP3 #132): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4508bfe7-4237-54d1-a985-bb9bed547048",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HonchkrowLVX.Name",
    display_name="Honchkrow LV.X",
    searchable_by=["Honchkrow LV.X", "Level-Up", "HonchkrowLVX"],
    subtypes=["Level-Up"],
    collector_number=132,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.LEVELUP,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    family_id=430,
    abilities=[
        Attack(
            title="Feint Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Wing",
            game_text="If the Defending Pok\u00e9mon would be Knocked Out by damage from this attack, you may search your discard pile for any 1 card, show it to your opponent, and put it into your hand.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)