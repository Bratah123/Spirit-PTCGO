from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    delta_beam,
    energy_converter,
    energy_converter_condition,
)


card = PokemonCardDef(
    guid="50fc805b-c98a-5c7c-b5a5-b7303e57f1a1",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    display_name="Porygon2",
    searchable_by=["Porygon2", "Stage 1", "Porygon2"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    family_id=233,
    abilities=[
        Ability(
            title="Energy Converter",
            game_text="Once during your turn (before your attack), you may choose 1 basic Energy card attached to 1 of your Pok\u00e9mon and choose an Energy type. Treat that Energy card as that type until the end of your turn. This power can't be used if Porygon2 is Asleep, Confused, or Paralyzed. If Porygon2 becomes Asleep, Confused, or Paralyzed, the Energy card goes back to its original type.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=energy_converter_condition,
            effect=energy_converter,
        ),
        Attack(
            title="Delta Beam",
            game_text="Flip a coin. If heads, choose whether the Defending Pok\u00e9mon becomes Asleep, Confused, or Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            effect=delta_beam,
        ),
    ],
)
