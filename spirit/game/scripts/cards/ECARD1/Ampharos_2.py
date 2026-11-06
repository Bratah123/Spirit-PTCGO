from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    energy_connect, energy_connect_condition, lightning_strike,
)


card = PokemonCardDef(
    guid="2a53bf50-7402-591e-96d9-99c705dd4e98",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Energy Connect",
            game_text="As often as you like during your turn (before your attack), you may take a basic Energy card attached to 1 of your Benched Pok\u00e9mon and attach it to your Active Pok\u00e9mon. This power can't be used if Ampharos is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.UNLIMITED,
            condition=energy_connect_condition,
            effect=energy_connect,
        ),
        Attack(
            title="Lightning Strike",
            game_text="You may discard all Lightning Energy cards attached to Ampharos. If you do, this attack's base damage is 80 instead of 40.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=lightning_strike,
        ),
    ],
)
