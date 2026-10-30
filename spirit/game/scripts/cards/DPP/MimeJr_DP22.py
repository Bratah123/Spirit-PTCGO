"""STUB: effect not implemented — do not guess mechanics.
Mime Jr. (DPP #DP22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="4609e6f8-e345-5c04-ba14-b4344405f38a",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimeJr.Name",
    display_name="Mime Jr.",
    searchable_by=["Mime Jr.", "Basic", "MimeJr"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=439,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Mr. Mime from your hand onto Mime Jr. (this counts as evolving Mime Jr.) and remove all damage counters from Mime Jr.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mime",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)