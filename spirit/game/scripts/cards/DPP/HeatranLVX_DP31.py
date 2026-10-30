"""STUB: effect not implemented — do not guess mechanics.
Heatran LV.X (DPP #DP31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="21943c87-f7fe-558a-9afa-5a7afb531e2a",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatranLVX.Name",
    display_name="Heatran LV.X",
    searchable_by=["Heatran LV.X", "Level-Up", "HeatranLVX"],
    subtypes=["Level-Up"],
    collector_number=31,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.LEVELUP,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name",
    family_id=485,
    abilities=[
        Ability(
            title="Heat Metal",
            game_text="Your opponent can't remove the Special Condition Burned by evolving or devolving his or her Burned Pok\u00e9mon. (This also includes putting a Pok\u00e9mon Level-Up card onto the Burned Pok\u00e9mon.) Whenever your opponent flips a coin for the Special Condition Burned between turns, treat it as tails.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Ability(
            title="Heat Wave",
            game_text="Once at the end of your turn, if Heatran is on your Bench, you may use this power. If you discarded basic Energy cards attached to your Fire or Metal Active Pok\u00e9mon by using that Pok\u00e9mon's attack this turn, attach up to 2 of those Energy cards to that Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
    ],
)