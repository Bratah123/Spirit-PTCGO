"""STUB: effect not implemented — do not guess mechanics.
Sceptile ex (EX4 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import green_heal, poison_ring

card = PokemonCardDef(
    guid="526c02fb-ae40-5e91-90d6-a111f93c9819",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptileex.Name",
    display_name="Sceptile ex",
    searchable_by=["Sceptile ex", "Stage 2", "ex", "Sceptileex"],
    subtypes=["Stage 2", "ex"],
    collector_number=93,
    set_code="EX4",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=254,
    abilities=[
        Attack(
            title="Green Heal",
            game_text="Remove 4 damage counters from each of your Pok\u00e9mon that has Grass Energy attached. If that Pok\u00e9mon has less than 4 damage counters, remove all of them.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=green_heal(),
        ),
        Attack(
            title="Poison Ring",
            game_text="The Defending Pok\u00e9mon is now Poisoned. The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=poison_ring(),
        ),
        Attack(
            title="Slashing Strike",
            game_text="Sceptile ex can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 3},
            damage=100,
            # STUB: attack effect not implemented
                        locks_next_turn=True,
effect=None,
        ),
    ],
)