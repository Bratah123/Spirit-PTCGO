"""STUB: effect not implemented — do not guess mechanics.
Shaymin LV.X (DPP #DP39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="01860cdb-dd90-5ce4-adc4-7b120b5f15c0",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminLVX.Name",
    display_name="Shaymin LV.X",
    searchable_by=["Shaymin LV.X", "Level-Up", "ShayminLVX"],
    subtypes=["Level-Up"],
    collector_number=39,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.LEVELUP,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    family_id=492,
    abilities=[
        Ability(
            title="Revenge Seed",
            game_text="If any of your Grass Pok\u00e9mon were Knocked Out by damage from an opponent's attack during his or her last turn, each of Shaymin's attacks does 60 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Energy Flare",
            game_text="You may move any number of Energy cards attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)