"""STUB: effect not implemented — do not guess mechanics.
Lucario LV.X (DPP #DP12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="83f5735b-122c-5b25-8e81-f142282adeaf",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioLVX.Name",
    display_name="Lucario LV.X",
    searchable_by=["Lucario LV.X", "Level-Up", "LucarioLVX"],
    subtypes=["Level-Up"],
    collector_number=12,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.LEVELUP,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    family_id=448,
    abilities=[
        Ability(
            title="Stance",
            game_text="Once during your turn (before your attack), when you put Lucario LV.X from your hand onto your Active Lucario, you may use this power. Prevent all effects of an attack, including damage, done to Lucario during your opponent's next turn. (If Lucario is no longer your Active Pok\u00e9mon, this effect ends.)",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Close Combat",
            game_text="During your opponent's next turn, any damage done to Lucario by attacks is increased by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)