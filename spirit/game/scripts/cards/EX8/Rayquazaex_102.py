"""STUB: effect not implemented — do not guess mechanics.
Rayquaza ex (EX8 #102): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import dragon_boost_on_bench, spiral_blast_basic_energy


card = PokemonCardDef(
    guid="138904b4-d4e7-530c-8a9a-3122476e9e98",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquazaex.Name",
    display_name="Rayquaza ex",
    searchable_by=["Rayquaza ex", "Basic", "ex", "Rayquazaex"],
    subtypes=["Basic", "ex"],
    collector_number=102,
    set_code="EX8",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.WATER,
    family_id=384,
    abilities=[
        Ability(
            title="Dragon Boost",
            game_text="Once during your turn, when you put Rayquaza ex from your hand onto your Bench, you may move any number of basic Energy cards attached to your Pok\u00e9mon to Rayquaza ex.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=dragon_boost_on_bench(),
        ),
        Attack(
            title="Spiral Blast",
            game_text="Does 20 damage for each basic Energy card attached to Rayquaza ex.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=spiral_blast_basic_energy(),
        ),
    ],
)