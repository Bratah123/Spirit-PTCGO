"""STUB: effect not implemented — do not guess mechanics.
Azumarill (DP1 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import defense_curl_flip_protect
from spirit.game.card_effects.dp import bubble_pump

card = PokemonCardDef(
    guid="b42a5ec6-9182-5bfc-b8a4-4eac9f6e0637",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Attack(
            title="Defense Curl",
            game_text="Flip a coin. If heads, prevent all damage done to Azumarill during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=defense_curl_flip_protect(),
        ),
        Attack(
            title="Bubble Pump",
            game_text="If Azumarill has 3 or more Energy attached to it, this attack does 40 damage plus 20 more damage. If Azurill is anywhere under Azumarill, flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            damage_operator="+",
            effect=bubble_pump(),
        ),
    ],
)