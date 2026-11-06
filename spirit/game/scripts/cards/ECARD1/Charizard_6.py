from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    burning_energy, burning_energy_condition, scorching_whirlwind,
)


card = PokemonCardDef(
    guid="b3728429-611e-56b7-9ff1-350cb3272bf3",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Burning Energy",
            game_text="Once during your turn (before your attack), you may turn all basic Energy attached to all of your Pok\u00e9mon into Fire Energy for the rest of the turn. This power can't be used if Charizard is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=burning_energy_condition,
            effect=burning_energy,
        ),
        Attack(
            title="Scorching Whirlwind",
            game_text="Flip 2 coins. If 1 of them is tails, discard 2 Energy cards attached to Charizard. If both are tails, discard all Energy cards attached to Charizard.",
            cost={PokemonTypes.FIRE: 4},
            damage=120,
            effect=scorching_whirlwind,
        ),
    ],
)
