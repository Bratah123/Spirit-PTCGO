"""STUB: effect not implemented — do not guess mechanics.
Ampharos (EX10 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import energy_connect_basic, energy_connect_condition, miraculous_thunder

card = PokemonCardDef(
    guid="d3927961-346e-5077-9a8a-c8772bac5ed0",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Energy Connect",
            activation=Activations.UNLIMITED,
            condition=energy_connect_condition(),
            game_text="As often as you like during your turn (before your attack), you may move a basic Energy card attached to 1 of your Benched Pok\u00e9mon to your Active Pok\u00e9mon. This power can't be used if Ampharos is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=energy_connect_basic(),
        ),
        Attack(
            title="Miraculous Thunder",
            game_text="You may discard all Lightning Energy attached to Ampharos. If you do, the Defending Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=miraculous_thunder(),
        ),
    ],
)