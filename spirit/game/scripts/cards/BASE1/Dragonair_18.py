from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    discard_opponent_energy_attack, flip_damage,
)


card = PokemonCardDef(
    guid="ef91abc5-9c39-5a88-aee6-3985ff31d0e8",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair", "Stage 1", "Dragonair"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="BASE1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Hyper Beam",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, choose 1 of them and discard it.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=20,
            effect=discard_opponent_energy_attack(),
        ),
    ],
)
