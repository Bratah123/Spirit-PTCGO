"""STUB: effect not implemented — do not guess mechanics.
Mime Jr. (DP1 #90): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import baby_evolution, baby_evolution_condition, mime_draw_equal_opponent

card = PokemonCardDef(
    guid="9aa97932-89dc-578c-af20-8317ab74d671",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimeJr.Name",
    display_name="Mime Jr.",
    searchable_by=["Mime Jr.", "Basic", "MimeJr"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="DP1",
    rarity=Rarities.Common,
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
            condition=baby_evolution_condition('Mr. Mime'),
            effect=baby_evolution('Mr. Mime'),
        ),
        Attack(
            title="Mime",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=mime_draw_equal_opponent(),
        ),
    ],
)