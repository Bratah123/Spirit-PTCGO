"""STUB: effect not implemented — do not guess mechanics.
Arcanine (DP3 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ecd0e636-bb0b-5cca-963d-8ccfcbf894b5",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Flame Dash",
            game_text="Once during your turn, when you play Arcanine from your hand to evolve 1 of your Benched Pok\u00e9mon, you may switch Arcanine with 1 of your Active Pok\u00e9mon. If you do, you may move any number of Energy cards attached to that Pok\u00e9mon to Arcanine.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Inferno Onrush",
            game_text="Arcanine does 40 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)