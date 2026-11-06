from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.ecard import energy_jump, energy_jump_condition


card = PokemonCardDef(
    guid="a91ce11f-0b0b-51c7-b7d4-041e5487b107",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alakazam.Name",
    display_name="Alakazam",
    searchable_by=["Alakazam", "Stage 2", "Alakazam"],
    subtypes=["Stage 2"],
    collector_number=151,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Energy Jump",
            game_text="Once during your turn (before your attack), you may move an Energy card from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Alakazam is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=energy_jump_condition,
            effect=energy_jump,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 damage plus 10 more damage for each Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("defender", cards=True), 10, base=30),
        ),
    ],
)
