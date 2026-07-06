from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import (
    concealed_cards, has_energy_in_hand, moonlight_shuriken,
)

card = PokemonCardDef(
    guid="2a297924-991d-552c-917f-d1b53741020d",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantGreninja.Name",
    display_name="Radiant Greninja",
    searchable_by=["Radiant Greninja", "Basic", "Radiant", "RadiantGreninja"],
    subtypes=["Basic", "Radiant"],
    collector_number=46,
    set_code="SWSH10",
    rarity=Rarities.RareRadiant,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=658,
    abilities=[
        Ability(
            title="Concealed Cards",
            game_text="You must discard an Energy card from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=has_energy_in_hand,
            effect=concealed_cards,
        ),
        Attack(
            title="Moonlight Shuriken",
            game_text="Discard 2 Energy from this Pok\u00e9mon. This attack does 90 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=moonlight_shuriken,
        ),
    ],
)
