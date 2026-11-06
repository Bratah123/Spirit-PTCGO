from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    miraculous_powder, miraculous_powder_condition, spiral_drain,
)


card = PokemonCardDef(
    guid="604a8fd3-086c-5a8b-b9cb-52be7aca1c90",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2", "Butterfree"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Ability(
            title="Miraculous Powder",
            game_text="Once during your turn (before your attack), you may remove all Special Conditions from your Active Pok\u00e9mon. This power can't be used if Butterfree is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=miraculous_powder_condition,
            effect=miraculous_powder,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Flip a coin. If heads, remove 2 damage counters from Butterfree.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=spiral_drain,
        ),
    ],
)
