"""STUB: effect not implemented — do not guess mechanics.
Darkrai LV.X (DPP #DP19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="168c9e8c-e0cb-5fbc-9f4e-239d8a066135",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiLVX.Name",
    display_name="Darkrai LV.X",
    searchable_by=["Darkrai LV.X", "Level-Up", "DarkraiLVX"],
    subtypes=["Level-Up"],
    collector_number=19,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.LEVELUP,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    family_id=491,
    abilities=[
        Ability(
            title="Dark Shadow",
            game_text="Each basic Darkness Energy card attached to your Darkness Pok\u00e9mon now has the effect \"If the Pok\u00e9mon Darkness Energy is attached to attacks, the attack does 10 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).\" You can't use more than 1 Dark Shadow Pok\u00e9-Body each turn.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Endless Darkness",
            game_text="The Defending Pok\u00e9mon is now Asleep. Flip 2 coins instead of 1 between turns. If either of them is tails, the Defending Pok\u00e9mon is still Asleep. If both of them are tails, the Defending Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)