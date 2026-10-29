from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    make_a_mess,
)

card = PokemonCardDef(
    guid="1964fdd6-f186-5d52-a3c6-b83630592ea4",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    display_name="Snubbull",
    searchable_by=["Snubbull", "Basic", "Snubbull"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=209,
    abilities=[
        Attack(
            title="Make a Mess",
            game_text="Discard up to 2 Trainer cards from your hand. This attack does 20 damage for each card you discarded in this way.",
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            damage_operator="x",
            effect=make_a_mess
        ),
    ],
)