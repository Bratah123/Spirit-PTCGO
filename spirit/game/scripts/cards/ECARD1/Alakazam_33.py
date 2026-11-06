from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    psymimic, psymimic_condition, syncroblast,
)


card = PokemonCardDef(
    guid="b6ed4fd2-9317-51cd-8257-8c1c36e12b61",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alakazam.Name",
    display_name="Alakazam",
    searchable_by=["Alakazam", "Stage 2", "Alakazam"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Psymimic",
            game_text="Once during your turn, instead of Alakazam's normal attack, you may choose 1 of your opponent's Pok\u00e9mon's attacks. Alakazam copies that attack including its Energy costs and anything else required in order to use that attack, such as discarding Energy cards. (No matter what type that Pok\u00e9mon is, Alakazam's type is still Psychic.) This power can't be used if Alakazam is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=psymimic_condition,
            ends_turn=True,
            effect=psymimic,
        ),
        Attack(
            title="Syncroblast",
            game_text="If Alakazam and the Defending Pok\u00e9mon don't have the same number of Energy cards attached to them, this attack's base damage is 20 instead of 80.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=syncroblast,
        ),
    ],
)
