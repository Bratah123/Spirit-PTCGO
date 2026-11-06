from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    jet_stream, jet_stream_condition, unused_energy_bonus,
)


card = PokemonCardDef(
    guid="fdc03efb-4962-5924-81db-c6d950cf2c8f",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Jet Stream",
            game_text="Once during your turn (before your attack), if Blastoise is your Active Pok\u00e9mon, you may flip a coin. If heads, discard an Energy card attached to Blastoise, if any. Then, if there are any Energy cards attached to the Defending Pok\u00e9mon, choose 1 of them and discard it. This power can't be used if Blastoise is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=jet_stream_condition,
            effect=jet_stream,
        ),
        Attack(
            title="Energy Cannon",
            game_text="Does 40 damage plus 10 more damage for each Energy attached to Blastoise but not used to pay for this attack's Energy Cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unused_energy_bonus(per=10, cap=20),
        ),
    ],
)
