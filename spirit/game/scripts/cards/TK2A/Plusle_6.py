"""Plusle (TK2A #6)."""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import dig_deep_energy_to_hand


card = PokemonCardDef(
    guid="30b0eac7-a76a-5eb4-a00b-0afc570c1809",
    key="TK2A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="TK2A",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=311,
    abilities=[
        Attack(
            title="Pickup Power",
            game_text="Search your discard pile for an Energy card, show it to your opponent, and put it in your hand",
            cost={PokemonTypes.COLORLESS: 1},
            effect=dig_deep_energy_to_hand(),
        ),
        Attack(
            title="Rear Spark",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=snipe_attack(20),
        ),
    ],
)