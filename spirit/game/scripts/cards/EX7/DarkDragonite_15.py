from spirit.game.card_effects.ex import dark_trance_move_darkness, double_wing_attack
"""STUB: effect not implemented — do not guess mechanics.
Dark Dragonite (EX7 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b23fc5ff-d65e-5c95-a97a-b7bdcf9dcd41",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkDragonite.Name",
    display_name="Dark Dragonite",
    searchable_by=["Dark Dragonite", "Stage 2", "DarkDragonite"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkDragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Dark Trance",
            game_text="As often as you like during your turn (before your attack), you may move a Darkness Energy card attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Dark Dragonite is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=dark_trance_move_darkness(),
        ),
        Attack(
            title="Double Wing Attack",
            game_text="Does 30 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=double_wing_attack(),
        ),
        Attack(
            title="Claw Swipe",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)