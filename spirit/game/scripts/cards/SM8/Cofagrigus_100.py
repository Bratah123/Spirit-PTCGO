from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    spirit_juggling,
)

card = PokemonCardDef(
    guid="239fb690-5ffc-533d-bcd5-dc7d10e82d06",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigus.Name",
    display_name="Cofagrigus",
    searchable_by=["Cofagrigus", "Stage 1", "Cofagrigus"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Attack(
            title="Spirit Juggling",
            game_text="Discard any number of your Benched Pok\u00e9mon. This attack does 30 more damage for each Benched Pok\u00e9mon you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=spirit_juggling
        ),
    ],
)