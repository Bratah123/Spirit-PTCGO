from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    count_energy, count_hand, damage_per, place_counters,
)


card = PokemonCardDef(
    guid="387cf2bd-f6b2-534d-b455-35dbf2554dc9",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoirex.Name",
    display_name="Gardevoir ex",
    searchable_by=["Gardevoir ex", "Stage 2", "ex", "Gardevoirex"],
    subtypes=["Stage 2", "ex"],
    collector_number=96,
    set_code="EX2",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Feedback",
            game_text="Count the number of cards in your opponent's hand. Put that many damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=place_counters(count_hand("opponent")),
        ),
        Attack(
            title="Psystorm",
            game_text="Does 10 damage times the total amount of Energy attached to all Pok\u00e9mon in play.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_energy("both"), 10),
        ),
    ],
)
