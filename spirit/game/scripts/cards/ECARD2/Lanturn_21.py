from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    electric_tackle, ion_coating, ion_coating_condition,
)


card = PokemonCardDef(
    guid="976e5dc4-5e34-5f0b-be80-cca1d977e12a",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1", "Lanturn"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Ability(
            title="Ion Coating",
            game_text="You may use this power once during each of your turns (before your attack). All Lightning Energy attached to your Active Pok\u00e9mon becomes Water Energy for the rest of the turn. (This effect ends if your Active Pok\u00e9mon retreats or is returned to your hand.) This power can't be used if Lanturn is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=ion_coating_condition,
            effect=ion_coating,
        ),
        Attack(
            title="Electric Tackle",
            game_text="This attack does 20 damage plus 10 damage for each Lightning Energy attached to Lanturn. Flip a coin. If tails, Lanturn does 10 damage to itself for each Lightning Energy attached to it.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=electric_tackle,
        ),
    ],
)
