from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    commanding_queen,
)

card = PokemonCardDef(
    guid="83dab3ee-d123-5a4b-b94c-b9d7542c555b",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1", "Vespiquen"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Attack(
            title="Commanding Queen",
            game_text="If you have 4 or fewer Grass Pok\u00e9mon on your Bench, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=120,
            effect=commanding_queen
        ),
    ],
)