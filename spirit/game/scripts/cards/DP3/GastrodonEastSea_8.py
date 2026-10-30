"""STUB: effect not implemented — do not guess mechanics.
Gastrodon East Sea (DP3 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="68e2191b-f3d7-5496-b5ba-bccfc99a2525",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GastrodonEastSea.Name",
    display_name="Gastrodon East Sea",
    searchable_by=["Gastrodon East Sea", "Stage 1", "GastrodonEastSea"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ShellosEastSea.Name",
    family_id=422,
    abilities=[
        Ability(
            title="Osmotic Pressure",
            game_text="Once during your turn (before your attack), if you have Gastrodon West Sea in play, you may move up to 3 damage counters from Gastrodon East Sea to 1 of your Gastrodon West Sea.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dwindling Wave",
            game_text="Does 80 damage minus 10 damage for each damage counter on Gastrodon East Sea.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)